import requests
from jsonschema import validate
from tests.utils import load_json


def test_update_user():
    url = "https://reqres.in/api/users"
    user_id = 2

    payload = {
        "name": "Dmitriy",
        "job": "Backend-developer"
    }

    response = requests.put(url + f'/{user_id}', data=payload)
    assert response.status_code == 200
    assert response.json()['name'] == 'Dmitriy'
    assert response.json()['job'] == 'Backend-developer'
    validate(response.json(), load_json('update_user.json'))
