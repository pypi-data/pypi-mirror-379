from typing import Any, Dict, List, Literal, Optional, Union
from pydantic import BaseModel, Field
import json

class TestAction(BaseModel):
    action: str = Field(..., description="The action to perform")
    arguments: Dict[str, Any] = Field(default_factory=dict, description="Arguments for the action")

class TestCase(BaseModel):
    initial_actions: List[TestAction] = Field(default_factory=list, description="List of initial actions")
    task: str = Field(..., description="Task to be performed in the test case")
    use_vision: bool = Field(default=False, description="Indicates if vision capabilities are used in the test case")

class TestSession(BaseModel):
    description: str = Field(..., description="Description of the test session")
    tests: List[TestCase] = Field(default_factory=list, description="List of test cases in the session")
    model: str = Field(..., description="LLM model to use for the test session")
    llm_provider: Literal['ollama', 'openai', 'anthropic', 'google', 'aws-bedrock', 'anthropic-bedrock', 'azure-openai', 'deepseek', 'groq', 'openrouter'] = Field(..., description="LLM provider to use for the test session")
    api_key: Optional[str] = Field(default=None, description="API key for the LLM provider")
    allowed_domains: Optional[List[str]] = Field(default=None, description="List of allowed domains for browser navigation")
    sensitive_data: Optional[Dict[str, Union[str, Dict[str, str]]]] = Field(default=None, description="Sensitive data to be passed to the agent")
    headless: bool = Field(default=False, description="Run browser in headless mode")

class TestCaseResult(BaseModel):
    type: Literal["test_case_result"] = Field(default="test_case_result", description="Type of the result")
    passed: bool = Field(default=False, description="Indicates if the test case passed")
    run_time: float = Field(default=0.0, description="Time taken for the test case in seconds")
    errors: List[str] = Field(default_factory=list, description="List of errors encountered during the test case")
    final_result: str = Field(default="", description="Final result of the test case execution")
    test_number: int = Field(default=0, description="Index of the test case in the session")
    total_tests: int = Field(default=0, description="Total number of tests in the session")

class TestSessionResult(BaseModel):
    type: Literal["test_session_result"] = Field(default="test_session_result", description="Type of the result")
    passed: bool = Field(default=False, description="Indicates if the test session passed")
    run_time: float = Field(default=0.0, description="Total time taken for the test session in seconds")
    description: str = Field(default="", description="Description of the test session")
    total_tests: int = Field(default=0, description="Total number of tests in the session")
    passed_tests: int = Field(default=0, description="Number of passed tests in the session")
    failed_tests: int = Field(default=0, description="Number of failed tests in the session")

class TestCaseInfo(BaseModel):
    type: Literal["test_case_info"] = Field(default="test_case_info", description="Type of the test case info")
    session_description: str = Field(default="", description="Description of the session")
    task: str = Field(default="", description="Task to be performed in the session")
    test_number: int = Field(default=0, description="Index of the test case in the session")
    total_tests: int = Field(default=0, description="Total number of tests in the session")

class TestSessionInfo(BaseModel):
    type: Literal["test_session_info"] = Field(default="test_session_info", description="Type of the test session info")
    description: str = Field(default="", description="Description of the test session")
    total_tests: int = Field(default=0, description="Total number of tests in the session")
