from unittest import mock

import pytest

from brasilapy.exceptions import ProcessorException
from brasilapy.processor import ClientProcessor, RequestsProcessor


@pytest.fixture
def client_processor_usable_class():
    class ClientProcessorUsable(ClientProcessor):
        handler = None
        base_url = "http://testapi.local"

        def get_data(self, *args, **kwargs) -> dict:
            return super().get_data(*args, **kwargs)

    return ClientProcessorUsable


class TestAbstractClientProcessor:
    def test_client_processor(self, client_processor_usable_class):
        with pytest.raises(NotImplementedError) as exc:
            client_processor_usable_class().get_data(endpoint="/test")

        assert "A get_data method must be created" in str(exc)


class TestRequestsProcessor:
    def test_get_data(self):
        requests_processor = RequestsProcessor()

        with mock.patch(
            "brasilapy.processor.RequestsProcessor.handler"
        ) as handler_mock:
            response_mock = mock.Mock()
            response_mock.status_code = 200
            response_mock.json.return_value = {"response": "ok"}

            handler_mock.get.return_value = response_mock

            requests_processor.get_data("/test")

        assert (
            handler_mock.method_calls[0].args[0] == "https://brasilapi.com.br/api/test"
        )
        assert handler_mock.method_calls[0].kwargs["params"] is None

    def test_get_data_with_params(self):
        requests_processor = RequestsProcessor()

        with mock.patch(
            "brasilapy.processor.RequestsProcessor.handler"
        ) as handler_mock:
            response_mock = mock.Mock()
            response_mock.status_code = 200
            response_mock.json.return_value = {"response": "ok"}

            handler_mock.get.return_value = response_mock

            requests_processor.get_data(
                endpoint="/test_with_arguments",
                params={"name1": "value1", "name2": "value2"},
            )

        assert (
            handler_mock.method_calls[0].args[0]
            == "https://brasilapi.com.br/api/test_with_arguments"
        )
        assert handler_mock.method_calls[0].kwargs["params"] == {
            "name1": "value1",
            "name2": "value2",
        }

    def test_get_data_with_error(self):
        requests_processor = RequestsProcessor()

        with mock.patch(
            "brasilapy.processor.RequestsProcessor.handler"
        ) as handler_mock, pytest.raises(ProcessorException) as exc:
            response_mock = mock.Mock()
            response_mock.status_code = 500
            response_mock.text = "NOT_OK_ERROR_MESSAGE_AS_TEXT"

            handler_mock.get.return_value = response_mock

            requests_processor.get_data("/test")

        assert "STATUS_CODE: 500 - NOT_OK_ERROR_MESSAGE_AS_TEXT" in str(exc.value)

        assert (
            handler_mock.method_calls[0].args[0] == "https://brasilapi.com.br/api/test"
        )
        assert handler_mock.method_calls[0].kwargs["params"] is None
