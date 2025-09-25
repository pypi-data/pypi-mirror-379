import pytest
from unittest.mock import AsyncMock, patch, MagicMock
from fastapi.testclient import TestClient
from eleventools.webhook_toolset import WebhookToolset, ToolConfig, ApiSchema, RequestBodySchema, PropertySchema


class TestWebhookToolsetBasic:
    """Test basic WebhookToolset functionality without API calls."""

    def test_init(self):
        """Test WebhookToolset initialization."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        assert tools.base_url == "http://localhost:8000"
        assert tools.api_key == "test-api-key"
        assert tools.agent_id == "test_agent_id"
        assert tools.agent_name == "test_agent"
        assert tools.tools == []
        assert tools.tool_ids == []
        assert tools.app is not None
        assert tools.api_base == "https://api.elevenlabs.io"
    
    def test_init_strips_trailing_slash(self):
        """Test that trailing slash is stripped from base_url."""
        tools = WebhookToolset("http://localhost:8000/", "test-api-key", "test_agent_id", "test_agent")
        assert tools.base_url == "http://localhost:8000"
    
    def test_simple_tool_decorator(self):
        """Test basic tool decorator functionality."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        
        @tools.tool()
        def simple_function():
            """A simple test function."""
            return {"status": "success"}
        
        assert len(tools.tools) == 1
        tool_config = tools.tools[0]
        
        assert tool_config["name"] == "test_agent_simple_function"
        assert tool_config["description"] == "A simple test function."
        assert tool_config["type"] == "webhook"
        assert tool_config["api_schema"]["method"] == "POST"
        assert tool_config["api_schema"]["url"] == "http://localhost:8000/simple_function"
        assert tool_config["api_schema"]["path_params_schema"] == {}
        assert tool_config["api_schema"]["query_params_schema"] is None
        assert tool_config["api_schema"]["request_body_schema"]["type"] == "object"
        assert tool_config["api_schema"]["request_body_schema"]["properties"] == {}
        assert tool_config["api_schema"]["request_headers"] == {}
        assert tool_config["api_schema"]["auth_connection"] is None
        assert tool_config["response_timeout_secs"] == 20
        assert tool_config["dynamic_variables"]["dynamic_variable_placeholders"] == {}
        assert tool_config["assignments"] == []
        assert tool_config["disable_interruptions"] is False
        assert tool_config["force_pre_tool_speech"] is False

    def test_async_tool_decorator(self):
        """Test tool decorator works with async functions."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")

        @tools.tool()
        async def async_function(x: int):
            return {"double": x * 2}

        client = TestClient(tools.app)
        response = client.post("/async_function", json={"x": 7})
        assert response.status_code == 200
        assert response.json() == {"double": 14}
    
    def test_tool_with_custom_parameters(self):
        """Test tool decorator with custom parameters."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        
        @tools.tool(
            name="custom_tool",
            description="Custom description",
            path="/custom/path",
            auth_connection_id="auth123",
            response_timeout_secs=30,
            dynamic_variable_placeholders={"var1": "value1"},
            assignments=["assignment1"],
            disable_interruptions=True,
            force_pre_tool_speech="enabled"
        )
        def custom_function():
            return {"result": "custom"}
        
        tool_config = tools.tools[0]
        
        assert tool_config["name"] == "test_agent_custom_tool"
        assert tool_config["description"] == "Custom description"
        assert tool_config["api_schema"]["method"] == "POST"
        assert tool_config["api_schema"]["url"] == "http://localhost:8000/custom/path"
        assert tool_config["api_schema"]["auth_connection"] == "auth123"
        assert tool_config["response_timeout_secs"] == 30
        assert tool_config["dynamic_variables"]["dynamic_variable_placeholders"] == {"var1": "value1"}
        assert tool_config["assignments"] == ["assignment1"]
        assert tool_config["disable_interruptions"] is True
        assert tool_config["force_pre_tool_speech"] is True
    
    def test_tool_with_parameters(self):
        """Test tool with function parameters."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        
        @tools.tool()
        def search_function(query: str, limit: int = 10, include_meta: bool = False):
            return {"query": query, "limit": limit, "meta": include_meta}
        
        tool_config = tools.tools[0]
        body_schema = tool_config["api_schema"]["request_body_schema"]
        
        assert body_schema["type"] == "object"
        assert body_schema["properties"]["query"]["type"] == "string"
        assert body_schema["properties"]["query"]["description"] == "Parameter query"
        assert body_schema["properties"]["query"]["constant_value"] == ""
        assert body_schema["properties"]["query"]["dynamic_variable"] == ""
        assert body_schema["properties"]["query"]["enum"] is None
        assert body_schema["properties"]["limit"]["type"] == "string"
        assert body_schema["properties"]["include_meta"]["type"] == "string"
        assert body_schema["required"] == ["query"]  # only query has no default
        
        # Verify no query or path params since everything goes in body
        assert tool_config["api_schema"]["query_params_schema"] is None
        assert tool_config["api_schema"]["path_params_schema"] == {}
    
    def test_get_json_type(self):
        """Test _get_json_type helper method."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        
        assert tools._get_json_type(str) == "string"
        assert tools._get_json_type(int) == "integer"
        assert tools._get_json_type(float) == "number"
        assert tools._get_json_type(bool) == "boolean"
        assert tools._get_json_type(list) == "array"
        assert tools._get_json_type(dict) == "object"
        assert tools._get_json_type(object) == "string"  # default fallback
    
    def test_get_tool_configs(self):
        """Test get_tool_configs method."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        
        @tools.tool()
        def tool1():
            return {"tool": 1}
        
        @tools.tool()
        def tool2():
            return {"tool": 2}
        
        configs = tools.get_tool_configs()
        assert len(configs) == 2
        assert configs[0]["name"] == "test_agent_tool1"
        assert configs[1]["name"] == "test_agent_tool2"
        assert isinstance(configs[0], dict)
        assert isinstance(configs[1], dict)
    
    def test_multiple_decorators(self):
        """Test applying multiple tool decorators."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        
        @tools.tool(name="first_tool")
        def func1():
            return {"tool": "first"}
        
        @tools.tool(name="second_tool")
        def func2():
            return {"tool": "second"}
        
        assert len(tools.tools) == 2
        assert tools.tools[0]["name"] == "test_agent_first_tool"
        assert tools.tools[1]["name"] == "test_agent_second_tool"
        assert tools.tools[0]["api_schema"]["method"] == "POST"
        assert tools.tools[1]["api_schema"]["method"] == "POST"
    
    def test_empty_function_parameters(self):
        """Test function with no parameters."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        
        @tools.tool()
        def no_params():
            return {"status": "ok"}
        
        tool_config = tools.tools[0]
        assert tool_config["api_schema"]["query_params_schema"] is None
        assert tool_config["api_schema"]["path_params_schema"] == {}
        assert tool_config["api_schema"]["request_body_schema"]["properties"] == {}
    
    def test_function_without_docstring(self):
        """Test function without docstring uses empty description."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        
        @tools.tool()
        def no_docstring():
            return {"result": "test"}
        
        tool_config = tools.tools[0]
        assert tool_config["description"] == ""


