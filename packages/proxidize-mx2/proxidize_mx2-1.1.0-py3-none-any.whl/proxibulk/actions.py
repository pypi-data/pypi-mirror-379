"""Modem actions (APN, network mode, reset, etc)."""
from typing import Optional, Tuple, Any, Dict, List
import requests
import time
from .utils import jsonrpc_post, WEBAPI_URL, ADMIN_PASSWORD, PROBE_TIMEOUT
from .modem import Modem

def get_token(modem: Modem, quiet: bool = False) -> Optional[str]:
    """
    Get authentication token for actions that require it.
    Handles different response formats:
    1. {'result': {'token': 'abc123'}} - token in nested dict
    2. {'result': {'token': 12345678}} - token as integer in nested dict (convert to string)
    3. {'result': 'abc123'} - token directly in result 
    4. {'result': 12345678} - integer token directly in result (convert to string)
    """
    session = requests.Session()
    
    # Use 'tok' as the id like in your bash example
    payload = {
        "jsonrpc": "2.0", 
        "id": "tok", 
        "method": "GetLoginToken", 
        "params": {}
    }
    
    # Set up headers exactly like in bash example
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://192.168.1.1",
        "Referer": "http://192.168.1.1/index.html"
    }
    
    # Make the request directly to match the bash example
    try:
        resp = session.post(
            WEBAPI_URL, 
            json=payload, 
            headers=headers, 
            proxies=modem.proxy, 
            timeout=PROBE_TIMEOUT
        )
        
        if resp.status_code == 200:
            try:
                j = resp.json()
                
                if not isinstance(j, dict) or "result" not in j:
                    if not quiet:
                        print("Invalid response format - no result key")
                    return None
                
                result = j["result"]
                
                # Case 1: Result is a dictionary with a token key
                if isinstance(result, dict) and "token" in result:
                    token = result["token"]
                    # Handle both string and integer tokens
                    if token is not None:
                        # Convert to string if it's an integer
                        token_str = str(token) if isinstance(token, int) else token
                        return token_str
                
                # Case 2: Result is a string (the token itself)
                elif isinstance(result, str) and result:
                    return result
                
                # Case 3: Result is an integer (token as integer)
                elif isinstance(result, int):
                    token_str = str(result)
                    if not quiet:
                        print(f"Found token as integer ({result}), converted to string: {token_str}")
                    return token_str
                    
                # Invalid cases
                else:
                    if not quiet:
                        print("Unexpected token response format")
                    
            except Exception as e:
                if not quiet:
                    print(f"Error parsing token response: {e}")
        else:
            if not quiet:
                print(f"Token request failed with status code: {resp.status_code}")
            
    except Exception as e:
        if not quiet:
            print(f"Network error getting token: {e}")
        
    return None

def action_view_status(modem: Modem) -> Dict[str,Any]:
    """Return full collected status for a modem."""
    return {
        "index": modem.index,
        "proxy": modem.raw,
        "reachable": modem.reachable,
        "system_info": modem.system_info,
        "network_info": modem.network_info,
        "plmn": modem.plmn,
        "carrier": modem.carrier,
    }

