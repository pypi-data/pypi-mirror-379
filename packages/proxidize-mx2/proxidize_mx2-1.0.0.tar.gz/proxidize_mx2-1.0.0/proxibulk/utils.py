
"""Utility functions (parsing, helpers, network, PLMN map)."""
import re
import json
import time
from typing import Optional, Tuple, Dict, Any, List
import requests
from requests.exceptions import RequestException
import os

PROBE_TIMEOUT = 10
PROBE_RETRIES = 2
WEBAPI_URL = "http://192.168.1.1/jrd/webapi"
ADMIN_PASSWORD = "admin"

PROXY_LINE_RE = re.compile(r"^([^:\s]+):(\d+):([^:\s]+):([^:\s]+)$")




def parse_proxy_line(line: str) -> Optional[Tuple[str,int,str,str]]:
    m = PROXY_LINE_RE.match(line.strip())
    if not m:
        return None
    host, port, user, pwd = m.group(1), int(m.group(2)), m.group(3), m.group(4)
    return host, port, user, pwd

def build_requests_proxy(host: str, port: int, user: str, pwd: str) -> Dict[str,str]:
    auth = f"{user}:{pwd}@"
    proxy_auth = f"http://{auth}{host}:{port}"
    return {"http": proxy_auth, "https": proxy_auth}

def jsonrpc_post(session: requests.Session, url: str, proxy: Dict[str,str], method: str, 
               params=None, headers=None, timeout=PROBE_TIMEOUT, retries=PROBE_RETRIES, no_log=False) -> Tuple[bool, Optional[dict]]:
    """
    Send a JSON-RPC request to the modem API.
    
    Args:
        session: Requests session to use
        url: API endpoint URL
        proxy: Proxy configuration dict
        method: API method name to call
        params: Method parameters (default: {})
        headers: Optional additional headers
        timeout: Request timeout in seconds
        
    Returns:
        Tuple of (success, response_json)
    """
    # Per API doc, params should be an object ({}), not a list, for info queries
    if params is None:
        params = {}
        
    # Prepare JSON-RPC payload
    payload = {
        "jsonrpc": "2.0", 
        "id": method, 
        "method": method, 
        "params": params
    }
    
    # Set up headers - follow the exact format from bash example
    request_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://192.168.1.1",
        "Referer": "http://192.168.1.1/index.html"
    }
    
    # Add any additional headers
    if headers:
        request_headers.update(headers)
    
    # Attempt request with retries
    for attempt in range(retries + 1):
        try:
            # Debug output removed for cleaner UI/UX - no verbose JSON output
            
            # Use timeout directly - we now manage this at the probe_modem level
            resp = session.post(
                url, 
                json=payload, 
                headers=request_headers, 
                proxies=proxy, 
                timeout=timeout
            )
            
            if resp.status_code == 200:
                try:
                    j = resp.json()
                    # Check for API error responses
                    if isinstance(j, dict) and "error" in j:
                        error = j.get("error", {})
                        code = error.get("code", "unknown")
                        message = error.get("message", "Unknown error")
                        return False, j
                    return True, j
                except Exception as e:
                    # Not valid JSON response - fail silently for cleaner UI
                    pass
                    
        except RequestException as e:
            # Network errors are now handled silently for cleaner UI - 
            # connection status will be reflected in the modem's reachable status
            pass
            
        # Wait before retry with faster backoff for probing
        if attempt < retries:
            if timeout <= 2:  # Ultra-fast mode
                time.sleep(0.05)  # Minimal delay for ultra-fast probing
            elif timeout <= 5:  # Fast mode
                time.sleep(0.1)   # Very short delay for fast probing
            else:
                time.sleep(0.2 * (attempt + 1))  # Increasing backoff for normal operations
        
    return False, None

def http_get(session: requests.Session, url: str, proxy: Dict[str,str], timeout=PROBE_TIMEOUT) -> Tuple[bool, Optional[requests.Response]]:
    # Determine retry settings based on timeout parameter
    # If timeout is less than standard PROBE_TIMEOUT, we're in "fast mode"
    retries = 1 if timeout <= 5 else PROBE_RETRIES
    
    for attempt in range(retries + 1):
        try:
            # For fast probing, use a shorter timeout on the first attempt
            current_timeout = timeout
            if attempt == 0 and timeout > 5:
                current_timeout = 5  # Use shorter timeout on first attempt
                
            r = session.get(url, proxies=proxy, timeout=current_timeout)
            if r.status_code == 200:
                return True, r
        except RequestException:
            pass
            
        # Faster retry logic for probing
        if attempt < retries:
            if timeout <= 5:  # Fast mode
                time.sleep(0.1)  # Very short delay for fast probing
            else:
                time.sleep(0.2 * (attempt + 1))  # Increasing backoff for normal operations
                
    return False, None

def extract_plmn(*json_objs) -> Optional[str]:
    for obj in json_objs:
        if not obj:
            continue
        found = search_for_keys(obj, ["plmn", "mcc", "mnc", "operatorNumeric", "operator"])
        if found:
            if "plmn" in found:
                return str(found["plmn"])
            if "operatorNumeric" in found:
                return str(found["operatorNumeric"])
            if "mcc" in found and "mnc" in found:
                return f"{found['mcc']}{found['mnc']}"
            if "operator" in found:
                digits = re.findall(r"\d{5,6}", str(found["operator"]))
                if digits:
                    return digits[0]
    return None

def search_for_keys(obj: Any, keys: List[str]) -> Optional[dict]:
    if isinstance(obj, dict):
        hits = {}
        for k, v in obj.items():
            lk = k.lower()
            if any(k2.lower() == lk for k2 in keys):
                hits[k] = v
        if hits:
            return hits
        for v in obj.values():
            res = search_for_keys(v, keys)
            if res:
                return res
    elif isinstance(obj, list):
        for item in obj:
            res = search_for_keys(item, keys)
            if res:
                return res
    return None
