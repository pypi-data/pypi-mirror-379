"""
ElevenTools - Use your Python functions as ElevenLabs agent tools

This library provides a convenient way to use your local functions with
ElevenLabs conversational AI agents through webhook integration.
"""

from .webhook_toolset import WebhookToolset

__version__ = "0.1.3"
__all__ = ["WebhookToolset"]