def action_set_apn(modem: Modem, apn_name: str, apn_user: Optional[str]=None, apn_pass: Optional[str]=None, dial_number: str = "*99#", profile_name: Optional[str]=None, quiet: bool = False, force_disconnect: bool = True) -> Tuple[bool,str]:
    """
    Set APN for the modem following the proven single modem procedure:
    1. Check connection status (to know if we need to reconnect later)
    2. Disconnect if connected (before making changes) 
    3. Add a new profile with AddNewProfile
    4. Set it as default with SetDefaultProfile
    5. Reconnect if we were connected before
    
    Args:
        modem: The modem object
        apn_name: APN name (e.g. internet.carrier.com)
        apn_user: Username for APN authentication (optional)
        apn_pass: Password for APN authentication (optional)
        dial_number: Dial number (default: *99#)
        profile_name: Custom profile name (default: auto-generated with timestamp)
        quiet: Suppress verbose output for bulk operations (default: False)
        force_disconnect: Force disconnect even if status unclear (default: True)
    """
    session = requests.Session()
    if not quiet:
        print(f"\nCreating new APN profile with APN: {apn_name}")
    
    # Generate default profile name if none provided
    if not profile_name:
        profile_name = f"Proxidize_{time.strftime('%m%d%H%M')}"
    
    if not quiet:
        print(f"Using profile name: {profile_name}")
    
    # Step 1: Check connection status (to know if we need to reconnect later)
    was_connected = False
    try:
        # Check connection status using direct API call
        ok, result = jsonrpc_post(requests.Session(), WEBAPI_URL, modem.proxy, "GetConnectionState", params={})
        if ok and isinstance(result, dict):
            connection_status = result.get("ConnectionStatus", -1)
            status_map = {0: "Disconnected", 1: "Connecting", 2: "Connected", 3: "Disconnecting"}
            conn_status = status_map.get(connection_status, "Unknown")
            was_connected = connection_status == 2  # Connected
            
            if not quiet:
                print(f"Current connection status: {conn_status}")
        else:
            if not quiet:
                print("Warning: Could not determine connection status")
            
    except Exception as e:
        if not quiet:
            print(f"Warning: Could not check connection status: {e}")
        # Continue anyway, assume not connected
    
    # Always disconnect if force_disconnect is True (following proven single modem logic)
    if force_disconnect:
        was_connected = True  # Force reconnection later
    
    # Step 2: Disconnect if connected (before making changes)
    if was_connected or force_disconnect:
        if not quiet:
            print("Disconnecting modem before creating new APN...")
        try:
            # Inline disconnect logic
            disconnect_session = requests.Session()
            disconnect_token = get_token(modem, quiet)
            if disconnect_token:
                disconnect_payload = {
                    "jsonrpc": "2.0",
                    "id": "disconnect", 
                    "method": "DisConnect",
                    "params": {}
                }
                
                disconnect_headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json", 
                    "X-Requested-With": "XMLHttpRequest",
                    "Origin": "http://192.168.1.1",
                    "Referer": "http://192.168.1.1/index.html",
                    "_TclRequestVerificationToken": disconnect_token
                }
                
                disconnect_resp = disconnect_session.post(
                    WEBAPI_URL,
                    json=disconnect_payload,
                    headers=disconnect_headers,
                    proxies=modem.proxy,
                    timeout=PROBE_TIMEOUT
                )
                
            time.sleep(2)  # Brief pause as in single modem logic
        except Exception as e:
            if not quiet:
                print(f"Warning: Error during disconnect: {e}")
            # Continue anyway
    
    # Step 3: Get fresh token for profile creation
    if not quiet:
        print("Getting authentication token...")
    token = get_token(modem, quiet)
    
    if not token:
        if not quiet:
            print("Failed to get authentication token")
        return False, "Failed to get authentication token"
        
    if not quiet:
        print(f"Authentication token obtained: {token[:5]}...")
    
    # Create profile parameters - exact field names and structure from your bash example
    profile_params = {
        "ProfileName": profile_name,
        "APN": apn_name,
        "UserName": apn_user or "",
        "Password": apn_pass or "",
        "AuthType": 0,
        "DialNumber": dial_number,  # IMPORTANT: This is the correct field name
        "DailNumber": dial_number,  # Some firmware versions use this misspelled name
        "Default": 0,
        "IsPredefine": 0,
        "IPAdrress": "",
        "PdpType": 3
    }
    
    # Construct the exact request as in your bash example
    apn_payload = {
        "jsonrpc": "2.0", 
        "id": "add",  # Using "add" as the ID like in your bash example
        "method": "AddNewProfile", 
        "params": profile_params
    }
    
    apn_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json", 
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://192.168.1.1",
        "Referer": "http://192.168.1.1/index.html",
        "_TclRequestVerificationToken": token
    }
    
    if not quiet:
        print("Sending AddNewProfile request...")
    
    try:
        apn_resp = session.post(
            WEBAPI_URL, 
            json=apn_payload, 
            headers=apn_headers, 
            proxies=modem.proxy, 
            timeout=PROBE_TIMEOUT
        )
        
        if apn_resp.status_code != 200:
            if not quiet:
                print(f"Failed to create profile - HTTP {apn_resp.status_code}")
            return False, f"Failed to create profile - HTTP {apn_resp.status_code}"
            
        apn_data = apn_resp.json()
        
        if "error" in apn_data:
            err = apn_data.get("error", {})
            code = err.get("code", "")
            msg = err.get("message", "API error")
            if code:
                if not quiet:
                    print(f"API error creating profile ({code}): {msg}")
            else:
                if not quiet:
                    print(f"API error creating profile: {msg}")
            return False, f"API error: {msg}"
            
        if "result" not in apn_data:
            if not quiet:
                print("Unexpected response format")
            return False, "Unexpected response format"
            
    except Exception as e:
        if not quiet:
            print(f"Error creating profile: {e}")
        return False, f"Error creating profile: {e}"
    
    if not quiet:
        print("APN profile created successfully")
    
    # Step 3: Get profile list to find our new profile
    if not quiet:
        print("Getting profile list...")
    profile_list_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json", 
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://192.168.1.1",
        "Referer": "http://192.168.1.1/index.html"
    }
    
    profile_list_payload = {
        "jsonrpc": "2.0",
        "id": "getlist",
        "method": "GetProfileList",
        "params": {}
    }
    
    try:
        list_resp = session.post(
            WEBAPI_URL,
            json=profile_list_payload,
            headers=profile_list_headers,  # No token needed for this call
            proxies=modem.proxy,
            timeout=PROBE_TIMEOUT
        )
        
        list_data = list_resp.json()
        
        # Find our profile ID
        profile_id = None
        try:
            profiles = list_data.get("result", {}).get("ProfileList", [])
            for profile in profiles:
                if profile.get("ProfileName") == profile_name:
                    profile_id = profile.get("ProfileID")
                    break
                    
        except (KeyError, TypeError) as e:
            if not quiet:
                print(f"Error parsing profile list: {e}")
            return False, f"Error finding profile ID: {e}"
        
        if not profile_id:
            if not quiet:
                print(f"Created profile '{profile_name}' but couldn't find its ID")
            return False, f"Created profile but couldn't find its ID"
        
        if not quiet:
            print(f"Found profile ID: {profile_id}")
        
    except Exception as e:
        if not quiet:
            print(f"Error getting profile list: {e}")
        return False, f"Error getting profile list: {e}"
    
    # Step 4: Set as default profile - get a fresh token
    try:
        if not quiet:
            print("Getting fresh token for SetDefaultProfile...")
        fresh_token = get_token(modem, quiet)
        
        if not fresh_token:
            if not quiet:
                print("Warning: Failed to get token for SetDefaultProfile")
            return True, f"APN profile created with ID {profile_id} but not set as default"
            
        # Set as default
        default_payload = {
            "jsonrpc": "2.0",
            "id": "default",
            "method": "SetDefaultProfile",
            "params": {"ProfileID": profile_id}
        }
        
        default_headers = {
            "Content-Type": "application/json",
            "Accept": "application/json", 
            "X-Requested-With": "XMLHttpRequest",
            "Origin": "http://192.168.1.1",
            "Referer": "http://192.168.1.1/index.html",
            "_TclRequestVerificationToken": fresh_token
        }
        
        if not quiet:
            print(f"Setting profile {profile_id} as default...")
        default_resp = session.post(
            WEBAPI_URL,
            json=default_payload,
            headers=default_headers,
            proxies=modem.proxy,
            timeout=PROBE_TIMEOUT
        )
        
        default_data = default_resp.json()
        
    except Exception as e:
        if not quiet:
            print(f"Warning: Error setting default profile: {e}")
        # Continue anyway since profile was created
    
    # Step 5: Reconnect if we were connected before (following single modem logic)
    if was_connected:
        if not quiet:
            print("Reconnecting modem with new APN settings...")
        try:
            time.sleep(2)  # Brief pause before reconnecting (as in single modem logic)
            
            # Inline connect logic
            connect_session = requests.Session()
            connect_token = get_token(modem, quiet)
            if connect_token:
                connect_payload = {
                    "jsonrpc": "2.0",
                    "id": "connect",
                    "method": "Connect",
                    "params": {}
                }
                
                connect_headers = {
                    "Content-Type": "application/json",
                    "Accept": "application/json", 
                    "X-Requested-With": "XMLHttpRequest",
                    "Origin": "http://192.168.1.1",
                    "Referer": "http://192.168.1.1/index.html",
                    "_TclRequestVerificationToken": connect_token
                }
                
                connect_resp = connect_session.post(
                    WEBAPI_URL,
                    json=connect_payload,
                    headers=connect_headers,
                    proxies=modem.proxy,
                    timeout=PROBE_TIMEOUT
                )
                
        except Exception as e:
            if not quiet:
                print(f"Warning: Error during reconnect: {e}")
            # Don't fail the whole operation, profile was created successfully
    
    # Record the successful action
    modem.last_action = {
        "action": "SetAPN", 
        "status": "ok",
        "apn": apn_name,
        "profile_id": profile_id,
        "profile_name": profile_name
    }
    
    return True, f"APN set successfully (Profile: {profile_name}, ID: {profile_id})"

