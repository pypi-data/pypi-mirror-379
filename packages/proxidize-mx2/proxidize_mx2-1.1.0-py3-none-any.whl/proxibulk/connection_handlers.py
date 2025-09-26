from typing import List
from .modem import Modem
from .actions import action_connect, action_disconnect, action_soft_restart
from .colors import COLOR_RED, COLOR_GREEN, COLOR_BLUE, COLOR_YELLOW, COLOR_BOLD, COLOR_RESET, print_colored

def connect_modem(modem: Modem):
    """Connect data on a single modem."""
    if not modem.reachable:
        print_colored("Cannot connect: Modem is unreachable.", COLOR_RED)
        return
    
    print_colored("\n" + "="*70, COLOR_GREEN, bold=True)
    print_colored(" CONNECT MODEM ", COLOR_GREEN, bold=True)
    print_colored("="*70, COLOR_GREEN, bold=True)
    
    print_colored(f"Modem: [{modem.index}] {modem.raw}", COLOR_BOLD)
    print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
    
    try:
        confirm = input("\nConnect data on this modem? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Connect operation cancelled.", COLOR_YELLOW)
            return
        
        print_colored("\nSending connect command to modem...", COLOR_YELLOW)
        
        ok, msg = action_connect(modem)
        
        if ok:
            print_colored(f"Connect command successful: {msg}", COLOR_GREEN)
            print_colored("Modem should be connected shortly", COLOR_GREEN)
        else:
            print_colored(f"Connect command failed: {msg}", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

def disconnect_modem(modem: Modem):
    """Disconnect data on a single modem."""
    if not modem.reachable:
        print_colored("Cannot disconnect: Modem is unreachable.", COLOR_RED)
        return
    
    print_colored("\n" + "="*70, COLOR_RED, bold=True)
    print_colored(" DISCONNECT MODEM ", COLOR_RED, bold=True)
    print_colored("="*70, COLOR_RED, bold=True)
    
    print_colored(f"Modem: [{modem.index}] {modem.raw}", COLOR_BOLD)
    print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
    
    try:
        confirm = input("\nDisconnect data on this modem? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Disconnect operation cancelled.", COLOR_YELLOW)
            return
        
        print_colored("\nSending disconnect command to modem...", COLOR_YELLOW)
        
        ok, msg = action_disconnect(modem)
        
        if ok:
            print_colored(f"Disconnect command successful: {msg}", COLOR_GREEN)
        else:
            print_colored(f"Disconnect command failed: {msg}", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)

def soft_restart_modem(modem: Modem):
    """Perform a soft restart (disconnect + wait + connect) on a single modem."""
    if not modem.reachable:
        print_colored("Cannot perform soft restart: Modem is unreachable.", COLOR_RED)
        return
    
    print_colored("\n" + "="*70, COLOR_YELLOW, bold=True)
    print_colored(" SOFT RESTART MODEM ", COLOR_YELLOW, bold=True)
    print_colored("="*70, COLOR_YELLOW, bold=True)
    
    print_colored(f"Modem: [{modem.index}] {modem.raw}", COLOR_BOLD)
    print_colored(f"Carrier: {modem.carrier or 'Unknown'}", COLOR_BLUE)
    
    try:
        print_colored("\nSoft restart will:", COLOR_BOLD)
        print_colored("  1. Disconnect data connection", COLOR_BLUE)
        print_colored("  2. Wait 10 seconds", COLOR_BLUE)
        print_colored("  3. Reconnect data connection", COLOR_BLUE)
        print_colored("\nThis is useful for refreshing the connection without rebooting the modem.", COLOR_BLUE)
        
        confirm = input("\nPerform soft restart on this modem? (y/n): ").strip().lower()
        if confirm != 'y':
            print_colored("Soft restart cancelled.", COLOR_YELLOW)
            return
        
        print_colored("\nInitiating soft restart sequence...", COLOR_YELLOW)
        
        ok, msg = action_soft_restart(modem)
        
        if ok:
            print_colored(f"Soft restart successful: {msg}", COLOR_GREEN)
        else:
            print_colored(f"Soft restart failed: {msg}", COLOR_RED)
            
    except KeyboardInterrupt:
        print_colored("\nOperation cancelled.", COLOR_YELLOW)
    except Exception as e:
        print_colored(f"An error occurred: {e}", COLOR_RED)
