from abc import ABC, abstractmethod

import requests
from requests import Session as RequestSession

from brasilapy.exceptions import ProcessorException


class ClientProcessor(ABC):

    handler: any
    base_url: str

    @abstractmethod
    def get_data(
        self,
        endpoint: str,
        queryset_params: dict[str, str] | list[dict[str, str]] | None = None,
    ) -> dict:
        raise NotImplementedError("A get_data method must be created")


class RequestsProcessor(ClientProcessor):

    handler: RequestSession = RequestSession()
    base_url = "https://brasilapi.com.br/api"

    def get_data(self, endpoint: str, params: dict | None = None) -> dict:
        response: requests.Response = self.handler.get(
            f"{self.base_url}{endpoint}", params=params
        )

        if response.status_code == 200:
            return response.json()
        else:
            raise ProcessorException(
                status_code=response.status_code, response_text=response.text
            )
