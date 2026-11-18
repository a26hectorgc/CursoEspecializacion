import requests
import json


def test_get_users():

    url = "https://api.github.com/search/repositories"

    response = requests.get(url)
    assert response.status_code == 200

    data = response.json()
    print(json.dumps(data, indent=2))


# "repository_search_url": "https://api.github.com/search/repositories?q={query}{&page,per_page,sort,order}"