class TestWebhookServerFunctionality:
    """Test FastAPI webhook server functionality."""
    
    def test_fastapi_integration(self):
        """Test FastAPI integration by making actual HTTP requests."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        
        @tools.tool()
        def hello_world():
            """Returns a hello world message."""
            return {"message": "Hello, World!"}
        
        @tools.tool()
        def get_user(user_id: str):
            return {"user_id": user_id}
        
        @tools.tool()
        def create_user(message: str, count: int = 1):
            return {"created": message, "count": count}
        
        client = TestClient(tools.app)
        
        # Test POST endpoint with no parameters
        response = client.post("/hello_world", json={})
        assert response.status_code == 200
        assert response.json() == {"message": "Hello, World!"}
        
        # Test POST endpoint with parameters in JSON body
        response = client.post("/get_user", json={"user_id": "123"})
        assert response.status_code == 200
        assert response.json() == {"user_id": "123"}
        
        # Test POST with optional parameters
        response = client.post("/create_user", json={"message": "test user", "count": 5})
        assert response.status_code == 200
        assert response.json() == {"created": "test user", "count": 5}
        
        # Test POST with only required parameters (optional gets default)
        response = client.post("/create_user", json={"message": "test user"})
        assert response.status_code == 200
        assert response.json() == {"created": "test user", "count": 1}
    
    def test_custom_path_with_parameters(self):
        """Test custom path with function parameters."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        
        @tools.tool(path="/api/custom")
        def custom_path_func(data: str):
            return {"data": data}
        
        tool_config = tools.tools[0]
        
        # URL should use custom path
        assert tool_config["api_schema"]["url"] == "http://localhost:8000/api/custom"
        
        # Parameters should be in request body
        body_schema = tool_config["api_schema"]["request_body_schema"]
        assert body_schema["properties"]["data"]["type"] == "string"
        assert body_schema["required"] == ["data"]
        
        # Test the actual endpoint
        client = TestClient(tools.app)
        response = client.post("/api/custom", json={"data": "test"})
        assert response.status_code == 200
        assert response.json() == {"data": "test"}
    
    def test_mixed_parameter_types(self):
        """Test function with mixed parameter types."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        
        @tools.tool()
        def mixed_params(id: int, query: str, optional_flag: bool = True):
            return {"id": id, "query": query, "flag": optional_flag}
        
        # Test the endpoint works
        client = TestClient(tools.app)
        response = client.post("/mixed_params", json={"id": 123, "query": "test", "optional_flag": False})
        assert response.status_code == 200
        assert response.json() == {"id": 123, "query": "test", "flag": False}


class TestElevenLabsAPIIntegration:
    """Test ElevenLabs API integration with mocks."""

    @pytest.fixture
    def toolset(self):
        """Create a WebhookToolset instance for testing."""
        return WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")

    @pytest.mark.asyncio
    async def test_get_agent_success(self, toolset):
        """Test successful agent retrieval."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "id": "test_agent_id",
            "name": "test_agent",
            "description": "Test agent"
        }

        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)
            
            result = await toolset._get_agent()
            
            assert result is not None
            assert result["name"] == "test_agent"
            mock_client.return_value.__aenter__.return_value.get.assert_called_once_with(
                "https://api.elevenlabs.io/v1/convai/agents/test_agent_id",
                headers={"xi-api-key": "test-api-key"}
            )

    

    @pytest.mark.asyncio
    async def test_get_agent_not_found(self, toolset):
        """Test agent retrieval when agent not found."""
        mock_response = MagicMock()
        mock_response.status_code = 404

        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)
            
            result = await toolset._get_agent()
            
            assert result is None

    @pytest.mark.asyncio
    async def test_get_agent_tools_success(self, toolset):
        """Test successful tools retrieval and filtering."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            "tools": [
                {
                    "id": "tool1",
                    "tool_config": {
                        "name": "test_agent_tool1",
                        "description": "Tool 1"
                    }
                },
                {
                    "id": "tool2",
                    "tool_config": {
                        "name": "other_agent_tool2",
                        "description": "Tool 2"
                    }
                },
                {
                    "id": "tool3",
                    "tool_config": {
                        "name": "test_agent_tool3",
                        "description": "Tool 3"
                    }
                }
            ]
        }

        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value.get = AsyncMock(return_value=mock_response)
            
            result = await toolset._get_agent_tools("test_agent_id")
            
            # Should only return tools with matching agent name prefix
            assert len(result) == 2
            assert result[0]["tool_config"]["name"] == "test_agent_tool1"
            assert result[1]["tool_config"]["name"] == "test_agent_tool3"
            
            mock_client.return_value.__aenter__.return_value.get.assert_called_once_with(
                "https://api.elevenlabs.io/v1/convai/tools",
                headers={"xi-api-key": "test-api-key"}
            )

    @pytest.mark.asyncio
    async def test_create_tool_success(self, toolset):
        """Test successful tool creation."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "new_tool_id"}

        tool_config = ToolConfig(
            name="test_agent_new_tool",
            description="A new tool",
            type="webhook"
        )

        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value.post = AsyncMock(return_value=mock_response)
            
            result = await toolset._create_tool("test_agent_id", tool_config)
            
            assert result is True
            mock_client.return_value.__aenter__.return_value.post.assert_called_once_with(
                "https://api.elevenlabs.io/v1/convai/tools",
                headers={"xi-api-key": "test-api-key", "Content-Type": "application/json"},
                json={"tool_config": tool_config}
            )

    @pytest.mark.asyncio
    async def test_create_tool_failure(self, toolset):
        """Test failed tool creation."""
        mock_response = MagicMock()
        mock_response.status_code = 422
        mock_response.json.return_value = {"detail": "Validation error"}

        tool_config = ToolConfig(
            name="test_agent_new_tool",
            description="A new tool",
            type="webhook"
        )

        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value.post = AsyncMock(return_value=mock_response)
            
            result = await toolset._create_tool("test_agent_id", tool_config)
            
            assert result is False

    @pytest.mark.asyncio
    async def test_update_tool_success(self, toolset):
        """Test successful tool update."""
        mock_response = MagicMock()
        mock_response.status_code = 200
        mock_response.json.return_value = {"id": "updated_tool_id"}

        tool_config = ToolConfig(
            name="test_agent_updated_tool",
            description="An updated tool",
            type="webhook"
        )

        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value.patch = AsyncMock(return_value=mock_response)
            
            result = await toolset._update_tool("test_agent_id", "tool_id", tool_config)

            # Successful update should return True
            assert result is True
            mock_client.return_value.__aenter__.return_value.patch.assert_called_once_with(
                "https://api.elevenlabs.io/v1/convai/tools/tool_id",
                headers={"xi-api-key": "test-api-key", "Content-Type": "application/json"},
                json={"tool_config": tool_config}
            )

    @pytest.mark.asyncio
    async def test_attach_agent_tools_success(self, toolset):
        """Test successful tool attachment to agent."""
        toolset.tool_ids = ["tool1", "tool2"]
        
        mock_response = MagicMock()
        mock_response.status_code = 200

        with patch("httpx.AsyncClient") as mock_client:
            mock_client.return_value.__aenter__.return_value.patch = AsyncMock(return_value=mock_response)
            
            result = await toolset._attach_agent_tools()
            
            assert result is True
            expected_body = {
                "conversation_config": {
                    "agent": {"prompt": {"tool_ids": ["tool1", "tool2"]}}
                }
            }
            mock_client.return_value.__aenter__.return_value.patch.assert_called_once_with(
                "https://api.elevenlabs.io/v1/convai/agents/test_agent_id",
                headers={"xi-api-key": "test-api-key"},
                json=expected_body
            )

    @pytest.mark.asyncio
    async def test_sync_tools_create_new(self, toolset):
        """Test syncing tools when tools need to be created."""
        # Add a tool to the toolset
        @toolset.tool()
        def test_function():
            return {"result": "test"}

        # Mock agent retrieval success
        mock_agent_response = MagicMock()
        mock_agent_response.status_code = 200
        mock_agent_response.json.return_value = {"name": "test_agent"}

        # Mock tools retrieval - no existing tools
        mock_tools_response = MagicMock()
        mock_tools_response.status_code = 200
        mock_tools_response.json.return_value = {"tools": []}

        # Mock tool creation success
        mock_create_response = MagicMock()
        mock_create_response.status_code = 200
        mock_create_response.json.return_value = {"id": "new_tool_id"}

        # Mock agent tools attachment success
        mock_attach_response = MagicMock()
        mock_attach_response.status_code = 200

        with patch("httpx.AsyncClient") as mock_client:
            mock_http_client = mock_client.return_value.__aenter__.return_value
            mock_http_client.get = AsyncMock(side_effect=[mock_agent_response, mock_tools_response])
            mock_http_client.post = AsyncMock(return_value=mock_create_response)
            mock_http_client.patch = AsyncMock(return_value=mock_attach_response)
            
            result = await toolset.sync_tools()
            
            assert result["status"] == "success"
            assert result["created"] == 1
            assert result["updated"] == 0
            assert result["total_tools"] == 1
            
            # Verify agent tools attachment was called
            mock_http_client.patch.assert_called()

    @pytest.mark.asyncio
    async def test_sync_tools_attach_all_ids_when_mixed(self, toolset):
        """When some tools exist and some are new, attach all IDs."""
        # Define two tools locally
        @toolset.tool()
        def tool_one():
            return {"result": "one"}

        @toolset.tool()
        def tool_two():
            return {"result": "two"}

        # Existing tools response contains only tool_one with same config
        existing_tool_config = toolset.tools[0]

        mock_agent_response = MagicMock()
        mock_agent_response.status_code = 200
        mock_agent_response.json.return_value = {"name": "test_agent"}

        mock_tools_response = MagicMock()
        mock_tools_response.status_code = 200
        mock_tools_response.json.return_value = {
            "tools": [
                {
                    "id": "existing_tool_id",
                    "tool_config": existing_tool_config,
                }
            ]
        }

        # Creating tool_two returns new_tool_id
        mock_create_response = MagicMock()
        mock_create_response.status_code = 200
        mock_create_response.json.return_value = {"id": "new_tool_id"}

        # Agent attachment success
        mock_attach_response = MagicMock()
        mock_attach_response.status_code = 200

        with patch("httpx.AsyncClient") as mock_client:
            mock_http_client = mock_client.return_value.__aenter__.return_value
            mock_http_client.get = AsyncMock(side_effect=[mock_agent_response, mock_tools_response])
            mock_http_client.post = AsyncMock(return_value=mock_create_response)
            mock_http_client.patch = AsyncMock(return_value=mock_attach_response)

            result = await toolset.sync_tools()

            assert result["status"] == "success"
            # One created (tool_two), zero updated; totals should reflect both tools defined
            assert result["created"] == 1
            assert result["updated"] == 0
            assert result["total_tools"] == 2

            # Verify that agent was updated with both IDs: existing + newly created
            expected_body = {
                "conversation_config": {
                    "agent": {"prompt": {"tool_ids": ["existing_tool_id", "new_tool_id"]}}
                }
            }
            mock_http_client.patch.assert_called_with(
                "https://api.elevenlabs.io/v1/convai/agents/test_agent_id",
                headers={"xi-api-key": "test-api-key"},
                json=expected_body,
            )

    @pytest.mark.asyncio
    async def test_sync_tools_up_to_date(self, toolset):
        """Test syncing tools when tools are up to date."""
        # Add a tool to the toolset
        @toolset.tool()
        def test_function():
            return {"result": "test"}

        # Mock agent retrieval success
        mock_agent_response = MagicMock()
        mock_agent_response.status_code = 200
        mock_agent_response.json.return_value = {"name": "test_agent"}

        # Mock tools retrieval - existing tool with same config
        existing_tool_config = toolset.tools[0]
        mock_tools_response = MagicMock()
        mock_tools_response.status_code = 200
        mock_tools_response.json.return_value = {
            "tools": [{
                "id": "existing_tool_id",
                "tool_config": existing_tool_config
            }]
        }

        # Mock agent tools attachment success
        mock_attach_response = MagicMock()
        mock_attach_response.status_code = 200

        with patch("httpx.AsyncClient") as mock_client:
            mock_http_client = mock_client.return_value.__aenter__.return_value
            mock_http_client.get = AsyncMock(side_effect=[mock_agent_response, mock_tools_response])
            mock_http_client.patch = AsyncMock(return_value=mock_attach_response)
            
            result = await toolset.sync_tools()
            
            assert result["status"] == "success"
            assert result["created"] == 0
            assert result["updated"] == 0
            assert result["total_tools"] == 1
            assert toolset.tool_ids == ["existing_tool_id"]

    @pytest.mark.asyncio
    async def test_sync_tools_agent_validation_failure(self, toolset):
        """Test syncing tools when agent validation fails."""
        mock_agent_response = MagicMock()
        mock_agent_response.status_code = 404

        with patch("httpx.AsyncClient") as mock_client:
            mock_http_client = mock_client.return_value.__aenter__.return_value
            mock_http_client.get = AsyncMock(return_value=mock_agent_response)
            
            result = await toolset.sync_tools()
            
            assert result["status"] == "error"
            assert result["created"] == 0
            assert result["updated"] == 0



