from pydantic import BaseModel

from openapi_agent_benchmark.evaluations.models.openapi_agent_token_summary import OpenAPIAgentTokenSummary


class OpenAPIAgentResult(BaseModel):
    start_time: float
    end_time: float
    duration: float
    token_summary: OpenAPIAgentTokenSummary
    input: str
    output: str
    verified: bool
