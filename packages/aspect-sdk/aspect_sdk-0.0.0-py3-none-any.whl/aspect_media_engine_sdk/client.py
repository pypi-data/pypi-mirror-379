# Unified client for the Aspect SDK
from aspect_media_engine_sdk._generated import Configuration
from aspect_media_engine_sdk.client_config import AspectClientConfig

# Import resource classes directly from submodules to avoid circular imports
from aspect_media_engine_sdk.resources.assets import Assets
from aspect_media_engine_sdk.resources.indexes import Indexes
from aspect_media_engine_sdk.resources.users import Users
from aspect_media_engine_sdk.resources.search import Search
from aspect_media_engine_sdk.resources.tasks import Tasks
from aspect_media_engine_sdk.resources.analyze import Analyze


class AspectClient:
    """Main client for the Aspect Media Engine SDK"""
    
    # Type annotations for resource attributes
    assets: Assets
    indexes: Indexes
    users: Users
    search: Search
    tasks: Tasks
    analyze: Analyze
    
    def __init__(self, config: AspectClientConfig):
        # Create configuration for the generated SDK
        sdk_config = Configuration(
            host=config.base_url or "https://api.aspect.ai",
            access_token=config.api_key,
        )
        
        # Store configs
        self.config = config
        self._sdk_config = sdk_config
        
        # Initialize resource instances
        self.assets = Assets(sdk_config)
        self.indexes = Indexes(sdk_config)
        self.users = Users(sdk_config)
        self.search = Search(sdk_config)
        self.tasks = Tasks(sdk_config)
        self.analyze = Analyze(sdk_config)