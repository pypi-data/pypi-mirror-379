from pydantic import BaseModel


class OpenAPIAgentTokenSummary(BaseModel):
    prompt_tokens: int
    completion_tokens: int
    total_tokens: int
