# ElevenLabs Webhook Server Example

This example demonstrates how to create and deploy webhook tools for ElevenLabs agents using the `WebhookToolset` class.

## Features

The example server includes several sample tools:

- **🌤️ Weather Tool** - Get current weather for any city
- **🔢 Calculator Tool** - Perform basic mathematical calculations  
- **🕐 Timezone Tool** - Get current time in different timezones
- **🎲 Random Fact Tool** - Get interesting random facts

## Setup

### 1. Install Dependencies

```bash
# Install required packages
pip install pytz  # for timezone tool
```

### 2. Environment Variables

Set the following environment variables:

```bash
export WEBHOOK_BASE_URL="https://your-domain.ngrok.io"
export ELEVENLABS_API_KEY="your_api_key_here" 
export AGENT_ID="your_agent_id_here"
export AGENT_NAME="your_agent_name_here"
```

**Getting these values:**

- **WEBHOOK_BASE_URL**: Your publicly accessible webhook URL (use ngrok for local development)
- **ELEVENLABS_API_KEY**: Get from [ElevenLabs dashboard](https://elevenlabs.io/app/settings/api-keys)
- **AGENT_ID**: Your ElevenLabs agent ID from the agents dashboard
- **AGENT_NAME**: Your agent's name (must match exactly, case-sensitive)

### 3. Expose Your Server (Development)

For local development, use ngrok to expose your server:

```bash
# Install ngrok if you haven't already
# Then run:
ngrok http 8000
```

Copy the HTTPS URL (e.g., `https://abc123.ngrok.io`) and set it as your `WEBHOOK_BASE_URL`.

## Running the Server

```bash
cd example
python server.py
```

The server will:
1. Register all webhook tools
2. Sync them with your ElevenLabs agent via API
3. Start the FastAPI server on port 8000

## Example Output

```
🌟 ElevenLabs Webhook Server Example
========================================
🔧 Registered tools:
  - your_agent_name_get_weather: Get current weather information for any city
  - your_agent_name_calculate: Perform basic mathematical calculations
  - your_agent_name_get_timezone: Get current time in different time zones
  - your_agent_name_random_fact: Get a random interesting fact

🔄 Syncing tools with ElevenLabs API...
✅ Sync complete: {'status': 'success', 'agent_id': 'your_agent_id', 'agent_name': 'your_agent_name', 'created': 4, 'updated': 0, 'total_tools': 4}

🚀 Starting webhook server...
📋 Available endpoints:
  POST /get_weather
  POST /calculate
  POST /get_timezone
  POST /random_fact
```

## Testing the Tools

You can test the webhook endpoints directly:

```bash
# Test weather tool
curl -X POST http://localhost:8000/get_weather \
  -H "Content-Type: application/json" \
  -d '{"city": "New York", "units": "fahrenheit"}'

# Test calculator
curl -X POST http://localhost:8000/calculate \
  -H "Content-Type: application/json" \
  -d '{"expression": "2 + 2 * 3"}'

# Test timezone
curl -X POST http://localhost:8000/get_timezone \
  -H "Content-Type: application/json" \
  -d '{"timezone": "America/New_York"}'

# Test random fact
curl -X POST http://localhost:8000/random_fact \
  -H "Content-Type: application/json" \
  -d '{}'
```

## Using with ElevenLabs Agent

Once your tools are synced, your ElevenLabs agent will be able to call them during conversations. The agent will automatically:

1. Detect when a tool is needed based on the conversation
2. Call the appropriate webhook endpoint with the required parameters
3. Use the response to continue the conversation

## Customizing Tools

To add your own tools, simply use the `@toolset.tool()` decorator:

```python
@toolset.tool(
    name="my_custom_tool",
    description="Description of what your tool does"
)
def my_custom_tool(param1: str, param2: int = 10):
    """Your tool implementation."""
    return {"result": f"Processed {param1} with {param2}"}
```

## Production Deployment

For production deployment:

1. **Use a production WSGI server** like Gunicorn:
   ```bash
   pip install gunicorn
   gunicorn -w 4 -k uvicorn.workers.UvicornWorker server:app
   ```

2. **Deploy to a cloud service** (AWS, GCP, Azure, etc.)

3. **Set up proper environment variable management**

4. **Configure HTTPS** with a valid SSL certificate

5. **Add authentication** if needed for your webhook endpoints

## Troubleshooting

- **Tools not syncing**: Check your API key and agent ID
- **Webhooks not reachable**: Ensure your WEBHOOK_BASE_URL is publicly accessible
- **Tool errors**: Check the server logs for detailed error messages
- **Agent not using tools**: Verify the tool descriptions are clear and the agent has the tools enabled