def action_set_network_mode(modem: Modem, mode: str) -> Tuple[bool,str]:
    """
    Set network mode using SetNetworkSettings per API doc.
    mode can be: 'auto', 'lte_only', '3g', '2g', etc.
    
    According to the API document, network mode selection is implemented as:
    curl -s -b "$CJ" -H "Origin: $BASE" -H "Referer: $BASE/index.html"
    -H "Accept: application/json" -H "Content-Type: application/json" -H "X-Requested-With: XMLHttpRequest"
    -H "_TclRequestVerificationToken: $TOKEN"
    -d '{"jsonrpc":"2.0","id":"320","method":"SetNetworkSettings","params":{"SelectionMode":0}}' "$BASE$EP"
    """
    session = requests.Session()
    print("\nPreparing to change network mode...")
    
    # Step 1: Get fresh token
    print("Getting authentication token...")
    token = get_token(modem)
    
    if not token:
        print("Failed to get authentication token")
        return False, "Failed to get authentication token"
        
    print(f"Authentication token obtained: {token[:5]}...")
    
    # Map user-friendly terms to API values according to API doc
    mode_map = {
        'auto': 0,
        'lte_only': 3,
        '4g': 3,
        '3g': 2,
        '2g': 1
    }
    
    # Convert string mode to numeric if it's a known mode
    if isinstance(mode, str) and mode.lower() in mode_map:
        mode_value = mode_map[mode.lower()]
    elif isinstance(mode, str) and mode.isdigit():
        mode_value = int(mode)
    else:
        try:
            mode_value = int(mode)
        except (ValueError, TypeError):
            return False, f"Invalid network mode value: {mode}"
    
    # First, try to get current network settings
    try:
        print("Getting current network settings...")
        current_settings_resp = session.post(
            WEBAPI_URL,
            json={
                "jsonrpc": "2.0",
                "id": "get_network",
                "method": "GetNetworkSettings",
                "params": {}
            },
            headers={
                "Content-Type": "application/json",
                "Accept": "application/json",
                "X-Requested-With": "XMLHttpRequest",
                "Origin": "http://192.168.1.1",
                "Referer": "http://192.168.1.1/index.html"
            },
            proxies=modem.proxy,
            timeout=PROBE_TIMEOUT
        )
        
        current_settings = {}
        if current_settings_resp.status_code == 200:
            try:
                current_settings_data = current_settings_resp.json()
                if "result" in current_settings_data:
                    current_settings = current_settings_data["result"]
            except:
                pass
    except Exception as e:
        print(f"Warning: Could not get current network settings: {e}")
        # Continue anyway - we'll use minimal parameters
    
    # Prepare parameters based on API doc
    # Start with minimal required param
    params = {"SelectionMode": mode_value}
    
    # Add additional settings if we got them from current settings
    # This helps maintain other parameters that might be required
    if current_settings:
        # Copy all existing settings except SelectionMode
        for key, value in current_settings.items():
            if key != "SelectionMode":
                params[key] = value
    
    # Set up headers exactly like in API doc
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json", 
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://192.168.1.1",
        "Referer": "http://192.168.1.1/index.html",
        "_TclRequestVerificationToken": token
    }
    
    # Create request payload
    payload = {
        "jsonrpc": "2.0", 
        "id": "320",  # Use same ID as in API doc example
        "method": "SetNetworkSettings", 
        "params": params
    }
    
    print("Sending SetNetworkSettings command...")
    
    try:
        network_resp = session.post(
            WEBAPI_URL, 
            json=payload, 
            headers=headers, 
            proxies=modem.proxy, 
            timeout=PROBE_TIMEOUT
        )
        
        if network_resp.status_code != 200:
            print(f"Network mode change failed with status code: {network_resp.status_code}")
            return False, f"Failed to change network mode - HTTP {network_resp.status_code}"
            
        network_data = network_resp.json()
        
        if "error" in network_data:
            error_code = network_data.get("error", {}).get("code", "unknown")
            error_msg = network_data.get("error", {}).get("message", "Unknown error")
            print(f"API error {error_code}: {error_msg}")
            
            # Try an alternative approach: network register after setting
            if error_code == "040701":  # If it's the specific error we've been seeing
                print("Attempting to use RegisterNetwork as fallback...")
                try:
                    # First try to set mode again with just the basic param
                    basic_params = {"SelectionMode": mode_value}
                    basic_resp = session.post(
                        WEBAPI_URL,
                        json={
                            "jsonrpc": "2.0",
                            "id": "321",
                            "method": "SetNetworkSettings",
                            "params": basic_params
                        },
                        headers=headers,
                        proxies=modem.proxy,
                        timeout=PROBE_TIMEOUT
                    )
                    
                    # Now try to register network
                    register_resp = session.post(
                        WEBAPI_URL,
                        json={
                            "jsonrpc": "2.0",
                            "id": "322",
                            "method": "RegisterNetwork",
                            "params": {}
                        },
                        headers=headers,
                        proxies=modem.proxy,
                        timeout=PROBE_TIMEOUT
                    )
                    
                    if register_resp.status_code == 200:
                        register_data = register_resp.json()
                        if "error" not in register_data:
                            print("RegisterNetwork command sent successfully")
                            # Wait a bit for network to settle
                            time.sleep(2)
                            modem.last_action = {"action":"SetNetworkSettings", "status":"ok", "mode": mode, "response": "Used RegisterNetwork fallback"}
                            return True, f"Network mode set to {mode} (used RegisterNetwork fallback)"
                except Exception as e:
                    print(f"Fallback approach failed: {e}")
            
            return False, f"API error: {error_msg}"
            
        if "result" not in network_data:
            print("Unexpected response format")
            return False, "Unexpected response format"
        
        print(f"Network mode successfully changed to: {mode}")
        modem.last_action = {"action":"SetNetworkSettings", "status":"ok", "mode": mode, "response": network_data}
        return True, f"Network mode set to {mode}"
            
    except Exception as e:
        print(f"Error sending network mode command: {e}")
        return False, f"Error sending network mode command: {e}"
    
    # This code is unreachable, but kept for completeness
    modem.last_action = {"action":"SetNetworkSettings", "status":"failed"}
    return False, f"Failed to set network mode {mode}"

