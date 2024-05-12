import requests
from jsonschema import validate
from tests.utils import load_json


def test_create_user():
    url = "https://reqres.in/api"
    endpoint = '/users'

    payload = {
        "name": "Ivan",
        "job": "QA-engineer"
    }

    response = requests.post(url + endpoint, data=payload)
    assert response.status_code == 201
    assert response.json()['name'] == 'Ivan'
    assert response.json()['job'] == 'QA-engineer'
    validate(response.json(), load_json('create_user.json'))
