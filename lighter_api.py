import requests
import logging
from typing import Optional, Dict, Any
from urllib.parse import urljoin
import os

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Configuration management using environment variables
BASE_URL = os.getenv("ZKLIGHTER_BASE_URL", "https://mainnet.zklighter.elliot.ai")
DEFAULT_TIMEOUT = int(os.getenv("REQUEST_TIMEOUT", "10"))
DEFAULT_HEADERS = {"accept": "application/json"}


class APIError(Exception):
    """Custom exception for API-related errors"""

    pass


def _make_request(
    url: str, params: Optional[Dict[str, Any]] = None, timeout: int = DEFAULT_TIMEOUT
) -> Optional[Dict[str, Any]]:
    """Centralized function to make HTTP requests with proper error handling."""
    try:
        logger.info(f"Making request to: {url}")
        response = requests.get(
            url, params=params, headers=DEFAULT_HEADERS, timeout=timeout
        )
        response.raise_for_status()
        return response.json()
    except requests.exceptions.Timeout:
        logger.error(f"Request timeout for URL: {url}")
        raise APIError(f"Request timeout after {timeout} seconds")
    except requests.exceptions.ConnectionError:
        logger.error(f"Connection error for URL: {url}")
        raise APIError("Failed to connect to the API")
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error {e.response.status_code} for URL: {url}")
        raise APIError(f"HTTP error: {e.response.status_code}")
    except requests.exceptions.RequestException as e:
        logger.error(f"Request error for URL {url}: {e}")
        raise APIError(f"Request failed: {str(e)}")
    except ValueError as e:
        logger.error(f"JSON parsing error for URL {url}: {e}")
        raise APIError(f"Invalid JSON response: {str(e)}")


# Utility function for health check
def health_check() -> bool:
    """Check if the API is accessible."""
    try:
        url = urljoin(BASE_URL, "")
        _make_request(url, timeout=5)
        return True
    except APIError:
        return False


def get_account_index(l1_address: str) -> Optional[Dict[str, Any]]:
    """Fetch account index by L1 address."""
    if not l1_address or not isinstance(l1_address, str):
        logger.error("Invalid L1 address provided")
        return None

    try:
        url = urljoin(BASE_URL, "/api/v1/accountsByL1Address")
        params = {"l1_address": l1_address}
        return _make_request(url, params=params)
    except APIError as e:
        logger.error(f"Failed to get account index for {l1_address}: {e}")
        return None


def get_account(by: str, value: str) -> Optional[Dict[str, Any]]:
    """Fetch account by index or L1 address."""
    if not isinstance(by, str) or not isinstance(value, str):
        logger.error("Invalid parameter types provided for 'by' or 'value'")
        return None

    if by not in ["index", "l1_address"]:
        logger.error(f"Invalid 'by' parameter '{by}'. Must be 'index' or 'l1_address'")
        return None

    if not value.strip():
        logger.error("Value cannot be empty")
        return None

    try:
        url = urljoin(BASE_URL, "/api/v1/account")
        params = {"by": by, "value": value}
        return _make_request(url, params=params)
    except APIError as e:
        logger.error(f"Failed to get account by {by}={value}: {e}")
        return None


def get_orderbook_details(market_id: Optional[str] = None) -> Optional[Dict[str, Any]]:
    """Fetch orderbook details for a specific market or all markets if no market_id is provided."""
    try:
        url = urljoin(BASE_URL, "/api/v1/orderBookDetails")
        params = {}
        if market_id:
            params["market_id"] = market_id
        return _make_request(url, params=params)
    except APIError as e:
        logger.error(
            f"Failed to get orderbook metadata for market {market_id if market_id else 'all markets'}: {e}"
        )
        return None


def fetch_candlesticks(
    market_id: str = "1",
    resolution: str = "1d",
    start_timestamp: int = 0,
    end_timestamp: int = 5000000000000,
    count_back: int = 10,
) -> Optional[Dict[str, Any]]:
    """Fetch candlesticks data with comprehensive parameters."""
    if not all(
        isinstance(param, (str, int))
        for param in [market_id, resolution, start_timestamp, end_timestamp, count_back]
    ):
        logger.error("Invalid parameter types provided")
        return None

    if start_timestamp >= end_timestamp:
        logger.error("start_timestamp must be less than end_timestamp")
        return None

    allowed_resolutions = {"1m", "5m", "15m", "30m", "1h", "4h", "12h", "1d", "1w"}
    if resolution not in allowed_resolutions:
        logger.error(
            f"Invalid resolution '{resolution}'. Allowed values: {allowed_resolutions}"
        )
        return None

    try:
        url = urljoin(BASE_URL, "/api/v1/candlesticks")
        params = {
            "market_id": market_id,
            "resolution": resolution,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "count_back": count_back,
        }
        return _make_request(url, params=params)
    except APIError as e:
        logger.error(f"Failed to fetch candlesticks with params {params}: {e}")
        return None


def fetch_funding_rates(
    market_id: str = "1",
    resolution: str = "1h",
    start_timestamp: int = 0,
    end_timestamp: int = 5000000000000,
    count_back: int = 10,
) -> Optional[Dict[str, Any]]:
    """Fetch funding rates data with comprehensive parameters."""
    if not all(
        isinstance(param, (str, int))
        for param in [market_id, resolution, start_timestamp, end_timestamp, count_back]
    ):
        logger.error("Invalid parameter types provided")
        return None

    if start_timestamp >= end_timestamp:
        logger.error("start_timestamp must be less than end_timestamp")
        return None

    allowed_resolutions = {"1h", "1d"}
    if resolution not in allowed_resolutions:
        logger.error(
            f"Invalid resolution '{resolution}'. Allowed values: {allowed_resolutions}"
        )
        return None

    try:
        url = urljoin(BASE_URL, "/api/v1/fundings")
        params = {
            "market_id": market_id,
            "resolution": resolution,
            "start_timestamp": start_timestamp,
            "end_timestamp": end_timestamp,
            "count_back": count_back,
        }
        return _make_request(url, params=params)
    except APIError as e:
        logger.error(f"Failed to fetch funding rates with params {params}: {e}")
        return None


def get_current_funding_rates() -> Optional[Dict[str, Any]]:
    """Fetch current funding rates for all markets."""
    try:
        url = urljoin(BASE_URL, "/api/v1/funding-rates")
        return _make_request(url)
    except APIError as e:
        logger.error(f"Failed to get current funding rates: {e}")
        return None