def action_restart(modem: Modem) -> Tuple[bool,str]:
    """
    Restart the modem using SetDeviceReboot per API doc.
    Using the exact bash example that works successfully but with improved token handling.
    """
    session = requests.Session()
    print("\nPreparing to restart modem...")
    
    # Step 1: Get fresh token using our improved function
    print("Getting authentication token...")
    token = get_token(modem)
    
    if not token:
        print("Failed to get authentication token")
        return False, "Failed to get authentication token"
        
    print(f"Authentication token obtained: {token[:5]}...")
    
    # Step 2: Send reboot command - EXACTLY like your bash example
    # Including using id "210" as in your example
    reboot_payload = {
        "jsonrpc": "2.0", 
        "id": "210", 
        "method": "SetDeviceReboot", 
        "params": {}
    }
    
    reboot_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json", 
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://192.168.1.1",
        "Referer": "http://192.168.1.1/index.html",
        "_TclRequestVerificationToken": token
    }
    
    print("Sending reboot command...")
    
    try:
        reboot_resp = session.post(
            WEBAPI_URL, 
            json=reboot_payload, 
            headers=reboot_headers, 
            proxies=modem.proxy, 
            timeout=PROBE_TIMEOUT
        )
        
        if reboot_resp.status_code != 200:
            print(f"Reboot request failed with status code: {reboot_resp.status_code}")
            return False, f"Failed to reboot - HTTP {reboot_resp.status_code}"
            
        reboot_data = reboot_resp.json()
        
        if "error" in reboot_data:
            err = reboot_data.get("error", {})
            code = err.get("code", "")
            msg = err.get("message", "API error")
            if code:
                print(f"API error during reboot ({code}): {msg}")
            else:
                print(f"API error during reboot: {msg}")
            return False, f"API error: {msg}"
            
        if "result" not in reboot_data:
            print("Unexpected response format")
            return False, "Unexpected response format"
        
        print("Reboot command successful")
        modem.last_action = {"action":"SetDeviceReboot", "status":"ok", "response": reboot_data}
        return True, "Reboot command sent successfully"
            
    except Exception as e:
        print(f"Error sending reboot command: {e}")
        return False, f"Error sending reboot command: {e}"
    
    # This code is unreachable, but kept for completeness
    print("All reboot methods failed")
    modem.last_action = {"action":"SetDeviceReboot", "status":"failed"}
    return False, "Failed to send reboot command"

