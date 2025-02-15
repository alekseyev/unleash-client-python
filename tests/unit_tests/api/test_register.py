import responses
from pytest import mark, param
from requests import ConnectionError
from UnleashClient.constants import REGISTER_URL
from UnleashClient.api import register_client
from tests.utilities.testing_constants import URL, APP_NAME, INSTANCE_ID, METRICS_INTERVAL, CUSTOM_HEADERS, CUSTOM_OPTIONS, DEFAULT_STRATEGY_MAPPING


FULL_REGISTER_URL = URL + REGISTER_URL


@responses.activate
@mark.parametrize("payload,status,expected", (
    param({"json": {}}, 202, True, id="success"),
    param({"json": {}}, 500, False, id="failure"),
    param({"body": ConnectionError("Test connection error")}, 200, False, id="exception"),
))
def test_register_client(payload, status, expected):
    responses.add(responses.POST, FULL_REGISTER_URL, status=status, **payload)

    result = register_client(URL,
                             APP_NAME,
                             INSTANCE_ID,
                             METRICS_INTERVAL,
                             CUSTOM_HEADERS,
                             CUSTOM_OPTIONS,
                             DEFAULT_STRATEGY_MAPPING)

    assert len(responses.calls) == 1
    assert result is expected