class TestToolConfigTypes:
    """Test TypedDict tool configuration types."""
    
    def test_property_schema_structure(self):
        """Test PropertySchema TypedDict structure."""
        prop = PropertySchema(
            type="string",
            description="Test property",
            constant_value="",
            dynamic_variable="",
            enum=None
        )
        
        assert prop["type"] == "string"
        assert prop["description"] == "Test property"
        assert prop["constant_value"] == ""
        assert prop["dynamic_variable"] == ""
        assert prop["enum"] is None
    
    def test_request_body_schema_structure(self):
        """Test RequestBodySchema TypedDict structure."""
        schema = RequestBodySchema(
            type="object",
            description="Test schema",
            properties={"test": PropertySchema(type="string", description="Test")},
            required=["test"]
        )
        
        assert schema["type"] == "object"
        assert schema["description"] == "Test schema"
        assert "test" in schema["properties"]
        assert schema["required"] == ["test"]
    
    def test_api_schema_structure(self):
        """Test ApiSchema TypedDict structure."""
        api_schema = ApiSchema(
            url="http://test.com",
            method="POST",
            request_body_schema=RequestBodySchema(type="object", properties={}, required=[]),
            request_headers={},
            path_params_schema={},
            query_params_schema=None,
            auth_connection=None
        )
        
        assert api_schema["url"] == "http://test.com"
        assert api_schema["method"] == "POST"
        assert api_schema["request_body_schema"]["type"] == "object"
        assert api_schema["request_headers"] == {}
        assert api_schema["path_params_schema"] == {}
        assert api_schema["query_params_schema"] is None
        assert api_schema["auth_connection"] is None
    
    def test_tool_config_structure(self):
        """Test ToolConfig TypedDict structure."""
        tool_config = ToolConfig(
            type="webhook",
            name="test_tool",
            description="Test tool",
            api_schema=ApiSchema(
                url="http://test.com",
                method="POST",
                request_body_schema=RequestBodySchema(type="object", properties={}, required=[]),
                request_headers={},
                path_params_schema={},
                query_params_schema=None,
                auth_connection=None
            ),
            response_timeout_secs=20,
            dynamic_variables={"dynamic_variable_placeholders": {}},
            assignments=[],
            disable_interruptions=False,
            force_pre_tool_speech=False
        )
        
        assert tool_config["type"] == "webhook"
        assert tool_config["name"] == "test_tool"
        assert tool_config["description"] == "Test tool"
        assert tool_config["api_schema"]["method"] == "POST"
        assert tool_config["response_timeout_secs"] == 20
        assert tool_config["dynamic_variables"]["dynamic_variable_placeholders"] == {}
        assert tool_config["assignments"] == []
        assert tool_config["disable_interruptions"] is False
        assert tool_config["force_pre_tool_speech"] is False