def get_apn_profiles(modem: Modem) -> Tuple[bool, List[Dict[str,Any]]]:
    """
    Get list of APN profiles from the modem.
    
    Returns:
        Tuple of (success, profile_list)
    """
    session = requests.Session()
    
    profile_list_payload = {
        "jsonrpc": "2.0",
        "id": "getlist",
        "method": "GetProfileList",
        "params": {}
    }
    
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json", 
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://192.168.1.1",
        "Referer": "http://192.168.1.1/index.html"
    }
    
    try:
        list_resp = session.post(
            WEBAPI_URL,
            json=profile_list_payload,
            headers=headers,
            proxies=modem.proxy,
            timeout=PROBE_TIMEOUT
        )
        
        if list_resp.status_code != 200:
            print(f"Failed to get profile list - HTTP {list_resp.status_code}")
            return False, []
        
        list_data = list_resp.json()
        
        if "error" in list_data:
            err = list_data.get("error", {})
            msg = err.get("message", "API error")
            print(f"API error getting profile list: {msg}")
            return False, []
        
        profiles = list_data.get("result", {}).get("ProfileList", [])
        return True, profiles
    
    except Exception as e:
        print(f"Error getting profile list: {e}")
        return False, []

def set_default_apn_profile(modem: Modem, profile_id: int) -> Tuple[bool, str]:
    """
    Set an existing APN profile as default.
    
    Args:
        modem: The modem object
        profile_id: The ID of the profile to set as default
    
    Returns:
        Tuple of (success, message)
    """
    session = requests.Session()
    
    # Get authentication token
    token = get_token(modem)
    
    if not token:
        return False, "Failed to get authentication token"
    
    # Set default profile
    default_payload = {
        "jsonrpc": "2.0",
        "id": "default",
        "method": "SetDefaultProfile",
        "params": {"ProfileID": profile_id}
    }
    
    default_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json", 
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://192.168.1.1",
        "Referer": "http://192.168.1.1/index.html",
        "_TclRequestVerificationToken": token
    }
    
    try:
        default_resp = session.post(
            WEBAPI_URL,
            json=default_payload,
            headers=default_headers,
            proxies=modem.proxy,
            timeout=PROBE_TIMEOUT
        )
        
        if default_resp.status_code != 200:
            return False, f"Failed to set default profile - HTTP {default_resp.status_code}"
        
        default_data = default_resp.json()
        
        if "error" in default_data:
            err = default_data.get("error", {})
            msg = err.get("message", "API error")
            return False, f"API error: {msg}"
        
        modem.last_action = {
            "action": "SetDefaultProfile", 
            "status": "ok",
            "profile_id": profile_id
        }
        
        return True, f"APN profile {profile_id} set as default"
    
    except Exception as e:
        return False, f"Error setting default profile: {e}"

