# providers/bedrock.py

import aioboto3, json, time, asyncio, os
from botocore.config import Config
from botocore.exceptions import ProfileNotFound, ClientError
from typing import Any, AsyncGenerator, Dict, Optional, Tuple

from .base import BaseProvider
from . import register_provider

# Default model ID
DEFAULT_MODEL_ID = "anthropic.claude-3-5-haiku-20241022-v1:0"


class BedrockProvider(BaseProvider):
    """Provider for AWS Bedrock LLM services."""

    def __init__(self, config: Optional[Dict[str, Any]] = None, logger=None):
        """
        Initialize the Bedrock provider.

        Args:
            config: Bedrock-specific configuration with keys like:
                - region: AWS region for Bedrock
                - profile_name: AWS profile to use
                - model_id: Bedrock model ID
                - timeout: Request timeout in seconds
            logger: Optional logger instance
        """
        super().__init__(config, logger)

        # Initialize to None, will be created on first use
        self.session = None
        self.session_params = None
        self.client_params = None
        self.model_id = DEFAULT_MODEL_ID

    async def initialize(self) -> None:
        """
        Initialize Bedrock session asynchronously.
        Called automatically by EmbeddedStream before first use.
        """
        await self.get_bedrock_clients()

    async def get_bedrock_clients(self) -> None:
        """
        Initialize Bedrock session and parameters.
        Creates aioboto3 session and caches configuration for on-demand client creation.
        """
        # Skip if already initialized
        if self.session is not None:
            self._log_debug("Using cached Bedrock session")
            return

        config = self.config

        # Ensure EC2 metadata service is enabled
        os.environ["AWS_EC2_METADATA_DISABLED"] = "false"

        # Region resolution with priority order
        region = (
            config.get("region")
            or os.environ.get("AWS_BEDROCK_REGION")
            or os.environ.get("AWS_REGION")
            or os.environ.get("AWS_DEFAULT_REGION", "us-west-2")
        )

        # Get the model ID (default is Claude 3.5 Haiku)
        model_id = config.get("model_id") or os.environ.get(
            "AWS_BEDROCK_MODEL_ID", DEFAULT_MODEL_ID
        )

        # Build boto3 config with potential overrides
        boto_config = Config(
            region_name=region,
            retries={"max_attempts": config.get("max_retries", 2)},
            read_timeout=config.get("timeout", 300),
            connect_timeout=config.get("timeout", 300),
        )

        self._log_debug(f"Initializing Bedrock clients in region: {region}")
        self._log_debug(f"Using model: {model_id}")

        # Session parameters (only if explicitly provided)
        session_params = {}
        if config.get("profile_name"):
            session_params["profile_name"] = config["profile_name"]
        if config.get("aws_access_key_id") and config.get("aws_secret_access_key"):
            session_params["aws_access_key_id"] = config["aws_access_key_id"]
            session_params["aws_secret_access_key"] = config["aws_secret_access_key"]
            if config.get("aws_session_token"):
                session_params["aws_session_token"] = config["aws_session_token"]

        # Client parameters
        client_params = {"config": boto_config}
        if config.get("endpoint_url"):
            client_params["endpoint_url"] = config["endpoint_url"]

        try:
            # Create session with optional parameters - uses default credential chain
            self.session = aioboto3.Session(**session_params)
            self.session_params = session_params
            self.client_params = client_params

            # Verify credentials by making a basic call
            try:
                async with self.session.client("sts") as sts:
                    identity = await sts.get_caller_identity()
                    self._log_debug(f"Using credentials for account: {identity['Account']}")
            except Exception as e:
                self._log_debug(f"Warning: Could not verify credentials: {e}")

        except Exception as e:
            self._log_error(f"Critical error initializing Bedrock session: {e}")
            self.session = None

    async def generate_stream(
        self,
        messages: list,
        model: Optional[str] = None,
        temperature: Optional[float] = None,
        max_gen_len: int = 4096,
        **kwargs,
    ) -> AsyncGenerator[str, None]:
        """
        Generate streaming responses from AWS Bedrock.

        Args:
            messages: List of conversation messages
            model: Model identifier (takes precedence over provider_config)
            temperature: Temperature for generation (defaults to 0.9 if None)
            max_gen_len: Maximum tokens to generate
            **kwargs: Additional keyword arguments (unused)

        Yields:
            Chunks of the generated response
        """
        # Initialize session if not already done
        if self.session is None:
            await self.get_bedrock_clients()

        # Use provided model or fall back to config/default
        model_id = model or self.config.get("model_id") or self.model_id

        # Use provided temperature or fall back to default
        if temperature is None:
            temperature = 0.9

        # Check if session was successfully initialized
        if self.session is None:
            yield self.format_error_chunk("Bedrock session initialization failed.")
            yield "data: [DONE]\n\n"
            return

        try:
            # Create runtime client using async context manager
            async with self.session.client("bedrock-runtime", **self.client_params) as runtime_client:
                response = await runtime_client.converse_stream(
                    modelId=model_id,
                    messages=[
                        {"role": m["role"], "content": [{"text": m["content"]}]}
                        for m in messages
                        if m["role"] != "system"
                    ],
                    system=[
                        {"text": m["content"]} for m in messages if m["role"] == "system"
                    ],
                    inferenceConfig={"maxTokens": max_gen_len, "temperature": temperature},
                )
                async for event in response.get("stream", []):
                    text = (
                        event.get("contentBlockDelta", {}).get("delta", {}).get("text", "")
                    )
                    if text:
                        chunk = {"choices": [{"delta": {"content": text}}]}
                        yield f"data: {json.dumps(chunk)}\n\n"
                        await asyncio.sleep(0)
                yield "data: [DONE]\n\n"
        except Exception as e:
            self._log_error(f"Error during generation: {str(e)}")
            yield self.format_error_chunk(str(e))
            yield "data: [DONE]\n\n"


def register():
    """Register this provider with the registry."""
    register_provider("bedrock", BedrockProvider)
