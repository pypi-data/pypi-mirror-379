import sys

class Colors:
    RED = '\033[91m'
    YELLOW = '\033[93m'
    CYAN = '\033[96m'
    BLUE = '\033[94m'
    RESET = '\033[0m'

class ViorSecretsError(Exception):
    """Base exception for Vior Secrets SDK"""
    pass

class AuthenticationError(ViorSecretsError):
    """Raised when authentication fails"""
    def __init__(self, message="Authentication failed"):
        super().__init__(message)
        
        if "Configuration not found" in message:
            print(f"\n{Colors.RED}Error:{Colors.RESET} No configuration found.")
            print(f"{Colors.YELLOW}Solution:{Colors.RESET} Run: {Colors.BLUE}vior configure{Colors.RESET}")
            print(f"{Colors.CYAN}Help:{Colors.RESET} Visit {Colors.BLUE}https://secrets.viorcloud.com/docs{Colors.RESET}")
            print()
            sys.exit(1)
        elif "Invalid API credentials" in message:
            print(f"\n{Colors.RED}Error:{Colors.RESET} Invalid credentials.")
            print(f"{Colors.YELLOW}Solution:{Colors.RESET} Check your API keys and run: {Colors.BLUE}vior configure{Colors.RESET}")
            print()
            sys.exit(1)
        elif "Access denied" in message:
            print(f"\n{Colors.RED}Error:{Colors.RESET} Access denied.")
            print(f"{Colors.YELLOW}Solution:{Colors.RESET} Check your account permissions.")
            print()
            sys.exit(1)

class ConfigurationError(ViorSecretsError):
    """Raised when there are configuration issues"""
    def __init__(self, message="Configuration error"):
        super().__init__(message)
        
        if "Vior CLI not found" in message:
            print(f"\n{Colors.RED}Error:{Colors.RESET} Vior CLI not installed.")
            print(f"{Colors.YELLOW}Solution:{Colors.RESET} Install with: {Colors.BLUE}pip install vior-cli{Colors.RESET}")
            print(f"{Colors.CYAN}Help:{Colors.RESET} Visit {Colors.BLUE}https://secrets.viorcloud.com/docs{Colors.RESET}")
            print()
            sys.exit(1)
        elif "CLI not responding" in message:
            print(f"\n{Colors.RED}Error:{Colors.RESET} CLI not responding.")
            print(f"{Colors.YELLOW}Solution:{Colors.RESET} Check your CLI installation and try again.")
            print()
            sys.exit(1)

class SecretNotFoundError(ViorSecretsError):
    """Raised when a requested secret is not found"""
    def __init__(self, secret_name):
        super().__init__(f"Secret '{secret_name}' not found")
        print(f"\n{Colors.RED}Error:{Colors.RESET} Secret '{secret_name}' not found.")
        print(f"{Colors.YELLOW}Solution:{Colors.RESET} Create the secret at {Colors.BLUE}https://secrets.viorcloud.com{Colors.RESET}")
        print()
        sys.exit(1)

class APIError(ViorSecretsError):
    """Raised when API requests fail"""
    def __init__(self, message="API error"):
        super().__init__(message)
        
        if "Unable to connect" in message:
            print(f"\n{Colors.RED}Error:{Colors.RESET} Cannot connect to Vior Secrets service.")
            print(f"{Colors.YELLOW}Solution:{Colors.RESET} Check your internet connection and try again.")
            print()
            sys.exit(1)
        elif "Request timeout" in message:
            print(f"\n{Colors.RED}Error:{Colors.RESET} Request timed out.")
            print(f"{Colors.YELLOW}Solution:{Colors.RESET} Check your connection and try again.")
            print()
            sys.exit(1)
        elif "Service temporarily unavailable" in message:
            print(f"\n{Colors.RED}Error:{Colors.RESET} Service temporarily unavailable.")
            print(f"{Colors.YELLOW}Solution:{Colors.RESET} Please try again in a few moments.")
            print()
            sys.exit(1)