from requests import Session as RequestSession
from abc import ABC


class ClientProcessor(ABC):

    handler: any
    base_url: str

    def __init__(self):
        if not self.handler or not self.base_url:
            raise NotImplementedError("You must setup class accordingly")

    def _get_data(self, endpoint: str, queryset_params: dict[str, str] | None = None) -> dict:
        raise NotImplementedError("Please define a _get_data method")


class RequestsProcessor(ClientProcessor):

    handler: RequestSession = RequestSession()
    base_url = "https://brasilapi.com.br/api"

    def get_data(self, endpoint: str, params: dict | None = None) -> dict:
        return self.handler.get(f"{self.base_url}{endpoint}", params=params).json()
