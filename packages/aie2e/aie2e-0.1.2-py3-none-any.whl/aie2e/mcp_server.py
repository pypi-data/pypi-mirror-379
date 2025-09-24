#!/usr/bin/env python3

import asyncio
import json
import logging
import os
import argparse
from typing import Optional

from fastmcp import FastMCP, Context

from .browser_test_runner import run_test_session
from .test_models import TestSession, TestCaseResult, TestSessionResult, TestSessionInfo

# Create FastMCP server instance
mcp = FastMCP("AIE2E Server")

# Global variable to store command line arguments
_global_args = None

@mcp.tool("run_test_session")
async def run_test_session_tool(
    description: str,
    tests: list,
    ctx: Context,
    allowed_domains: list = [],
    sensitive_data: dict = {}
) -> str:
    """
    Execute an AI-powered end-to-end test session with multiple test cases using browser automation.

    Use this tool when you need to:
    - Test web applications end-to-end using AI agents
    - Validate user workflows across multiple pages or steps
    - Perform regression testing of web interfaces

    Args:
        description: Description of the test session
        tests: List of test cases to execute sequentially
        allowed_domains: List of allowed domains for browser navigation (optional)
        sensitive_data: Sensitive data dictionary for form filling (optional)

    Returns:
        JSON string containing the test session results summary

    Streams test results as they are generated using MCP notifications for real-time feedback.
    """

    # Use global command line arguments for LLM configuration
    if _global_args is None:
        raise RuntimeError("Server not properly initialized. Command line arguments are missing.")

    test_session = TestSession.model_validate({
        "description": description,
        "tests": tests,
        "model": _global_args.model,
        "llm_provider": _global_args.llm_provider,
        "api_key": _global_args.api_key,
        "allowed_domains": allowed_domains,
        "sensitive_data": sensitive_data,
        "headless": _global_args.headless
    })
    
    session_passed = True
    total_run_time = 0.0
    test_results = []
    
    # Send session start notification
    session_info = TestSessionInfo(description=test_session.description, total_tests=len(test_session.tests))
    await ctx.info(json.dumps(session_info.model_dump(), indent=2))

    # Stream test results as they are generated       
    async for result in run_test_session(test_session):
        await ctx.info(json.dumps(result.model_dump(), indent=2))
        if isinstance(result, TestCaseResult):
            session_passed = session_passed and result.passed
            total_run_time += result.run_time
            test_results.append(result)        
    
    session_result = TestSessionResult(
        passed=session_passed,
        run_time=total_run_time,
        description=test_session.description,
        total_tests=len(test_session.tests),
        passed_tests=sum(1 for result in test_results if result.passed),
        failed_tests=sum(1 for result in test_results if not result.passed)
    )

    return json.dumps(session_result.model_dump(), indent=2)

def configure_logging(transport: str) -> None:
    """Configure logging and telemetry based on transport type.
    
    Args:
        transport: Either 'stdio' or 'http'. For stdio, all logging is disabled
                  to prevent interference with MCP protocol communication.
    """
    # Always disable telemetry and warnings
    os.environ["ANONYMIZED_TELEMETRY"] = "false"
    os.environ["PYTHONWARNINGS"] = "ignore"
    
    if transport == "stdio":
        # Disable all logging for stdio transport to avoid protocol interference
        os.environ["BROWSER_USE_LOG_LEVEL"] = "CRITICAL"
        logging.disable(logging.CRITICAL)
    elif transport == "http":
        # Allow normal logging for HTTP transport
        os.environ["BROWSER_USE_LOG_LEVEL"] = "INFO"

def main():
    """Main entry point for the AIE2E FastMCP server."""
    global _global_args

    parser = argparse.ArgumentParser(description="AIE2E MCP Server")

    # Transport configuration
    parser.add_argument(
        "--transport",
        choices=["stdio", "http"],
        default="stdio",
        help="Transport type to use (default: stdio)"
    )
    parser.add_argument(
        "--host",
        default="localhost",
        help="Host to bind to for HTTP transport (default: localhost)"
    )
    parser.add_argument(
        "--port",
        type=int,
        default=3001,
        help="Port to bind to for HTTP transport (default: 3001)"
    )

    # LLM configuration
    parser.add_argument(
        "--model",
        required=True,
        help="LLM model to use (e.g., 'gemini-2.5-pro', 'gpt-4', 'claude-3-sonnet')"
    )
    parser.add_argument(
        "--llm-provider",
        choices=['ollama', 'openai', 'anthropic', 'google', 'aws-bedrock', 'anthropic-bedrock', 'azure-openai', 'deepseek', 'groq', 'openrouter'],
        required=True,
        help="LLM provider to use"
    )
    parser.add_argument(
        "--api-key",
        help="API key for the LLM provider (can also be set via environment variables)"
    )

    # Browser configuration
    parser.add_argument(
        "--headless",
        action="store_true",
        help="Run browser in headless mode (no UI)"
    )
    
    args = parser.parse_args()

    # Store arguments globally for use in MCP tools
    _global_args = args

    # Configure logging based on transport type
    configure_logging(args.transport)
    
    try:
        if args.transport == "stdio":
            # Run FastMCP with stdio
            mcp.run(transport="stdio")

        elif args.transport == "http":
            # Run FastMCP with streamable HTTP
            mcp.run(transport="http", host=args.host, port=args.port)

    except (OSError, BrokenPipeError) as e:
        logging.warning(f"Connection error: {e}")
    except KeyboardInterrupt:
        logging.info("Server shutdown requested")
    except Exception as e:
        logging.error(f"Server error: {e}")
        raise

if __name__ == "__main__":
    main()