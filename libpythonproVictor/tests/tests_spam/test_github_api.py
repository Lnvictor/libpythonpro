from pytest_mock import mocker

from libpythonproVictor import github_api
from unittest.mock import Mock
import pytest


@pytest.fixture(mocker)
def avatar_url():
    resp_url = Mock()
    resp_url.json.return_value = {"login": "Lnvictor",
                                  "id": 51089294,
                                  "node_id": "MDQ6VXNlcjUxMDg5Mjk0",
                                  "avatar_url": "https://avatars2.githubusercontent.com/u/51089294?v=4"}

    get_mock = mocker.patch('libpythonproVictor.github_api.buscar_avatar')
    get_mock.return_value = resp_url
    return github_api


def test_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('Lnvictor')
    assert 'https://avatars2.githubusercontent.com/u/51089294?v=4'== url


def test_buscar_avatar_integracao():
    url = github_api.buscar_avatar('Lnvictor')
    assert 'https://avatars2.githubusercontent.com/u/51089294?v=4'== url
