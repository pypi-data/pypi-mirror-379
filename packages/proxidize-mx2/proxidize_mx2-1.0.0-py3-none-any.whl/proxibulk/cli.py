"""CLI and user interaction."""
from typing import List, Optional, Dict, Any, Callable, Tuple
import json
import sys
import os
import time
import requests
import argparse
import csv
from .modem import Modem
from .probe import probe_modem
from .actions import (
    action_set_apn, action_set_network_mode, action_restart, action_reset,
    get_apn_profiles, set_default_apn_profile, action_connect, action_disconnect,
    action_soft_restart
)
from .utils import parse_proxy_line, jsonrpc_post
from .utils import WEBAPI_URL, ADMIN_PASSWORD
from .connection_handlers_bulk import bulk_connect_modems, bulk_disconnect_modems, bulk_soft_restart_modems
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime
from pyfiglet import Figlet

# Version information
__version__ = "1.0.0"

# Configuration
MAX_WORKERS = 120  # Maximum number of concurrent threads

# Brand colors for professional identity
COLOR_YELLOW = "\033[93m"    # Brand primary (Proxidize yellow)
COLOR_PURPLE = "\033[95m"    # Brand secondary (Proxidize purple)
COLOR_GREEN = "\033[92m"     # Success/safe operations
COLOR_RED = "\033[91m"       # Errors/dangerous operations  
COLOR_ORANGE = "\033[38;5;208m"  # Warnings
COLOR_BLUE = "\033[94m"      # General information
COLOR_RESET = "\033[0m"
COLOR_BOLD = "\033[1m"

# Cross-platform Unicode symbols with ASCII fallbacks
def get_safe_unicode(symbol_type: str) -> str:
    """Get Unicode symbols with ASCII fallbacks for Windows compatibility."""
    symbols = {
        'success': ('✓', 'OK'),
        'error': ('✗', 'X'),
        'filled_block': ('█', '#'),
        'empty_block': ('░', '-'),
    }
    
    unicode_char, ascii_fallback = symbols.get(symbol_type, ('?', '?'))
    
    # Check if we can safely use Unicode
    try:
        # Test if the symbol can be encoded with the current encoding
        unicode_char.encode(sys.stdout.encoding or 'ascii')
        return unicode_char
    except (UnicodeEncodeError, AttributeError):
        return ascii_fallback

# Global settings - Removed verbose mode for cleaner UI/UX

def parse_command_line_args():
    """
    Parse command line arguments and set global configuration.
    Returns the parsed arguments object.
    """
    parser = argparse.ArgumentParser(
        description="Proxidize: MX2 Manager - A multi-threaded MX2 family modem manager"
    )
    
    # Parse args (no verbose flag anymore)
    args = parser.parse_args()
    
    return args

def print_banner():
    """
    Print the initial branded banner - used only at startup.
    """
    try:
        figlet = Figlet(font='doom')
        title = figlet.renderText('Proxidize ')
        
        print_colored(title, COLOR_YELLOW)
        print_colored("----------------------------------------------------------", COLOR_YELLOW)
        print_colored("MX2 Manager " + "A multi-threaded MX2 manager tool  " + f"v{__version__}", COLOR_RESET)
        print_colored("----------------------------------------------------------", COLOR_YELLOW)
    except Exception as e:
        # Fallback if figlet fails
        print_colored("\n" + "="*70, COLOR_YELLOW, bold=True)
        print_colored(" PROXIDIZE: MX2 MANAGER ", COLOR_YELLOW, bold=True)
        print_colored("="*70, COLOR_YELLOW, bold=True)
        print_colored(f"A multi-threaded MX2 manager tool v{__version__}", COLOR_RESET)

def print_header(subtitle=""):
    """
    Print consistent branded header across all screens.
    """
    # Clear screen for Windows/Unix compatibility
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Main branded header - always visible
    try:
        figlet = Figlet(font='doom')
        title = figlet.renderText('Proxidize ')
        
        print_colored(title, COLOR_YELLOW)
        print_colored("----------------------------------------------------------", COLOR_YELLOW)
        print_colored("MX2 Manager " + "A multi-threaded MX2 manager tool  " + f"v{__version__}", COLOR_RESET)
        print_colored("----------------------------------------------------------", COLOR_YELLOW)
        
        if subtitle:
            print_colored(f"Current Section: {subtitle}", COLOR_PURPLE, bold=True)
            print_colored("="*70, COLOR_PURPLE)
    except Exception as e:
        # Fallback if figlet fails
        print_colored("\n" + "="*70, COLOR_YELLOW, bold=True)
        print_colored(" PROXIDIZE: MX2 MANAGER ", COLOR_YELLOW, bold=True)
        print_colored("="*70, COLOR_YELLOW, bold=True)
        print_colored(f"A multi-threaded MX2 manager tool v{__version__}", COLOR_RESET)
        
        if subtitle:
            print_colored(f"Current Section: {subtitle}", COLOR_PURPLE, bold=True)
            print_colored("="*70, COLOR_PURPLE)


def print_colored(text: str, color: str = "", bold: bool = False) -> None:
    """
    Print text with brand-appropriate colors.
    
    Args:
        text: The text to print
        color: ANSI color code to use
        bold: Whether to make text bold
    """
    if os.name == 'nt':  # Windows may need special handling
        try:
            import colorama
            colorama.init()
        except ImportError:
            # If colorama not available, just print without colors
            print(text)
            return
    
    format_text = ""
    if bold:
        format_text += COLOR_BOLD
    if color:
        format_text += color
    
    if format_text:
        print(f"{format_text}{text}{COLOR_RESET}")
    else:
        print(text)

def prompt_multiline_input(prompt_text="Paste proxies (one per line) and finish with an empty line:"):
    """
    Prompt for multiline input with clear instructions and validation feedback.
    Returns a list of non-empty lines entered by the user.
    """
    print_header("PROXY INPUT")
    print(prompt_text)
    print("Format required: host:port:username:password")
    print("Press Enter twice (empty line) when done.")
    print("-"*70)
    
    lines = []
    try:
        while True:
            line = input().strip()
            if not line:
                break
            lines.append(line)
    except EOFError:
        # Handle EOF (Ctrl+D on Unix, Ctrl+Z on Windows)
        print("\nInput complete.")
    
    valid_count = 0
    for line in lines:
        if parse_proxy_line(line) is not None:
            valid_count += 1
    
    if lines:
        print(f"\nReceived {len(lines)} lines, {valid_count} valid proxies.")
    else:
        print("No input received.")
    
    return lines

