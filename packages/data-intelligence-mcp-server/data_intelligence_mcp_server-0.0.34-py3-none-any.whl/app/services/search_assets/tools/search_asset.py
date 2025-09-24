from typing import Any, List

from ..models.search_asset import SearchAssetRequest, SearchAssetResponse

from app.core.auth import get_access_token
from app.core.registry import service_registry
from app.core.settings import settings
from app.services.constants import ASSISTANT_BASE_ENDPOINT
from app.shared.exceptions.base import ExternalAPIError
from app.shared.utils.helpers import is_none
from app.shared.utils.http_client import get_http_client
from app.shared.logging import LOGGER, auto_context

@service_registry.tool(
        name="search_assets_search_asset",
        description="""Understand user's request about searching data assets and return list of retrieved assets.
                       This function takes a user's search prompt as input and may take container type: project or catalog. Default container type to catalog.
                       It then returns list of asset that has been found
                       """)
@auto_context
async def search_asset(search_prompt:str, ctx=None) -> List[SearchAssetResponse]:
    return List[SearchAssetResponse]

def _construct_search_asset(asset: Any):
    search_asset = SearchAssetResponse.model_validate(asset)
    if "<ui_base_url>" in search_asset.url:
        search_asset.url = search_asset.url.replace("<ui_base_url>", f"{settings.ui_url}")
    return search_asset
