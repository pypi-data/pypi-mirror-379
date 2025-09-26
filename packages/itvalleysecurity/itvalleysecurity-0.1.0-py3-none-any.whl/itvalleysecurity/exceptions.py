class InvalidToken(Exception): 
    """Exception raised when a JWT token is invalid."""
    pass

class ConfigError(Exception): 
    """Exception raised for configuration errors."""
    pass
