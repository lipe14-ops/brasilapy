from dataclasses import dataclass


@dataclass(frozen=True)
class ApiResponseDTO:
    """API response model.

    Params:
        header <dictionary<string, any>>: http header.
        status <integer>:  response status code.
        content <dictionary<string, any>>: API response. 
    """
    
    headers: dict
    status: int
    content: dict
