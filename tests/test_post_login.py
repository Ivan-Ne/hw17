import requests
from jsonschema import validate
from tests.utils import load_json


def test_login_successful():
    url = "https://reqres.in/api/login"

    payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    response = requests.post(url, data=payload)
    assert response.status_code == 200
    assert response.json()['token'] == 'QpwL5tke4Pnpja7X4'
    validate(response.json(), load_json('login_successful.json'))


def test_login_unsuccessful():
    url = "https://reqres.in/api/login"

    payload = {
        "email": "test@mail.ru"
    }

    response = requests.post(url, data=payload)
    assert response.status_code == 400
    validate(response.json(), load_json('login_unsuccessful.json'))
