# Main entry point for the Aspect SDK
from .client import AspectClient
from .client_config import AspectClientConfig

# Re-export resource classes for advanced usage
from .resources.assets import Assets, AssetCreateRequest
from .resources.indexes import Indexes
from .resources.users import Users
from .resources.search import Search
from .resources.tasks import Tasks
from .resources.analyze import Analyze

# Re-export everything from the generated SDK (packaged under the same top-level module)
from ._generated import (
    # API classes
    AnalyzeApi,
    AssetsApi,
    IndexesApi,
    SearchApi,
    TasksApi,
    UsersApi,
    PreviewsApi,
    ProxiesApi,

    # API client classes
    ApiResponse,
    ApiClient,
    Configuration,

    # Exception classes
    OpenApiException,
    ApiTypeError,
    ApiValueError,
    ApiKeyError,
    ApiAttributeError,
    ApiException,

    # Model classes
    AnalyzeAskRequest,
    AnalyzeAskResponse,
    AnalyzeBoxCoordinate,
    AnalyzeBoxRequest,
    AnalyzeBoxResponse,
    AnalyzePointCoordinate,
    AnalyzePointRequest,
    AnalyzePointResponse,
    AssetCreateResponse,
    AssetDownloadGetResponse,
    AssetGetResponse,
    AssetListResponse,
    AssetStorageVariant,
    AssetType,
    AssetUpdateRequest,
    AssetUpdateResponse,
    FeatureInfo,
    FeatureState,
    FeatureType,
    HTTPValidationError,
    IndexCreateRequest,
    IndexCreateResponse,
    IndexGetResponse,
    IndexListResponse,
    IndexUpdateRequest,
    IndexUpdateResponse,
    PreviewGetResponse,
    ProxyGetResponse,
    TaskCreateRequest,
    TaskCreateResponse,
    TaskGetResponse,
    UserGetResponse,
    ValidationError,
    ValidationErrorLocInner,
)

# Re-export custom types
from .custom.task_extensions import WaitForDoneOptions, TaskExtensions

__all__ = [
    # Main client
    "AspectClient",
    "AspectClientConfig",

    # Resource classes
    "Assets",
    "Indexes",
    "Users",
    "Search",
    "Tasks",
    "Analyze",

    # Custom types
    "WaitForDoneOptions",
    "TaskExtensions",

    # Generated API classes
    "AnalyzeApi",
    "AssetsApi",
    "IndexesApi",
    "SearchApi",
    "TasksApi",
    "UsersApi",
    "PreviewsApi",
    "ProxiesApi",

    # API client classes
    "ApiResponse",
    "ApiClient",
    "Configuration",

    # Exception classes
    "OpenApiException",
    "ApiTypeError",
    "ApiValueError",
    "ApiKeyError",
    "ApiAttributeError",
    "ApiException",

    # Model classes
    "AnalyzeAskRequest",
    "AnalyzeAskResponse",
    "AnalyzeBoxCoordinate",
    "AnalyzeBoxRequest",
    "AnalyzeBoxResponse",
    "AnalyzePointCoordinate",
    "AnalyzePointRequest",
    "AnalyzePointResponse",
    "AssetCreateResponse",
    "AssetDownloadGetResponse",
    "AssetCreateRequest",
    "AssetGetResponse",
    "AssetListResponse",
    "AssetStorageVariant",
    "AssetType",
    "AssetUpdateRequest",
    "AssetUpdateResponse",
    "FeatureInfo",
    "FeatureState",
    "FeatureType",
    "HTTPValidationError",
    "IndexCreateRequest",
    "IndexCreateResponse",
    "IndexGetResponse",
    "IndexListResponse",
    "IndexUpdateRequest",
    "IndexUpdateResponse",
    "PreviewGetResponse",
    "ProxyGetResponse",
    "TaskCreateRequest",
    "TaskCreateResponse",
    "TaskGetResponse",
    "UserGetResponse",
    "ValidationError",
    "ValidationErrorLocInner",
]


