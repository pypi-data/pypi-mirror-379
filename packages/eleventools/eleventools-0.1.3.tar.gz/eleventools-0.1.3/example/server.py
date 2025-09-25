#!/usr/bin/env python3
"""
Example ElevenLabs webhook server demonstrating tool integration.

This example shows how to create webhook tools for an ElevenLabs agent
and sync them with the API.
"""

import asyncio
import logging
import os
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from eleventools import WebhookToolset

def create_weather_server():
    """Create a webhook server with weather and utility tools."""
    
    # Configuration - replace with your actual values
    WEBHOOK_BASE_URL = os.getenv("WEBHOOK_BASE_URL", "https://your-domain.ngrok.io")
    ELEVENLABS_API_KEY = os.getenv("ELEVENLABS_API_KEY", "your_api_key_here")
    AGENT_ID = os.getenv("AGENT_ID", "your_agent_id_here")
    AGENT_NAME = os.getenv("AGENT_NAME", "your_agent_name_here")
    
    # Initialize the toolset
    toolset = WebhookToolset(
        base_url=WEBHOOK_BASE_URL,
        xi_api_key=ELEVENLABS_API_KEY,
        agent_id=AGENT_ID,
        agent_name=AGENT_NAME
    )
    
    # Weather tool
    @toolset.tool(
        name="get_weather",
        description="Get current weather information for any city"
    )
    def get_weather(city: str, units: str = "celsius"):
        """Get weather information for a specific city."""
        # In a real implementation, you'd call a weather API
        weather_data = {
            "city": city,
            "temperature": f"22°{units[0].upper()}",
            "condition": "Sunny",
            "humidity": "65%",
            "wind": "10 km/h"
        }
        return {
            "weather": weather_data,
            "message": f"Current weather in {city}: {weather_data['condition']}, {weather_data['temperature']}"
        }
    
    # Calculator tool
    @toolset.tool(
        name="calculate",
        description="Perform basic mathematical calculations"
    )
    def calculate(expression: str):
        """Safely evaluate mathematical expressions."""
        try:
            # Simple safety check for basic math operations
            allowed_chars = set('0123456789+-*/.() ')
            if not all(c in allowed_chars for c in expression):
                return {"error": "Only basic math operations are allowed"}
            
            result = eval(expression)
            return {
                "expression": expression,
                "result": result,
                "message": f"{expression} = {result}"
            }
        except Exception as e:
            return {"error": f"Calculation error: {str(e)}"}
    
    # Time zone tool
    @toolset.tool(
        name="get_timezone",
        description="Get current time in different time zones"
    )
    def get_timezone(timezone: str = "UTC"):
        """Get current time in the specified timezone."""
        from datetime import datetime
        import pytz
        
        try:
            tz = pytz.timezone(timezone)
            current_time = datetime.now(tz)
            formatted_time = current_time.strftime("%Y-%m-%d %H:%M:%S %Z")
            
            return {
                "timezone": timezone,
                "current_time": formatted_time,
                "message": f"Current time in {timezone}: {formatted_time}"
            }
        except Exception as e:
            return {"error": f"Timezone error: {str(e)}"}
    
    # Random fact tool
    @toolset.tool(
        name="random_fact",
        description="Get a random interesting fact"
    )
    def random_fact():
        """Return a random interesting fact."""
        import random
        
        facts = [
            "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old and still perfectly edible.",
            "Octopuses have three hearts and blue blood.",
            "A group of flamingos is called a 'flamboyance'.",
            "Bananas are berries, but strawberries aren't.",
            "The shortest war in history lasted only 38-45 minutes between Britain and Zanzibar in 1896.",
            "A shrimp's heart is in its head.",
            "It's impossible to hum while holding your nose closed.",
            "The word 'set' has the most different meanings in the English language."
        ]
        
        fact = random.choice(facts)
        return {
            "fact": fact,
            "message": f"Here's an interesting fact: {fact}"
        }
    
    return toolset


async def sync_and_run():
    """Sync tools with ElevenLabs API and start the server."""
    logging.basicConfig(level=logging.INFO)
    
    toolset = create_weather_server()
    
    print("🔧 Registered tools:")
    for tool in toolset.get_tool_configs():
        print(f"  - {tool['name']}: {tool['description']}")
    
    print("\n🔄 Syncing tools with ElevenLabs API...")
    try:
        sync_result = await toolset.sync_tools()
        if sync_result.get("status") == "success":
            print(f"✅ Sync complete: {sync_result}")
        else:
            print(f"❌ Sync failed: {sync_result.get('message', 'Unknown error')}")
            print("⚠️  Common issues:")
            print("   - Check that AGENT_ID is correct")
            print("   - Verify AGENT_NAME matches exactly (case-sensitive)")
            print("   - Ensure API key has proper permissions")
            print("⚠️  Continuing with server start anyway...")
    except Exception as e:
        print(f"❌ Sync failed with exception: {e}")
        print("⚠️  Continuing with server start...")
    
    print("\n🚀 Starting webhook server...")
    print("📋 Available endpoints:")
    for tool in toolset.get_tool_configs():
        tool_name = tool['name'].replace(f"{os.getenv('AGENT_NAME', 'agent')}_", "")
        print(f"  POST /{tool_name}")
    
    # Start the server
    await toolset.serve(host="0.0.0.0", port=8000)


if __name__ == "__main__":
    print("🌟 ElevenLabs Webhook Server Example")
    print("=" * 40)
    
    # Check for required environment variables
    required_vars = ["WEBHOOK_BASE_URL", "ELEVENLABS_API_KEY", "AGENT_ID", "AGENT_NAME"]
    missing_vars = [var for var in required_vars if not os.getenv(var)]
    
    if missing_vars:
        print("❌ Missing required environment variables:")
        for var in missing_vars:
            print(f"  - {var}")
        print("\nPlease set these environment variables and try again.")
        print("\nExample:")
        print("export WEBHOOK_BASE_URL='https://your-domain.ngrok.io'")
        print("export ELEVENLABS_API_KEY='your_api_key_here'")
        print("export AGENT_ID='your_agent_id_here'")
        print("export AGENT_NAME='your_agent_name_here'")
        sys.exit(1)
    
    # Run the async function
    asyncio.run(sync_and_run())