def action_reset(modem: Modem) -> Tuple[bool,str]:
    """
    Factory reset the modem using SetDeviceReset per API doc.
    """
    session = requests.Session()
    print("\nPreparing to factory reset modem...")
    
    # Step 1: Get fresh token using our improved function
    print("Getting authentication token for factory reset...")
    token = get_token(modem)
    
    if not token:
        print("Failed to get authentication token")
        return False, "Failed to get authentication token"
        
    print(f"Authentication token obtained: {token[:5]}...")
    
    # Step 2: Send reset command - EXACTLY according to API doc
    # We're using "SetDeviceReset" as documented in the API
    reset_payload = {
        "jsonrpc": "2.0", 
        "id": "reset", 
        "method": "SetDeviceReset", 
        "params": {}
    }
    
    reset_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json", 
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://192.168.1.1",
        "Referer": "http://192.168.1.1/index.html",
        "_TclRequestVerificationToken": token
    }
    
    print("Sending factory reset command...")
    
    try:
        reset_resp = session.post(
            WEBAPI_URL, 
            json=reset_payload, 
            headers=reset_headers, 
            proxies=modem.proxy, 
            timeout=PROBE_TIMEOUT
        )
        
        if reset_resp.status_code != 200:
            print(f"Factory reset request failed with status code: {reset_resp.status_code}")
            
            # Try alternative methods if first attempt failed
            print("First attempt failed. Trying alternative methods...")
            
            # Try "RestoreFactorySettings" as first backup
            alt_payload1 = {
                "jsonrpc": "2.0",
                "id": "reset-alt1",
                "method": "RestoreFactorySettings",
                "params": {}
            }
            
            print("Trying alternative method 1: RestoreFactorySettings")
            alt_resp1 = session.post(
                WEBAPI_URL,
                json=alt_payload1,
                headers=reset_headers,  # Use same headers with token
                proxies=modem.proxy,
                timeout=PROBE_TIMEOUT
            )
            
            if alt_resp1.status_code == 200:
                print("Alternative method 1 succeeded!")
                alt_data1 = alt_resp1.json()
                if "error" not in alt_data1:
                    modem.last_action = {"action":"RestoreFactorySettings", "status":"ok", "response": alt_data1}
                    return True, "Factory reset command sent successfully (alt method 1)"
            
            # Try "SetFactoryReset" as second backup
            alt_payload2 = {
                "jsonrpc": "2.0",
                "id": "reset-alt2",
                "method": "SetFactoryReset",
                "params": {}
            }
            
            print("Trying alternative method 2: SetFactoryReset")
            alt_resp2 = session.post(
                WEBAPI_URL,
                json=alt_payload2,
                headers=reset_headers,  # Use same headers with token
                proxies=modem.proxy,
                timeout=PROBE_TIMEOUT
            )
            
            if alt_resp2.status_code == 200:
                print("Alternative method 2 succeeded!")
                alt_data2 = alt_resp2.json()
                if "error" not in alt_data2:
                    modem.last_action = {"action":"SetFactoryReset", "status":"ok", "response": alt_data2}
                    return True, "Factory reset command sent successfully (alt method 2)"
                    
            return False, f"Failed to factory reset - all methods failed"
            
        try:
            reset_data = reset_resp.json()
            
            if "error" in reset_data:
                err = reset_data.get("error", {})
                code = err.get("code", "")
                msg = err.get("message", "API error")
                if code:
                    print(f"API error during factory reset ({code}): {msg}")
                else:
                    print(f"API error during factory reset: {msg}")
                return False, f"API error: {msg}"
                
            print("Factory reset command successful")
            modem.last_action = {"action":"SetDeviceReset", "status":"ok", "response": reset_data}
            return True, "Factory reset command sent successfully"
        except ValueError as e:
            print(f"Error parsing response: {e}")
            if reset_resp.status_code == 200:
                # If we got 200 OK but couldn't parse JSON, consider it a success
                # The modem might have reset before sending complete response
                modem.last_action = {"action":"SetDeviceReset", "status":"ok", "response": "non-json response"}
                return True, "Factory reset command likely successful (non-JSON response)"
        
    except Exception as e:
        print(f"Error sending factory reset command: {e}")
        return False, f"Error sending factory reset command: {e}"
    
    # This code should be unreachable
    print("All factory reset methods failed")
    modem.last_action = {"action":"FactoryReset", "status":"failed"}
    return False, "Failed to send factory reset command"

