from abc import ABC, abstractmethod

from requests import Session as RequestSession


class ClientProcessor(ABC):

    handler: any
    base_url: str

    @abstractmethod
    def get_data(
        self, endpoint: str, queryset_params: dict[str, str] | None = None
    ) -> dict:
        raise NotImplementedError("Please define a _get_data method")


class RequestsProcessor(ClientProcessor):

    handler: RequestSession = RequestSession()
    base_url = "https://brasilapi.com.br/api"

    def get_data(self, endpoint: str, params: dict | None = None) -> dict:
        return self.handler.get(f"{self.base_url}{endpoint}", params=params).json()
