import requests
from jsonschema import validate
from tests.utils import load_json


def test_get_user():
    url = "https://reqres.in/api"
    user_id = 9
    response = requests.get(f'{url}/users/{user_id}')
    assert response.status_code == 200
    assert response.json()['data']['email'] == 'tobias.funke@reqres.in'
    assert response.json()['data']['first_name'] == 'Tobias'
    assert response.json()['data']['last_name'] == 'Funke'
    validate(response.json(), load_json('get_user.json'))


def test_get_not_found_user():
    url = "https://reqres.in/api"
    user_id = 9999999
    response = requests.get(f'{url}/users/{user_id}')
    assert response.status_code == 404
    assert response.json() == {}
