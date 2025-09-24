import os
from dataclasses import dataclass
from typing import Optional


@dataclass
class Settings:
    api_key: Optional[str]
    base_url: Optional[str]
    chat_model: str = "gpt4o"
    embed_backend: str = "local"  # openai|ollama|local
    embed_model: Optional[str] = None
    embeddings_url: Optional[str] = None
    device: Optional[str] = None


def from_env() -> Settings:
    # Support both new TEXT2QNA_* variables and legacy OPENAI_* variables
    # The new variables are preferred as they better reflect that any OpenAI-compatible 
    # API can be used (OpenAI, Claude, local models, etc). Legacy variables are kept
    # for backward compatibility but will be deprecated in a future version.
    api_key = os.getenv("TEXT2QNA_API_KEY") or os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("TEXT2QNA_BASE_URL") or os.getenv("OPENAI_BASE_URL")
    
    return Settings(
        api_key=api_key,
        base_url=base_url,
        chat_model=os.getenv("TEXT2QNA_MODEL", "llama3.2"),
        embed_backend=os.getenv("TEXT2QNA_EMBED_BACKEND", "local"),
        embed_model=os.getenv("TEXT2QNA_EMBED_MODEL"),
        embeddings_url=os.getenv("TEXT2QNA_EMBED_URL"),
        device=os.getenv("TEXT2QNA_DEVICE"),
    )


