import requests
import re
from brasilapy.src.dtos import ApiResponseDTO
from brasilapy.src.interfaces import IApiRoute
from brasilapy.src.errors  import ParameterError
from brasilapy.src.adapters import StringFormatter


class ApiRouteGet(IApiRoute):
    """API route GET requester method."""

    def __init__(self, name: str, url: str) -> None:
        """
        Params:
            name <string>: route name. 
            url: <string>: request url endpoint.
        """
        
        self.name = name
        self.url = url
 
    def request(self, parameter_value: str = None, query: dict[str, str] = {}) -> ApiResponseDTO:
        """makes a get request.

        Params:
            parameter_value <string>: request path parameter value.
            query: <dictionary<string, string>>: http query parameters.
  
        Exceptions:
            TypeError: throws when "parameter_name" is not a instance of string type.
            ParameterError: throws when the parameter is invalid (when it exists or not).

        Returns <ApiResponseDTO>:
            response model.
        """

        request_url = self.url
        parameter_name = None
            
        if parameters_list := re.findall("[{][a-zA-Z]{1,}[}]", self.url):
            parameter_name = StringFormatter.handler(parameters_list.pop(), ['{', '}'])

        if parameters_list and parameter_value:
            raise ParameterError('request there are no parameters.')

        if parameter_name:
            if not isinstance(parameter_value, str):
                raise TypeError(f'parameter "{parameter_name}" must be a string.')

            if not parameter_value:
                raise ParameterError(f'parameter "{parameter_name}" is required.')
            
            request_url = self.url.format_map({ parameter_name: parameter_value })

        requester = requests.get(request_url, params=query)
        
        return ApiResponseDTO(
            headers=requester.headers,
            status=requester.status_code, 
            content=requester.json()
        )
        