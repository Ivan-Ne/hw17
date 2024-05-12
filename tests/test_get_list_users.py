import requests


def test_get_list_users():
    url = "https://reqres.in/api"
    page_id = 0
    response = requests.get(f'{url}/users?page={page_id}')
    assert response.status_code == 200
