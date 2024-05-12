import requests


def test_delete_user():
    url = "https://reqres.in/api/users"
    user_id = 2

    response = requests.delete(url + f'/{user_id}')
    assert response.status_code == 204
    assert response.text == ''
