"""
Utility functions for BloxAPI
"""

from typing import Dict, Any, Optional
import re


def validate_asset_id(asset_id: int) -> bool:
    """
    Validate if an asset ID is potentially valid
    
    Args:
        asset_id (int): The asset ID to validate
        
    Returns:
        bool: True if the asset ID seems valid
    """
    return isinstance(asset_id, int) and asset_id > 0


def validate_user_id(user_id: int) -> bool:
    """
    Validate if a user ID is potentially valid
    
    Args:
        user_id (int): The user ID to validate
        
    Returns:
        bool: True if the user ID seems valid
    """
    return isinstance(user_id, int) and user_id > 0


def parse_roblox_url(url: str) -> Optional[Dict[str, Any]]:
    """
    Parse a Roblox URL to extract relevant information
    
    Args:
        url (str): The Roblox URL to parse
        
    Returns:
        Optional[Dict[str, Any]]: Parsed information or None if invalid
    """
    patterns = {
        'user': r'https?://(?:www\.)?roblox\.com/users/(\d+)',
        'asset': r'https?://(?:www\.)?roblox\.com/catalog/(\d+)',
        'game': r'https?://(?:www\.)?roblox\.com/games/(\d+)',
        'place': r'https?://(?:www\.)?roblox\.com/games/(\d+)'
    }
    
    for type_name, pattern in patterns.items():
        match = re.search(pattern, url)
        if match:
            return {
                'type': type_name,
                'id': int(match.group(1)),
                'url': url
            }
    
    return None


def format_robux(amount: int) -> str:
    """
    Format a Robux amount with proper comma separation
    
    Args:
        amount (int): The Robux amount
        
    Returns:
        str: Formatted Robux string
    """
    return f"R$ {amount:,}"


class BloxAPIError(Exception):
    """Base exception for BloxAPI"""
    pass


class InvalidAssetError(BloxAPIError):
    """Raised when an invalid asset ID is provided"""
    pass


class InvalidUserError(BloxAPIError):
    """Raised when an invalid user ID is provided"""
    pass


class APIRequestError(BloxAPIError):
    """Raised when an API request fails"""
    pass
