import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.content)
# b'{"current_user_url":"https://api.github.com/user", ...}'

# print(type(response.content))
# <class 'bytes'>


# print(response.text)
# print("---------------------------------------")
# print(response.json())
# print(type(response.json()))

# diccionario = response.json()
# print(diccionario("userid"))

# response = requests.get(
#     "https://jsonplaceholder.typicode.com/posts",
#     params={"id": "1"},
# )


# print(response.headers)
# print(response.headers["Content-Type"])


# import requests

# url = "https://jsonplaceholder.typicode.com/posts"

# data = {
#     "title": "Aprendendo Python",
#     "body": "Esta é unha publicación de proba",
#     "userId": 1,
# }

# # Indica que os datos a enviar hai que convertelos a JSON
# response = requests.post(url, json=data)

# # resposta do servidor
# print("Status code:", response.status_code)
# print("Resposta:", response.json())


def test_get_user():

    url = "https://jsonplaceholder.typicode.com/users/1"

    response = requests.get(url)

    # Validar código HTTP
    assert response.status_code == 200

    # Obtener respuesta JSON
    data = response.json()

    # Validar datos
    assert data["id"] == 1
    assert data["name"] == "Leanne Graham"
    assert data["username"] == "Bret"

    print("Test executado correctamente")
