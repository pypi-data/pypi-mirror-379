from fastapi import FastAPI, Body
from icecream import ic
import uvicorn
import inspect
import json
import hashlib
import httpx
import logging
from typing import Any, Callable, Dict, List, Optional, Type, TypedDict, Union


class PropertySchema(TypedDict, total=False):
    """Schema for individual properties in request body schema"""

    constant_value: str
    description: str
    dynamic_variable: str
    enum: Optional[List[str]]
    type: str


class RequestBodySchema(TypedDict, total=False):
    """Schema for request body configuration"""

    description: str
    properties: Dict[str, PropertySchema]
    required: List[str]
    type: str


class ApiSchema(TypedDict, total=False):
    """API schema configuration for webhook tools"""

    auth_connection: Optional[Any]
    method: str
    path_params_schema: Dict[str, Any]
    query_params_schema: Optional[Dict[str, Any]]
    request_body_schema: RequestBodySchema
    request_headers: Dict[str, str]
    url: str


class DynamicVariables(TypedDict, total=False):
    """Dynamic variables configuration"""

    dynamic_variable_placeholders: Dict[str, Any]


class ToolConfig(TypedDict, total=False):
    """Complete configuration for an ElevenLabs webhook tool"""

    api_schema: ApiSchema
    assignments: List[Any]
    description: str
    disable_interruptions: bool
    dynamic_variables: DynamicVariables
    force_pre_tool_speech: bool
    name: str
    response_timeout_secs: int
    type: str


