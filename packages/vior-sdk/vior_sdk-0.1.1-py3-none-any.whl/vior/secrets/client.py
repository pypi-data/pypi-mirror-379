import subprocess
import requests
import json
import time
from .exceptions import AuthenticationError, ConfigurationError, SecretNotFoundError, APIError

class SecretsClient:
    def __init__(self, max_retries=2, retry_delay=1):
        self.config = None
        self.access_key = None
        self.private_key = None
        self.server_url = None
        self.max_retries = max_retries
        self.retry_delay = retry_delay
        
        self._load_config()
        self._test_api_access()
    
    def _load_config(self):
        try:
            result = subprocess.run(
                ['vior', 'sdk-need-auth'], 
                capture_output=True, 
                text=True,
                timeout=10
            )
            
            if result.returncode != 0:
                error_msg = result.stdout.strip()
                if "No configuration found" in error_msg:
                    raise AuthenticationError("Configuration not found")
                # Don't expose internal CLI errors
                raise AuthenticationError("Configuration error")
            
            try:
                self.config = json.loads(result.stdout.strip())
                self.access_key = self.config.get('access_key')
                self.private_key = self.config.get('private_key')
                self.server_url = self.config.get('server_url')
                
                if not all([self.access_key, self.private_key, self.server_url]):
                    raise AuthenticationError("Invalid configuration format")
                    
            except (json.JSONDecodeError, KeyError):
                raise AuthenticationError("Invalid configuration format")
            
        except subprocess.TimeoutExpired:
            raise ConfigurationError("CLI not responding")
        except FileNotFoundError:
            raise ConfigurationError("Vior CLI not found")
        except (AuthenticationError, ConfigurationError):
            raise
        except Exception:
            # Don't expose internal exceptions
            raise ConfigurationError("Configuration error")
    
    def _test_api_access(self):
        """Test API access with retry logic for transient failures"""
        for attempt in range(self.max_retries + 1):
            try:
                headers = {
                    "X-Access-Key": self.access_key,
                    "X-Private-Key": self.private_key,
                    "Content-Type": "application/json"
                }
                
                response = requests.get(
                    f"{self.server_url}/auth/validate-api-keys",
                    headers=headers,
                    timeout=10
                )
                
                if response.status_code == 200:
                    try:
                        result = response.json()
                        if not result.get('valid'):
                            raise AuthenticationError("Invalid API credentials")
                        return  # Success
                    except (json.JSONDecodeError, KeyError):
                        raise AuthenticationError("Invalid server response")
                
                elif response.status_code == 401:
                    raise AuthenticationError("Invalid API credentials")
                elif response.status_code == 403:
                    raise AuthenticationError("Access denied")
                elif response.status_code == 500 and attempt < self.max_retries:
                    # Retry transient server errors
                    time.sleep(self.retry_delay)
                    continue
                else:
                    raise APIError("Service temporarily unavailable")
                    
            except requests.exceptions.ConnectionError:
                if attempt < self.max_retries:
                    time.sleep(self.retry_delay)
                    continue
                raise APIError("Unable to connect to service")
            except requests.exceptions.Timeout:
                if attempt < self.max_retries:
                    time.sleep(self.retry_delay)
                    continue
                raise APIError("Request timeout")
            except (AuthenticationError, APIError):
                raise
            except Exception:
                # Don't expose internal request exceptions
                if attempt < self.max_retries:
                    time.sleep(self.retry_delay)
                    continue
                raise APIError("Service error")
    
    def get_secret(self, secret_name, format="dict"):
        """
        Retrieve a secret by name
        
        Args:
            secret_name (str): Name of the secret to retrieve
            format (str): Output format - "dict", "json", "env", or "raw"
        
        Returns:
            Secret data in the specified format
        """
        if not secret_name or not isinstance(secret_name, str):
            raise ValueError("Secret name must be a non-empty string")
            
        if format not in ["dict", "json", "env", "raw"]:
            raise ValueError("Format must be one of: dict, json, env, raw")
        
        for attempt in range(self.max_retries + 1):
            try:
                headers = {
                    "X-Access-Key": self.access_key,
                    "X-Private-Key": self.private_key,
                    "Content-Type": "application/json"
                }
                
                response = requests.get(
                    f"{self.server_url}/secrets/view-sdk/{secret_name}",
                    headers=headers,
                    timeout=10
                )
                
                if response.status_code == 200:
                    try:
                        secret_data = response.json()
                        entries = secret_data.get('entries', {})
                        return self._format_secret_data(entries, format)
                    except (json.JSONDecodeError, KeyError):
                        raise APIError("Invalid server response")
                        
                elif response.status_code == 404:
                    raise SecretNotFoundError(secret_name)
                elif response.status_code == 401:
                    raise AuthenticationError("Invalid API credentials")
                elif response.status_code == 403:
                    raise AuthenticationError("Access denied")
                elif response.status_code == 500 and attempt < self.max_retries:
                    time.sleep(self.retry_delay)
                    continue
                else:
                    raise APIError("Failed to retrieve secret")
                    
            except requests.exceptions.ConnectionError:
                if attempt < self.max_retries:
                    time.sleep(self.retry_delay)
                    continue
                raise APIError("Unable to connect to service")
            except requests.exceptions.Timeout:
                if attempt < self.max_retries:
                    time.sleep(self.retry_delay)
                    continue
                raise APIError("Request timeout")
            except (SecretNotFoundError, AuthenticationError, APIError, ValueError):
                raise
            except Exception:
                if attempt < self.max_retries:
                    time.sleep(self.retry_delay)
                    continue
                raise APIError("Service error")
    
    def _format_secret_data(self, entries, format):
        """Format secret data according to requested format"""
        try:
            if format == "dict":
                return entries
            elif format == "json":
                return json.dumps(entries, indent=2)
            elif format == "env":
                return "\n".join([f"{key}={value}" for key, value in entries.items()])
            elif format == "raw":
                if len(entries) == 1:
                    return list(entries.values())[0]
                else:
                    return entries
        except Exception:
            raise APIError("Failed to format secret data")
    
    def verify_connection(self):
        """Verify connection to the API service"""
        try:
            self._test_api_access()
            return {
                "status": "authenticated", 
                "message": "Successfully connected to Vior Secrets",
                "server": self.server_url
            }
        except Exception as e:
            return {
                "status": "error", 
                "message": str(e)
            }
    
    def get_status(self):
        """Get current authentication status"""
        try:
            self._test_api_access()
            return f"Connected to {self.server_url}"
        except Exception as e:
            return f"Not connected: {str(e)}"