#!/usr/bin/env python3
"""
Simple ElevenLabs webhook server example.

A minimal example showing basic tool creation and server setup.
"""

import asyncio
import os
from pathlib import Path
import sys

# Add parent directory to path for imports
sys.path.append(str(Path(__file__).parent.parent))

from eleventools import WebhookToolset


async def main():
    """Simple example with basic tools."""
    
    # Configuration
    BASE_URL = "http://localhost:8000"  # Change to your ngrok URL for production
    API_KEY = "your_api_key_here"       # Replace with your actual API key
    AGENT_ID = "your_agent_id_here"     # Replace with your actual agent ID
    AGENT_NAME = "your_agent_name"      # Replace with your actual agent name
    
    # Create toolset
    toolset = WebhookToolset(
        base_url=BASE_URL,
        xi_api_key=API_KEY,
        agent_id=AGENT_ID,
        agent_name=AGENT_NAME
    )
    
    # Simple greeting tool
    @toolset.tool(
        name="greet",
        description="Generate a personalized greeting message"
    )
    def greet_user(name: str, language: str = "english"):
        """Generate a greeting in different languages."""
        greetings = {
            "english": f"Hello, {name}! Nice to meet you!",
            "spanish": f"¡Hola, {name}! ¡Mucho gusto!",
            "french": f"Bonjour, {name}! Ravi de vous rencontrer!",
            "german": f"Hallo, {name}! Freut mich, Sie kennenzulernen!"
        }
        
        greeting = greetings.get(language.lower(), greetings["english"])
        return {
            "greeting": greeting,
            "language": language,
            "name": name
        }
    
    # Echo tool
    @toolset.tool(
        name="echo",
        description="Echo back the provided message"
    )
    def echo_message(message: str):
        """Echo the message back to the user."""
        return {
            "original": message,
            "echoed": f"You said: {message}",
            "length": len(message)
        }
    
    # Show registered tools
    print("Registered tools:")
    for tool in toolset.get_tool_configs():
        print(f"  - {tool['name']}: {tool['description']}")
    
    # Uncomment the following lines when you have valid credentials:
    # print("\nSyncing tools...")
    # result = await toolset.sync_tools()
    # print(f"Sync result: {result}")
    
    # Start server
    print(f"\nStarting server at {BASE_URL}")
    print("Test endpoints:")
    print(f"  POST {BASE_URL}/greet")
    print(f"  POST {BASE_URL}/echo")
    
    await toolset.serve(port=8000)


if __name__ == "__main__":
    asyncio.run(main())