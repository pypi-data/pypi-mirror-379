class APIError(Exception):
    """Base 3CX API exception, all specific exceptions inherit from it."""
    pass


class InvalidResponse(APIError):
    """Raised when api response is not valid json or request failed"""