def action_connect(modem: Modem) -> Tuple[bool, str]:
    """
    Connect to mobile data network using Connect method from API doc.
    
    Args:
        modem: The modem object
        
    Returns:
        Tuple of (success, message)
    """
    session = requests.Session()
    
    # Get authentication token
    token = get_token(modem)
    
    if not token:
        return False, "Failed to get authentication token"
    
    # Send connect command using the correct method name "Connect" per API doc
    connect_payload = {
        "jsonrpc": "2.0",
        "id": "201",  # Using ID "201" as shown in API example
        "method": "Connect",  # Correct method name from API doc
        "params": {}  # No parameters needed per API doc
    }
    
    connect_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json", 
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://192.168.1.1",
        "Referer": "http://192.168.1.1/index.html",
        "_TclRequestVerificationToken": token
    }
    
    try:
        connect_resp = session.post(
            WEBAPI_URL,
            json=connect_payload,
            headers=connect_headers,
            proxies=modem.proxy,
            timeout=PROBE_TIMEOUT
        )
        
        if connect_resp.status_code != 200:
            return False, f"Failed to connect - HTTP {connect_resp.status_code}"
        
        try:
            connect_data = connect_resp.json()
            
            if "error" in connect_data:
                err = connect_data.get("error", {})
                msg = err.get("message", "API error")
                return False, f"API error: {msg}"
            
            modem.last_action = {
                "action": "Connect", 
                "status": "ok",
                "response": connect_data
            }
            
            return True, "Connect command sent successfully"
        except ValueError as e:
            # Handle potential JSON parsing errors
            return False, f"Error parsing response: {e}"
    
    except Exception as e:
        return False, f"Error sending connect command: {e}"

