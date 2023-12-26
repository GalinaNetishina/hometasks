import os
import requests

import pytest
from dotenv import load_dotenv

from src.enums.errors import ErrorMessages


load_dotenv()
token = os.getenv('TOKEN')

headers = {
        "Authorization": "OAuth " + token
    }
base_url = "https://cloud-api.yandex.net/v1/disk/resources/"
names = ["folder1",
        "folder2",
        "folder3"]
invalid_names = ["path/folder", "///"]


def create_folder(folder_name) -> requests.Response:
    params = {"path": folder_name, }
    resp = requests.put(base_url, headers=headers, params=params)
    return resp


class Test_api:
    @pytest.mark.parametrize("name", names)
    def test_response_code(self, name):
        resp = create_folder(name)
        assert resp.status_code == 201, ErrorMessages.WRONG_STATUS_CODE.value

    @pytest.mark.parametrize("name", names)
    def test_existed_folders(self, name):
        resp = create_folder(name)
        assert resp.status_code == 409, ErrorMessages.WRONG_STATUS_CODE.value

    @pytest.mark.parametrize("name", invalid_names)
    @pytest.mark.xfail
    def test_incorrect_name(self, name):
        resp = create_folder(name)
        assert resp.status_code == 201

    @pytest.mark.parametrize("name", names)
    def test_clear(self, name):
        requests.delete(base_url, headers=headers, params={"path": name})
