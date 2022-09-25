import pytest
from unittest import mock
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

        with mock.patch('brasilapy.processor.RequestsProcessor.handler.get') as get_mock:
            requests_processor.get_data('/test')

        get_mock.assert_called_once()
        assert get_mock.call_args_list[0].args[0] == "https://brasilapi.com.br/api/test"
        assert get_mock.call_args_list[0].kwargs['params'] is None

    def test_get_data_with_params(self):
        requests_processor = RequestsProcessor()

        with mock.patch('brasilapy.processor.RequestsProcessor.handler.get') as get_mock:
            requests_processor.get_data(endpoint='/test_with_arguments', params={"name1": "value1", "name2": "value2"})

        get_mock.assert_called_once()
        assert get_mock.call_args_list[0].args[0] == "https://brasilapi.com.br/api/test_with_arguments"
        assert get_mock.call_args_list[0].kwargs['params'] == {"name1": "value1", "name2": "value2"}