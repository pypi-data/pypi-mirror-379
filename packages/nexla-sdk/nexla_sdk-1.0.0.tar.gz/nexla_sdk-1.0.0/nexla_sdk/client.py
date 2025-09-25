"""
Nexla API client
"""
import logging
import os
from typing import Dict, Any, Optional, Type, TypeVar, Union, List

from pydantic import ValidationError as PydanticValidationError

from .exceptions import NexlaError, AuthenticationError, ServerError, ValidationError, NotFoundError
from .auth import TokenAuthHandler
from .http_client import HttpClientInterface, RequestsHttpClient, HttpClientError
from . import telemetry
from .resources.flows import FlowsResource  
from .resources.sources import SourcesResource
from .resources.destinations import DestinationsResource
from .resources.credentials import CredentialsResource
from .resources.lookups import LookupsResource
from .resources.nexsets import NexsetsResource
from .resources.users import UsersResource
from .resources.organizations import OrganizationsResource
from .resources.teams import TeamsResource
from .resources.projects import ProjectsResource
from .resources.notifications import NotificationsResource
from .resources.metrics import MetricsResource

logger = logging.getLogger(__name__)

T = TypeVar('T')


class NexlaClient:
    """
    Client for the Nexla API
    
    The Nexla API supports two authentication methods:
    
    1. **Service Key Authentication** (recommended):
       Service keys are long-lived credentials created in the Nexla UI. The SDK
       obtains session tokens using the service key on demand and re-obtains a new
       token as needed. No refresh endpoint is used.
       
    2. **Direct Access Token Authentication**:
       Use a pre-obtained access token directly. These tokens are not refreshed by the SDK.
    
    Examples:
        # Method 1: Using service key (recommended for automation)
        client = NexlaClient(service_key="your-service-key")
        
        # Method 2: Using access token directly (manual/short-term use)
        client = NexlaClient(access_token="your-access-token")
        
        # Using the client (same regardless of authentication method)
        flows = client.flows.list()
        
    Note:
        - Service keys should be treated as highly sensitive credentials
        - Only provide either service_key OR access_token, not both
        - When using direct access tokens, ensure they have sufficient lifetime
          for your operations as they cannot be automatically refreshed
    """
    
    def __init__(self, 
                 service_key: Optional[str] = None,
                 access_token: Optional[str] = None,
                 base_url: Optional[str] = None,
                 api_version: str = "v1",
                 token_refresh_margin: int = 3600,
                 http_client: Optional[HttpClientInterface] = None,
                 trace_enabled: Optional[bool] = None):
        """
        Initialize the Nexla client
        
        Args:
            service_key: Nexla service key for authentication (mutually exclusive with access_token)
            access_token: Nexla access token for direct authentication (mutually exclusive with service_key)
            base_url: Nexla API base URL (defaults to environment variable or standard URL)
            api_version: API version to use
            token_refresh_margin: Seconds before token expiry to trigger refresh (default: 5 minutes)
            http_client: HTTP client implementation (defaults to RequestsHttpClient)
            trace_enabled: Explicitly enable/disable OpenTelemetry tracing. If None,
                           tracing auto-enables when a global OTEL config is detected.
            
        Raises:
            NexlaError: If neither or both authentication methods are provided
            
        Environment Variables:
            NEXLA_SERVICE_KEY: Service key (used if no authentication parameters are provided)
            NEXLA_ACCESS_TOKEN: Access token (used if no authentication parameters are provided and NEXLA_SERVICE_KEY is not set)
            NEXLA_API_URL: Base URL for the Nexla API (used if base_url parameter is not provided)
        """
        # Check environment variables only if neither parameter is provided
        if not service_key and not access_token:
            # First check for service_key in environment
            service_key = os.getenv("NEXLA_SERVICE_KEY")
            # Only check for access_token if service_key is not available
            if not service_key:
                access_token = os.getenv("NEXLA_ACCESS_TOKEN")
            
        # Check for base_url in environment if not provided as parameter
        if not base_url:
            base_url = os.getenv("NEXLA_API_URL")
            if not base_url:
                base_url = "https://dataops.nexla.io/nexla-api"
            
        # Validate authentication parameters
        if not service_key and not access_token:
            raise NexlaError(
                "Either service_key or access_token must be provided either as parameters "
                "or via NEXLA_SERVICE_KEY/NEXLA_ACCESS_TOKEN environment variables"
            )
        if service_key and access_token:
            raise NexlaError("Cannot provide both service_key and access_token. Choose one authentication method.")
            
        self.api_url = base_url.rstrip('/')
        self.api_version = api_version

        # Determine if tracing should be active and get a tracer
        self._trace_enabled = False
        if trace_enabled is True:
            self._trace_enabled = True
        elif trace_enabled is None and telemetry.is_tracing_configured():
            logger.debug("Global OpenTelemetry configuration detected. Enabling tracing for Nexla SDK.")
            self._trace_enabled = True

        self.tracer = telemetry.get_tracer(self._trace_enabled)

        # Initialize HTTP client (instrumented if tracer provided)
        self.http_client = http_client or RequestsHttpClient(tracer=self.tracer)
        
        # Initialize authentication handler
        self.auth_handler = TokenAuthHandler(
            service_key=service_key,
            access_token=access_token,
            base_url=base_url,
            api_version=api_version,
            token_refresh_margin=token_refresh_margin,
            http_client=self.http_client
        )
        
        # Initialize API endpoints
        self.flows = FlowsResource(self)
        self.sources = SourcesResource(self)
        self.destinations = DestinationsResource(self)
        self.credentials = CredentialsResource(self)
        self.lookups = LookupsResource(self)
        self.nexsets = NexsetsResource(self)
        self.users = UsersResource(self)
        self.organizations = OrganizationsResource(self)
        self.teams = TeamsResource(self)
        self.projects = ProjectsResource(self)
        self.notifications = NotificationsResource(self)
        self.metrics = MetricsResource(self)

    def get_access_token(self) -> str:
        """
        Get a valid access token.
        
        For service keys, the SDK obtains tokens as needed and re-obtains a new
        one if the current token is near expiry. Direct access tokens are used as-is.
        
        Returns:
            A valid access token string
            
        Raises:
            AuthenticationError: If no valid token is available or refresh fails
            
        Examples:
            # Get a valid access token
            token = client.get_access_token()
            
            # Use the token for external API calls
            headers = {"Authorization": f"Bearer {token}"}
        """
        return self.auth_handler.ensure_valid_token()

    def refresh_access_token(self) -> str:
        """
        Obtain a fresh token and return it.
        
        For service keys, this obtains a new token. Direct access tokens cannot
        be refreshed and will raise an AuthenticationError.
        
        Returns:
            Refreshed access token string
            
        Raises:
            AuthenticationError: If token refresh fails
            
        Examples:
            # Force refresh and get new token
            new_token = client.refresh_access_token()
        """
        self.auth_handler.refresh_session_token()
        return self.auth_handler.get_access_token()

    def _convert_to_model(self, data: Union[Dict[str, Any], List[Dict[str, Any]]], model_class: Type[T]) -> Union[T, List[T]]:
        """
        Convert API response data to a Pydantic model
        
        Args:
            data: API response data, either a dict or a list of dicts
            model_class: Pydantic model class to convert to
            
        Returns:
            Pydantic model instance or list of instances
            
        Raises:
            ValidationError: If validation fails
        """
        try:
            logger.debug(f"Converting data to model: {model_class.__name__}")
            logger.debug(f"Data to convert: {data}")
            
            if isinstance(data, list):
                result = [model_class.model_validate(item) for item in data]
                logger.debug(f"Converted list result: {result}")
                return result
            
            result = model_class.model_validate(data)
            logger.debug(f"Converted single result: {result}")
            return result
        except PydanticValidationError as e:
            # Log the validation error details
            logger.error(f"Validation error converting to {model_class.__name__}: {e}")
            raise ValidationError(f"Failed to convert API response to {model_class.__name__}: {e}")
            
    def request(self, method: str, path: str, **kwargs) -> Union[Dict[str, Any], None]:
        """
        Send a request to the Nexla API
        
        Args:
            method: HTTP method
            path: API path
            **kwargs: Additional arguments to pass to HTTP client
            
        Returns:
            API response as a dictionary or None for 204 No Content responses
            
        Raises:
            AuthenticationError: If authentication fails
            ServerError: If the API returns an error
        """
        url = f"{self.api_url}{path}"
        headers = {
            "Accept": f"application/vnd.nexla.api.{self.api_version}+json",
            "Content-Type": "application/json"
        }
        
        # If custom headers are provided, merge them with the default headers
        if "headers" in kwargs:
            headers.update(kwargs.pop("headers"))
            
        try:
            # Let auth handler manage getting a valid token and handling auth retries
            return self.auth_handler.execute_authenticated_request(
                method=method,
                url=url,
                headers=headers,
                **kwargs
            )
        except HttpClientError as e:
            # Map HTTP client errors to appropriate Nexla exceptions
            self._handle_http_error(e, method, path, url, kwargs)
        except Exception as e:
            raise NexlaError(
                message=f"Request failed: {e}",
                operation=f"{method.lower()}_request",
                context={
                    "method": method,
                    "path": path,
                    "url": url,
                    "kwargs": {k: v for k, v in kwargs.items() if k not in ['json', 'data']}
                },
                original_error=e
            ) from e

    def _handle_http_error(self, error: HttpClientError, method: str, path: str, url: str, kwargs: dict):
        """
        Handle HTTP client errors by mapping them to appropriate Nexla exceptions
        
        Args:
            error: The HTTP client error
            method: HTTP method that failed
            path: API path that failed
            url: Full URL that failed
            kwargs: Request parameters
            
        Raises:
            AuthenticationError: If authentication fails (401)
            NotFoundError: If resource not found (404)
            ServerError: For other API errors
        """
        status_code = getattr(error, 'status_code', None)
        error_data = getattr(error, 'response', {})
        
        error_msg = f"API request failed: {error}"
        
        if error_data:
            if "message" in error_data:
                error_msg = f"API error: {error_data['message']}"
            elif "error" in error_data:
                error_msg = f"API error: {error_data['error']}"
        
        # Extract resource information (prefer server-provided fields, fallback to path)
        resource_type = None
        resource_id = None
        if isinstance(error_data, dict):
            resource_type = error_data.get("resource_type") or None
            resource_id = error_data.get("resource_id") or None
        if not resource_type or not resource_id:
            # Fallback to parsing the path
            if path:
                path_parts = path.strip('/').split('/')
                if not resource_type and len(path_parts) >= 1:
                    resource_type = path_parts[0]
                if not resource_id and len(path_parts) >= 2 and path_parts[1].isdigit():
                    resource_id = path_parts[1]
        # Final defaults
        if not resource_type:
            resource_type = "unknown"
        
        # Build context
        context = {
            "method": method,
            "path": path,
            "url": url,
            "status_code": status_code,
            "api_response": error_data,
            "request_params": {k: v for k, v in kwargs.items() if k not in ['json', 'data']}
        }
        
        # Map status codes to specific exceptions
        if status_code == 400:
            raise ValidationError(
                error_msg,
                status_code=status_code,
                response=error_data,
                operation=f"{method.lower()}_request",
                resource_type=resource_type,
                resource_id=resource_id,
                context=context,
                original_error=error
            ) from error
        elif status_code == 401:
            raise AuthenticationError(
                "Authentication failed. Check your service key.",
                operation=f"{method.lower()}_request",
                resource_type=resource_type,
                resource_id=resource_id,
                context=context,
                original_error=error
            ) from error
        elif status_code == 403:
            from .exceptions import AuthorizationError
            raise AuthorizationError(
                error_msg,
                status_code=status_code,
                response=error_data,
                operation=f"{method.lower()}_request",
                resource_type=resource_type,
                resource_id=resource_id,
                context=context,
                original_error=error
            ) from error
        elif status_code == 404:
            raise NotFoundError(
                f"Resource not found: {resource_type}/{resource_id or 'unknown'}",
                resource_type=resource_type,
                resource_id=resource_id,
                operation=f"{method.lower()}_request",
                context=context,
                original_error=error
            ) from error
        elif status_code == 409:
            from .exceptions import ResourceConflictError
            raise ResourceConflictError(
                error_msg,
                status_code=status_code,
                response=error_data,
                operation=f"{method.lower()}_request",
                resource_type=resource_type,
                resource_id=resource_id,
                context=context,
                original_error=error
            ) from error
        elif status_code == 429:
            from .exceptions import RateLimitError
            retry_after = None
            # Try to parse retry-after from headers or body
            headers = getattr(error, 'headers', {}) or {}
            if headers:
                retry_after_hdr = headers.get('Retry-After') or headers.get('retry-after')
                if retry_after_hdr:
                    try:
                        retry_after = int(retry_after_hdr)
                    except Exception:
                        retry_after = None
            if not retry_after and isinstance(error_data, dict):
                retry_after = error_data.get('retry_after')
            raise RateLimitError(
                error_msg,
                retry_after=retry_after,
                status_code=status_code,
                response=error_data,
                operation=f"{method.lower()}_request",
                resource_type=resource_type,
                resource_id=resource_id,
                context=context,
                original_error=error
            ) from error
        else:
            raise ServerError(
                error_msg,
                status_code=status_code,
                response=error_data,
                operation=f"{method.lower()}_request",
                resource_type=resource_type,
                resource_id=resource_id,
                context=context,
                original_error=error
            ) from error 
