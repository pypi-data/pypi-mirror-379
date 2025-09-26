"""Entry point for Proxidize MX2 Manager CLI."""
import os
import sys
from .cli import (
    prompt_multiline_input, probe_all, print_basic_summary, print_banner,
    interactive_menu, print_colored, parse_command_line_args,
    COLOR_BLUE, COLOR_RED, COLOR_GREEN, COLOR_BOLD, COLOR_YELLOW
)
from .utils import parse_proxy_line
from .modem import Modem

def main():
    """Main entry point for the Proxidize MX2 Manager tool."""
    try:
        # Initialize colorama on Windows if available
        if os.name == 'nt':
            try:
                import colorama
                colorama.init()
            except ImportError:
                pass
        
        # Parse command line arguments
        args = parse_command_line_args()
        
        # Display the fancy banner
        print_banner()
        
        print("\nWelcome to Proxidize MX2 Manager!")
        print("This tool helps you manage multiple JRD/TCL MX2 family modems via their HTTP proxies.")
        
        # Get proxy input
        lines = prompt_multiline_input("Paste proxies (one per line) and finish with an empty line:")
        if not lines:
            print("No proxies provided. Exiting.")
            return
        
        # Parse proxies while maintaining index order
        proxies = []
        for i, line in enumerate(lines, start=1):
            parsed = parse_proxy_line(line)
            if not parsed:
                print(f"[Line {i}] Invalid format -> '{line}' (expected host:port:username:password). Skipping.")
                continue
            host, port, user, pwd = parsed
            p = Modem(index=i, raw=line.strip(), host=host, port=port, user=user, pwd=pwd)
            proxies.append(p)
        
        if not proxies:
            print("No valid proxies parsed. Exiting.")
            return
        
        # Probe all modems with ultra-fast mode only for basic reachability check
        # We specifically do NOT gather carrier info at this stage
        print("\nPerforming initial probe to check modem connectivity...")
        print("This will check if modems are reachable but won't gather detailed information yet.")
        
        probed = probe_all(proxies, get_carrier_info=False)  # Explicitly disable carrier info gathering
        
        # Ensure consistent ordering by input index
        probed_sorted = sorted(probed, key=lambda m: m.index)
        
        # Show a basic summary without carrier groups
        print_basic_summary(probed_sorted)
        
        # Start interactive menu
        interactive_menu(probed_sorted)
        
        print("\nThank you for using Proxidize MX2 Manager!")
        
    except KeyboardInterrupt:
        print("\n\nOperation cancelled by user. Exiting.")
        sys.exit(1)
    except Exception as e:
        print(f"\nAn unexpected error occurred: {str(e)}")
        sys.exit(1)

if __name__ == "__main__":
    main()