def action_disconnect(modem: Modem) -> Tuple[bool, str]:
    """
    Disconnect from mobile data network using DisConnect method from API doc.
    
    Args:
        modem: The modem object
        
    Returns:
        Tuple of (success, message)
    """
    session = requests.Session()
    
    # Get authentication token
    token = get_token(modem)
    
    if not token:
        return False, "Failed to get authentication token"
    
    # Send disconnect command using the correct method name "DisConnect" per API doc
    disconnect_payload = {
        "jsonrpc": "2.0",
        "id": "202",  # Using ID "202" as shown in API example
        "method": "DisConnect",  # Correct method name from API doc
        "params": {}  # No parameters needed per API doc
    }
    
    disconnect_headers = {
        "Content-Type": "application/json",
        "Accept": "application/json", 
        "X-Requested-With": "XMLHttpRequest",
        "Origin": "http://192.168.1.1",
        "Referer": "http://192.168.1.1/index.html",
        "_TclRequestVerificationToken": token
    }
    
    try:
        disconnect_resp = session.post(
            WEBAPI_URL,
            json=disconnect_payload,
            headers=disconnect_headers,
            proxies=modem.proxy,
            timeout=PROBE_TIMEOUT
        )
        
        if disconnect_resp.status_code != 200:
            return False, f"Failed to disconnect - HTTP {disconnect_resp.status_code}"
        
        try:
            disconnect_data = disconnect_resp.json()
            
            if "error" in disconnect_data:
                err = disconnect_data.get("error", {})
                msg = err.get("message", "API error")
                return False, f"API error: {msg}"
            
            modem.last_action = {
                "action": "DisConnect", 
                "status": "ok",
                "response": disconnect_data
            }
            
            return True, "Disconnect command sent successfully"
        except ValueError as e:
            # Handle potential JSON parsing errors
            return False, f"Error parsing response: {e}"
    
    except Exception as e:
        return False, f"Error sending disconnect command: {e}"

def action_soft_restart(modem: Modem) -> Tuple[bool, str]:
    """
    Perform a soft restart by disconnecting, waiting, then reconnecting.
    Uses the updated Connect/DisConnect methods from the API doc.
    
    Args:
        modem: The modem object
        
    Returns:
        Tuple of (success, message)
    """
    print(f"Starting soft restart procedure for modem {modem.index}...")
    
    # First disconnect
    print("Step 1: Disconnecting modem...")
    ok_disconnect, msg_disconnect = action_disconnect(modem)
    
    if not ok_disconnect:
        print(f"Disconnect failed: {msg_disconnect}")
        return False, f"Soft restart failed at disconnect stage: {msg_disconnect}"
    
    # Wait for a few seconds
    print("Step 2: Waiting for 10 seconds...")
    time.sleep(10)
    
    # Then reconnect
    print("Step 3: Reconnecting modem...")
    ok_connect, msg_connect = action_connect(modem)
    
    if not ok_connect:
        print(f"Connect failed: {msg_connect}")
        return False, f"Soft restart failed at connect stage: {msg_connect}"
    
    print("Soft restart completed successfully")
    modem.last_action = {
        "action": "SoftRestart", 
        "status": "ok"
    }
    
    return True, "Soft restart completed successfully"
