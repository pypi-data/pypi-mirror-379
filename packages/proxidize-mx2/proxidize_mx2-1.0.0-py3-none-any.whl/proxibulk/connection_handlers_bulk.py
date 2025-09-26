from typing import List, Tuple
import time
import concurrent.futures

from .modem import Modem
from .actions import action_connect, action_disconnect, action_soft_restart
from .colors import COLOR_RED, COLOR_GREEN, COLOR_BLUE, COLOR_YELLOW, COLOR_PURPLE, COLOR_ORANGE, COLOR_BOLD, COLOR_RESET, print_colored

def print_header(subtitle=""):
    """Print consistent branded header across all screens."""
    import os
    os.system('cls' if os.name == 'nt' else 'clear')
    
    try:
        from pyfiglet import Figlet
        figlet = Figlet(font='doom')
        title = figlet.renderText('Proxidize ')
        
        print_colored(title, COLOR_YELLOW)
        print_colored("----------------------------------------------------------", COLOR_YELLOW)
        print_colored("MX2 Manager " + "A multi-threaded MX2 manager tool", COLOR_RESET)
        print_colored("----------------------------------------------------------", COLOR_YELLOW)
        
        if subtitle:
            print_colored(f"Current Section: {subtitle}", COLOR_PURPLE, bold=True)
            print_colored("="*70, COLOR_PURPLE)
    except Exception as e:
        # Fallback if figlet fails
        print_colored("\n" + "="*70, COLOR_YELLOW, bold=True)
        print_colored(" PROXIDIZE: MX2 MANAGER ", COLOR_YELLOW, bold=True)
        print_colored("="*70, COLOR_YELLOW, bold=True)
        print_colored("A multi-threaded MX2 manager tool", COLOR_RESET)
        
        if subtitle:
            print_colored(f"Current Section: {subtitle}", COLOR_PURPLE, bold=True)
            print_colored("="*70, COLOR_PURPLE)

def bulk_connect_modems(modems: List[Modem]):
    """Connect data on all modems in the group."""
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print("No reachable modems in this group to connect.")
        return
    
    print_header("QUICK CONNECT ALL MODEMS")
    
    print_colored(f"Target: {len(reachable_modems)} reachable modems", COLOR_BLUE)
    carrier = modems[0].carrier or "Unknown"
    print_colored(f"Group: {carrier}", COLOR_PURPLE)
    
    try:
        confirm = input(f"\nConfirm connect ALL modems? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("\nOperation cancelled.", COLOR_ORANGE)
            return
        
        print_colored(f"\nExecuting connect operations on {len(reachable_modems)} modems with {min(len(reachable_modems), 5)} workers...", COLOR_BLUE)
        
        # Use our bulk execution helper
        _bulk_execute(reachable_modems, action_connect, "connect")
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_ORANGE)
        
def bulk_disconnect_modems(modems: List[Modem]):
    """Disconnect data on all modems in the group."""
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print("No reachable modems in this group to disconnect.")
        return
    
    print_header("QUICK DISCONNECT ALL MODEMS")
    
    print_colored(f"Target: {len(reachable_modems)} reachable modems", COLOR_BLUE)
    carrier = modems[0].carrier or "Unknown"
    print_colored(f"Group: {carrier}", COLOR_PURPLE)
    
    try:
        confirm = input(f"\nConfirm disconnect ALL modems? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("\nOperation cancelled.", COLOR_ORANGE)
            return
        
        print_colored(f"\nExecuting disconnect operations on {len(reachable_modems)} modems with {min(len(reachable_modems), 5)} workers...", COLOR_BLUE)
        
        # Use our bulk execution helper
        _bulk_execute(reachable_modems, action_disconnect, "disconnect")
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_ORANGE)
        
def bulk_soft_restart_modems(modems: List[Modem]):
    """Perform soft restart (disconnect + wait + connect) on all modems in the group."""
    reachable_modems = [m for m in modems if m.reachable]
    
    if not reachable_modems:
        print("No reachable modems in this group to soft restart.")
        return
    
    print_header("SOFT RESTART ALL MODEMS")
    
    print_colored(f"Target: {len(reachable_modems)} reachable modems", COLOR_BLUE)
    carrier = modems[0].carrier or "Unknown"
    print_colored(f"Group: {carrier}", COLOR_PURPLE)
    
    try:
        print_colored("\nThis will disconnect all modems, wait 10 seconds, then reconnect them.", COLOR_ORANGE)
        confirm = input(f"\nConfirm soft restart of ALL modems? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("\nOperation cancelled.", COLOR_ORANGE)
            return
        
        print_colored(f"\nExecuting soft restart operations on {len(reachable_modems)} modems with {min(len(reachable_modems), 5)} workers...", COLOR_BLUE)
        
        # Use our bulk execution helper
        _bulk_execute(reachable_modems, action_soft_restart, "soft restart")
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_ORANGE)

def _bulk_execute(modems: List[Modem], action_func, action_name: str):
    """Execute an action on multiple modems with parallel workers and proper progress tracking."""
    start_time = time.time()
    results = []
    
    # Determine number of workers - don't use more workers than modems
    # but cap at 5 to avoid overwhelming the system or proxy server
    max_workers = min(len(modems), 5)
    
    # Execute operations in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        # Start the operations and mark each future with its modem
        future_to_modem = {executor.submit(action_func, modem): modem for modem in modems}
        
        # Process results as they complete
        for i, future in enumerate(concurrent.futures.as_completed(future_to_modem), 1):
            modem = future_to_modem[future]
            try:
                success, message = future.result()
                
                if success:
                    status = "SUCCESS"
                else:
                    status = "FAILED"
                
                print(f"[{i}/{len(modems)}] [{modem.index}] {modem.raw} -> {status}: {message}")
                
                results.append({
                    "modem": modem,
                    "success": success,
                    "message": message
                })
                
            except Exception as e:
                print(f"[{i}/{len(modems)}] [{modem.index}] {modem.raw} -> ERROR: {str(e)}")
                results.append({
                    "modem": modem,
                    "success": False,
                    "message": f"Exception: {str(e)}"
                })
    
    # Summary
    end_time = time.time()
    successful = sum(1 for r in results if r["success"])
    failed = len(results) - successful
    
    print("\nOperation Summary:")
    print(f"  - Total modems: {len(results)}")
    print(f"  - Successful: {successful}")
    if failed > 0:
        print(f"  - Failed: {failed}")
    print(f"  - Time taken: {end_time - start_time:.2f} seconds")
    
    return results
