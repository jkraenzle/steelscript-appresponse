import json

import pytest
import requests

from tests.settings import USERNAME, PASSWORD, AR_ENDPOINT, \
    WIREMOCK_SERVER, WIREMOCK_START_RECORDING, WIREMOCK_STOP_RECORDING, \
    WIREMOCK_SNAPSHOT, WIREMOCK_RESET
from steelscript.common.service import UserAuth
from steelscript.appresponse.core.appresponse import AppResponse

try:
    import steelscript.common.connection
except ImportError:
    raise ImportError("Cannot import steelscript connection dependency.")


@pytest.fixture(scope="module")
def user_auth():
    return UserAuth(USERNAME, PASSWORD)


@pytest.fixture()
def app(user_auth):
    # return AppResponse(WIREMOCK_SERVER, auth=user_auth)
    return AppResponse(AR_ENDPOINT, auth=user_auth)


def pytest_configure(config):
    steelscript.common.connection.Connection.REST_DEBUG = 2
    steelscript.common.connection.Connection.REST_BODY_LINES = 200
    # start_api = "%s/%s" % (WIREMOCK_SERVER, WIREMOCK_START_RECORDING)
    # reset_api = "%s/%s" % (WIREMOCK_SERVER, WIREMOCK_RESET)
    # reset = requests.delete(reset_api)
    # req = requests.post(start_api, data=json.dumps(
    #     {'targetBaseUrl': AR_ENDPOINT}))
    # print("Started WireMock Recording for ARX. Response from server: %s" %
    #       req.content)


# def pytest_unconfigure(config):
#     stop_api = "%s/%s" % (WIREMOCK_SERVER, WIREMOCK_STOP_RECORDING)
#     snapshot_api = "%s/%s" % (WIREMOCK_SERVER, WIREMOCK_SNAPSHOT)
#     req = requests.post(stop_api, data=json.dumps(
#         {'targetBaseUrl': AR_ENDPOINT}))
#     print("Stopped WireMock Recording for ARX. Response from server: %s" %
#           req.content)
#     snap = requests.post(snapshot_api)
#     print("Created snapshot. Response was: %s" % snap.content)
