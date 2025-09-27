# -----------------------------------------------------------------------------
#  Copyright (c) OpenAGI Foundation
#  All rights reserved.
#
#  This file is part of the official API project.
#  Licensed under the MIT License.
# -----------------------------------------------------------------------------

import os
from functools import wraps

import httpx

from .exceptions import (
    APIError,
    AuthenticationError,
    ConfigurationError,
    NetworkError,
    NotFoundError,
    RateLimitError,
    RequestTimeoutError,
    ServerError,
    ValidationError,
)
from .logging import get_logger
from .sync_client import ErrorResponse, LLMResponse

logger = get_logger("async_client")


def async_log_trace_on_failure(func):
    """Async decorator that logs trace ID when a method fails."""

    @wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            return await func(*args, **kwargs)
        except Exception as e:
            # Try to get response from the exception if it has one
            if (response := getattr(e, "response", None)) is not None:
                logger.error(f"Request Id: {response.headers.get('x-request-id', '')}")
                logger.error(f"Trace Id: {response.headers.get('x-trace-id', '')}")
            raise

    return wrapper


class AsyncClient:
    """Async HTTP client for the OAGI API."""

    def __init__(self, base_url: str | None = None, api_key: str | None = None):
        # Get from environment if not provided
        self.base_url = base_url or os.getenv("OAGI_BASE_URL")
        self.api_key = api_key or os.getenv("OAGI_API_KEY")

        # Validate required configuration
        if not self.base_url:
            raise ConfigurationError(
                "OAGI base URL must be provided either as 'base_url' parameter or "
                "OAGI_BASE_URL environment variable"
            )

        if not self.api_key:
            raise ConfigurationError(
                "OAGI API key must be provided either as 'api_key' parameter or "
                "OAGI_API_KEY environment variable"
            )

        self.base_url = self.base_url.rstrip("/")
        self.client = httpx.AsyncClient(base_url=self.base_url)
        self.timeout = 60

        logger.info(f"AsyncClient initialized with base_url: {self.base_url}")

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        await self.client.aclose()

    async def close(self):
        """Close the underlying httpx async client"""
        await self.client.aclose()

    @async_log_trace_on_failure
    async def create_message(
        self,
        model: str,
        screenshot: str,  # base64 encoded
        task_description: str | None = None,
        task_id: str | None = None,
        instruction: str | None = None,
        max_actions: int | None = 5,
        last_task_id: str | None = None,
        history_steps: int | None = None,
        api_version: str | None = None,
    ) -> LLMResponse:
        """
        Call the /v1/message endpoint to analyze task and screenshot

        Args:
            model: The model to use for task analysis
            screenshot: Base64-encoded screenshot image
            task_description: Description of the task (required for new sessions)
            task_id: Task ID for continuing existing task
            instruction: Additional instruction when continuing a session (only works with task_id)
            max_actions: Maximum number of actions to return (1-20)
            last_task_id: Previous task ID to retrieve history from (only works with task_id)
            history_steps: Number of historical steps to include from last_task_id (default: 1, max: 10)
            api_version: API version header

        Returns:
            LLMResponse: The response from the API

        Raises:
            httpx.HTTPStatusError: For HTTP error responses
        """
        headers = {}
        if api_version:
            headers["x-api-version"] = api_version
        if self.api_key:
            headers["x-api-key"] = self.api_key

        payload = {"model": model, "screenshot": screenshot}

        if task_description is not None:
            payload["task_description"] = task_description
        if task_id is not None:
            payload["task_id"] = task_id
        if instruction is not None:
            payload["instruction"] = instruction
        if max_actions is not None:
            payload["max_actions"] = max_actions
        if last_task_id is not None:
            payload["last_task_id"] = last_task_id
        if history_steps is not None:
            payload["history_steps"] = history_steps

        logger.info(f"Making async API request to /v1/message with model: {model}")
        logger.debug(
            f"Request includes task_description: {task_description is not None}, task_id: {task_id is not None}"
        )

        try:
            response = await self.client.post(
                "/v1/message", json=payload, headers=headers, timeout=self.timeout
            )
        except httpx.TimeoutException as e:
            logger.error(f"Request timed out after {self.timeout} seconds")
            raise RequestTimeoutError(
                f"Request timed out after {self.timeout} seconds", e
            )
        except httpx.NetworkError as e:
            logger.error(f"Network error: {e}")
            raise NetworkError(f"Network error: {e}", e)

        try:
            response_data = response.json()
        except ValueError:
            # If response is not JSON, raise API error
            logger.error(f"Non-JSON API response: {response.status_code}")
            raise APIError(
                f"Invalid response format (status {response.status_code})",
                status_code=response.status_code,
                response=response,
            )

        # Check if it's an error response (non-200 status or has error field)
        if response.status_code != 200:
            error_resp = ErrorResponse(**response_data)
            if error_resp.error:
                error_code = error_resp.error.code
                error_msg = error_resp.error.message
                logger.error(f"API Error [{error_code}]: {error_msg}")

                # Map to specific exception types based on status code
                exception_class = self._get_exception_class(response.status_code)
                raise exception_class(
                    error_msg,
                    code=error_code,
                    status_code=response.status_code,
                    response=response,
                )
            else:
                # Error response without error details
                logger.error(
                    f"API error response without details: {response.status_code}"
                )
                exception_class = self._get_exception_class(response.status_code)
                raise exception_class(
                    f"API error (status {response.status_code})",
                    status_code=response.status_code,
                    response=response,
                )

        # Parse successful response
        result = LLMResponse(**response_data)

        # Check if the response contains an error (even with 200 status)
        if result.error:
            logger.error(
                f"API Error in response: [{result.error.code}]: {result.error.message}"
            )
            raise APIError(
                result.error.message,
                code=result.error.code,
                status_code=200,
                response=response,
            )

        logger.info(
            f"Async API request successful - task_id: {result.task_id}, step: {result.current_step}, complete: {result.is_complete}"
        )
        logger.debug(f"Response included {len(result.actions)} actions")
        return result

    def _get_exception_class(self, status_code: int) -> type[APIError]:
        """Get the appropriate exception class based on status code."""
        status_map = {
            401: AuthenticationError,
            404: NotFoundError,
            422: ValidationError,
            429: RateLimitError,
        }

        if status_code >= 500:
            return ServerError

        return status_map.get(status_code, APIError)

    async def health_check(self) -> dict:
        """
        Call the /health endpoint for health check

        Returns:
            dict: Health check response
        """
        logger.debug("Making async health check request")
        try:
            response = await self.client.get("/health")
            response.raise_for_status()
            result = response.json()
            logger.debug("Async health check successful")
            return result
        except httpx.HTTPStatusError as e:
            logger.warning(f"Async health check failed: {e}")
            raise
