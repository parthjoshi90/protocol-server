from enum import Enum
from pydantic import BaseModel, Field
from typing import Optional


class Type1(Enum):
    CONTEXT_ERROR = "CONTEXT-ERROR"
    CORE_ERROR = "CORE-ERROR"
    DOMAIN_ERROR = "DOMAIN-ERROR"
    POLICY_ERROR = "POLICY-ERROR"
    JSON_SCHEMA_ERROR = "JSON-SCHEMA-ERROR"


class Error(BaseModel):
    type: Type1
    code: str = Field(
        ...,
        description="ONDC specific error code. For full list of error codes, refer to docs/drafts/Error Codes.md of this repo",
    )
    path: Optional[str] = Field(
        None,
        description="Path to json schema generating the error. Used only during json schema validation errors",
    )
    message: Optional[str] = Field(
        None, description="Human readable message describing the error"
    )
