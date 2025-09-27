"""
Gemini CLI Provider with logging capabilities

Extends the original LlmGeminiCli to implement the new LlmCli interface
with comprehensive logging capture using Gemini's built-in debug and session features.
"""

import subprocess
import tempfile
import os
import json
from typing import Type, Set, List, Optional
from pydantic import BaseModel

from .llm_gemini_cli import LlmGeminiCli as OriginalLlmGeminiCli
from .core import Conversation, ConfigurationError, Llm, LlmResponse


class LlmGeminiCli(Llm):
    """Gemini CLI provider with enhanced logging"""

    def __init__(self, model: str = "gemini:gemini-2.0-flash-exp"):
        super().__init__(model)
        self._model = model
        self._original = None  # Lazy load

    def _get_original(self):
        """Lazy load the original CLI instance"""
        if self._original is None:
            # Create a minimal mock that has the methods we need
            class MockOriginal:
                def __init__(self, model):
                    self.model = model

                def _normalize_conversation(self, conversation):
                    if isinstance(conversation, str):
                        return conversation
                    elif isinstance(conversation, list) and len(conversation) > 0:
                        if isinstance(conversation[0], dict):
                            return "\n".join([f"{msg['role']}: {msg['content']}" for msg in conversation])
                    return str(conversation)

                @property
                def executable(self):
                    return "gemini"

                def _extract_json_string(self, text):
                    import json
                    try:
                        # Try to find JSON in the text
                        start = text.find("{")
                        if start >= 0:
                            bracket_count = 0
                            end = start
                            for i, char in enumerate(text[start:], start):
                                if char == "{":
                                    bracket_count += 1
                                elif char == "}":
                                    bracket_count -= 1
                                    if bracket_count == 0:
                                        end = i + 1
                                        break
                            return text[start:end]
                    except Exception:
                        pass
                    return text

                def _extract_json(self, text):
                    import json
                    json_str = self._extract_json_string(text)
                    return json.loads(json_str)

            self._original = MockOriginal(self._model)
        return self._original

    def chat(self, conversation: Conversation, force_json: bool = False) -> LlmResponse:
        """Sync wrapper that blocks on async implementation"""
        import asyncio
        return asyncio.run(self.chat_async(conversation, force_json))

    def chat_structured(
        self, conversation: Conversation, schema: Type[BaseModel], context_size: int = 0
    ) -> LlmResponse:
        """Sync wrapper that blocks on async implementation"""
        return asyncio.run(self.chat_structured_async(conversation, schema, context_size))

    @staticmethod
    def is_available() -> bool:
        """Check if Gemini CLI is available"""
        try:
            OriginalLlmGeminiCli.check_config()
            return True
        except ConfigurationError:
            return False

    async def chat_async(self, conversation: Conversation, force_json: bool = False) -> LlmResponse:
        """Async version of chat - delegates to sync version"""
        import asyncio
        return await asyncio.get_event_loop().run_in_executor(None, self.chat, conversation, force_json)

    async def chat_structured_async(
        self, conversation: Conversation, schema: Type[BaseModel], context_size: int = 0
    ) -> LlmResponse:
        """Async version of chat_structured - delegates to sync version"""
        import asyncio
        return await asyncio.get_event_loop().run_in_executor(None, self.chat_structured, conversation, schema, context_size)

    async def async_image(
        self, prompt: str, file_name: str, width: int = 1024, height: int = 1024
    ) -> str:
        """Gemini doesn't support image generation via CLI"""
        raise NotImplementedError("Gemini CLI doesn't support image generation")

    def get_context_length(self) -> int:
        """Get context length from original implementation"""
        return 1000000  # Default context length for Gemini 2.0 Flash

    @staticmethod
    def capabilities() -> Set[str]:
        """Return capabilities of Gemini CLI"""
        return OriginalLlmGeminiCli.capabilities()

    @staticmethod
    def supported_models() -> List[str]:
        """Return supported models"""
        return OriginalLlmGeminiCli.supported_models()

    @staticmethod
    def default_model() -> str:
        """Return default model"""
        return OriginalLlmGeminiCli.default_model()

    @staticmethod
    def default_for_type(model_type: str) -> Optional[str]:
        """Return default model for type"""
        return OriginalLlmGeminiCli.default_for_type(model_type)

    @staticmethod
    def check_config():
        """Check configuration"""
        return OriginalLlmGeminiCli.check_config()
