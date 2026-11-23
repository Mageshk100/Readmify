from dataclasses import dataclass

@dataclass
class LiteLLMConfig:
    DEFAULT_MODEL: str = "openai/gpt-oss-20b"