def probe_all(modems: List[Modem], get_carrier_info: bool = True) -> List[Modem]:
    """
    Probe all modems in parallel while providing visual feedback.
    Preserves input order in results regardless of completion order.
    
    Args:
        modems: List of modems to probe
        get_carrier_info: Whether to collect carrier info after initial fast probe
    """
    n = len(modems)
    if n == 0:
        return []
        
    workers = min(n, MAX_WORKERS)
    
    print_header("MODEM PROBING")
    print_colored(f"Scanning {n} modems for connectivity...", COLOR_BLUE, bold=True)
    if workers > 1:
        print_colored(f"Using {workers} concurrent connections for optimal speed", COLOR_BLUE)
    print()
    
    # Progress tracking
    total_done = 0
    success_count = 0
    start_time = time.time()
    
    # Keep results ordered by input index
    results = [None] * n
    
    # Step 1: Ultra-fast initial probe to quickly determine which modems are reachable
    with ThreadPoolExecutor(max_workers=workers) as ex:
        futures = {ex.submit(probe_modem, m, fast_probe=True, get_full_info=False, ultra_fast=True): m.index-1 for m in modems}
        
        completed = 0
        for fut in as_completed(futures):
            idx = futures[fut]
            completed += 1
            
            try:
                modem = fut.result()
                if modem.reachable:
                    success_count += 1
                    status = get_safe_unicode('success')
                    status_color = COLOR_GREEN
                else:
                    modems[idx].reachable = False
                    modems[idx].error = "Failed ultra-fast probe"
                    status = get_safe_unicode('error')
                    status_color = COLOR_RED
            except Exception as e:
                modems[idx].reachable = False
                modems[idx].error = f"probe exception: {e}"
                status = get_safe_unicode('error')
                status_color = COLOR_RED
            
            # Update progress bar
            progress_percent = (completed * 100) // n
            filled_blocks = min(25, progress_percent // 4)
            progress_bar = get_safe_unicode('filled_block') * filled_blocks + get_safe_unicode('empty_block') * (25 - filled_blocks)
            print(f"\r[{progress_bar}] {progress_percent:3d}% | {completed:3d}/{n:3d} | {success_count:3d} reachable", end="", flush=True)
        
        # Final newline after progress bar
        print()
    
    # Step 2: Now do a more thorough probe on only the reachable modems to get carrier info
    # Only if get_carrier_info is True (we may defer this to when needed for multi-group)
    reachable_modems = [m for m in modems if m.reachable]
    
    if reachable_modems and get_carrier_info:
        print(f"Gathering carrier info for {len(reachable_modems)} reachable modems...")
        
        with ThreadPoolExecutor(max_workers=workers) as ex:
            detailed_futures = {ex.submit(probe_modem, m, fast_probe=False, get_full_info=True): m.index-1 for m in reachable_modems}
            
            detailed_completed = 0
            for fut in as_completed(detailed_futures):
                idx = detailed_futures[fut]
                detailed_completed += 1
                
                try:
                    modem = fut.result()
                    # Update the original modem in the results list
                    for i, m in enumerate(modems):
                        if m.index == modem.index:
                            modems[i] = modem
                            break
                    
                except Exception as e:
                    # If detailed probe fails, keep the modem marked as reachable
                    # but note the error in gathering detailed info
                    for i, m in enumerate(modems):
                        if m.index == reachable_modems[idx].index:
                            m.error = f"Detailed probe error: {e}"
                            break
                
                # Update progress bar for carrier info gathering
                progress_percent = (detailed_completed * 100) // len(reachable_modems)
                filled_blocks = min(25, progress_percent // 4)
                progress_bar = get_safe_unicode('filled_block') * filled_blocks + get_safe_unicode('empty_block') * (25 - filled_blocks)
                print(f"\r[{progress_bar}] {progress_percent:3d}% | {detailed_completed:3d}/{len(reachable_modems):3d} | Gathering carrier info...", end="", flush=True)
        
        # Final newline after progress bar
        print()
    
    # Final stats
    elapsed = time.time() - start_time
    failed_count = n - success_count
    
    print_colored(f"\n{get_safe_unicode('success')} Scan complete in {elapsed:.1f}s", COLOR_GREEN, bold=True)
    print_colored(f"  • {success_count} reachable modems", COLOR_GREEN if success_count > 0 else COLOR_YELLOW)
    if failed_count > 0:
        print_colored(f"  • {failed_count} unreachable modems", COLOR_YELLOW)
    
    # Return the original modems list with updated info
    return modems

def group_by_carrier(modems: List[Modem]) -> Dict[str, List[Modem]]:
    """
    Group modems by carrier name, preserving order within groups.
    """
    groups = {}
    for m in modems:
        key = m.carrier if m.carrier else "Unknown"
        groups.setdefault(key, []).append(m)
    return groups

def print_basic_summary(modems: List[Modem]):
    """
    Print a basic summary of modem probing results without carrier information.
    Just shows reachable vs unreachable counts.
    """
    total = len(modems)
    reachable = sum(1 for m in modems if m.reachable)
    unreachable = total - reachable
    
    print_header("CONNECTION SUMMARY")
    
    print(f"Total modems: {total}")
    print(f"  - Reachable: {reachable}")
    print(f"  - Unreachable: {unreachable}")
    
    print("\nCarrier information will be gathered when selecting 'Bulk Management'.")
    print("For faster initial probing, only basic connectivity was checked.")

def print_summary(modems: List[Modem]):
    """
    Print a summary of modem probing results, including carrier groups.
    """
    total = len(modems)
    reachable = sum(1 for m in modems if m.reachable)
    unreachable = total - reachable
    
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(" SUMMARY RESULTS ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    print_colored(f"Total modems: {total}", COLOR_BOLD)
    print_colored(f"  - Reachable: {reachable}", COLOR_GREEN if reachable > 0 else "")
    print_colored(f"  - Unreachable: {unreachable}", COLOR_RED if unreachable > 0 else COLOR_GREEN)
    
    # Check if carrier information is available
    have_carrier_info = any(m.carrier for m in modems if m.reachable)
    
    if not have_carrier_info:
        print_colored("\nCarrier information will be gathered when selecting groups.", COLOR_YELLOW)
        print_colored("For faster initial probing, only basic connectivity was checked.", COLOR_YELLOW)
    else:
        # Group by carrier
        groups = group_by_carrier(modems)
        
        print_colored("\nCarrier Groups:", COLOR_BOLD)
        for carrier, lst in groups.items():
            reachable_count = sum(1 for m in lst if m.reachable)
            
            # Color based on success rate
            if reachable_count == len(lst):
                color = COLOR_GREEN
            elif reachable_count > 0:
                color = COLOR_YELLOW
            else:
                color = COLOR_RED
                
            print_colored(f"  - {carrier}: {len(lst)} modems ({reachable_count} reachable)", color)
    
    print_colored("-"*70, COLOR_BLUE)

def save_results_csv(modems: List[Modem]):
    """
    Dummy function that does nothing - CSV generation disabled.
    Kept for API compatibility.
    """
    return None

def refresh_connections(modems: List[Modem]) -> List[Modem]:
    """
    Re-probe all modems to refresh their reachable status.
    Only checks connectivity, does not gather carrier information.
    
    Args:
        modems: List of modems to re-probe
        
    Returns:
        Updated list of modems
    """
    print_colored("\nRefreshing modem connections...", COLOR_YELLOW)
    return probe_all(modems, get_carrier_info=False)

def handle_bulk_all_modems(modems: List[Modem]):
    """
    Handle bulk operations for all modems, regardless of carrier.
    """
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print_colored("No reachable modems to operate on.", COLOR_RED)
        return
    
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(" BULK OPERATIONS - ALL MODEMS ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    print_colored(f"Target: {len(reachable_modems)} reachable modems", COLOR_BOLD)
    print_colored(f"Total modems: {len(modems)}", COLOR_BLUE)
    
    # Handle operations on all modems as a single group
    handle_bulk_menu_for_group(reachable_modems)

def handle_bulk_by_carrier(modems: List[Modem]):
    """
    Handle bulk operations for modems grouped by carrier.
    First gathers carrier information if not already available.
    """
    print_header("BULK OPERATIONS - BY CARRIER")
    
    # Check if we need to collect carrier info
    need_carrier_info = False
    for m in modems:
        if m.reachable and not m.carrier:
            need_carrier_info = True
            break
    
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print("No reachable modems to operate on.")
        return
    
    # If carrier info is needed, collect it now
    if need_carrier_info:
        print("\nGathering carrier information for all modems...")
        print("This process may take a moment to complete.")
        
        workers = min(len(reachable_modems), MAX_WORKERS)
        
        with ThreadPoolExecutor(max_workers=workers) as ex:
            detailed_futures = {ex.submit(probe_modem, m, fast_probe=False, get_full_info=True): i 
                                for i, m in enumerate(reachable_modems)}
            
            for fut in as_completed(detailed_futures):
                try:
                    idx = detailed_futures[fut]
                    modem = fut.result()
                    
                    # Update the original modem
                    original_idx = next(i for i, m in enumerate(modems) if m.index == modem.index)
                    modems[original_idx] = modem
                    
                except Exception as e:
                    print_colored(f"Error getting carrier info for modem {idx+1}: {e}", COLOR_RED)
    
    # Group modems by carrier
    groups = group_by_carrier(modems)
    carrier_keys = list(groups.keys())
    
    print_colored("\nAvailable carrier groups:", COLOR_BOLD)
    for i, carrier in enumerate(carrier_keys, start=1):
        group_modems = groups[carrier]
        reachable = sum(1 for m in group_modems if m.reachable)
        
        # Select color based on reachability
        if reachable == len(group_modems):
            color = COLOR_GREEN
        elif reachable > 0:
            color = COLOR_YELLOW
        else:
            color = COLOR_RED
            
        print_colored(f"  {i}. Group: {carrier} ({len(group_modems)} modems, {reachable} reachable)", color)
    
    # Add "All Groups" and "Back" options
    all_opt = len(carrier_keys) + 1
    back_opt = all_opt + 1
    
    print_colored(f"  {all_opt}. Multiple groups", COLOR_GREEN)
    print_colored(f"  {back_opt}. Back to main menu", COLOR_YELLOW)
    
    # Get user choice
    try:
        choice = input("\nEnter group number: ").strip()
        if not choice.isdigit():
            print_colored("Invalid choice. Please enter a number.", COLOR_RED)
            return
            
        choice_num = int(choice)
        
        if choice_num == back_opt:
            return
        elif choice_num == all_opt:
            handle_multi_group_selection(modems, groups, carrier_keys)
        elif 1 <= choice_num <= len(carrier_keys):
            carrier = carrier_keys[choice_num - 1]
            group_modems = groups[carrier]
            handle_bulk_menu_for_group(group_modems)
        else:
            print_colored("Invalid option. Please try again.", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

def export_modems_to_csv(modems: List[Modem]):
    """
    Export comprehensive modem information to a CSV file.
    Includes connection status, network mode, carrier, APN profiles, and public IP addresses.
    """
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print_colored("No reachable modems to export.", COLOR_RED)
        return
    
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(" EXPORT MODEM INFORMATION TO CSV ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    print_colored(f"Gathering detailed information from {len(reachable_modems)} modems...", COLOR_YELLOW)
    print_colored("This will collect connection status, network settings, APN profiles, and public IPs.", COLOR_YELLOW)
    
    # CSV headers - Enhanced for diagnosis with public IP
    headers = [
        'Index', 'Proxy', 'Status', 'Connection_Status', 'Network_Mode', 
        'Signal_Strength', 'RSRP_dBm', 'RSRQ_dB', 'SINR_dB', 'Signal_Quality',
        'Carrier', 'PLMN', 'IPv4_Address', 'IPv6_Address', 'Public_IP', 'IMEI',
        'Default_APN_Profile', 'APN_Name', 'APN_Username', 'APN_Auth_Type',
        'PDP_Type', 'Dial_Number', 'Export_Timestamp'
    ]
    
    modem_data = []
    workers = min(len(reachable_modems), MAX_WORKERS)
    
    def gather_modem_info(modem):
        """Gather comprehensive information from a single modem"""
        try:
            # Basic info
            info = {
                'Index': modem.index,
                'Proxy': modem.raw,
                'Status': 'Reachable' if modem.reachable else 'Unreachable',
                'Carrier': modem.carrier or 'Unknown',
                'PLMN': modem.plmn or 'Unknown',
                'Export_Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            
            # Get connection state
            try:
                session = requests.Session()
                ok, j = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetConnectionState", params={})
                if ok and j and 'result' in j:
                    result = j['result']
                    connection_status = result.get("ConnectionStatus", -1)
                    status_map = {0: "Disconnected", 1: "Connecting", 2: "Connected", 3: "Disconnecting"}
                    info['Connection_Status'] = status_map.get(connection_status, f"Unknown({connection_status})")
                    info['IPv4_Address'] = result.get('IPv4Address', 'N/A')
                    info['IPv6_Address'] = result.get('IPv6Address', 'N/A')
                else:
                    info['Connection_Status'] = 'Unknown'
                    info['IPv4_Address'] = 'N/A'
                    info['IPv6_Address'] = 'N/A'
            except Exception as e:
                info['Connection_Status'] = 'Error'
                info['IPv4_Address'] = 'Error'
                info['IPv6_Address'] = 'Error'
            
            # Get public IP address from eth0.me
            try:
                if info['Connection_Status'] == 'Connected':
                    # Configure the proxy with the modem's credentials
                    proxy_url = f"http://{modem.user}:{modem.pwd}@{modem.host}:{modem.port}"
                    proxies = {
                        'http': proxy_url,
                        'https': proxy_url
                    }
                    
                    # Try to get public IP from eth0.me
                    response = requests.get("http://eth0.me", proxies=proxies, timeout=10)
                    if response.status_code == 200:
                        info['Public_IP'] = response.text.strip()
                    else:
                        info['Public_IP'] = 'N/A'
                else:
                    info['Public_IP'] = 'Not Connected'
            except Exception as e:
                info['Public_IP'] = 'Error'
            
            # Get enhanced signal and network information using same functions as single modem menu
            try:
                # Network mode using our enhanced function
                network_mode_str, _ = get_network_mode(modem)
                info['Network_Mode'] = network_mode_str
                
                # Enhanced signal information using our function
                signal_str, _ = get_signal_strength(modem)
                info['Signal_Strength'] = signal_str
                
                # Extract detailed signal values
                rsrp = rsrq = sinr = "N/A"
                signal_quality = "Unknown"
                
                if signal_str and isinstance(signal_str, str):
                    if "RSRP:" in signal_str:
                        try:
                            rsrp = signal_str.split("RSRP:")[1].split()[0].replace("dBm", "").strip()
                            rsrp_val = float(rsrp)
                            if rsrp_val >= -70:
                                signal_quality = "Excellent"
                            elif rsrp_val >= -85:
                                signal_quality = "Good"
                            elif rsrp_val >= -100:
                                signal_quality = "Fair"
                            else:
                                signal_quality = "Poor"
                        except:
                            pass
                    
                    if "RSRQ:" in signal_str:
                        try:
                            rsrq = signal_str.split("RSRQ:")[1].split()[0].replace("dB", "").strip()
                        except:
                            pass
                    
                    if "SINR:" in signal_str:
                        try:
                            sinr = signal_str.split("SINR:")[1].split()[0].replace("dB", "").strip()
                        except:
                            pass
                
                info['RSRP_dBm'] = rsrp
                info['RSRQ_dB'] = rsrq
                info['SINR_dB'] = sinr
                info['Signal_Quality'] = signal_quality
                
                # Get IMEI using same function as single modem menu
                imei_result = get_modem_imei(modem)
                if isinstance(imei_result, tuple):
                    info['IMEI'] = imei_result[0]
                else:
                    info['IMEI'] = imei_result
                
            except Exception as e:
                info['Network_Mode'] = 'Error'
                info['Signal_Strength'] = 'Error'
                info['RSRP_dBm'] = 'Error'
                info['RSRQ_dB'] = 'Error'
                info['SINR_dB'] = 'Error'
                info['Signal_Quality'] = 'Error'
                info['IMEI'] = 'Error'
            
            # Get APN information using same function as single modem menu
            try:
                # Use the exact same function that works in single modem operations
                default_apn_result = get_default_apn_profile(modem)
                
                # Extract the APN name from the tuple result
                if isinstance(default_apn_result, tuple):
                    apn_display = str(default_apn_result[0])
                else:
                    apn_display = str(default_apn_result)
                
                # Try to get detailed profile information using the same API call structure as the working function
                session = requests.Session()
                ok, j = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetProfileList", params={})
                
                if ok and isinstance(j, dict) and "result" in j:
                    # Use the same structure as the working get_default_apn_profile function
                    profiles = j.get("result", {}).get("ProfileList", [])
                    
                    # Find default profile using the same logic (Default = 1, not Flag = 1)
                    default_profile = None
                    for profile in profiles:
                        if profile.get("Default", 0) == 1:
                            default_profile = profile
                            break
                    
                    if default_profile:
                        # Use the same field names as in the API documentation
                        info['Default_APN_Profile'] = default_profile.get('ProfileName', 'Profile 1')
                        info['APN_Name'] = default_profile.get('APN', 'N/A')  # Use 'APN' not 'ApnName'
                        info['APN_Username'] = default_profile.get('UserName', 'N/A')  # Use 'UserName' not 'Username'
                        
                        # Convert auth type number to readable format using correct field name
                        auth_type = default_profile.get('AuthType', 0)  # Use 'AuthType' not 'AuthMode'
                        auth_types = {0: "None", 1: "PAP", 2: "CHAP", -1: "PAP & CHAP"}
                        info['APN_Auth_Type'] = auth_types.get(auth_type, f"Type {auth_type}")
                        
                        # Convert PDP type number to readable format using correct field name
                        pdp_type = default_profile.get('PdpType', 0)  # Use 'PdpType' not 'PDPType'
                        pdp_types = {1: "IPv4", 2: "IPv6", 3: "IPv4v6", -1: "Auto"}
                        info['PDP_Type'] = pdp_types.get(pdp_type, f"Type {pdp_type}")
                        
                        info['Dial_Number'] = default_profile.get('DailNumber', '*99#')  # Use 'DailNumber' as per API doc
                    else:
                        # No default profile found, use basic info from the working function
                        info['Default_APN_Profile'] = apn_display if apn_display not in ["Unknown", "N/A", "No Default"] else "N/A"
                        info['APN_Name'] = apn_display if apn_display not in ["Unknown", "N/A", "No Default"] else "N/A"
                        info['APN_Username'] = 'N/A'
                        info['APN_Auth_Type'] = 'N/A'
                        info['PDP_Type'] = 'N/A'
                        info['Dial_Number'] = 'N/A'
                else:
                    # Fallback to basic info from the working function
                    info['Default_APN_Profile'] = apn_display if apn_display not in ["Unknown", "N/A", "No Default"] else "N/A"
                    info['APN_Name'] = apn_display if apn_display not in ["Unknown", "N/A", "No Default"] else "N/A"
                    info['APN_Username'] = 'N/A'
                    info['APN_Auth_Type'] = 'N/A'
                    info['PDP_Type'] = 'N/A'
                    info['Dial_Number'] = 'N/A'
                    
            except Exception as e:
                info['Default_APN_Profile'] = 'Error'
                info['APN_Name'] = 'Error'
                info['APN_Username'] = 'Error'
                info['APN_Auth_Type'] = 'Error'
                info['PDP_Type'] = 'Error'
                info['Dial_Number'] = 'Error'
            
            return modem, info, True, "Success"
            
        except Exception as e:
            # Return basic info even if detailed gathering fails
            basic_info = {
                'Index': modem.index,
                'Proxy': modem.raw,
                'Status': 'Reachable' if modem.reachable else 'Unreachable',
                'Carrier': modem.carrier or 'Unknown',
                'PLMN': modem.plmn or 'Unknown',
                'Connection_Status': 'Error',
                'Network_Mode': 'Error',
                'Signal_Strength': 'Error',
                'RSRP_dBm': 'Error',
                'RSRQ_dB': 'Error',
                'SINR_dB': 'Error',
                'Signal_Quality': 'Error',
                'IPv4_Address': 'Error',
                'IPv6_Address': 'Error',
                'Public_IP': 'Error',
                'IMEI': 'Error',
                'Default_APN_Profile': 'Error',
                'APN_Name': 'Error',
                'APN_Username': 'Error',
                'APN_Auth_Type': 'Error',
                'PDP_Type': 'Error',
                'Dial_Number': 'Error',
                'Export_Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            }
            return modem, basic_info, False, f"Error: {str(e)}"
    
    # Gather information from all modems in parallel
    print_colored("\nGathering modem information:", COLOR_BOLD)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_modem = {executor.submit(gather_modem_info, modem): modem for modem in reachable_modems}
        
        for i, future in enumerate(as_completed(future_to_modem), 1):
            modem = future_to_modem[future]
            try:
                modem_obj, info, success, message = future.result()
                modem_data.append(info)
                
                # Simple progress indicator
                status_text = "SUCCESS" if success else "PARTIAL"
                print(f"[{i}/{len(reachable_modems)}] Modem [{modem.index}]: {status_text}")
                
            except Exception as e:
                # Add basic error entry
                error_info = {
                    'Index': modem.index,
                    'Proxy': modem.raw,
                    'Status': 'Error',
                    'Export_Timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                }
                # Fill remaining fields with 'Error'
                for header in headers:
                    if header not in error_info:
                        error_info[header] = 'Error'
                
                modem_data.append(error_info)
                print_colored(f"\n[{i}/{len(reachable_modems)}] Modem [{modem.index}]: ERROR - {str(e)}", COLOR_RED)
    
    # Show summary and ask for save location
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(" EXPORT SUMMARY ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    # Show summary statistics
    successful_exports = len([d for d in modem_data if d.get('Connection_Status') not in ['Error']])
    connected_count = len([d for d in modem_data if d.get('Connection_Status') == 'Connected'])
    unique_carriers = set([d.get('Carrier', 'Unknown') for d in modem_data if d.get('Carrier')])
    unique_apns = set([d.get('APN_Name', 'Unknown') for d in modem_data if d.get('APN_Name') not in ['N/A', 'Error', 'None']])
    
    print_colored(f"✓ Successfully gathered data from {successful_exports}/{len(reachable_modems)} modems", COLOR_GREEN)
    print_colored(f"✓ Connected modems: {connected_count}", COLOR_GREEN if connected_count > 0 else COLOR_YELLOW)
    print_colored(f"✓ Unique carriers: {len(unique_carriers)} ({', '.join(sorted(unique_carriers))})", COLOR_BLUE)
    print_colored(f"✓ Unique APNs: {len(unique_apns)}", COLOR_BLUE)
    
    # Ask for save location
    print_colored("\nSave Options:", COLOR_BOLD)
    print_colored("  Press Enter: Save to current directory with timestamp", COLOR_YELLOW)
    print_colored("  Type filename: Save with custom filename", COLOR_YELLOW)
    print_colored("  Type 'q': Cancel export", COLOR_RED)
    
    user_input = input("\nEnter filename (or press Enter for default): ").strip()
    
    if user_input.lower() == 'q':
        print_colored("Export cancelled.", COLOR_YELLOW)
        return
    
    if user_input:
        # Custom filename
        if not user_input.endswith('.csv'):
            user_input += '.csv'
        csv_filename = user_input
    else:
        # Default filename with timestamp
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        csv_filename = f"modem_export_{timestamp}.csv"
    
    # Write to CSV file
    try:
        with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            writer.writeheader()
            
            # Sort by modem index for consistent output
            modem_data.sort(key=lambda x: x['Index'])
            
            for data in modem_data:
                writer.writerow(data)
        
        print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
        print_colored(" CSV EXPORT COMPLETED ", COLOR_BLUE, bold=True)
        print_colored("="*70, COLOR_BLUE, bold=True)
        
        print_colored(f"✓ Successfully exported {len(modem_data)} modems to: {csv_filename}", COLOR_GREEN)
        print_colored(f"✓ File location: {os.path.abspath(csv_filename)}", COLOR_GREEN)
        print_colored(f"✓ Export timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}", COLOR_GREEN)
        
        # Show a preview of the data
        print_colored("\nCSV Preview (first 3 rows):", COLOR_BOLD)
        print_colored("-" * 70, COLOR_BLUE)
        
        for i, data in enumerate(modem_data[:3], 1):
            print_colored(f"Row {i}: Index={data['Index']}, Status={data['Connection_Status']}, "
                         f"Carrier={data['Carrier']}, APN={data['APN_Name']}", COLOR_YELLOW)
        
        if len(modem_data) > 3:
            print_colored(f"... and {len(modem_data) - 3} more rows", COLOR_YELLOW)
        
        print_colored("-" * 70, COLOR_BLUE)
        
    except Exception as e:
        print_colored(f"\n✗ Failed to write CSV file: {str(e)}", COLOR_RED)
        return
    
    input("\nPress Enter to continue...")

def test_internet_connectivity(modems: List[Modem]):
    """
    Test if modems can access the internet by making HTTP requests to external services.
    Displays the results in a table format.
    """
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print_colored("No reachable modems to test.", COLOR_RED)
        return
    
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(" INTERNET CONNECTIVITY TEST ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    print_colored(f"Testing {len(reachable_modems)} modems for internet connectivity...", COLOR_YELLOW)
    print_colored("This will check if the modems can access the internet via HTTP.", COLOR_YELLOW)
    print_colored("The test will try to fetch your public IP from external services.", COLOR_YELLOW)
    
    # External services to test connectivity (fallbacks if one fails)
    test_urls = [
        "http://eth0.me",
        "http://icanhazip.com",
        "http://ifconfig.me/ip",
        "http://api.ipify.org"
    ]
    
    results = []
    workers = min(len(reachable_modems), MAX_WORKERS)
    
    # Function to test a single modem
    def test_modem_connectivity(modem):
        if not modem.reachable:
            return modem, False, "Modem not reachable", None
        
        session = requests.Session()
        timeout = 15  # Seconds
        
        for url in test_urls:
            try:
                # Configure the proxy with the modem's credentials
                # Properly format the proxy URL with protocol, credentials, host and port
                proxy_url = f"http://{modem.user}:{modem.pwd}@{modem.host}:{modem.port}"
                proxies = {
                    'http': proxy_url,
                    'https': proxy_url
                }
                
                # Make request through the proxy
                response = session.get(url, proxies=proxies, timeout=timeout)
                
                if response.status_code == 200:
                    # Successfully connected, return the IP (trimmed of whitespace)
                    public_ip = response.text.strip()
                    return modem, True, f"Connected via {url}", public_ip
                
            except requests.RequestException:
                # Try next URL if this one fails
                continue
        
        # If we get here, all URLs failed
        return modem, False, "Failed to connect to any test service", None
    
    # Test all modems in parallel
    print_colored("\nTesting connectivity:", COLOR_BOLD)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        future_to_modem = {executor.submit(test_modem_connectivity, modem): modem for modem in reachable_modems}
        
        for i, future in enumerate(as_completed(future_to_modem), 1):
            modem = future_to_modem[future]
            try:
                modem, success, message, public_ip = future.result()
                results.append((modem, success, message, public_ip))
                
                # Print progress
                status_text = "SUCCESS" if success else "FAILED"
                print(f"[{i}/{len(reachable_modems)}] Modem [{modem.index}]: {status_text}")
                
            except Exception as e:
                results.append((modem, False, f"Error: {str(e)}", None))
                print_colored(f"[{i}/{len(reachable_modems)}] Modem [{modem.index}]: ERROR - {str(e)}", COLOR_RED)
    
    # Count successes and failures
    success_count = sum(1 for _, success, _, _ in results if success)
    fail_count = len(results) - success_count
    
    # Print results table
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(" CONNECTIVITY TEST RESULTS ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    print_colored(f"Summary: {success_count} connected, {fail_count} failed (out of {len(results)} tested)", 
                 COLOR_GREEN if fail_count == 0 else COLOR_YELLOW)
    
    # Print table header
    print_colored("\n{:<6} {:<30} {:<10} {:<20}".format("Index", "Proxy", "Status", "Public IP"), COLOR_BOLD)
    print_colored("-"*70, COLOR_BLUE)
    
    # Sort results by modem index for consistent display
    results.sort(key=lambda x: x[0].index)
    
    # Print table rows
    for modem, success, message, public_ip in results:
        status = "CONNECTED" if success else "FAILED"
        status_color = COLOR_GREEN if success else COLOR_RED
        ip_display = public_ip or "N/A"
        
        # Truncate proxy string if too long
        proxy_display = modem.raw
        if len(proxy_display) > 30:
            proxy_display = proxy_display[:27] + "..."
            
        print_colored(
            "{:<6} {:<30} {:<10} {:<20}".format(
                modem.index, proxy_display, status, ip_display
            ),
            status_color
        )
    
    print_colored("-"*70, COLOR_BLUE)
    input("\nPress Enter to continue...")
    return

def interactive_menu(modems: List[Modem]):
    """
    Main interactive menu for bulk and single modem operations.
    """
    while True:
        # Get modem stats for the header
        total = len(modems)
        reachable = sum(1 for m in modems if m.reachable)
        unreachable = total - reachable
        
        print_header("MAIN MENU")
        
        # Always show the reachable/unreachable counts with appropriate colors
        status_color = COLOR_GREEN if unreachable == 0 else COLOR_ORANGE if reachable > 0 else COLOR_RED
        print_colored(f"Modem Status: {reachable} reachable, {unreachable} unreachable (Total: {total})", status_color)
        
        print_colored("\nChoose an option:", COLOR_BLUE, bold=True)
        print_colored("  1. Bulk Management", COLOR_PURPLE)
        print_colored("  2. Single Modem", COLOR_BLUE)
        print_colored("  3. Refresh connections", COLOR_YELLOW)
        print_colored("  4. Exit", COLOR_YELLOW)
        
        # Get user choice
        try:
            choice = input("\nEnter choice number: ").strip()
            if not choice.isdigit():
                print_colored("Invalid choice. Please enter a number.", COLOR_RED)
                continue
                
            choice_num = int(choice)
            
            if choice_num == 1:  # Bulk Management
                handle_bulk_by_carrier(modems)
            elif choice_num == 2:  # Single Modem
                handle_single_modem_menu(modems)
            elif choice_num == 3:  # Refresh connections
                modems = refresh_connections(modems)
                print_basic_summary(modems)
            elif choice_num == 4:  # Exit
                print_colored("Exiting...", COLOR_YELLOW)
                break
            else:
                print_colored("Invalid option. Please try again.", COLOR_RED)
                
        except KeyboardInterrupt:
            print_colored("\nOperation cancelled. Returning to main menu...", COLOR_ORANGE)
        except Exception as e:
            print_colored(f"An error occurred: {e}", COLOR_RED)

def choose_modem_by_index(modems: List[Modem]) -> Optional[Modem]:
    """
    Prompt user to select a modem by its index.
    Returns the selected modem or None if invalid.
    """
    print_colored("\nAvailable modems:", COLOR_BOLD)
    
    # Display modem list with indices for reference
    for m in sorted(modems, key=lambda x: x.index):
        status = "OK" if m.reachable else "UNREACHABLE"
        color = COLOR_GREEN if m.reachable else COLOR_RED
        print_colored(f"  [{m.index}] {m.raw} - {status} - {m.carrier or 'Unknown'}", color)
    
    while True:
        try:
            idx_input = input("\nEnter modem index number (or 'q' to go back): ").strip()
            
            if idx_input.lower() == 'q':
                return None
                
            if not idx_input.isdigit():
                print_colored("Invalid input. Please enter a numeric index.", COLOR_RED)
                continue
                
            idx = int(idx_input)
            
            # Find modem with matching index
            modem = next((m for m in modems if m.index == idx), None)
            
            if modem is None:
                print_colored(f"No modem found with index {idx}. Please try again.", COLOR_RED)
                continue
                
            return modem
            
        except KeyboardInterrupt:
            print_colored("\nSelection cancelled.", COLOR_YELLOW)
            return None
            
        except Exception as e:
            print_colored(f"Error: {e}", COLOR_RED)

def attempt_reconnect_modem(modem: Modem) -> Modem:
    """
    Attempt to reconnect to an unreachable modem.
    This function tries various approaches to re-establish connection.
    
    Args:
        modem: The unreachable modem object
        
    Returns:
        The modem object (potentially updated if reconnection successful)
    """
    if modem.reachable:
        # If already reachable, no need to reconnect
        return modem
        
    print_colored("\nAttempting to reconnect to unreachable modem...", COLOR_YELLOW)
    
    # Store original values
    index = modem.index
    raw = modem.raw
    
    try:
        # Method 1: Simple reprobe (most basic attempt)
        print_colored("Attempt 1: Re-probing modem...", COLOR_YELLOW)
        updated_modem = probe_modem(modem)
        
        if updated_modem.reachable:
            print_colored("Reconnection successful! Modem is now reachable.", COLOR_GREEN)
            # Ensure original values are preserved
            updated_modem.index = index
            updated_modem.raw = raw
            return updated_modem
            
        # Method 2: Try with a longer timeout
        print_colored("Attempt 2: Re-probing with extended timeout...", COLOR_YELLOW)
        # Temporarily increase the global timeout
        import proxibulk.probe as probe_module
        original_timeout = probe_module.PROBE_TIMEOUT
        probe_module.PROBE_TIMEOUT = 20  # Double the timeout
        
        try:
            updated_modem = probe_modem(modem)
            if updated_modem.reachable:
                print_colored("Reconnection successful with extended timeout!", COLOR_GREEN)
                # Preserve original values
                updated_modem.index = index
                updated_modem.raw = raw
                return updated_modem
        finally:
            # Restore original timeout
            probe_module.PROBE_TIMEOUT = original_timeout
            
        # Method 3: Try different API endpoints if available
        print_colored("Attempt 3: Trying alternative endpoints...", COLOR_YELLOW)
        # Store original endpoint
        import proxibulk.utils as utils_module
        original_url = utils_module.WEBAPI_URL
        alternate_urls = [
            "http://192.168.1.1/jrd/webapi",  # Standard endpoint
            "http://192.168.1.1/api",         # Alternate endpoint used in some firmware
            "http://192.168.1.1/goform/webApi" # Another alternate endpoint
        ]
        
        for alt_url in alternate_urls:
            if alt_url == original_url:
                continue
                
            try:
                print_colored(f"Trying endpoint: {alt_url}", COLOR_YELLOW)
                utils_module.WEBAPI_URL = alt_url
                updated_modem = probe_modem(modem)
                if updated_modem.reachable:
                    print_colored(f"Reconnection successful using alternate endpoint: {alt_url}", COLOR_GREEN)
                    # Preserve original values
                    updated_modem.index = index
                    updated_modem.raw = raw
                    return updated_modem
            except Exception:
                pass
        
        # Restore original endpoint if none of the alternates worked
        utils_module.WEBAPI_URL = original_url
        
        print_colored("All reconnection attempts failed. Modem remains unreachable.", COLOR_RED)
        print_colored("Check your network connection to the proxy or try again later.", COLOR_YELLOW)
        
        return modem
        
    except Exception as e:
        print_colored(f"Error during reconnection attempts: {e}", COLOR_RED)
        return modem

def refresh_modem_status(modem: Modem) -> Modem:
    """
    Refresh a modem's status by re-probing it.
    Also attempts reconnection if the modem is unreachable.
    
    Args:
        modem: The modem object to refresh
        
    Returns:
        The updated modem object
    """
    print_colored("\nRefreshing modem status...", COLOR_YELLOW)
    try:
        # Store the original index and raw values
        index = modem.index
        raw = modem.raw
        
        # Use ultra-fast probe first for an extremely quick connectivity check
        print_colored("Using ultra-fast probing to check connectivity...", COLOR_YELLOW)
        updated_modem = probe_modem(modem, fast_probe=True, get_full_info=False, ultra_fast=True)
        
        # If ultra-fast probe is successful, do a full probe to get all information
        if updated_modem.reachable:
            print_colored("Ultra-fast probe successful, modem is reachable!", COLOR_GREEN)
            print_colored("Gathering detailed network information...", COLOR_YELLOW)
            # Now do a more thorough probe to get all the information
            updated_modem = probe_modem(modem, fast_probe=False, get_full_info=True)
        
        # Ensure index and raw values are preserved
        updated_modem.index = index
        updated_modem.raw = raw
        
        # If modem is unreachable after refresh, attempt reconnection
        if not updated_modem.reachable:
            print_colored("Modem is unreachable after refresh. Attempting reconnection...", COLOR_YELLOW)
            updated_modem = attempt_reconnect_modem(updated_modem)
        
        print_colored("Modem status refreshed successfully.", COLOR_GREEN)
        return updated_modem
    except Exception as e:
        print_colored(f"Error refreshing modem status: {e}", COLOR_RED)
        return modem

def get_connection_status(modem: Modem) -> Tuple[str, str]:
    """
    Get the connection status for a modem.
    
    Args:
        modem: The modem object
        
    Returns:
        Tuple of (status_text, color)
    """
    if not modem.reachable:
        return "UNREACHABLE", COLOR_RED
        
    session = requests.Session()
    try:
        # Get connection state
        ok, j = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetConnectionState", params={})
        if ok and isinstance(j, dict) and "result" in j:
            result = j["result"]
            connection_status = result.get("ConnectionStatus", -1)
            
            # Status codes from API doc:
            # 0=disconnected, 1=connecting, 2=connected, 3=disconnecting
            if connection_status == 0:
                return "DISCONNECTED", COLOR_RED
            elif connection_status == 1:
                return "CONNECTING", COLOR_YELLOW
            elif connection_status == 2:
                return "CONNECTED", COLOR_GREEN
            elif connection_status == 3:
                return "DISCONNECTING", COLOR_YELLOW
            else:
                return "UNKNOWN", COLOR_YELLOW
    except Exception:
        pass
    
    return "UNKNOWN", COLOR_YELLOW

def get_signal_strength(modem: Modem) -> Tuple[str, str]:
    """
    Get the enhanced signal strength for a modem with RSRP/RSRQ/SINR.
    
    Args:
        modem: The modem object
        
    Returns:
        Tuple of (signal_text, color)
    """
    if not modem.reachable:
        return "No Signal", COLOR_RED
    
    session = requests.Session()
    try:
        # First try to get detailed signal info from GetNetworkInfo
        ok, j = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetNetworkInfo", params={})
        if ok and isinstance(j, dict) and "result" in j:
            result = j["result"]
            
            # Extract signal measurements
            rsrp = result.get("RSRP") or result.get("rsrp") or result.get("RSRP_dBm")
            rsrq = result.get("RSRQ") or result.get("rsrq") or result.get("RSRQ_dB")
            sinr = result.get("SINR") or result.get("sinr") or result.get("SINR_dB")
            signal_strength = result.get("SignalStrength") or result.get("SignalLevel") or result.get("SignalBar")
            
            # Build comprehensive signal string
            signal_parts = []
            
            # Add RSRP if available
            if rsrp is not None and str(rsrp) not in ["", "N/A", "0", "-"]:
                try:
                    rsrp_val = float(rsrp)
                    signal_parts.append(f"RSRP: {rsrp_val}dBm")
                except (ValueError, TypeError):
                    signal_parts.append(f"RSRP: {rsrp}")
            
            # Add RSRQ if available
            if rsrq is not None and str(rsrq) not in ["", "N/A", "0", "-"]:
                try:
                    rsrq_val = float(rsrq)
                    signal_parts.append(f"RSRQ: {rsrq_val}dB")
                except (ValueError, TypeError):
                    signal_parts.append(f"RSRQ: {rsrq}")
            
            # Add SINR if available
            if sinr is not None and str(sinr) not in ["", "N/A", "0", "-"]:
                try:
                    sinr_val = float(sinr)
                    signal_parts.append(f"SINR: {sinr_val}dB")
                except (ValueError, TypeError):
                    signal_parts.append(f"SINR: {sinr}")
            
            # If we have detailed measurements, return them
            if signal_parts:
                signal_text = " | ".join(signal_parts)
                
                # Determine color based on RSRP if available
                if rsrp is not None:
                    try:
                        rsrp_val = float(rsrp)
                        if rsrp_val >= -70:
                            return signal_text, COLOR_GREEN
                        elif rsrp_val >= -85:
                            return signal_text, COLOR_YELLOW
                        else:
                            return signal_text, COLOR_RED
                    except (ValueError, TypeError):
                        pass
                
                return signal_text, COLOR_BLUE
            
            # Fall back to basic signal strength
            if signal_strength is not None:
                try:
                    signal_num = int(signal_strength)
                    # Map signal value to description
                    if signal_num >= 4:
                        return f"Excellent ({signal_num}/5)", COLOR_GREEN
                    elif signal_num == 3:
                        return f"Good ({signal_num}/5)", COLOR_GREEN
                    elif signal_num == 2:
                        return f"Fair ({signal_num}/5)", COLOR_YELLOW
                    elif signal_num == 1:
                        return f"Poor ({signal_num}/5)", COLOR_RED
                    else:
                        return f"No Signal ({signal_num}/5)", COLOR_RED
                except ValueError:
                    return f"{signal_strength}", COLOR_BLUE
        
        # Fallback to cached network_info if direct call failed
        if modem.network_info and "result" in modem.network_info:
            result = modem.network_info["result"]
            # Try different field names that might contain signal strength
            signal = result.get("SignalStrength")
            if signal is None:
                signal = result.get("SignalLevel")
            if signal is None:
                signal = result.get("SignalBar")
            
            if signal is not None:
                try:
                    signal_num = int(signal)
                    # Map signal value to description
                    if signal_num >= 4:
                        return f"Excellent ({signal_num}/5)", COLOR_GREEN
                    elif signal_num == 3:
                        return f"Good ({signal_num}/5)", COLOR_GREEN
                    elif signal_num == 2:
                        return f"Fair ({signal_num}/5)", COLOR_YELLOW
                    elif signal_num == 1:
                        return f"Poor ({signal_num}/5)", COLOR_RED
                    else:
                        return f"No Signal ({signal_num}/5)", COLOR_RED
                except ValueError:
                    return f"{signal}", COLOR_BLUE
    
    except Exception:
        pass
    
    return "Unknown", COLOR_YELLOW

def get_network_mode(modem: Modem) -> Tuple[str, str]:
    """
    Get the network mode for a modem by checking connection state and network registration.
    
    Args:
        modem: The modem object
        
    Returns:
        Tuple of (mode_text, color)
    """
    if not modem.reachable:
        return "N/A", COLOR_RED
    
    session = requests.Session()
    try:
        # Get network registration state first for accurate network type
        ok, j = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetNetworkInfo", params={})
        if ok and isinstance(j, dict) and "result" in j:
            result = j["result"]
            
            # Try to get the actual network type from various fields
            # Check multiple possible field names that indicate current network type
            network_type = None
            
            # Common field names for network type
            possible_fields = ["CurrentNetworkType", "NetworkType", "RAT", "AccessTechnology", 
                             "CurrentSystemMode", "SystemMode", "ServiceDomain"]
            
            for field in possible_fields:
                if field in result and result[field] is not None:
                    network_type = result[field]
                    break
            
            # Also check if there's a more specific connection info
            if network_type is None:
                # Try to get from connection state which might have more accurate info
                ok2, j2 = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetConnectionState", params={})
                if ok2 and isinstance(j2, dict) and "result" in j2:
                    conn_result = j2["result"]
                    for field in ["NetworkType", "AccessTechnology", "RAT"]:
                        if field in conn_result and conn_result[field] is not None:
                            network_type = conn_result[field]
                            break
            
            if network_type is not None:
                # Map network type values to human-readable names
                if isinstance(network_type, int):
                    # Updated mapping based on common LTE modem values
                    mode_map = {
                        0: "No Service",
                        1: "GSM (2G)",
                        2: "GPRS (2G)", 
                        3: "EDGE (2G)",
                        4: "WCDMA (3G)",
                        5: "HSDPA (3G)",
                        6: "HSUPA (3G)",
                        7: "HSPA (3G)",
                        8: "TD-SCDMA (3G)",
                        9: "HSPA+ (3G+)",
                        10: "LTE (4G)",
                        11: "LTE (4G)",
                        12: "LTE (4G)",
                        13: "LTE (4G)",
                        14: "LTE (4G)",
                        15: "LTE (4G)",
                        16: "LTE (4G)",
                        17: "LTE (4G)",
                        18: "LTE (4G)",
                        19: "LTE (4G)",
                        20: "5G NR",
                        21: "5G NR",
                    }
                    mode_text = mode_map.get(network_type, f"LTE (4G)")  # Default to LTE for unknown high values
                elif isinstance(network_type, str):
                    # Handle string values
                    network_type_lower = network_type.lower()
                    if "lte" in network_type_lower or "4g" in network_type_lower:
                        mode_text = "LTE (4G)"
                    elif "5g" in network_type_lower or "nr" in network_type_lower:
                        mode_text = "5G NR"
                    elif "3g" in network_type_lower or "wcdma" in network_type_lower or "hspa" in network_type_lower:
                        mode_text = "WCDMA (3G)"
                    elif "2g" in network_type_lower or "gsm" in network_type_lower:
                        mode_text = "GSM (2G)"
                    else:
                        mode_text = str(network_type)
                else:
                    mode_text = str(network_type)
                
                # Add color based on generation
                if '5G' in mode_text:
                    return mode_text, "\033[96m"  # Cyan for 5G
                elif '4G' in mode_text or 'LTE' in mode_text:
                    return mode_text, COLOR_GREEN
                elif '3G' in mode_text:
                    return mode_text, COLOR_BLUE
                elif '2G' in mode_text:
                    return mode_text, COLOR_YELLOW
                else:
                    return mode_text, COLOR_BLUE
        
    except Exception:
        pass
    
    return "Unknown", COLOR_YELLOW

def get_default_apn_profile(modem: Modem) -> Tuple[str, str]:
    """
    Get the default APN profile name for a modem.
    
    Args:
        modem: The modem object
        
    Returns:
        Tuple of (apn_name, color)
    """
    if not modem.reachable:
        return "N/A", COLOR_RED
    
    session = requests.Session()
    try:
        ok, j = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetProfileList", params={})
        if ok and isinstance(j, dict) and "result" in j:
            profiles = j.get("result", {}).get("ProfileList", [])
            
            for profile in profiles:
                if profile.get("Default", 0) == 1:
                    profile_name = profile.get("ProfileName", "Unknown")
                    apn = profile.get("APN", "")
                    if apn:
                        return f"{profile_name} ({apn})", COLOR_GREEN
                    else:
                        return profile_name, COLOR_GREEN
            
            # No default profile found
            return "No Default", COLOR_YELLOW
        
    except Exception:
        pass
    
    return "Unknown", COLOR_YELLOW

def get_modem_imei(modem: Modem) -> Tuple[str, str]:
    """
    Get the IMEI for a modem.
    
    Args:
        modem: The modem object
        
    Returns:
        Tuple of (imei, color)
    """
    if not modem.reachable:
        return "N/A", COLOR_RED
    
    # Check if system_info already has IMEI
    if modem.system_info and "result" in modem.system_info:
        result = modem.system_info["result"]
        imei = result.get("IMEI") or result.get("Imei") or result.get("imei")
        if imei:
            return str(imei), COLOR_BLUE
    
    # Try to fetch system info if not available
    session = requests.Session()
    try:
        ok, j = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "GetSystemInfo", params={})
        if ok and isinstance(j, dict) and "result" in j:
            result = j["result"]
            imei = result.get("IMEI") or result.get("Imei") or result.get("imei")
            if imei:
                return str(imei), COLOR_BLUE
        
    except Exception:
        pass
    
    return "Unknown", COLOR_YELLOW

def handle_single_modem_menu(modems: List[Modem]):
    """
    Menu for actions on a single selected modem.
    """
    print_header("SINGLE MODEM OPERATIONS")
    
    # Select a modem
    modem = choose_modem_by_index(modems)
    if not modem:
        return
    
    # If modem is unreachable, try to reconnect automatically
    if not modem.reachable:
        print_colored("Selected modem is unreachable. Attempting automatic reconnection...", COLOR_ORANGE)
        modem = attempt_reconnect_modem(modem)
    
    while True:
        # Get connection status, network mode, signal strength, default APN, and IMEI
        conn_status, conn_color = get_connection_status(modem)
        network_mode, mode_color = get_network_mode(modem)
        signal, signal_color = get_signal_strength(modem)
        default_apn, apn_color = get_default_apn_profile(modem)
        imei, imei_color = get_modem_imei(modem)
        
        # Enhanced header with more information
        print_colored(f"\nMODEM [{modem.index}] STATUS", COLOR_PURPLE, bold=True)
        print_colored("="*70, COLOR_PURPLE)
        
        print_colored(f"Proxy: {modem.raw}", COLOR_BLUE)
        print_colored(f"Connection: {conn_status}", conn_color)
        print_colored(f"Network Mode: {network_mode}", mode_color)
        print_colored(f"Signal: {signal}", signal_color)
        print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
        print_colored(f"PLMN: {modem.plmn or 'Unknown'}", COLOR_BLUE)
        print_colored(f"Default APN: {default_apn}", apn_color)
        print_colored(f"IMEI: {imei}", imei_color)
        print_colored("="*70, COLOR_PURPLE)
        
        print_colored("\nChoose action:", COLOR_BLUE, bold=True)
        print_colored("  1. View current modem status", COLOR_BLUE)
        print_colored("  2. APN Operations", COLOR_PURPLE)
        print_colored("  3. Change network mode", COLOR_PURPLE)
        print_colored("  4. Quick Connect", COLOR_GREEN)
        print_colored("  5. Quick Disconnect", COLOR_RED)
        print_colored("  6. Restart modem", COLOR_ORANGE)
        print_colored("  7. Soft restart modem (disconnect + wait + connect)", COLOR_ORANGE)
        print_colored("  8. Reset modem (WARNING: Factory Reset)", COLOR_RED)
        print_colored("  9. Refresh modem status", COLOR_GREEN)
        print_colored("  10. Test Internet connectivity", COLOR_BLUE)
        print_colored("  11. Back to main menu", COLOR_YELLOW)
        
        try:
            choice = input("\nChoice: ").strip()
            
            if choice == "1":
                view_modem_status(modem)
            elif choice == "2":
                handle_apn_operations_menu(modem)
            elif choice == "3":
                change_network_mode(modem)
            elif choice == "4":
                connect_modem(modem)
            elif choice == "5":
                disconnect_modem(modem)
            elif choice == "6":
                restart_modem(modem)
            elif choice == "7":
                soft_restart_modem(modem)
            elif choice == "8":
                reset_modem(modem)
            elif choice == "9":
                modem = refresh_modem_status(modem)
            elif choice == "10":
                # Test internet connectivity for this single modem
                test_internet_connectivity([modem])
            elif choice == "11":
                return
            else:
                print_colored("Invalid option. Please try again.", COLOR_RED)
                
        except KeyboardInterrupt:
            print_colored("\nOperation cancelled. Returning to menu...", COLOR_YELLOW)
        except Exception as e:
            print_colored(f"An error occurred: {e}", COLOR_RED)

def handle_bulk_menu_for_group(group_modems: List[Modem]):
    """
    Menu for bulk operations on a group of modems.
    """
    if not group_modems:
        print("No modems in this group.")
        return
        
    # Check if all modems have the same carrier (handling combined groups)
    carriers = set(m.carrier for m in group_modems if m.carrier)
    
    if len(carriers) == 1:
        carrier = next(iter(carriers)) or "Unknown"
        header = f"BULK OPERATIONS: {carrier}"
        group_desc = f"Group: {carrier}"
    else:
        # Multiple carriers in the selection
        carrier_counts = {}
        for m in group_modems:
            carrier = m.carrier or "Unknown"
            carrier_counts[carrier] = carrier_counts.get(carrier, 0) + 1
            
        header = "BULK OPERATIONS: MULTIPLE CARRIERS"
        
        # Format the group description with carrier counts
        carrier_list = [f"{carrier} ({count})" for carrier, count in carrier_counts.items()]
        group_desc = f"Groups: {', '.join(carrier_list)}"
    
    reachable = sum(1 for m in group_modems if m.reachable)
    
    while True:
        print_header(header)
        
        print(group_desc)
        print(f"Modems: {len(group_modems)} total, {reachable} reachable")
        
        print_colored("\nChoose bulk action:", COLOR_BLUE, bold=True)
        print_colored("  1. View Status (All Modems)", COLOR_PURPLE)
        print_colored("  2. APN Operations (Bulk)", COLOR_PURPLE)
        print_colored("  3. Change Network Mode (All)", COLOR_PURPLE)
        print_colored("  4. Quick Connect All", COLOR_GREEN)
        print_colored("  5. Quick Disconnect All", COLOR_RED)
        print_colored("  6. Restart All Modems", COLOR_YELLOW)
        print_colored("  7. Soft Restart All (Disconnect → Wait → Connect)", COLOR_YELLOW)
        print_colored("  8. Reset All Modems (⚠️ FACTORY RESET)", COLOR_RED)
        print_colored("  9. Test Internet Connectivity", COLOR_BLUE)
        print_colored("  10. Export Information to CSV", COLOR_BLUE)
        print_colored("  11. Back to Main Menu", COLOR_YELLOW)
        
        try:
            choice = input("\nChoice: ").strip()
            
            # After getting a choice, we don't want to clear the screen on the next loop
            # if the chosen function prints its own output.
            
            if choice == "1":
                bulk_view_status(group_modems)
                continue  # Go to next loop iteration to show menu again
            elif choice == "2":
                handle_bulk_apn_operations(group_modems)
                continue
            elif choice == "3":
                bulk_change_network_mode(group_modems)
                continue
            elif choice == "4":
                bulk_connect_modems(group_modems)
            elif choice == "5":
                bulk_disconnect_modems(group_modems)
            elif choice == "6":
                bulk_restart_modems(group_modems)
            elif choice == "7":
                bulk_soft_restart_modems(group_modems)
            elif choice == "8":
                bulk_reset_modems(group_modems)
            elif choice == "9":
                test_internet_connectivity(group_modems)
            elif choice == "10":
                export_modems_to_csv(group_modems)
            elif choice == "11":
                return  # Exit the loop and go back to the main menu
            else:
                print_colored("Invalid option. Please try again.", COLOR_RED)
                time.sleep(2) # Give user time to read the error
                continue

            # For actions that don't have their own sub-menu, we might want a pause
            # But for now, we will just loop back to the menu.
            
        except KeyboardInterrupt:
            print_colored("\nOperation cancelled. Returning to main menu...", COLOR_YELLOW)
            return
        except Exception as e:
            print_colored(f"An error occurred: {e}", COLOR_RED)
            time.sleep(3)

def handle_multi_group_selection(modems: List[Modem], groups: Dict[str, List[Modem]], carrier_keys: List[str]):
    """
    Allow selection of multiple carrier groups for bulk operations.
    """
    print_colored("\n" + "="*70, COLOR_GREEN, bold=True)
    print_colored(" MULTIPLE GROUP SELECTION ", COLOR_GREEN, bold=True)
    print_colored("="*70, COLOR_GREEN, bold=True)
    
    # First check if carrier information is available or if we need to collect it
    need_carrier_info = False
    for m in modems:
        if m.reachable and not m.carrier:
            need_carrier_info = True
            break
    
    # If we need carrier info (because we did ultra-fast probing initially)
    # we should collect it now before proceeding with group operations
    if need_carrier_info:
        print_colored("\nGathering carrier information for modem grouping...", COLOR_YELLOW)
        reachable_modems = [m for m in modems if m.reachable]
        
        if reachable_modems:
            workers = min(len(reachable_modems), MAX_WORKERS)
            total_done = 0
            
            with ThreadPoolExecutor(max_workers=workers) as ex:
                detailed_futures = {ex.submit(probe_modem, m, fast_probe=False, get_full_info=True): i 
                                    for i, m in enumerate(reachable_modems)}
                
                for fut in as_completed(detailed_futures):
                    idx = detailed_futures[fut]
                    try:
                        modem = fut.result()
                        # Update the original modem in the list
                        original_idx = next(i for i, m in enumerate(modems) if m.index == modem.index)
                        modems[original_idx] = modem
                        
                        # Determine status text and color
                        status = "OK" if modem.reachable else "FAILED"
                        plmn = modem.plmn or ""
                        carrier = modem.carrier or "Unknown"
                        
                        # Progress indicator
                        total_done += 1
                        progress = f"[{total_done}/{len(reachable_modems)}]"
                        
                        # Print result line with colors - only in verbose mode
                        print(f"{progress} [{modem.index}] {modem.raw} -> {status} | {carrier} | {plmn}")
                    except Exception as e:
                        print_colored(f"Error getting carrier info: {e}", COLOR_RED)
        
        # Rebuild the groups with the updated carrier info
        groups = group_by_carrier(modems)
        carrier_keys = list(groups.keys())
    
    print_colored("\nSelect multiple carrier groups to operate on together:", COLOR_BOLD)
    print_colored("Enter the group numbers separated by commas (e.g., 1,3,4)", COLOR_BLUE)
    
    # Show all carrier groups with their numbers
    for i, carrier in enumerate(carrier_keys, start=1):
        group_modems = groups[carrier]
        reachable = sum(1 for m in group_modems if m.reachable)
        
        # Select color based on reachability
        if reachable == len(group_modems):
            color = COLOR_GREEN
        elif reachable > 0:
            color = COLOR_YELLOW
        else:
            color = COLOR_RED
            
        print_colored(f"  {i}. Group: {carrier} ({len(group_modems)} modems, {reachable} reachable)", color)
    
    try:
        # Get user input for group selection
        selection = input("\nEnter group numbers (comma-separated) or 'a' for all groups: ").strip()
        
        # Handle 'all' selection
        if selection.lower() == 'a':
            selected_groups = list(range(1, len(carrier_keys) + 1))
        else:
            # Parse comma-separated input
            try:
                selected_groups = [int(x.strip()) for x in selection.split(',') if x.strip().isdigit()]
            except ValueError:
                print_colored("Invalid input format. Please use numbers separated by commas.", COLOR_RED)
                return
        
        # Validate selected groups
        valid_groups = [g for g in selected_groups if 1 <= g <= len(carrier_keys)]
        
        if not valid_groups:
            print_colored("No valid groups selected.", COLOR_RED)
            return
            
        # Combine modems from all selected groups
        combined_modems = []
        for group_num in valid_groups:
            carrier = carrier_keys[group_num - 1]
            combined_modems.extend(groups[carrier])
        
        # Show summary of selection
        selected_carriers = [carrier_keys[g - 1] for g in valid_groups]
        reachable_count = sum(1 for m in combined_modems if m.reachable)
        
        print_colored("\n" + "="*70, COLOR_GREEN, bold=True)
        print_colored(" COMBINED GROUP OPERATIONS ", COLOR_GREEN, bold=True)
        print_colored("="*70, COLOR_GREEN, bold=True)
        
        print_colored(f"Selected carrier groups: {', '.join(selected_carriers)}", COLOR_BOLD)
        print_colored(f"Total modems: {len(combined_modems)} ({reachable_count} reachable)", 
                     COLOR_GREEN if reachable_count == len(combined_modems) else COLOR_YELLOW)
                     
        # Use the bulk menu with the combined modems
        handle_bulk_menu_for_group(combined_modems)
        
    except KeyboardInterrupt:
        print_colored("\nSelection cancelled. Returning to main menu...", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)
            

def _bulk_execute(modems: List[Modem], action_fn: Callable, action_name: str):
    """
    Execute an action on multiple modems in parallel.
    Preserves order in reporting and provides visual feedback.
    """
    if not modems:
        print_colored("No modems to process.", COLOR_RED)
        return
        
    n = len(modems)
    workers = min(n, MAX_WORKERS)
    
    print_colored(f"\nExecuting {action_name} on {n} modems with {workers} workers...")
    print_colored("-"*70, COLOR_BLUE)
    
    success_count = 0
    failed_modems = []
    start_time = time.time()
    
    with ThreadPoolExecutor(max_workers=workers) as ex:
        future_map = {ex.submit(action_fn, m): m for m in modems}
        
        for i, fut in enumerate(as_completed(future_map), 1):
            modem = future_map[fut]
            progress = f"[{i}/{n}]"
            
            try:
                ok, msg = fut.result()
                
                if ok:
                    success_count += 1
                    print(f"{progress} [{modem.index}] {modem.raw} -> SUCCESS: {msg}")
                else:
                    failed_modems.append(modem)
                    print(f"{progress} [{modem.index}] {modem.raw} -> FAILED: {msg}")
            except Exception as e:
                failed_modems.append(modem)
                # Always show errors, even in non-verbose mode
                print_colored(f"\n{progress} [{modem.index}] {modem.raw} -> ERROR: {str(e)}", COLOR_RED)
    
    elapsed = time.time() - start_time
    
    # Print summary
    print_colored("\nOperation Summary:", COLOR_BOLD)
    print_colored(f"  - Total modems: {n}", COLOR_BOLD)
    print_colored(f"  - Successful: {success_count}", COLOR_GREEN if success_count > 0 else "")
    print_colored(f"  - Failed: {len(failed_modems)}", COLOR_RED if failed_modems else COLOR_GREEN)
    print_colored(f"  - Time taken: {elapsed:.2f} seconds", COLOR_BLUE)
    
    if failed_modems:
        print_colored("\nFailed modems:", COLOR_RED)
        for m in failed_modems:
            print_colored(f"  - [{m.index}] {m.raw}", COLOR_RED)

# Single modem action implementations
def view_modem_status(modem: Modem):
    """Display detailed status information for a modem."""
    if not modem.reachable:
        print_colored("Modem is unreachable. Attempting reconnection to view status...", COLOR_YELLOW)
        modem = attempt_reconnect_modem(modem)
        if not modem.reachable:
            print_colored("Cannot view status: Modem is still unreachable after reconnection attempts.", COLOR_RED)
            return
    
    # Refresh modem status to get latest information
    print_colored("Fetching latest status information...", COLOR_YELLOW)
    updated_modem = refresh_modem_status(modem)
    
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(f" MODEM STATUS: [{updated_modem.index}] ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    # Basic info
    print_colored("Basic Information:", COLOR_BOLD)
    print_colored(f"  Index: {updated_modem.index}", COLOR_BLUE)
    print_colored(f"  Proxy: {updated_modem.raw}", COLOR_BLUE)
    print_colored(f"  Status: {'Reachable' if updated_modem.reachable else 'Unreachable'}", 
                 COLOR_GREEN if updated_modem.reachable else COLOR_RED)
    print_colored(f"  Carrier: {updated_modem.carrier or 'Unknown'}", COLOR_BLUE)
    print_colored(f"  PLMN: {updated_modem.plmn or 'Unknown'}", COLOR_BLUE)
    
    # System info
    if updated_modem.system_info:
        print_colored("\nSystem Information:", COLOR_BOLD)
        for key, value in updated_modem.system_info.items():
            if isinstance(value, dict) and key == "result":
                for k, v in value.items():
                    print_colored(f"  {k}: {v}", COLOR_BLUE)
            else:
                print_colored(f"  {key}: {value}", COLOR_BLUE)
    
    # Network info
    if updated_modem.network_info:
        print_colored("\nNetwork Information:", COLOR_BOLD)
        for key, value in updated_modem.network_info.items():
            if isinstance(value, dict) and key == "result":
                for k, v in value.items():
                    print_colored(f"  {k}: {v}", COLOR_BLUE)
            else:
                print_colored(f"  {key}: {value}", COLOR_BLUE)
    
    # Get current APN profiles
    print_colored("\nFetching APN Profiles...", COLOR_YELLOW)
    session = requests.Session()
    ok, j = jsonrpc_post(session, WEBAPI_URL, updated_modem.proxy, "GetProfileList", params={})
    
    if ok and isinstance(j, dict) and "result" in j:
        profiles = j.get("result", {}).get("ProfileList", [])
        
        if profiles:
            print_colored("\nAPN Profiles:", COLOR_BOLD)
            print_colored("-" * 75, COLOR_BLUE)
            print_colored(f"{'ID':<4} {'Name':<20} {'APN':<20} {'Dial Number':<12} {'Default':<7}", COLOR_BOLD)
            print_colored("-" * 75, COLOR_BLUE)
            
            for profile in profiles:
                profile_id = str(profile.get("ProfileID", "?"))
                profile_name = profile.get("ProfileName", "Unknown")[:19]
                apn = profile.get("APN", "Unknown")[:19]
                dial_number = profile.get("DailNumber", "*99#")[:11]
                
                is_default = profile.get("Default", 0) == 1
                default_str = "YES" if is_default else "NO"
                
                color = COLOR_GREEN if is_default else COLOR_BLUE
                print_colored(f"{profile_id:<4} {profile_name:<20} {apn:<20} {dial_number:<12} {default_str:<7}", color)
            
            print_colored("-" * 75, COLOR_BLUE)
        else:
            print_colored("\nNo APN profiles found.", COLOR_YELLOW)
    else:
        print_colored("\nFailed to retrieve APN profiles.", COLOR_RED)
    
    # Get connection state
    print_colored("\nFetching Connection State...", COLOR_YELLOW)
    ok, j = jsonrpc_post(session, WEBAPI_URL, updated_modem.proxy, "GetConnectionState", params={})
    
    if ok and isinstance(j, dict) and "result" in j:
        conn_state = j.get("result", {})
        if conn_state:
            status_map = {
                0: ("Disconnected", COLOR_RED),
                1: ("Connecting", COLOR_YELLOW),
                2: ("Connected", COLOR_GREEN),
                3: ("Disconnecting", COLOR_YELLOW)
            }
            
            status_val = conn_state.get("ConnectionStatus", 0)
            status_text, status_color = status_map.get(status_val, ("Unknown", ""))
            
            print_colored("\nConnection Status:", COLOR_BOLD)
            print_colored(f"  Status: {status_text}", status_color)
            print_colored(f"  IPv4: {conn_state.get('IPv4Adrress', 'Not assigned')}", COLOR_BLUE)
            print_colored(f"  IPv6: {conn_state.get('IPv6Adrress', 'Not assigned')}", COLOR_BLUE)
            print_colored(f"  DNS: {conn_state.get('PrimaryDNS', 'Unknown')}", COLOR_BLUE)
    else:
        print_colored("\nFailed to retrieve connection state.", COLOR_RED)
    
    input("\nPress Enter to continue...")

def handle_apn_operations_menu(modem: Modem):
    """
    Comprehensive APN operations submenu for a single modem.
    """
    if not modem.reachable:
        print_colored("Modem is unreachable. Attempting reconnection...", COLOR_YELLOW)
        modem = attempt_reconnect_modem(modem)
        if not modem.reachable:
            print_colored("Cannot access APN operations: Modem is still unreachable.", COLOR_RED)
            return

    # Cache APN profiles to avoid refetching on every menu display
    cached_profiles = None
    current_default_id = None
    
    while True:
        # Fetch APN profiles if not cached
        if cached_profiles is None:
            print_colored("Fetching APN profiles...", COLOR_YELLOW)
            ok, profiles = get_apn_profiles(modem)
            if not ok:
                print_colored("Failed to retrieve APN profiles.", COLOR_RED)
                return
            cached_profiles = profiles
            # Find current default
            for profile in cached_profiles:
                if profile.get("Default", 0) == 1:
                    current_default_id = profile.get("ProfileID")
                    break

        # Display header with profile summary
        print_colored("\n" + "="*70, COLOR_PURPLE, bold=True)
        print_colored(" APN OPERATIONS ", COLOR_PURPLE, bold=True)
        print_colored("="*70, COLOR_PURPLE, bold=True)
        
        print_colored(f"Modem: [{modem.index}] {modem.raw}", COLOR_BOLD)
        print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
        
        # Display APN profiles in table format
        if cached_profiles:
            print_colored(f"\nAvailable APN Profiles ({len(cached_profiles)} total):", COLOR_BOLD)
            print_colored("-" * 75, COLOR_BLUE)
            print_colored(f"{'ID':<4} {'Name':<20} {'APN':<20} {'Dial Number':<12} {'Default':<7}", COLOR_BOLD)
            print_colored("-" * 75, COLOR_BLUE)
            
            for profile in cached_profiles:
                profile_id = str(profile.get("ProfileID", "?"))
                profile_name = profile.get("ProfileName", "Unknown")[:19]
                apn = profile.get("APN", "Unknown")[:19]
                dial_number = profile.get("DailNumber", "*99#")[:11]
                
                is_default = profile.get("Default", 0) == 1
                default_str = "YES" if is_default else "NO"
                
                color = COLOR_GREEN if is_default else COLOR_BLUE
                print_colored(f"{profile_id:<4} {profile_name:<20} {apn:<20} {dial_number:<12} {default_str:<7}", color)
            
            print_colored("-" * 75, COLOR_BLUE)
        else:
            print_colored("\nNo APN profiles available.", COLOR_YELLOW)
        
        # Menu options
        print_colored("\nChoose APN operation:", COLOR_BLUE, bold=True)
        print_colored("  1. View profile details", COLOR_BLUE)
        print_colored("  2. Add new APN profile", COLOR_GREEN)
        print_colored("  3. Edit existing profile", COLOR_YELLOW)
        print_colored("  4. Delete profile", COLOR_RED)
        print_colored("  5. Set default profile", COLOR_PURPLE)
        print_colored("  6. Update APN profiles (refresh)", COLOR_BLUE)
        print_colored("  7. Back to modem menu", COLOR_YELLOW)
        
        try:
            choice = input("\nChoice: ").strip()
            
            if choice == "1":
                view_profile_details(modem, cached_profiles)
            elif choice == "2":
                success = add_new_apn_profile(modem)
                if success:
                    cached_profiles = None  # Force refresh
            elif choice == "3":
                success = edit_apn_profile(modem, cached_profiles)
                if success:
                    cached_profiles = None  # Force refresh
            elif choice == "4":
                success = delete_apn_profile(modem, cached_profiles)
                if success:
                    cached_profiles = None  # Force refresh
            elif choice == "5":
                success = set_default_apn_from_menu(modem, cached_profiles, current_default_id)
                if success:
                    cached_profiles = None  # Force refresh
            elif choice == "6":
                cached_profiles = None  # Force refresh on next loop
                print_colored("APN profiles will be refreshed.", COLOR_GREEN)
            elif choice == "7":
                return
            else:
                print_colored("Invalid option. Please try again.", COLOR_RED)
                
        except KeyboardInterrupt:
            print_colored("\nOperation cancelled. Returning to modem menu...", COLOR_YELLOW)
            return
        except Exception as e:
            print_colored(f"An error occurred: {e}", COLOR_RED)

def view_profile_details(modem: Modem, profiles: List[Dict]):
    """Display detailed information for a selected APN profile."""
    if not profiles:
        print_colored("No profiles available.", COLOR_YELLOW)
        return
    
    print_colored("\nSelect profile to view details:", COLOR_BOLD)
    for i, profile in enumerate(profiles, 1):
        profile_name = profile.get("ProfileName", "Unknown")
        is_default = profile.get("Default", 0) == 1
        status = " [DEFAULT]" if is_default else ""
        print_colored(f"  {i}. {profile_name}{status}", COLOR_GREEN if is_default else COLOR_BLUE)
    
    try:
        choice = input("\nEnter profile number (or 'q' to cancel): ").strip()
        if choice.lower() == 'q':
            return
        
        choice_num = int(choice)
        if choice_num < 1 or choice_num > len(profiles):
            print_colored("Invalid profile number.", COLOR_RED)
            return
        
        profile = profiles[choice_num - 1]
        
        # Display detailed information
        print_colored("\n" + "="*50, COLOR_BLUE, bold=True)
        print_colored(" PROFILE DETAILS ", COLOR_BLUE, bold=True)
        print_colored("="*50, COLOR_BLUE, bold=True)
        
        print_colored(f"Profile ID: {profile.get('ProfileID', 'Unknown')}", COLOR_BLUE)
        print_colored(f"Name: {profile.get('ProfileName', 'Unknown')}", COLOR_BLUE)
        print_colored(f"APN: {profile.get('APN', 'Unknown')}", COLOR_BLUE)
        print_colored(f"Dial Number: {profile.get('DailNumber', '*99#')}", COLOR_BLUE)
        print_colored(f"Username: {profile.get('UserName', '[Empty]') or '[Empty]'}", COLOR_BLUE)
        print_colored(f"Password: {'[Set]' if profile.get('Password') else '[Empty]'}", COLOR_BLUE)
        
        # Protocol/Auth type
        auth_type_map = {0: "None", 1: "PAP", 2: "CHAP", -1: "PAP & CHAP"}
        auth_type = auth_type_map.get(profile.get("AuthType", 0), "Unknown")
        print_colored(f"Protocol: {auth_type}", COLOR_BLUE)
        
        # PDP type
        pdp_type_map = {1: "IPv4", 2: "IPv6", 3: "IPv4v6", -1: "Auto"}
        pdp_type = pdp_type_map.get(profile.get("PdpType", -1), "Unknown")
        print_colored(f"PDP Type: {pdp_type}", COLOR_BLUE)
        print_colored(f"Default Profile: {'Yes' if profile.get('Default', 0) == 1 else 'No'}", 
                     COLOR_GREEN if profile.get('Default', 0) == 1 else COLOR_BLUE)
        print_colored(f"Predefined: {'Yes' if profile.get('IsPredefine', 0) == 1 else 'No'}", COLOR_BLUE)
        
        input("\nPress Enter to continue...")
        
    except (ValueError, KeyboardInterrupt):
        print_colored("Operation cancelled.", COLOR_YELLOW)

def add_new_apn_profile(modem: Modem) -> bool:
    """Add a new APN profile to the modem."""
    print_colored("\n" + "="*50, COLOR_GREEN, bold=True)
    print_colored(" ADD NEW APN PROFILE ", COLOR_GREEN, bold=True)
    print_colored("="*50, COLOR_GREEN, bold=True)
    
    try:
        # Get profile details from user
        profile_name = input("Profile Name: ").strip()
        if not profile_name:
            print_colored("Profile name is required.", COLOR_RED)
            return False
        
        apn = input("APN: ").strip()
        if not apn:
            print_colored("APN is required.", COLOR_RED)
            return False
        
        dial_number = input("Dial Number (default: *99#): ").strip()
        if not dial_number:
            dial_number = "*99#"
        
        username = input("Username (optional): ").strip()
        password = input("Password (optional): ").strip()
        
        # Protocol/Authentication type
        print_colored("\nProtocol:", COLOR_BOLD)
        print_colored("  0. None")
        print_colored("  1. PAP") 
        print_colored("  2. CHAP")
        print_colored("  3. PAP & CHAP")
        
        auth_choice = input("Enter protocol (default: 0): ").strip()
        if auth_choice == "3":
            auth_type = -1  # Auto (PAP & CHAP)
        else:
            auth_type = int(auth_choice) if auth_choice else 0
        
        # Set as default option
        set_default = input("\nSet as default profile? (y/n, default: n): ").strip().lower() == 'y'
        
        # Confirm creation
        print_colored(f"\nProfile Summary:", COLOR_BOLD)
        print_colored(f"  Name: {profile_name}")
        print_colored(f"  APN: {apn}")
        print_colored(f"  Dial Number: {dial_number}")
        print_colored(f"  Username: {username or '[Empty]'}")
        print_colored(f"  Password: {'[Set]' if password else '[Empty]'}")
        auth_name = {0: "None", 1: "PAP", 2: "CHAP", -1: "PAP & CHAP"}.get(auth_type, "Unknown")
        print_colored(f"  Protocol: {auth_name}")
        print_colored(f"  Set as Default: {'Yes' if set_default else 'No'}")
        
        confirm = input("\nCreate this profile? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Profile creation cancelled.", COLOR_YELLOW)
            return False
        
        # Create the profile using API
        print_colored("Creating APN profile...", COLOR_YELLOW)
        
        # Check if we need to disconnect before changes if setting as default
        was_connected = False
        if set_default:
            conn_status, _ = get_connection_status(modem)
            was_connected = "CONNECTED" in conn_status
            
            if was_connected:
                print_colored("Disconnecting modem before setting new default APN...", COLOR_YELLOW)
                action_disconnect(modem)
                time.sleep(2)  # Brief pause
        
        # Create profile via direct API call
        session = requests.Session()
        params = {
            "ProfileName": profile_name,
            "APN": apn,
            "UserName": username,
            "Password": password,
            "AuthType": auth_type,
            "DailNumber": dial_number,
            "Default": 0,  # Don't set as default yet
            "IsPredefine": 0,
            "IPAdrress": "",
            "PdpType": 3  # Default to IPv4v6 (dual stack)
        }
        
        ok, result = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "AddNewProfile", params)
        
        if not ok:
            print_colored("Failed to create APN profile.", COLOR_RED)
            return False
        
        print_colored("APN profile created successfully!", COLOR_GREEN)
        
        # If user wants to set as default, do it now
        if set_default:
            print_colored("Setting as default profile...", COLOR_YELLOW)
            # Need to get the new profile ID first
            time.sleep(1)  # Brief pause for profile to be created
            ok, profiles = get_apn_profiles(modem)
            if ok:
                # Find the profile we just created
                new_profile = None
                for profile in profiles:
                    if profile.get("ProfileName") == profile_name and profile.get("APN") == apn:
                        new_profile = profile
                        break
                
                if new_profile:
                    profile_id = new_profile.get("ProfileID")
                    ok, msg = set_default_apn_profile(modem, profile_id)
                    if ok:
                        print_colored("Set as default profile successfully!", COLOR_GREEN)
                        
                        # Reconnect if we were connected before
                        if was_connected:
                            print_colored("Reconnecting modem with new APN...", COLOR_YELLOW)
                            time.sleep(2)  # Brief pause
                            action_connect(modem)
                    else:
                        print_colored(f"Failed to set as default: {msg}", COLOR_RED)
                else:
                    print_colored("Could not find newly created profile to set as default.", COLOR_YELLOW)
        
        return True
        
    except (ValueError, KeyboardInterrupt):
        print_colored("Operation cancelled.", COLOR_YELLOW)
        return False
    except Exception as e:
        print_colored(f"Error creating profile: {e}", COLOR_RED)
        return False

def edit_apn_profile(modem: Modem, profiles: List[Dict]) -> bool:
    """Edit an existing APN profile."""
    if not profiles:
        print_colored("No profiles available to edit.", COLOR_YELLOW)
        return False
    
    print_colored("\n" + "="*50, COLOR_YELLOW, bold=True)
    print_colored(" EDIT APN PROFILE ", COLOR_YELLOW, bold=True)
    print_colored("="*50, COLOR_YELLOW, bold=True)
    
    # Show profiles
    print_colored("Select profile to edit:", COLOR_BOLD)
    for i, profile in enumerate(profiles, 1):
        profile_name = profile.get("ProfileName", "Unknown")
        is_default = profile.get("Default", 0) == 1
        status = " [DEFAULT]" if is_default else ""
        print_colored(f"  {i}. {profile_name}{status}", COLOR_GREEN if is_default else COLOR_BLUE)
    
    try:
        choice = input("\nEnter profile number (or 'q' to cancel): ").strip()
        if choice.lower() == 'q':
            return False
        
        choice_num = int(choice)
        if choice_num < 1 or choice_num > len(profiles):
            print_colored("Invalid profile number.", COLOR_RED)
            return False
        
        profile = profiles[choice_num - 1]
        profile_id = profile.get("ProfileID")
        
        print_colored(f"\nEditing Profile: {profile.get('ProfileName', 'Unknown')}", COLOR_BOLD)
        print_colored("Leave empty to keep current value:", COLOR_BLUE)
        
        # Get new values (allow empty to keep current)
        current_name = profile.get("ProfileName", "")
        new_name = input(f"Profile Name [{current_name}]: ").strip()
        if not new_name:
            new_name = current_name
        
        current_apn = profile.get("APN", "")
        new_apn = input(f"APN [{current_apn}]: ").strip()
        if not new_apn:
            new_apn = current_apn
        
        current_dial = profile.get("DailNumber", "*99#")
        new_dial_number = input(f"Dial Number [{current_dial}]: ").strip()
        if not new_dial_number:
            new_dial_number = current_dial
        
        current_user = profile.get("UserName", "")
        new_username = input(f"Username [{current_user}]: ").strip()
        if not new_username:
            new_username = current_user
        
        current_pass = profile.get("Password", "")
        new_password = input(f"Password [{'[Current]' if current_pass else '[Empty]'}]: ").strip()
        if not new_password:
            new_password = current_pass
        
        # Protocol selection with current value shown
        current_auth = profile.get("AuthType", 0)
        auth_map = {0: "None", 1: "PAP", 2: "CHAP", -1: "PAP & CHAP"}
        current_auth_name = auth_map.get(current_auth, "Unknown")
        
        print_colored(f"\nProtocol [Current: {current_auth_name}]:", COLOR_BOLD)
        print_colored("  0. None")
        print_colored("  1. PAP")
        print_colored("  2. CHAP") 
        print_colored("  3. PAP & CHAP")
        
        auth_input = input("Enter protocol (empty to keep current): ").strip()
        if auth_input == "3":
            new_auth_type = -1  # PAP & CHAP
        elif auth_input:
            new_auth_type = int(auth_input)
        else:
            new_auth_type = current_auth
        
        # Confirm changes
        print_colored(f"\nProfile Changes Summary:", COLOR_BOLD)
        print_colored(f"  Name: {current_name} -> {new_name}")
        print_colored(f"  APN: {current_apn} -> {new_apn}")
        print_colored(f"  Dial Number: {current_dial} -> {new_dial_number}")
        print_colored(f"  Username: {current_user} -> {new_username}")
        print_colored(f"  Password: {'[Changed]' if new_password != current_pass else '[Unchanged]'}")
        print_colored(f"  Protocol: {current_auth_name} -> {auth_map.get(new_auth_type, 'Unknown')}")
        
        confirm = input("\nApply these changes? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Changes cancelled.", COLOR_YELLOW)
            return False
        
        # Apply changes via API
        print_colored("Updating APN profile...", COLOR_YELLOW)
        
        session = requests.Session()
        params = {
            "ProfileID": profile_id,
            "ProfileName": new_name,
            "APN": new_apn,
            "UserName": new_username,
            "Password": new_password,
            "AuthType": new_auth_type,
            "DailNumber": new_dial_number,
            "Default": profile.get("Default", 0),  # Keep current default status
            "IsPredefine": profile.get("IsPredefine", 0),
            "IPAdrress": profile.get("IPAdrress", ""),
            "PdpType": profile.get("PdpType", 3)  # Keep current PDP type
        }
        
        ok, result = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "EditProfile", params)
        
        if ok:
            print_colored("APN profile updated successfully!", COLOR_GREEN)
            return True
        else:
            print_colored("Failed to update APN profile.", COLOR_RED)
            return False
            
    except (ValueError, KeyboardInterrupt):
        print_colored("Operation cancelled.", COLOR_YELLOW)
        return False
    except Exception as e:
        print_colored(f"Error editing profile: {e}", COLOR_RED)
        return False

def delete_apn_profile(modem: Modem, profiles: List[Dict]) -> bool:
    """Delete an APN profile from the modem."""
    if not profiles:
        print_colored("No profiles available to delete.", COLOR_YELLOW)
        return False
    
    # Check if there are non-default profiles to delete
    non_default_profiles = [p for p in profiles if p.get("Default", 0) != 1]
    if not non_default_profiles:
        print_colored("Cannot delete profiles - only default profile exists.", COLOR_RED)
        return False
    
    print_colored("\n" + "="*50, COLOR_RED, bold=True)
    print_colored(" DELETE APN PROFILE ", COLOR_RED, bold=True)
    print_colored("="*50, COLOR_RED, bold=True)
    
    print_colored("WARNING: This will permanently delete the selected profile!", COLOR_RED, bold=True)
    print_colored("Default profiles cannot be deleted.", COLOR_YELLOW)
    
    # Show non-default profiles only
    print_colored("\nAvailable profiles to delete:", COLOR_BOLD)
    deletable_profiles = []
    for i, profile in enumerate(profiles):
        if profile.get("Default", 0) != 1:  # Not default
            deletable_profiles.append(profile)
            profile_name = profile.get("ProfileName", "Unknown")
            print_colored(f"  {len(deletable_profiles)}. {profile_name}", COLOR_BLUE)
    
    if not deletable_profiles:
        print_colored("No deletable profiles found.", COLOR_YELLOW)
        return False
    
    try:
        choice = input("\nEnter profile number to delete (or 'q' to cancel): ").strip()
        if choice.lower() == 'q':
            return False
        
        choice_num = int(choice)
        if choice_num < 1 or choice_num > len(deletable_profiles):
            print_colored("Invalid profile number.", COLOR_RED)
            return False
        
        profile = deletable_profiles[choice_num - 1]
        profile_id = profile.get("ProfileID")
        profile_name = profile.get("ProfileName", "Unknown")
        
        # Final confirmation
        confirm = input(f"\nAre you sure you want to delete profile '{profile_name}'? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Deletion cancelled.", COLOR_YELLOW)
            return False
        
        # Delete via API
        print_colored("Deleting APN profile...", COLOR_YELLOW)
        
        session = requests.Session()
        params = {"ProfileID": profile_id}
        
        ok, result = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "DeleteProfile", params)
        
        if ok:
            print_colored("APN profile deleted successfully!", COLOR_GREEN)
            return True
        else:
            print_colored("Failed to delete APN profile.", COLOR_RED)
            return False
            
    except (ValueError, KeyboardInterrupt):
        print_colored("Operation cancelled.", COLOR_YELLOW)
        return False
    except Exception as e:
        print_colored(f"Error deleting profile: {e}", COLOR_RED)
        return False

def set_default_apn_from_menu(modem: Modem, profiles: List[Dict], current_default_id) -> bool:
    """Set a different APN profile as default with proper connection handling."""
    if not profiles:
        print_colored("No profiles available.", COLOR_YELLOW)
        return False
    
    print_colored("\n" + "="*50, COLOR_PURPLE, bold=True)
    print_colored(" SET DEFAULT APN PROFILE ", COLOR_PURPLE, bold=True)
    print_colored("="*50, COLOR_PURPLE, bold=True)
    
    # Show available profiles
    print_colored("Select profile to set as default:", COLOR_BOLD)
    for i, profile in enumerate(profiles, 1):
        profile_name = profile.get("ProfileName", "Unknown")
        profile_id = profile.get("ProfileID")
        is_default = profile.get("Default", 0) == 1
        
        if is_default:
            print_colored(f"  {i}. {profile_name} [CURRENT DEFAULT]", COLOR_GREEN)
        else:
            print_colored(f"  {i}. {profile_name}", COLOR_BLUE)
    
    try:
        choice = input("\nEnter profile number (or 'q' to cancel): ").strip()
        if choice.lower() == 'q':
            return False
        
        choice_num = int(choice)
        if choice_num < 1 or choice_num > len(profiles):
            print_colored("Invalid profile number.", COLOR_RED)
            return False
        
        selected_profile = profiles[choice_num - 1]
        profile_id = selected_profile.get("ProfileID")
        profile_name = selected_profile.get("ProfileName", "Unknown")
        
        # Check if it's already the default
        if selected_profile.get("Default", 0) == 1:
            print_colored("This profile is already the default.", COLOR_YELLOW)
            return False
        
        # Confirm selection
        confirm = input(f"\nSet profile '{profile_name}' as default? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Operation cancelled.", COLOR_YELLOW)
            return False
        
        # Check connection status before making changes
        conn_status, _ = get_connection_status(modem)
        was_connected = "CONNECTED" in conn_status
        
        print_colored("Setting default APN profile...", COLOR_YELLOW)
        
        # Disconnect if connected (as per requirement)
        if was_connected:
            print_colored("Disconnecting modem before changing default APN...", COLOR_YELLOW)
            action_disconnect(modem)
            time.sleep(2)  # Brief pause
        
        # Set new default
        ok, msg = set_default_apn_profile(modem, profile_id)
        
        if ok:
            print_colored(f"Default APN profile set successfully!", COLOR_GREEN)
            
            # Reconnect if we were connected before
            if was_connected:
                print_colored("Reconnecting modem with new default APN...", COLOR_YELLOW)
                time.sleep(2)  # Brief pause before reconnecting
                action_connect(modem)
                
            return True
        else:
            print_colored(f"Failed to set default APN profile: {msg}", COLOR_RED)
            
            # If we disconnected but failed to set new default, try to reconnect with old settings
            if was_connected:
                print_colored("Attempting to reconnect with previous settings...", COLOR_YELLOW)
                time.sleep(2)
                action_connect(modem)
            
            return False
            
    except (ValueError, KeyboardInterrupt):
        print_colored("Operation cancelled.", COLOR_YELLOW)
        return False
    except Exception as e:
        print_colored(f"Error setting default profile: {e}", COLOR_RED)
        return False

def set_default_apn_profile_menu(modem: Modem):
    """Menu to select an existing APN profile and set it as default."""
    if not modem.reachable:
        print_colored("Modem is unreachable. Attempting reconnection before changing APN profile...", COLOR_YELLOW)
        modem = attempt_reconnect_modem(modem)
        if not modem.reachable:
            print_colored("Cannot change default APN: Modem is still unreachable after reconnection attempts.", COLOR_RED)
            return
    
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(" SET DEFAULT APN PROFILE ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    print_colored(f"Modem: [{modem.index}] {modem.raw}", COLOR_BOLD)
    print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
    
    try:
        # Fetch available profiles
        print_colored("\nFetching available APN profiles...", COLOR_YELLOW)
        ok, profiles = get_apn_profiles(modem)
        
        if not ok or not profiles:
            print_colored("No APN profiles found or error retrieving profiles.", COLOR_RED)
            return
        
        # Display available profiles
        print_colored("\nAvailable APN Profiles:", COLOR_BOLD)
        for i, profile in enumerate(profiles, 1):
            is_default = profile.get("Default", 0) == 1
            profile_id = profile.get("ProfileID", "Unknown")
            profile_name = profile.get("ProfileName", "Unknown")
            apn = profile.get("APN", "")
            
            status = "[DEFAULT]" if is_default else ""
            status_color = COLOR_GREEN if is_default else ""
            
            print_colored(f"  {i}. Profile {profile_id}: {profile_name} {status}", 
                         COLOR_BLUE + status_color)
            print_colored(f"     APN: {apn}", COLOR_BLUE)
        
        # Ask which profile to set as default
        choice = input("\nEnter number of profile to set as default (or 'q' to cancel): ").strip()
        
        if choice.lower() == 'q':
            print_colored("Operation cancelled.", COLOR_YELLOW)
            return
        
        try:
            choice_num = int(choice)
            if choice_num < 1 or choice_num > len(profiles):
                print_colored("Invalid profile number.", COLOR_RED)
                return
            
            selected_profile = profiles[choice_num - 1]
            profile_id = selected_profile.get("ProfileID")
            profile_name = selected_profile.get("ProfileName", "Unknown")
            
            # Confirm selection
            confirm = input(f"\nSet profile '{profile_name}' (ID: {profile_id}) as default? (y/n): ").strip().lower()
            if confirm != 'y':
                print_colored("Operation cancelled.", COLOR_YELLOW)
                return
            
            # Call set_default_apn_profile
            print_colored("\nSetting default APN profile...", COLOR_YELLOW)
            ok, msg = set_default_apn_profile(modem, profile_id)
            
            if ok:
                print_colored(f"Default APN profile set successfully: {msg}", COLOR_GREEN)
            else:
                print_colored(f"Failed to set default APN profile: {msg}", COLOR_RED)
                
        except ValueError:
            print_colored("Invalid input. Please enter a valid number.", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

def change_apn_settings(modem: Modem):
    """Change APN settings for a single modem."""
    if not modem.reachable:
        print_colored("Modem is unreachable. Attempting reconnection before changing APN settings...", COLOR_YELLOW)
        modem = attempt_reconnect_modem(modem)
        if not modem.reachable:
            print_colored("Cannot change APN: Modem is still unreachable after reconnection attempts.", COLOR_RED)
            return
    
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(" CHANGE APN SETTINGS ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    print_colored(f"Modem: [{modem.index}] {modem.raw}", COLOR_BOLD)
    print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
    
    # Show field descriptions based on the WebUI
    print_colored("\nAPN Profile Settings:", COLOR_BOLD)
    
    try:
        # Profile name (Optional, will be auto-generated if not provided)
        profile_name = input("\nEnter Profile Name (leave blank for auto-generated): ").strip() or None
        
        # Dial number (Required per WebUI)
        dial_number = input("Enter Dial Number [*99#]: ").strip() or "*99#"
        
        # APN (Optional per WebUI)
        apn = input("Enter APN: ").strip()
        
        # Username and password (Optional per WebUI)
        username = input("Username (optional, press Enter to skip): ").strip() or ""
        password = input("Password (optional, press Enter to skip): ").strip() or ""
        
        # Protocol/Authentication type (matches WebUI's "None, PAP, CHAP, PAP&CHAP")
        print_colored("\nProtocol:", COLOR_BLUE)
        print_colored("  0: None (Default)", COLOR_BLUE)
        print_colored("  1: PAP", COLOR_BLUE)
        print_colored("  2: CHAP", COLOR_BLUE)
        print_colored("  3: PAP&CHAP", COLOR_BLUE)
        auth_type = input("Choose protocol [0]: ").strip() or "0"
        try:
            auth_type = int(auth_type)
            if auth_type not in [0, 1, 2, 3]:
                auth_type = 0
        except ValueError:
            auth_type = 0
        
        # Display summary
        print_colored(f"\nSetting up APN profile for modem [{modem.index}]...", COLOR_BLUE)
        print_colored(f"  Profile Name: {profile_name or '(auto-generated)'}", COLOR_BLUE)
        print_colored(f"  APN: {apn or '(none)'}", COLOR_BLUE)
        print_colored(f"  Username: {username or '(none)'}", COLOR_BLUE)
        print_colored(f"  Password: {'(set)' if password else '(none)'}", COLOR_BLUE)
        print_colored(f"  Protocol: {['None', 'PAP', 'CHAP', 'PAP&CHAP'][auth_type]}", COLOR_BLUE)
        print_colored(f"  Dial Number: {dial_number}", COLOR_BLUE)
        
        confirm = input("\nConfirm changes? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Operation cancelled.", COLOR_YELLOW)
            return
        
        # Call the updated action_set_apn with all parameters
        print_colored("\nSetting up APN profile...", COLOR_YELLOW)
        ok, msg = action_set_apn(modem, apn, username, password, dial_number, profile_name)
        
        if ok:
            print_colored(f"APN profile created successfully: {msg}", COLOR_GREEN)
        else:
            print_colored(f"Failed to create APN profile: {msg}", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

def change_network_mode(modem: Modem):
    """Change network mode for a single modem with proper disconnect/reconnect flow."""
    if not modem.reachable:
        print_colored("Modem is unreachable. Attempting reconnection before changing network mode...", COLOR_YELLOW)
        modem = attempt_reconnect_modem(modem)
        if not modem.reachable:
            print_colored("Cannot change network mode: Modem is still unreachable after reconnection attempts.", COLOR_RED)
            return
    
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(" CHANGE NETWORK MODE ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    print_colored(f"Modem: [{modem.index}] {modem.raw}", COLOR_BOLD)
    print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
    
    # Get current network mode
    current_mode, _ = get_network_mode(modem)
    print_colored(f"Current Network Mode: {current_mode}", COLOR_BLUE)
    
    # Network mode options - using actual API values that work with modems
    network_modes = [
        (0, "Automatic (2G/3G/4G)"),
        (2, "4G LTE Only"), 
        (1, "3G Only"),
        (13, "2G Only")
    ]
    
    print_colored("\nSelect new network mode:", COLOR_BOLD)
    for i, (mode_value, mode_desc) in enumerate(network_modes, 1):
        print_colored(f"  {i}. {mode_desc}", COLOR_YELLOW)
    
    try:
        choice = input("\nEnter choice number (or 'q' to cancel): ").strip()
        if choice.lower() == 'q':
            print_colored("Operation cancelled.", COLOR_YELLOW)
            return
            
        if not choice.isdigit():
            print_colored("Invalid choice. Operation cancelled.", COLOR_YELLOW)
            return
            
        choice_num = int(choice)
        if choice_num < 1 or choice_num > len(network_modes):
            print_colored("Invalid option. Operation cancelled.", COLOR_RED)
            return
            
        # Get the selected mode
        selected_mode_value, selected_mode_desc = network_modes[choice_num - 1]
        
        # Confirm selection
        confirm = input(f"\nChange network mode to '{selected_mode_desc}'? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Operation cancelled.", COLOR_YELLOW)
            return
        
        # Check current connection status
        conn_status, _ = get_connection_status(modem)
        was_connected = "CONNECTED" in conn_status
        
        print_colored(f"\nChanging network mode to {selected_mode_desc}...", COLOR_BLUE)
        print_colored("Process: Disconnect → Set Network Mode → Wait → Connect", COLOR_YELLOW)
        
        success = True
        
        # Step 1: Disconnect if connected
        if was_connected:
            print_colored("Step 1/4: Disconnecting modem...", COLOR_YELLOW)
            ok, msg = action_disconnect(modem)
            if not ok:
                print_colored(f"Failed to disconnect modem: {msg}", COLOR_RED)
                success = False
            else:
                print_colored("✓ Modem disconnected successfully", COLOR_GREEN)
                time.sleep(2)  # Brief pause after disconnect
        else:
            print_colored("Step 1/4: Modem already disconnected", COLOR_GREEN)
        
        if success:
            # Step 2: Set network mode via direct API call
            print_colored("Step 2/4: Setting network mode...", COLOR_YELLOW)
            
            session = requests.Session()
            
            # Try to set network selection mode first
            params = {
                "SelectionMode": 0,  # Automatic selection
                "NetworkMode": selected_mode_value,
                "PreferredMode": selected_mode_value
            }
            
            ok, result = jsonrpc_post(session, WEBAPI_URL, modem.proxy, "SetNetworkSettings", params)
            
            if ok:
                print_colored("✓ Network mode set successfully", COLOR_GREEN)
                
                # Step 3: Wait for modem to apply settings and search for network
                print_colored("Step 3/4: Waiting for modem to apply settings (15 seconds)...", COLOR_YELLOW)
                for i in range(15, 0, -1):
                    print(f"\rWaiting... {i} seconds remaining", end="", flush=True)
                    time.sleep(1)
                print()  # New line after countdown
                
                print_colored("✓ Settings applied, modem ready", COLOR_GREEN)
                
                # Step 4: Reconnect if we were connected before
                if was_connected:
                    print_colored("Step 4/4: Reconnecting modem...", COLOR_YELLOW)
                    print_colored("Note: It may take additional time to connect to cell tower with new mode", COLOR_BLUE)
                    
                    ok, msg = action_connect(modem)
                    if ok:
                        print_colored("✓ Reconnection initiated successfully", COLOR_GREEN)
                        print_colored("The modem will now search for and connect to the network.", COLOR_BLUE)
                        print_colored("This may take 30-60 seconds depending on signal conditions.", COLOR_BLUE)
                    else:
                        print_colored(f"⚠ Reconnection failed: {msg}", COLOR_YELLOW)
                        print_colored("You may need to manually connect after the mode change takes effect.", COLOR_YELLOW)
                else:
                    print_colored("Step 4/4: Modem was not connected, no reconnection needed", COLOR_GREEN)
                
                print_colored(f"\n✓ Network mode change to '{selected_mode_desc}' completed!", COLOR_GREEN)
                print_colored("Use 'Refresh modem status' to check the current network mode.", COLOR_BLUE)
                
            else:
                print_colored("✗ Failed to set network mode via API", COLOR_RED)
                success = False
        
        if not success:
            print_colored(f"\n✗ Network mode change failed", COLOR_RED)
            if was_connected:
                print_colored("Attempting to reconnect with previous settings...", COLOR_YELLOW)
                time.sleep(2)
                action_connect(modem)
    
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"\nError changing network mode: {e}", COLOR_RED)
    
    input("\nPress Enter to continue...")

def reset_modem(modem: Modem):
    """Factory reset a single modem with confirmation."""
    if not modem.reachable:
        print_colored("Modem is unreachable. Attempting reconnection before factory reset...", COLOR_YELLOW)
        modem = attempt_reconnect_modem(modem)
        if not modem.reachable:
            print_colored("Cannot reset: Modem is still unreachable after reconnection attempts.", COLOR_RED)
            return
    
    print_colored("\n" + "="*70, COLOR_RED, bold=True)
    print_colored(" ⚠️ FACTORY RESET MODEM ⚠️ ", COLOR_RED, bold=True)
    print_colored("="*70, COLOR_RED, bold=True)
    
    print_colored(f"Modem: [{modem.index}] {modem.raw}", COLOR_BOLD)
    print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
    
    print_colored("\nWARNING: This will FACTORY RESET the modem. All settings will be lost.\nYou'll also lost access to this Modem for upto 10 Mins.", COLOR_RED, bold=True)
    print_colored("This action cannot be undone!", COLOR_RED, bold=True)
    
    try:
        confirm = input("\nType 'RESET' (all caps) to confirm reset: ").strip()
        if confirm != "RESET":
            print_colored("Reset cancelled. Incorrect confirmation.", COLOR_YELLOW)
            return
        
        ok, msg = action_reset(modem)
        
        if ok:
            print_colored(f"Reset command sent successfully: {msg}", COLOR_GREEN)
            print_colored("\n⚠️ IMPORTANT: The modem will disconnect and restart automatically.", COLOR_YELLOW)
            print_colored("You will need to wait for upto 10 minutes for the modem", COLOR_YELLOW)
            print_colored("to complete the factory reset process before it becomes available again.", COLOR_YELLOW)
        else:
            print_colored(f"Failed to reset modem: {msg}", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nReset cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

def restart_modem(modem: Modem):
    """Restart a single modem."""
    if not modem.reachable:
        print_colored("Modem is unreachable. Attempting reconnection before restarting...", COLOR_YELLOW)
        modem = attempt_reconnect_modem(modem)
        if not modem.reachable:
            print_colored("Cannot restart: Modem is still unreachable after reconnection attempts.", COLOR_RED)
            return
    
    print_colored("\n" + "="*70, COLOR_YELLOW, bold=True)
    print_colored(" RESTART MODEM ", COLOR_YELLOW, bold=True)
    print_colored("="*70, COLOR_YELLOW, bold=True)
    
    print_colored(f"Modem: [{modem.index}] {modem.raw}", COLOR_BOLD)
    print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
    
    try:
        confirm = input("\nConfirm restart this modem? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Restart cancelled.", COLOR_YELLOW)
            return
        
        # Call the improved implementation directly
        print_colored("\nSending restart command to modem...", COLOR_YELLOW)
        ok, msg = action_restart(modem)
        
        if ok:
            print_colored(f"Restart command successful: {msg}", COLOR_GREEN)
            print_colored("Modem will restart and may be unavailable for a few minutes", COLOR_YELLOW)
        else:
            print_colored(f"Failed to restart modem: {msg}", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nRestart cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

def connect_modem(modem: Modem):
    """Connect a single modem to data network."""
    if not modem.reachable:
        print_colored("Modem is unreachable. Attempting reconnection before connecting...", COLOR_YELLOW)
        modem = attempt_reconnect_modem(modem)
        if not modem.reachable:
            print_colored("Cannot connect: Modem is still unreachable after reconnection attempts.", COLOR_RED)
            return
    
    print_colored("\n" + "="*70, COLOR_GREEN, bold=True)
    print_colored(" CONNECT MODEM ", COLOR_GREEN, bold=True)
    print_colored("="*70, COLOR_GREEN, bold=True)
    
    print_colored(f"Modem: [{modem.index}] {modem.raw}", COLOR_BOLD)
    print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
    
    try:
        confirm = input("\nConfirm connect this modem? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Connect cancelled.", COLOR_YELLOW)
            return
        
        print_colored("\nSending connect command to modem...", COLOR_YELLOW)
        ok, msg = action_connect(modem)
        
        if ok:
            print_colored(f"Connect command successful: {msg}", COLOR_GREEN)
        else:
            print_colored(f"Failed to connect modem: {msg}", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nConnect cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

def disconnect_modem(modem: Modem):
    """Disconnect a single modem from data network."""
    if not modem.reachable:
        print_colored("Modem is unreachable. Attempting reconnection before disconnecting...", COLOR_YELLOW)
        modem = attempt_reconnect_modem(modem)
        if not modem.reachable:
            print_colored("Cannot disconnect: Modem is still unreachable after reconnection attempts.", COLOR_RED)
            return
    
    print_colored("\n" + "="*70, COLOR_RED, bold=True)
    print_colored(" DISCONNECT MODEM ", COLOR_RED, bold=True)
    print_colored("="*70, COLOR_RED, bold=True)
    
    print_colored(f"Modem: [{modem.index}] {modem.raw}", COLOR_BOLD)
    print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
    
    try:
        confirm = input("\nConfirm disconnect this modem? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Disconnect cancelled.", COLOR_YELLOW)
            return
        
        print_colored("\nSending disconnect command to modem...", COLOR_YELLOW)
        ok, msg = action_disconnect(modem)
        
        if ok:
            print_colored(f"Disconnect command successful: {msg}", COLOR_GREEN)
        else:
            print_colored(f"Failed to disconnect modem: {msg}", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nDisconnect cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

def soft_restart_modem(modem: Modem):
    """Perform a soft restart on a single modem (disconnect + wait + connect)."""
    if not modem.reachable:
        print_colored("Modem is unreachable. Attempting reconnection before soft restarting...", COLOR_YELLOW)
        modem = attempt_reconnect_modem(modem)
        if not modem.reachable:
            print_colored("Cannot soft restart: Modem is still unreachable after reconnection attempts.", COLOR_RED)
        return
    
    print_colored("\n" + "="*70, COLOR_YELLOW, bold=True)
    print_colored(" SOFT RESTART MODEM ", COLOR_YELLOW, bold=True)
    print_colored("="*70, COLOR_YELLOW, bold=True)
    
    print_colored(f"Modem: [{modem.index}] {modem.raw}", COLOR_BOLD)
    print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
    print_colored("\nThis will disconnect the modem, wait 10 seconds, then reconnect.", COLOR_BLUE)
    
    try:
        confirm = input("\nConfirm soft restart this modem? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Soft restart cancelled.", COLOR_YELLOW)
            return
        
        print_colored("\nPerforming soft restart...", COLOR_YELLOW)
        ok, msg = action_soft_restart(modem)
        
        if ok:
            print_colored(f"Soft restart successful: {msg}", COLOR_GREEN)
        else:
            print_colored(f"Failed to soft restart modem: {msg}", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nSoft restart cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

# Bulk action implementations
def bulk_set_default_apn(modems: List[Modem]):
    """Select an APN profile and set it as default for all modems in a group."""
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print_colored("No reachable modems in this group to update.", COLOR_RED)
        return
    
    # For a batch operation, we'll get the APN profiles from the first modem
    # and apply the selected profile ID to all modems
    first_modem = reachable_modems[0]
    
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(" BULK SET DEFAULT APN PROFILE ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    print_colored(f"Target: {len(reachable_modems)} reachable modems", COLOR_BOLD)
    carrier = modems[0].carrier or "Unknown"
    print_colored(f"Group: {carrier}", COLOR_BLUE)
    
    try:
        # Fetch available profiles from the first modem
        print_colored("\nFetching available APN profiles from the first modem...", COLOR_YELLOW)
        ok, profiles = get_apn_profiles(first_modem)
        
        if not ok or not profiles:
            print_colored("No APN profiles found or error retrieving profiles.", COLOR_RED)
            return
        
        # Display available profiles
        print_colored("\nAvailable APN Profiles:", COLOR_BOLD)
        for i, profile in enumerate(profiles, 1):
            is_default = profile.get("Default", 0) == 1
            profile_id = profile.get("ProfileID", "Unknown")
            profile_name = profile.get("ProfileName", "Unknown")
            apn = profile.get("APN", "")
            
            status = "[DEFAULT]" if is_default else ""
            status_color = COLOR_GREEN if is_default else ""
            
            print_colored(f"  {i}. Profile {profile_id}: {profile_name} {status}", 
                         COLOR_BLUE + status_color)
            print_colored(f"     APN: {apn}", COLOR_BLUE)
        
        # Ask which profile to set as default
        choice = input("\nEnter number of profile to set as default for ALL modems (or 'q' to cancel): ").strip()
        
        if choice.lower() == 'q':
            print_colored("Operation cancelled.", COLOR_YELLOW)
            return
        
        try:
            choice_num = int(choice)
            if choice_num < 1 or choice_num > len(profiles):
                print_colored("Invalid profile number.", COLOR_RED)
                return
            
            selected_profile = profiles[choice_num - 1]
            profile_id = selected_profile.get("ProfileID")
            profile_name = selected_profile.get("ProfileName", "Unknown")
            
            # Confirm selection
            confirm = input(f"\nSet profile '{profile_name}' (ID: {profile_id}) as default for ALL modems? (y/n): ").strip().lower()
            if confirm != 'y':
                print_colored("Operation cancelled.", COLOR_YELLOW)
                return
            
            # Execute in bulk
            _bulk_execute(
                reachable_modems,
                lambda m: set_default_apn_profile(m, profile_id),
                "set default APN profile"
            )
                
        except ValueError:
            print_colored("Invalid input. Please enter a valid number.", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

# Global cache for bulk status data
_bulk_status_cache = {}
_cache_timestamp = None

def bulk_view_status(modems: List[Modem]):
    """
    Displays a comprehensive status table and summary for a group of modems.
    Uses caching to avoid repeated data gathering and provides refresh option.
    """
    global _bulk_status_cache, _cache_timestamp
    
    # --- 1. Initial Setup ---
    if not modems:
        print_colored("No modems in this group.", COLOR_YELLOW)
        input("\nPress Enter to continue...")
        return

    reachable_modems = [m for m in modems if m.reachable]
    if not reachable_modems:
        print_colored("\nNo reachable modems to display status for.", COLOR_RED)
        input("\nPress Enter to continue...")
        return
    
    # Create cache key based on modem indices
    cache_key = tuple(sorted([m.index for m in reachable_modems]))
    use_cache = False
    
    # Check if we have cached data for this group
    if cache_key in _bulk_status_cache and _cache_timestamp:
        cache_age_minutes = (time.time() - _cache_timestamp) / 60
        if cache_age_minutes < 5:  # Cache valid for 5 minutes
            use_cache = True
    
    modem_data = []
    
    if use_cache:
        modem_data = _bulk_status_cache[cache_key]
    else:
        # --- 2. Gather Fresh Data ---
        def gather_modem_info(modem):
            """Gather comprehensive info for a single modem using the same functions as single modem menu"""
            try:
                # Use exact same functions as single modem menu (they work perfectly)
                conn_status, _ = get_connection_status(modem)
                signal_str, _ = get_signal_strength(modem)
                default_apn_result = get_default_apn_profile(modem)
                
                # Clean connection status
                conn_clean = conn_status.split()[0] if isinstance(conn_status, str) and conn_status else "Unknown"
                
                # Extract RSRP and RSRQ from enhanced signal string
                rsrp = "N/A"
                rsrq = "N/A"
                if signal_str and isinstance(signal_str, str):
                    if "RSRP:" in signal_str:
                        try:
                            rsrp = signal_str.split("RSRP:")[1].split()[0].replace("dBm", "").strip()
                        except:
                            rsrp = "N/A"
                    
                    if "RSRQ:" in signal_str:
                        try:
                            rsrq = signal_str.split("RSRQ:")[1].split()[0].replace("dB", "").strip()
                        except:
                            rsrq = "N/A"
                
                # Clean APN exactly like single modem menu
                apn_clean = "None"
                if default_apn_result:
                    if isinstance(default_apn_result, tuple):
                        # If it's a tuple like ('Orange Internet (net.orange.jo)', '\x1b[92m'), take first element
                        apn_clean = str(default_apn_result[0])
                    else:
                        apn_clean = str(default_apn_result)
                    
                    # Clean up common unwanted text
                    if "Not Found" in apn_clean:
                        apn_clean = "None"
                
                return {
                    'id': modem.index,
                    'connection': conn_clean,
                    'rsrp': rsrp,
                    'rsrq': rsrq,
                    'apn': apn_clean,
                    'carrier': modem.carrier or "Unknown"
                }
                
            except Exception as e:
                return {
                    'id': modem.index,
                    'connection': "Error",
                    'rsrp': "N/A",
                    'rsrq': "N/A",
                    'apn': "Error",
                    'carrier': modem.carrier or "Unknown"
                }
        
        print_colored(f"\nGathering status for {len(reachable_modems)} reachable modems...", COLOR_YELLOW)
        
        # Use threading for faster processing
        with ThreadPoolExecutor(max_workers=min(len(reachable_modems), MAX_WORKERS)) as executor:
            futures = [executor.submit(gather_modem_info, modem) for modem in reachable_modems]
            
            for future in as_completed(futures):
                try:
                    result = future.result()
                    modem_data.append(result)
                except Exception as e:
                    # Add error entry if future fails
                    modem_data.append({
                        'id': 0,
                        'connection': "Error",
                        'rsrp': "N/A",
                        'rsrq': "N/A", 
                        'apn': "Error",
                        'carrier': "Unknown"
                    })
        
        # Cache the results
        _bulk_status_cache[cache_key] = modem_data
        _cache_timestamp = time.time()
        print_colored("Status gathering complete!", COLOR_GREEN)

    # --- 3. Display Results ---
    while True:
        os.system('cls' if os.name == 'nt' else 'clear')
        print_colored("\n" + "="*120, COLOR_BLUE, bold=True)
        print_colored(" BULK STATUS VIEW ", COLOR_BLUE, bold=True)
        print_colored("="*120, COLOR_BLUE, bold=True)
        
        if use_cache:
            cache_age = int((time.time() - _cache_timestamp) / 60)
            print_colored(f"Showing cached data ({cache_age} minutes old)", COLOR_YELLOW)
        else:
            print_colored("Showing fresh data", COLOR_GREEN)

        # Display Results Table
        print_colored("\n" + "="*120, COLOR_BLUE)
        print_colored(" STATUS RESULTS ", COLOR_BLUE, bold=True)
        print_colored("="*120, COLOR_BLUE)
        print_colored(f"{'ID':<5}{'Status':<15}{'RSRP (dBm)':<15}{'RSRQ (dB)':<15}{'Default APN':<25}{'Carrier':<20}", COLOR_BOLD)
        print_colored("-"*120, COLOR_BLUE)

        for data in sorted(modem_data, key=lambda x: x['id']):
            # Color for Connection Status
            if 'CONNECTED' in data['connection'].upper(): status_color = COLOR_GREEN
            elif 'DISCONNECTED' in data['connection'].upper(): status_color = COLOR_RED
            else: status_color = COLOR_YELLOW
            
            # Build the row
            id_str = f"{data['id']:<5}"
            status_str = f"{data['connection']:<15}"
            rsrp_str = f"{data['rsrp']:<15}"
            rsrq_str = f"{data['rsrq']:<15}"
            apn_str = f"{str(data['apn'])[:24]:<25}"
            carrier_str = f"{str(data['carrier'])[:19]:<20}"
            
            # Print the whole line with color for status
            if 'CONNECTED' in data['connection'].upper():
                print_colored(f"{id_str}{status_str}{rsrp_str}{rsrq_str}{apn_str}{carrier_str}", COLOR_GREEN)
            elif 'DISCONNECTED' in data['connection'].upper():
                print_colored(f"{id_str}{status_str}{rsrp_str}{rsrq_str}{apn_str}{carrier_str}", COLOR_RED)
            else:
                print_colored(f"{id_str}{status_str}{rsrp_str}{rsrq_str}{apn_str}{carrier_str}", COLOR_YELLOW)

        # --- 4. Display Summary ---
        print_colored("\n" + "="*120, COLOR_BLUE)
        print_colored(" SUMMARY ", COLOR_BLUE, bold=True)
        print_colored("="*120, COLOR_BLUE)

        # Connection Summary
        conn_summary = {}
        for data in modem_data:
            conn_summary.setdefault(data['connection'], []).append(data['id'])
        print_colored("\nConnection Status:", COLOR_BOLD)
        for status, ids in conn_summary.items():
            color = COLOR_GREEN if 'CONNECTED' in status.upper() else COLOR_RED if 'DISCONNECTED' in status.upper() else COLOR_YELLOW
            print_colored(f"  - {status}: {len(ids)} modems (IDs: {', '.join(map(str, sorted(ids)))})", color)

        # APN Summary
        apn_summary = {}
        for data in modem_data:
            # Clean APN data in case there are still tuple remnants
            apn = data['apn']
            if isinstance(apn, tuple):
                apn = str(apn[0])
            apn_summary.setdefault(apn, []).append(data['id'])
        print_colored("\nAPN Usage:", COLOR_BOLD)
        for apn, ids in apn_summary.items():
            color = COLOR_GREEN if apn not in ["None", "Error"] else COLOR_YELLOW
            print_colored(f"  - {apn}: {len(ids)} modems (IDs: {', '.join(map(str, sorted(ids)))})", color)

        # --- 5. User Input ---
        print_colored("\n" + "="*120, COLOR_BLUE)
        choice = input("Press Enter to return to the Bulk Operations menu or R to refresh data again: ").strip().lower()
        
        if choice == 'r':
            # Clear cache and refresh
            if cache_key in _bulk_status_cache:
                del _bulk_status_cache[cache_key]
            _cache_timestamp = None
            use_cache = False
            
            # Refresh the data
            def gather_modem_info(modem):
                """Gather comprehensive info for a single modem using the same functions as single modem menu"""
                try:
                    # Use exact same functions as single modem menu (they work perfectly)
                    conn_status, _ = get_connection_status(modem)
                    signal_str, _ = get_signal_strength(modem)
                    default_apn_result = get_default_apn_profile(modem)
                    
                    # Clean connection status
                    conn_clean = conn_status.split()[0] if isinstance(conn_status, str) and conn_status else "Unknown"
                    
                    # Extract RSRP and RSRQ from enhanced signal string
                    rsrp = "N/A"
                    rsrq = "N/A"
                    if signal_str and isinstance(signal_str, str):
                        if "RSRP:" in signal_str:
                            try:
                                rsrp = signal_str.split("RSRP:")[1].split()[0].replace("dBm", "").strip()
                            except:
                                rsrp = "N/A"
                        
                        if "RSRQ:" in signal_str:
                            try:
                                rsrq = signal_str.split("RSRQ:")[1].split()[0].replace("dB", "").strip()
                            except:
                                rsrq = "N/A"
                    
                    # Clean APN exactly like single modem menu
                    apn_clean = "None"
                    if default_apn_result:
                        if isinstance(default_apn_result, tuple):
                            # If it's a tuple like ('Orange Internet (net.orange.jo)', '\x1b[92m'), take first element
                            apn_clean = str(default_apn_result[0])
                        else:
                            apn_clean = str(default_apn_result)
                        
                        # Clean up common unwanted text
                        if "Not Found" in apn_clean:
                            apn_clean = "None"
                    
                    return {
                        'id': modem.index,
                        'connection': conn_clean,
                        'rsrp': rsrp,
                        'rsrq': rsrq,
                        'apn': apn_clean,
                        'carrier': modem.carrier or "Unknown"
                    }
                    
                except Exception as e:
                    return {
                        'id': modem.index,
                        'connection': "Error",
                        'rsrp': "N/A",
                        'rsrq': "N/A",
                        'apn': "Error",
                        'carrier': modem.carrier or "Unknown"
                    }
            
            print_colored(f"\nRefreshing status for {len(reachable_modems)} reachable modems...", COLOR_YELLOW)
            
            modem_data = []
            # Use threading for faster processing
            with ThreadPoolExecutor(max_workers=min(len(reachable_modems), MAX_WORKERS)) as executor:
                futures = [executor.submit(gather_modem_info, modem) for modem in reachable_modems]
                
                for future in as_completed(futures):
                    try:
                        result = future.result()
                        modem_data.append(result)
                    except Exception as e:
                        # Add error entry if future fails
                        modem_data.append({
                            'id': 0,
                            'connection': "Error",
                            'rsrp': "N/A",
                            'rsrq': "N/A", 
                            'apn': "Error",
                            'carrier': "Unknown"
                        })
            
            # Cache the fresh results
            _bulk_status_cache[cache_key] = modem_data
            _cache_timestamp = time.time()
            use_cache = False
            print_colored("Status refresh complete!", COLOR_GREEN)
        else:
            break

def handle_bulk_apn_operations(modems: List[Modem]):
    """Handle bulk APN operations menu."""
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print_colored("No reachable modems in this group for APN operations.", COLOR_RED)
        input("Press Enter to continue...")
        return
    
    while True:
        print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
        print_colored(" BULK APN OPERATIONS ", COLOR_BLUE, bold=True)
        print_colored("="*70, COLOR_BLUE, bold=True)
        
        print_colored(f"Operating on {len(reachable_modems)} reachable modems", COLOR_BLUE)
        
        print_colored("\nChoose APN operation:", COLOR_BOLD)
        print_colored("  1. Set Default APN Profile (from existing profiles)", COLOR_PURPLE)
        print_colored("  2. Create and Apply New APN Settings", COLOR_PURPLE)
        print_colored("  3. View APN Profiles on All Modems", COLOR_BLUE)
        print_colored("  4. Back to Bulk Menu", COLOR_YELLOW)
        
        try:
            choice = input("\nEnter choice: ").strip()
            
            if choice == "1":
                bulk_set_default_apn(reachable_modems)
            elif choice == "2":
                bulk_create_and_apply_apn(reachable_modems)
            elif choice == "3":
                bulk_view_apn_profiles(reachable_modems)
            elif choice == "4":
                break
            else:
                print_colored("Invalid option. Please try again.", COLOR_RED)
                
        except KeyboardInterrupt:
            print_colored("\nOperation cancelled.", COLOR_YELLOW)
            break

def bulk_create_and_apply_apn(modems: List[Modem]):
    """Create and apply APN settings to all modems using existing action_set_apn function."""
    print_colored("\n" + "="*60, COLOR_BLUE, bold=True)
    print_colored(" APPLY APN SETTINGS TO ALL MODEMS ", COLOR_BLUE, bold=True)
    print_colored("="*60, COLOR_BLUE, bold=True)
    
    # Get APN details from user (simplified for bulk operations)
    print_colored("Enter APN settings to apply to all modems:", COLOR_BOLD)
    
    profile_name = input("Profile Name: ").strip()
    if not profile_name:
        print_colored("Profile name is required.", COLOR_RED)
        return
    
    apn = input("APN: ").strip()
    if not apn:
        print_colored("APN is required.", COLOR_RED)
        return
    
    dial_number = input("Dial Number (default: *99#): ").strip() or "*99#"
    username = input("Username (optional): ").strip()
    password = input("Password (optional): ").strip()
    
    # Confirm settings
    print_colored(f"\nAPN settings to apply:", COLOR_BOLD)
    print_colored(f"  Profile Name: {profile_name}", COLOR_BLUE)
    print_colored(f"  APN: {apn}", COLOR_BLUE)
    print_colored(f"  Dial Number: {dial_number}", COLOR_BLUE)
    print_colored(f"  Username: {username or '(none)'}", COLOR_BLUE)
    print_colored(f"  Password: {'*' * len(password) if password else '(none)'}", COLOR_BLUE)
    
    confirm = input(f"\nApply these APN settings to {len(modems)} modems? (y/n): ").strip().lower()
    if confirm != 'y':
        print_colored("Operation cancelled.", COLOR_YELLOW)
        return
    
    # Apply to all modems using existing action_set_apn
    success_count = 0
    
    print_colored(f"\nApplying APN settings to {len(modems)} modems...", COLOR_BLUE)
    
    # Optimize thread count based on number of modems
    workers = min(len(modems), MAX_WORKERS)
    with ThreadPoolExecutor(max_workers=workers) as executor:
        def apply_apn_to_modem(modem):
            try:
                ok, msg = action_set_apn(modem, apn, username, password, dial_number, profile_name, quiet=True, force_disconnect=True)
                if ok:
                    return True, f"✓ {modem.index}: APN settings applied successfully"
                else:
                    return False, f"✗ {modem.index}: {msg}"
            except Exception as e:
                return False, f"✗ {modem.index}: Error - {str(e)}"
        
        futures = [executor.submit(apply_apn_to_modem, modem) for modem in modems]
        
        for future in as_completed(futures):
            success, message = future.result()
            if success:
                success_count += 1
                print_colored(message, COLOR_GREEN)
            else:
                print_colored(message, COLOR_RED)
    
    print_colored(f"\n✓ APN settings applied successfully to {success_count}/{len(modems)} modems", COLOR_GREEN if success_count > 0 else COLOR_RED)
    input("Press Enter to continue...")

def bulk_view_apn_profiles(modems: List[Modem]):
    """View APN profiles from all modems using the same logic as single modem operations."""
    print_colored("\n" + "="*60, COLOR_BLUE, bold=True)
    print_colored(" APN PROFILES ON ALL MODEMS ", COLOR_BLUE, bold=True)
    print_colored("="*60, COLOR_BLUE, bold=True)
    
    print_colored(f"Gathering APN profiles from {len(modems)} modems...", COLOR_BLUE)
    print_colored("Note: This may take a moment to retrieve all profile information...\n", COLOR_YELLOW)
    
    for i, modem in enumerate(modems, 1):
        # Use the same working logic as the single modem operations
        try:
            # Use the working get_apn_profiles function from actions.py
            ok, profiles = get_apn_profiles(modem)
            
            if ok and profiles:
                print_colored(f"Modem {modem.index} ({modem.carrier or 'Unknown'}):", COLOR_BOLD)
                # Display profiles table using the correct structure
                print_colored("  " + "-" * 75, COLOR_BLUE)
                print_colored(f"  {'ID':<4} {'Name':<20} {'APN':<20} {'Dial Number':<12} {'Default':<7}", COLOR_BOLD)
                print_colored("  " + "-" * 75, COLOR_BLUE)
                
                for profile in profiles:
                    # Use the correct field names from the API documentation
                    profile_id = str(profile.get("ProfileID", "?"))
                    name = profile.get("ProfileName", "Unknown")[:19]
                    apn = profile.get("APN", "Unknown")[:19]  # Correct field name is 'APN'
                    dial_number = profile.get("DailNumber", "*99#")[:11]  # Note the typo 'DailNumber' in API
                    
                    # Use the correct field name for default detection
                    is_default = profile.get("Default", 0) == 1
                    default_str = "YES" if is_default else "NO"
                    
                    color = COLOR_GREEN if is_default else COLOR_BLUE
                    print_colored(f"  {profile_id:<4} {name:<20} {apn:<20} {dial_number:<12} {default_str:<7}", color)
                
                print_colored("  " + "-" * 75, COLOR_BLUE)
            elif ok and not profiles:
                print_colored(f"Modem {modem.index}: No profiles found", COLOR_YELLOW)
            else:
                print_colored(f"Modem {modem.index}: Error retrieving profiles", COLOR_RED)
                
        except Exception as e:
            print_colored(f"Modem {modem.index}: Error - {str(e)}", COLOR_RED)
        
        if i < len(modems):
            print()  # Add spacing between modems
    
    input("\nPress Enter to continue...")

def bulk_change_apn(modems: List[Modem]):
    """Change APN settings for multiple modems at once."""
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print("No reachable modems in this group to update.")
        return
    
    print_header("BULK CHANGE APN SETTINGS")
    
    print(f"Target: {len(reachable_modems)} reachable modems")
    carrier = modems[0].carrier or "Unknown"
    print(f"Group: {carrier}")
    
    # Show field descriptions based on the WebUI
    print("\nAPN Profile Settings:")
    
    try:
        # Profile name (Optional, will be auto-generated if not provided)
        profile_name = input("\nEnter Profile Name (leave blank for auto-generated): ").strip() or None
        
        # Dial number (Required per WebUI)
        dial_number = input("Enter Dial Number [*99#]: ").strip() or "*99#"
        
        # APN (Optional per WebUI)
        apn = input("Enter APN for all modems: ").strip()
        
        # Username and password (Optional per WebUI)
        username = input("Username (optional, press Enter to skip): ").strip() or ""
        password = input("Password (optional, press Enter to skip): ").strip() or ""
        
        # Protocol/Authentication type (matches WebUI's "None, PAP, CHAP, PAP&CHAP")
        print_colored("\nProtocol:", COLOR_BLUE)
        print_colored("  0: None (Default)", COLOR_BLUE)
        print_colored("  1: PAP", COLOR_BLUE)
        print_colored("  2: CHAP", COLOR_BLUE)
        print_colored("  3: PAP&CHAP", COLOR_BLUE)
        auth_type = input("Choose protocol [0]: ").strip() or "0"
        try:
            auth_type = int(auth_type)
            if auth_type not in [0, 1, 2, 3]:
                auth_type = 0
        except ValueError:
            auth_type = 0
        
        # Display summary
        print_colored(f"\nSetting up APN profiles for {len(reachable_modems)} modems...", COLOR_BLUE)
        print_colored(f"  Profile Name: {profile_name or '(auto-generated)'}", COLOR_BLUE)
        print_colored(f"  APN: {apn or '(none)'}", COLOR_BLUE)
        print_colored(f"  Username: {username or '(none)'}", COLOR_BLUE)
        print_colored(f"  Password: {'(set)' if password else '(none)'}", COLOR_BLUE)
        print_colored(f"  Protocol: {['None', 'PAP', 'CHAP', 'PAP&CHAP'][auth_type]}", COLOR_BLUE)
        print_colored(f"  Dial Number: {dial_number}", COLOR_BLUE)
        
        confirm = input("\nConfirm changes for ALL modems? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Operation cancelled.", COLOR_YELLOW)
            return
        
        # Execute in bulk using the improved action_set_apn function with all parameters
        _bulk_execute(
            reachable_modems,
            lambda m: action_set_apn(m, apn, username, password, dial_number, profile_name),
            "APN update"
        )
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

def bulk_change_network_mode(modems: List[Modem]):
    """Change network mode for multiple modems at once."""
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print_colored("No reachable modems in this group to update.", COLOR_RED)
        return
    
    print_colored("\n" + "="*70, COLOR_BLUE, bold=True)
    print_colored(" BULK CHANGE NETWORK MODE ", COLOR_BLUE, bold=True)
    print_colored("="*70, COLOR_BLUE, bold=True)
    
    print_colored(f"Target: {len(reachable_modems)} reachable modems", COLOR_BOLD)
    carrier = modems[0].carrier or "Unknown"
    print_colored(f"Group: {carrier}", COLOR_BLUE)
    
    # Network mode options with numeric menu
    network_modes = [
        ("auto", "Automatic mode selection"),
        ("lte_only", "4G LTE only"),
        ("3g", "3G only"),
        ("2g", "2G only")
    ]
    
    print_colored("\nSelect network mode for ALL modems:", COLOR_YELLOW)
    for i, (mode_key, mode_desc) in enumerate(network_modes, 1):
        print_colored(f"  {i}. {mode_desc}", COLOR_YELLOW)
    
    try:
        choice = input("\nEnter choice number: ").strip()
        if not choice.isdigit():
            print_colored("Invalid choice. Operation cancelled.", COLOR_YELLOW)
            return
            
        choice_num = int(choice)
        if choice_num < 1 or choice_num > len(network_modes):
            print_colored("Invalid option. Operation cancelled.", COLOR_RED)
            return
            
        # Get the selected mode
        selected_mode_key, selected_mode_desc = network_modes[choice_num - 1]
        
        # Confirm selection
        confirm = input(f"\nSet network mode to '{selected_mode_desc}' for ALL modems? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Operation cancelled.", COLOR_YELLOW)
            return
        
        print_colored("\nChanging network mode on multiple modems...", COLOR_YELLOW)
        print_colored("This may take some time to complete as each modem needs to reconfigure.", COLOR_YELLOW)
        print_colored("The network mode change may take up to 30 seconds to fully apply on each modem.", COLOR_YELLOW)
        
        # Execute in bulk with smaller worker count to avoid overwhelming the modems
        workers = min(5, len(reachable_modems))
        print_colored(f"Using {workers} parallel workers for better stability...", COLOR_YELLOW)
        
        # Execute in bulk
        _bulk_execute(
            reachable_modems,
            lambda m: action_set_network_mode(m, selected_mode_key),
            "network mode update"
        )
        
        print_colored("\nNote: It may take some time for the modems to fully apply the new network mode.", COLOR_YELLOW)
        print_colored("You may need to refresh the modem status after a minute to see the updated network mode.", COLOR_YELLOW)
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

def bulk_reset_modems(modems: List[Modem]):
    """Factory reset multiple modems with confirmation."""
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print_colored("No reachable modems in this group to reset.", COLOR_RED)
        return
    
    print_colored("\n" + "="*70, COLOR_RED, bold=True)
    print_colored(" ⚠️ BULK FACTORY RESET MODEMS ⚠️ ", COLOR_RED, bold=True)
    print_colored("="*70, COLOR_RED, bold=True)
    
    print_colored(f"Target: {len(reachable_modems)} reachable modems", COLOR_BOLD)
    carrier = modems[0].carrier or "Unknown"
    print_colored(f"Group: {carrier}", COLOR_BLUE)
    
    print_colored("\n⚠️ WARNING: This will FACTORY RESET all selected modems. All settings will be lost.", 
                 COLOR_RED, bold=True)
    print_colored("This action CANNOT be undone!", COLOR_RED, bold=True)
    print_colored(f"You are about to reset {len(reachable_modems)} modems!", COLOR_RED, bold=True)
    
    try:
        confirm = input("\nType 'RESETALL' (all caps) to confirm reset of ALL modems: ").strip()
        if confirm != "RESETALL":
            print_colored("Reset cancelled. Incorrect confirmation.", COLOR_YELLOW)
            return
        
        # Double-check
        confirm2 = input(f"\nAre you ABSOLUTELY SURE you want to reset {len(reachable_modems)} modems? (y/n): ").strip().lower()
        if confirm2 != 'y':
            print_colored("Reset cancelled.", COLOR_YELLOW)
            return
        
        # Execute in bulk
        _bulk_execute(
            reachable_modems,
            lambda m: action_reset(m),
            "factory reset"
        )
        
        print_colored("\n⚠️ IMPORTANT: The modems will disconnect and restart automatically.", COLOR_YELLOW)
        print_colored("You will need to wait approximately 2 minutes for the modems", COLOR_YELLOW)
        print_colored("to complete the factory reset process before they become available again.", COLOR_YELLOW)
            
    except KeyboardInterrupt:
        print_colored("\nReset cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

def bulk_restart_modems(modems: List[Modem]):
    """Restart multiple modems with improved feedback and error handling."""
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print_colored("No reachable modems in this group to restart.", COLOR_RED)
        return
    
    print_colored("\n" + "="*70, COLOR_YELLOW, bold=True)
    print_colored(" BULK RESTART MODEMS ", COLOR_YELLOW, bold=True)
    print_colored("="*70, COLOR_YELLOW, bold=True)
    
    print_colored(f"Target: {len(reachable_modems)} reachable modems", COLOR_BOLD)
    carrier = modems[0].carrier or "Unknown"
    print_colored(f"Group: {carrier}", COLOR_BLUE)
    
    try:
        confirm = input(f"\nConfirm restart of {len(reachable_modems)} modems? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Restart cancelled.", COLOR_YELLOW)
            return
        
        # Execute in bulk using our completely rewritten action_restart function
        # that follows the exact working bash example
        print_colored("\nStarting modem restarts...", COLOR_YELLOW)
        print_colored("Each modem will take approximately 1-2 minutes to fully restart", COLOR_YELLOW)
        
        _bulk_execute(
            reachable_modems,
            action_restart,
            "restart"
        )
        
        print_colored(f"\n{COLOR_YELLOW}Note: Modems will take approximately 1-2 minutes to fully restart.{COLOR_RESET}")
        print_colored(f"{COLOR_YELLOW}You may need to refresh the modem status after this time to see updated information.{COLOR_RESET}")
            
    except KeyboardInterrupt:
        print_colored("\nRestart cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)
