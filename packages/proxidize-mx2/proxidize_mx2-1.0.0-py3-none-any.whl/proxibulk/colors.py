# Color constants for professional branding
COLOR_YELLOW = "\033[93m"    # Brand primary
COLOR_PURPLE = "\033[95m"    # Brand secondary
COLOR_GREEN = "\033[92m"     # Success/safe operations
COLOR_RED = "\033[91m"       # Errors/dangerous operations  
COLOR_ORANGE = "\033[38;5;208m"  # Warnings
COLOR_BLUE = "\033[94m"      # General information
COLOR_RESET = "\033[0m"
COLOR_BOLD = "\033[1m"

# Cross-platform Unicode symbols with ASCII fallbacks
def get_unicode_symbol(symbol_type: str) -> str:
    """Get Unicode symbols with ASCII fallbacks for Windows compatibility."""
    import sys
    import os
    
    symbols = {
        'success': ('✓', 'OK'),
        'error': ('✗', 'X'),
        'filled_block': ('█', '#'),
        'empty_block': ('░', '-'),
        'medium_block': ('▒', '='),
        'dark_block': ('▓', '*')
    }
    
    unicode_char, ascii_fallback = symbols.get(symbol_type, ('?', '?'))
    
    # Check if we can safely use Unicode
    try:
        # Test if the symbol can be encoded with the current encoding
        unicode_char.encode(sys.stdout.encoding or 'ascii')
        return unicode_char
    except (UnicodeEncodeError, AttributeError):
        return ascii_fallback

def print_colored(text: str, color: str = "", bold: bool = False) -> None:
    """Print text with brand-appropriate colors and Windows support."""
    import os
    if os.name == 'nt':  # Windows handling
        try:
            import colorama
            colorama.init()
        except ImportError:
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