class WebhookToolset:
    def __init__(self, base_url: str, xi_api_key: str, agent_id: str, agent_name: str):
        self.app = FastAPI()
        self.base_url = base_url.rstrip("/")
        self.api_key = xi_api_key
        self.agent_id = agent_id
        self.agent_name = agent_name
        self.tools: List[ToolConfig] = []
        self.api_base = "https://api.elevenlabs.io"
        self.logger = logging.getLogger(f"webhook_toolset.{agent_name}")
        # Align logger level with the global/root logger
        root_level = logging.getLogger().getEffectiveLevel()
        if not self.logger.handlers:
            handler = logging.StreamHandler()
            formatter = logging.Formatter(
                "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
            )
            handler.setFormatter(formatter)
            handler.setLevel(root_level)
            self.logger.addHandler(handler)
        self.logger.setLevel(root_level)

        self.tool_ids: List[str] = []

    def _safe_error_payload(self, response: Any) -> str:
        """Return a best-effort string of error payload from a response."""
        try:
            data = response.json()
            return json.dumps(data)
        except Exception:
            try:
                return getattr(response, "text", "") or str(response)
            except Exception:
                return ""

    def tool(
        self,
        name: Optional[str] = None,
        description: Optional[str] = None,
        path: Optional[str] = None,
        auth_connection_id: Optional[str] = None,
        response_timeout_secs: int = 20,
        dynamic_variable_placeholders: Optional[Dict[str, Any]] = None,
        assignments: Optional[List[Any]] = None,
        disable_interruptions: bool = False,
        force_pre_tool_speech: str = "auto",
    ) -> Callable[[Callable[..., Any]], Callable[..., Any]]:
        """
        Decorator factory for creating ElevenLabs tools from functions.
        All tools use POST method and accept parameters as JSON body.

        Args:
            name: Name of the tool. Defaults to function name.
            description: Description of the tool. Defaults to function docstring.
            path: Route path. Defaults to "/{tool_name}".
            auth_connection_id: Optional auth connection ID.
            response_timeout_secs: Response timeout in seconds. Defaults to 20.
            dynamic_variable_placeholders: Dynamic variable placeholders dict.
            assignments: List of assignments for the tool.
            disable_interruptions: Whether to disable interruptions. Defaults to False.
            force_pre_tool_speech: Force pre-tool speech setting. Defaults to "auto".
        """

        def decorator(func: Callable[..., Any]) -> Callable[..., Any]:
            base_tool_name = name or func.__name__
            tool_name = f"{self.agent_name}_{base_tool_name}"
            desc = description or (func.__doc__ or "")
            route_path = path or f"/{base_tool_name}"

            self.logger.info(f"Registering tool: {tool_name} at {route_path}")

            sig = inspect.signature(func)
            params = sig.parameters

            input_model_schema: Dict[str, Union[str, Dict[str, Dict[str, str]], List[str]]] = {}
            if params:
                properties: Dict[str, Dict[str, str]] = {}
                required_fields: List[str] = []

                for pname, p in params.items():
                    param_type = (
                        p.annotation if p.annotation != inspect.Parameter.empty else str
                    )
                    json_type = self._get_json_type(param_type)
                    properties[pname] = {"type": json_type}

                    if p.default is inspect.Parameter.empty:
                        required_fields.append(pname)

                input_model_schema = {
                    "type": "object",
                    "properties": properties,
                    "required": required_fields,
                }

            async def endpoint(body: Dict[str, Any] = Body(default={})) -> Any:
                # Support both sync and async tool functions
                if inspect.iscoroutinefunction(func):
                    return await func(**body)
                return func(**body)

            self.app.add_api_route(route_path, endpoint, methods=["POST"])

            # Convert input_model_schema properties to proper format
            properties_schema: Dict[str, PropertySchema] = {}
            if input_model_schema and "properties" in input_model_schema:
                schema_properties = input_model_schema["properties"]
                if isinstance(schema_properties, dict):
                    for prop_name, _ in schema_properties.items():
                        properties_schema[prop_name] = PropertySchema(
                            type="string",
                            description=f"Parameter {prop_name}",
                            constant_value="",
                            dynamic_variable="",
                            enum=None,
                        )

            required_list: List[str] = []
            if input_model_schema:
                required_field = input_model_schema.get("required", [])
                if isinstance(required_field, list):
                    required_list = required_field

            request_body_schema = RequestBodySchema(
                type="object",
                properties=properties_schema,
                description="",
                required=required_list,
            )

            api_schema = ApiSchema(
                url=f"{self.base_url}{route_path}",
                method="POST",
                request_body_schema=request_body_schema,
                request_headers={},
                auth_connection=auth_connection_id,
                path_params_schema={},
                query_params_schema=None,
            )

            dynamic_vars = DynamicVariables(
                dynamic_variable_placeholders=dynamic_variable_placeholders or {}
            )

            tool_config = ToolConfig(
                type="webhook",
                name=tool_name,
                description=desc,
                api_schema=api_schema,
                response_timeout_secs=response_timeout_secs,
                dynamic_variables=dynamic_vars,
                assignments=assignments or [],
                disable_interruptions=disable_interruptions,
                force_pre_tool_speech=(
                    True if force_pre_tool_speech == "enabled" else False
                ),
            )

            self.tools.append(tool_config)
            return func

        return decorator

    def _get_json_type(self, python_type: Type[Any]) -> str:
        """
        Convert Python type annotation to JSON schema type string.

        Args:
            python_type: Python type to convert

        Returns:
            JSON schema type string, defaults to 'string' for unknown types
        """
        type_mapping = {
            str: "string",
            int: "integer",
            float: "number",
            bool: "boolean",
            list: "array",
            dict: "object",
        }
        return type_mapping.get(python_type, "string")

    def get_tool_configs(self) -> List[ToolConfig]:
        """
        Get all registered tool configurations.

        Returns:
            List of tool configuration dictionaries
        """
        return self.tools

    async def _get_agent(self) -> Optional[Dict[str, Any]]:
        """
        Retrieve agent information from ElevenLabs API by agent ID and validate name.

        Returns:
            Agent configuration dictionary if found and name matches, None otherwise
        """
        self.logger.info(
            f"Looking for agent: {self.agent_id} (expected name: {self.agent_name})"
        )
        async with httpx.AsyncClient() as client:
            headers = {"xi-api-key": self.api_key}

            try:
                self.logger.debug(f"Getting agent by ID: {self.agent_id}")
                response = await client.get(
                    f"{self.api_base}/v1/convai/agents/{self.agent_id}", headers=headers
                )
                if response.status_code == 200:
                    agent = response.json()
                    agent_name = agent.get("name", "")

                    self.logger.info(f"Found and validated agent: {agent_name}")
                    return agent
                else:
                    payload = self._safe_error_payload(response)
                    self.logger.error(
                        f"Failed to get agent, status: {response.status_code}, error: {payload}"
                    )
            except Exception as e:
                self.logger.error(f"Error getting agent: {e}")

            return None

    async def _attach_agent_tools(self) -> bool:
        self.logger.info(
            f"Updating tools for agent {self.agent_id} (name: {self.agent_name})"
        )
        async with httpx.AsyncClient() as client:
            headers = {"xi-api-key": self.api_key}

            try:
                self.logger.debug(f"Getting agent by ID: {self.agent_id}")
                body = {
                    "conversation_config": {
                        "agent": {"prompt": {"tool_ids": self.tool_ids}}
                    }
                }
                response = await client.patch(
                    f"{self.api_base}/v1/convai/agents/{self.agent_id}",
                    headers=headers,
                    json=body,
                )
                if response.status_code == 200:
                    self.logger.info(
                        f"Successfully updated tool config for agent {self.agent_name}"
                    )
                    payload = self._safe_error_payload(response)
                    self.logger.debug(f"Updated tool config: {payload}")
                    return True
                else:
                    payload = self._safe_error_payload(response)
                    self.logger.error(
                        f"Failed to attach tools to agent, status: {response.status_code}, error: {payload}"
                    )
            except Exception as e:
                self.logger.error(f"Error getting agent: {e}")

            return False

    async def _get_agent_tools(self, agent_id: str) -> List[Dict[str, Any]]:
        """
        Retrieve all tools configured in the workspace.

        Note: Based on the API documentation, tools are workspace-wide,
        not agent-specific. This method filters tools by agent name prefix.

        Args:
            agent_id: The ID of the agent (used for filtering by name prefix)

        Returns:
            List of tool configuration dictionaries for this agent
        """
        self.logger.info(f"Getting tools for agent: {self.agent_name}")
        async with httpx.AsyncClient() as client:
            headers = {"xi-api-key": self.api_key}
            try:
                response = await client.get(
                    f"{self.api_base}/v1/convai/tools", headers=headers
                )
                if response.status_code == 200:
                    all_tools = response.json().get("tools", [])
                    tool_names = [
                        tool.get("tool_config", {}).get("name", "unnamed")
                        for tool in all_tools
                    ]
                    self.logger.debug(f"All tool names from API: {tool_names}")
                    agent_tools = [
                        tool
                        for tool in all_tools
                        if tool.get("tool_config", {})
                        .get("name", "")
                        .startswith(f"{self.agent_name}_")
                    ]
                    self.logger.info(
                        f"Found {len(agent_tools)} tools for agent {self.agent_name} (out of {len(all_tools)} total)"
                    )
                    if agent_tools:
                        self.logger.debug(
                            f"Sample existing tool structure: {agent_tools[0]}"
                        )
                    elif all_tools:
                        self.logger.debug(
                            f"Sample tool structure (not our agent): {all_tools[0]}"
                        )
                    return agent_tools
                else:
                    payload = self._safe_error_payload(response)
                    self.logger.error(
                        f"Failed to get tools, status: {response.status_code}, error: {payload}"
                    )
                    return []
            except Exception as e:
                self.logger.error(f"Error getting tools: {e}")
                return []

    async def _create_tool(self, agent_id: str, tool_config: ToolConfig) -> bool:
        """
        Create a new tool in the workspace via ElevenLabs API.

        Args:
            agent_id: The ID of the agent (not used in API, kept for compatibility)
            tool_config: Complete tool configuration dictionary

        Returns:
            True if tool was created successfully, False otherwise
        """
        tool_name = tool_config.get("name", "unknown")
        self.logger.info(f"Creating tool: {tool_name}")
        async with httpx.AsyncClient() as client:
            headers = {"xi-api-key": self.api_key, "Content-Type": "application/json"}
            try:
                response = await client.post(
                    f"{self.api_base}/v1/convai/tools",
                    headers=headers,
                    json={"tool_config": tool_config},
                )
                if response.status_code in [200, 201]:
                    self.logger.info(f"Successfully created tool: {tool_name}")
                    try:
                        created_id = response.json().get("id")
                        if created_id:
                            self.tool_ids.append(created_id)
                    except Exception:
                        self.logger.error("Failed to parse tool creation response JSON for id")
                    return True
                else:
                    payload = self._safe_error_payload(response)
                    self.logger.error(
                        f"Failed to create tool: {tool_name}, status: {response.status_code}, error: {payload}"
                    )
                    return False
            except Exception as e:
                self.logger.error(f"Error creating tool {tool_name}: {e}")
                return False

    async def _update_tool(
        self, agent_id: str, tool_id: str, tool_config: ToolConfig
    ) -> bool:
        """
        Update an existing tool via ElevenLabs API.

        Note: Since the update endpoint is not available in the provided documentation,
        this method currently logs the need for an update but doesn't perform it.

        Args:
            agent_id: The ID of the agent (not used in API, kept for compatibility)
            tool_id: The ID of the tool to update
            tool_config: Complete updated tool configuration dictionary

        Returns:
            True if tool was updated successfully, False otherwise
        """
        tool_name = tool_config.get("name", "unknown")
        self.logger.info(f"Updating tool: {tool_name}")
        async with httpx.AsyncClient() as client:
            headers = {"xi-api-key": self.api_key, "Content-Type": "application/json"}
            try:
                response = await client.patch(
                    f"{self.api_base}/v1/convai/tools/{tool_id}",
                    headers=headers,
                    json={"tool_config": tool_config},
                )
                if response.status_code in [200, 201]:
                    self.logger.info(f"Successfully updated tool: {tool_name}")
                    return True
                else:
                    payload = self._safe_error_payload(response)
                    self.logger.error(
                        f"Failed to update tool: {tool_name}, status: {response.status_code}, error: {payload}"
                    )
                    return False
            except Exception as e:
                self.logger.error(f"Error updating tool {tool_name}: {e}")
                return False

    async def sync_tools(self) -> Dict[str, Union[str, int]]:
        """
        Synchronize local tool definitions with ElevenLabs API.

        Validates agent name matches expected value, then compares local tool
        configurations with remote ones using hash comparison. Creates new tools
        and updates existing ones that have changed.

        Returns:
            Dictionary containing sync results with status, counts, agent info
        """
        self.logger.info(f"Starting tool sync for {len(self.tools)} tools")
        agent = await self._get_agent()
        if not agent:
            error_msg = f"Cannot sync tools - agent validation failed (ID: {self.agent_id}, expected name: {self.agent_name})"
            self.logger.error(error_msg)
            return {"status": "error", "message": error_msg, "created": 0, "updated": 0}

        self.logger.info(f"Agent validated: {self.agent_name}")
        existing_tools = await self._get_agent_tools(self.agent_id)

        existing_tools_map: Dict[str, Dict[str, Any]] = {}
        for tool in existing_tools:
            tool_config = tool.get("tool_config", {})
            tool_name = tool_config.get("name")
            if tool_name:
                existing_tools_map[tool_name] = {
                    "id": tool.get("id"),
                    "tool_config": tool_config,
                }

        created = 0
        updated = 0

        for tool_config in self.tools:
            tool_name = tool_config.get("name", "")
            if not tool_name:
                continue

            if tool_name in existing_tools_map:
                existing_tool_data = existing_tools_map[tool_name]
                tool_id = existing_tool_data.get("id")
                if tool_id:
                    self.tool_ids.append(tool_id)
                existing_tool_config = existing_tool_data["tool_config"]

                if tool_config != existing_tool_config:
                    ic([tool_config, existing_tool_config])
                    self.logger.info(f"Tool {tool_name} needs updating")
                    if tool_id:
                        success = await self._update_tool(
                            self.agent_id, tool_id, tool_config
                        )
                        if success:
                            updated += 1
                else:
                    self.logger.debug(f"Tool {tool_name} is up to date")
            else:
                self.logger.info(f"Tool {tool_name} doesn't exist, creating")
                success = await self._create_tool(self.agent_id, tool_config)
                if success:
                    created += 1

        await self._attach_agent_tools()

        result = {
            "status": "success",
            "agent_id": self.agent_id,
            "agent_name": self.agent_name,
            "created": created,
            "updated": updated,
            "total_tools": len(self.tools),
        }
        self.logger.info(f"Tool sync complete: {result}")
        return result

    def run(self, host: str = "0.0.0.0", port: int = 8000, **kwargs: Any):
        """
        Start the FastAPI webhook server.

        Args:
            host: Host address to bind to
            port: Port number to listen on
            **kwargs: Additional arguments passed to uvicorn.run
        """
        uvicorn.run(self.app, host=host, port=port, **kwargs)

    async def serve(self, host: str = "0.0.0.0", port: int = 8000, **kwargs: Any):
        """
        Start the FastAPI webhook server asynchronously.

        Use this method when calling from within an async context.

        Args:
            host: Host address to bind to
            port: Port number to listen on
            **kwargs: Additional arguments passed to uvicorn.Config
        """
        config = uvicorn.Config(self.app, host=host, port=port, **kwargs)
        server = uvicorn.Server(config)
        await server.serve()
