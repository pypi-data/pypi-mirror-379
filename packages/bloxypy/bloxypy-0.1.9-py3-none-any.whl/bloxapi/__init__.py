"""
BloxAPI - Advanced Roblox wrapper for the Roblox API
"""

from .client import Client
from .utils import (
    BloxAPIError, 
    InvalidAssetError, 
    InvalidUserError, 
    APIRequestError,
    validate_asset_id,
    validate_user_id,
    parse_roblox_url,
    format_robux
)

__version__ = "0.1.9"
__author__ = "jmkdev"
__email__ = "jmkdev@gmail.com"

# Make Client and utilities available at package level
__all__ = [
    "Client", 
    "BloxAPIError", 
    "InvalidAssetError", 
    "InvalidUserError", 
    "APIRequestError",
    "validate_asset_id",
    "validate_user_id", 
    "parse_roblox_url",
    "format_robux"
]
