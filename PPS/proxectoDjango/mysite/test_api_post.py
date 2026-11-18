import requests
import json


def test_get_users():

    url = "https://jsonplaceholder.typicode.com/users"

    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    assert isinstance(data, list)
    assert len(data) > 0


def test_get_users_1():

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"


def test_get_users_inexistente():

    url = "https://jsonplaceholder.typicode.com/users/150"

    response = requests.get(url)

    assert response.status_code == 404


def test_post_users():

    url = "https://jsonplaceholder.typicode.com/users"

    payload = {"name": "Rahmon", "username": "manolo", "email": "manolo@test.com"}

    response = requests.post(url, json=payload)
    assert response.status_code == 201

    data = response.json()
    assert data["name"] == "Rahmon"
    assert data["username"] == "manolo"


def test_put_users():

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1

    payload = {"name": "Rahmon", "username": "manolo"}

    response = requests.patch(url, json=payload)
    # response = requests.put(url, json=payload)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1
    assert data["name"] == "Rahmon"
    assert data["username"] == "manolo"

    print(json.dumps(data, indent=2))


def test_delete_users():

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    assert data["id"] == 1

    response = requests.delete(url)


# 3


def test_get_posts_1_2_3():

    url1 = "https://jsonplaceholder.typicode.com/posts/1"
    url2 = "https://jsonplaceholder.typicode.com/posts/2"
    url3 = "https://jsonplaceholder.typicode.com/posts/3"

    print("-------EXERCICIO 3-------")

    response = requests.get(url1)
    assert response.status_code == 200

    data = response.json()
    print(json.dumps(data, indent=2))

    response = requests.get(url2)
    assert response.status_code == 200

    data = response.json()
    print(json.dumps(data, indent=2))

    response = requests.get(url3)
    assert response.status_code == 200

    data = response.json()
    print(json.dumps(data, indent=2))