class TestElevenLabsCompatibility:
    """Test compatibility with ElevenLabs API expectations."""
    
    def test_tool_config_matches_api_format(self):
        """Test that generated tool configs match ElevenLabs API format."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "test_agent_id", "test_agent")
        
        @tools.tool(
            description="Test weather tool",
            response_timeout_secs=30,
            disable_interruptions=True
        )
        def get_weather(city: str, units: str = "celsius"):
            """Get weather for a city."""
            return {"weather": f"Sunny in {city}", "units": units}
        
        tool_config = tools.tools[0]
        
        # Verify all required fields are present
        assert "type" in tool_config
        assert "name" in tool_config
        assert "description" in tool_config
        assert "api_schema" in tool_config
        assert "response_timeout_secs" in tool_config
        assert "dynamic_variables" in tool_config
        assert "assignments" in tool_config
        assert "disable_interruptions" in tool_config
        assert "force_pre_tool_speech" in tool_config
        
        # Verify api_schema structure
        api_schema = tool_config["api_schema"]
        assert "url" in api_schema
        assert "method" in api_schema
        assert "request_body_schema" in api_schema
        assert "request_headers" in api_schema
        assert "path_params_schema" in api_schema
        assert "query_params_schema" in api_schema
        assert "auth_connection" in api_schema
        
        # Verify request_body_schema structure
        body_schema = api_schema["request_body_schema"]
        assert body_schema["type"] == "object"
        assert "properties" in body_schema
        assert "required" in body_schema
        assert "description" in body_schema
        
        # Verify property structure
        city_prop = body_schema["properties"]["city"]
        assert city_prop["type"] == "string"
        assert city_prop["description"] == "Parameter city"
        assert city_prop["constant_value"] == ""
        assert city_prop["dynamic_variable"] == ""
        assert city_prop["enum"] is None
        
        # Verify required fields
        assert body_schema["required"] == ["city"]  # units has default value
    
    def test_agent_name_prefixing(self):
        """Test that tool names are properly prefixed with agent name."""
        tools = WebhookToolset("http://localhost:8000", "test-api-key", "my_agent_123", "test_agent")
        
        @tools.tool(name="weather")
        def get_weather():
            return {}
        
        @tools.tool()  # No name provided, should use function name
        def calculate():
            return {}
        
        assert tools.tools[0]["name"] == "test_agent_weather"
        assert tools.tools[1]["name"] == "test_agent_calculate"
    
    def test_webhook_url_generation(self):
        """Test that webhook URLs are generated correctly."""
        tools = WebhookToolset("https://myapp.com:8080", "test-api-key", "agent1", "test_agent")
        
        @tools.tool()
        def process_data():
            return {}
        
        @tools.tool(path="/custom/webhook")
        def custom_path():
            return {}
        
        assert tools.tools[0]["api_schema"]["url"] == "https://myapp.com:8080/process_data"
        assert tools.tools[1]["api_schema"]["url"] == "https://myapp.com:8080/custom/webhook"
