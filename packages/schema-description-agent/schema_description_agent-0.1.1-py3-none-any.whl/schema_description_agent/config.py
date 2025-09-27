from pydantic import BaseModel, Field

class SchemaDescriptionConfig(BaseModel):
    """Configuration settings for the Table Description Agent."""

    # AI Provider Configuration
    ai_provider: str = Field(default="openai", description="AI provider to use")
    model_name: str = Field(default="gpt-4o", description="AI model to use")
    temperature: float = Field(default=0.3, ge=0.0, le=2.0, description="AI model temperature")
    max_tokens: int = Field(default=4000, ge=100, le=8000, description="Maximum tokens for AI response")

