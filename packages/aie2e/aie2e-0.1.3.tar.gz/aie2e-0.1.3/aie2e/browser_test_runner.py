import os

from .test_models import TestCaseInfo, TestAction, TestCase, TestCaseResult, TestSession, TestSessionResult
from .constants import DEFAULT_TEST_AGENT_SYSTEM_MESSAGE, DEFAULT_VIEWPORT_WIDTH, DEFAULT_VIEWPORT_HEIGHT

from browser_use import Agent, BrowserProfile, BrowserSession
from browser_use.llm import ChatOllama, ChatOpenAI, ChatAnthropic, ChatGoogle, ChatAWSBedrock, ChatAnthropicBedrock, ChatAzureOpenAI, ChatDeepSeek, ChatGroq, ChatOpenRouter, BaseChatModel
from pydantic import Field
from typing import List, AsyncGenerator, Union, Dict, Any

def get_initial_actions(actions_list: List[TestAction]) -> List[Dict[str, Dict[str, Any]]]:
    return [{action.action: action.arguments} for action in actions_list]

def get_agent(test_session: TestSession, test_case: TestCase, browser_session: BrowserSession) -> Agent:
    if test_session.llm_provider == 'ollama':
        llm = ChatOllama(model=test_session.model)
        tool_calling_method = "raw"
    elif test_session.llm_provider == 'openai':
        llm = ChatOpenAI(model=test_session.model, api_key=test_session.api_key)
        tool_calling_method = None
    elif test_session.llm_provider == 'anthropic':
        llm = ChatAnthropic(model=test_session.model, api_key=test_session.api_key)
        tool_calling_method = None
    elif test_session.llm_provider == 'google':
        llm = ChatGoogle(model=test_session.model, api_key=test_session.api_key)
        tool_calling_method = None
    elif test_session.llm_provider == 'aws-bedrock':
        llm = ChatAWSBedrock(model=test_session.model, api_key=test_session.api_key)
        tool_calling_method = None
    elif test_session.llm_provider == 'anthropic-bedrock':
        llm = ChatAnthropicBedrock(model=test_session.model, api_key=test_session.api_key)
        tool_calling_method = None
    elif test_session.llm_provider == 'azure-openai':
        llm = ChatAzureOpenAI(model=test_session.model, api_key=test_session.api_key)
        tool_calling_method = None
    elif test_session.llm_provider == 'deepseek':
        llm = ChatDeepSeek(model=test_session.model, api_key=test_session.api_key)
        tool_calling_method = None
    elif test_session.llm_provider == 'groq':
        llm = ChatGroq(model=test_session.model, api_key=test_session.api_key)
        tool_calling_method = None
    elif test_session.llm_provider == 'openrouter':
        llm = ChatOpenRouter(model=test_session.model, api_key=test_session.api_key)
        tool_calling_method = None
    else:
        raise ValueError(f"Unsupported LLM provider: {test_session.llm_provider}")
    
    return Agent(
        extend_system_message=DEFAULT_TEST_AGENT_SYSTEM_MESSAGE,
        initial_actions=get_initial_actions(test_case.initial_actions),
        task=test_case.task,
        use_vision=test_case.use_vision,
        browser_session=browser_session,
        llm=llm,
        tool_calling_method=tool_calling_method,
        sensitive_data=test_session.sensitive_data,
    )

async def run_test_session(test_run: TestSession) -> AsyncGenerator[Union[TestCaseResult, TestCaseInfo], None]:
    """Execute a test session using browser automation.
    
    This async generator function creates a browser session and executes each test case
    sequentially, yielding progress information and results as they become available.
    
    Args:
        test_run: TestSession containing test cases, LLM configuration, and browser settings
        
    Yields:
        TestCaseInfo: Progress information when starting each test case
        TestCaseResult: Complete results when each test case finishes (success or failure)
        
    Raises:
        Exception: Any browser session startup/shutdown errors are propagated
    """
    profile = BrowserProfile(
        keep_alive=True,
        viewport={'width': DEFAULT_VIEWPORT_WIDTH, 'height': DEFAULT_VIEWPORT_HEIGHT},
        headless=test_run.headless
    )
    session = BrowserSession(browser_profile=profile, allowed_domains=test_run.allowed_domains)
    await session.start()

    try:
        for test_index, test_case in enumerate(test_run.tests):
            test_number = test_index + 1
            total_tests = len(test_run.tests)
            yield TestCaseInfo(
                session_description=test_run.description,
                task=test_case.task,
                test_number=test_number,
                total_tests=total_tests,
            )

            try:
                agent = get_agent(test_run, test_case, session)
                result = await agent.run()
                yield TestCaseResult(
                    passed=result.is_successful() or False,
                    run_time=result.total_duration_seconds(),
                    errors=[error for error in (result.errors() if result.has_errors() else []) if error is not None],
                    final_result=result.final_result() or "",
                    test_number=test_number,
                    total_tests=total_tests,
                )
            except Exception as e:
                yield TestCaseResult(
                    passed=False,
                    run_time=0.0,
                    errors=[f"Agent execution failed: {str(e)}"],
                    final_result="Test failed due to agent execution error",
                    test_number=test_number,
                    total_tests=total_tests,
                )
    finally:
        await session.kill()
