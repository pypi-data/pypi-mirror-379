"""Probing and network functions."""
from typing import Dict, Tuple, Optional, Any
import requests
from requests.exceptions import RequestException
import time
from .utils import build_requests_proxy, jsonrpc_post, http_get, extract_plmn
from .modem import Modem

# Ultra-fast timeout for initial probing
ULTRA_FAST_TIMEOUT = 5  # Ultra fast for initial connectivity check
PROBE_TIMEOUT = 10       # Fast for detailed probing
PROBE_RETRIES = 1       # No retries for initial probe (we'll handle retries at a higher level)

# For operations that need more reliability (like connecting/disconnecting)
OPERATION_TIMEOUT = 10
OPERATION_RETRIES = 2

WEBUI_INDEX_URL = "http://192.168.1.1/"
WEBAPI_URL = "http://192.168.1.1/jrd/webapi"
ADMIN_PASSWORD = "admin"

# Set of fastest API methods to check for modem connectivity
# These are typically the most lightweight calls that will respond quickly
FAST_API_METHODS = ["GetLoginToken", "GetLoginState", "HeartBeat"]


def probe_modem(modem: Modem, fast_probe: bool = True, get_full_info: bool = True, ultra_fast: bool = False) -> Modem:
    """
    Probe a modem to determine if it's reachable and get its basic information.
    
    Args:
        modem: The modem to probe
        fast_probe: If True, use faster timeouts and minimal API calls
        get_full_info: If True, get full network info (can be skipped for basic connectivity check)
        ultra_fast: If True, use ultra-fast mode with minimal API calls and shortest timeouts
        
    Returns:
        The updated modem object
    """
    session = requests.Session()
    modem.proxy = build_requests_proxy(modem.host, modem.port, modem.user, modem.pwd)
    
    # Use appropriate timeout based on probe mode
    if ultra_fast:
        timeout = ULTRA_FAST_TIMEOUT  # Ultra-fast mode (2s)
        retries = 0                    # No retries in ultra-fast mode
    elif fast_probe:
        timeout = PROBE_TIMEOUT        # Fast mode (4s)
        retries = PROBE_RETRIES        # Limited retries in fast mode
    else:
        timeout = OPERATION_TIMEOUT    # Normal mode (10s)
        retries = OPERATION_RETRIES    # Full retries in normal mode
    
    # In ultra-fast mode, we'll try multiple lightweight API methods in sequence
    # and stop at the first success
    if ultra_fast:
        for method in FAST_API_METHODS:
            # Using no_log=True to avoid cluttering logs during fast probing
            ok, j = jsonrpc_post(session, WEBAPI_URL, modem.proxy, method, params={}, 
                                timeout=timeout, retries=retries, no_log=True)
            if ok:
                modem.reachable = True
                return modem
        
        # If all fast methods failed, try one more method with a slightly longer timeout
        ok, j = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetSystemInfo", params={}, 
                           timeout=timeout+1, retries=retries, no_log=True)
        if ok:
            modem.reachable = True
            modem.system_info = j
            return modem
            
        modem.reachable = False
        modem.error = "Unreachable or unsupported WebUI"
        return modem
    
    # Standard probing logic for fast and normal modes
    # Step 1: Try the most important API call directly (skipping WebUI index page)
    ok, j = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetSystemInfo", params={}, 
                       timeout=timeout, retries=retries)
    if ok and isinstance(j, dict):
        modem.reachable = True
        modem.system_info = j
        
        # If we only need basic connectivity check, we can stop here
        if not get_full_info:
            # Try to extract basic info from system_info
            plmn = extract_plmn(modem.system_info, {})
            if plmn:
                modem.plmn = plmn
            return modem
            
        # Get network info for full probe
        ok2, j2 = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetNetworkInfo", params={}, 
                             timeout=timeout, retries=retries)
        if ok2 and isinstance(j2, dict):
            modem.network_info = j2
            # Extract PLMN
            plmn = extract_plmn(modem.system_info, modem.network_info)
            if plmn:
                modem.plmn = plmn
            # Extract carrier name from NetworkInfo per API doc
            result = j2.get("result") if isinstance(j2, dict) else None
            carrier = None
            if result and isinstance(result, dict):
                carrier = result.get("NetworkName")
                if not carrier or carrier == "N/A":
                    carrier = result.get("SpnName")
                if not carrier or carrier == "N/A":
                    carrier = result.get("PLMN_name")
            modem.carrier = carrier if carrier and carrier != "N/A" else "Unknown/Unsupported"
            
            # Get connection state if doing full probe
            # Skip this for faster probing as it's not essential for basic identification
            if not fast_probe:
                try:
                    ok_conn, j_conn = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetConnectionState", params={}, 
                                                 timeout=timeout, retries=retries)
                    if ok_conn and isinstance(j_conn, dict):
                        modem.connection_state = j_conn
                except Exception:
                    pass
                
            return modem
            
        # Only try GetSimStatus if we need full info and GetNetworkInfo failed
        if get_full_info:
            ok3, j3 = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetSimStatus", params={}, 
                                 timeout=timeout, retries=retries)
            if ok3 and isinstance(j3, dict):
                modem.network_info = j3
        
        modem.carrier = "Unknown/Unsupported"
        return modem
        
    # If GetSystemInfo failed, try GetLoginToken as a fallback
    # This is a lightweight API call that most modems should support
    ok, j = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetLoginToken", params={}, 
                       timeout=timeout, retries=retries)
    if ok and isinstance(j, dict):
        modem.reachable = True
        modem.system_info = j
        plmn = extract_plmn(modem.system_info, modem.network_info)
        if plmn:
            modem.plmn = plmn
        modem.carrier = "Unknown/Unsupported"
        return modem
        
    modem.reachable = False
    modem.error = "Unreachable or unsupported WebUI"
    return modem
