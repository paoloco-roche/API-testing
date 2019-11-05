import requests
import json
import jsonpath
import pytest

#API url


@pytest.mark.Smoke

def test_fetch_user_details():
    url = "https://reqres.in/api/users?page=2"

    #1. open the file
    response = requests.get(url)

    #2. parse as json format
    json_response = json.loads(response.text)

    #4. validate response code
    assert response.status_code == 200

    #6. pick id from json path
    for i in range(0,3):
        first_name = jsonpath.jsonpath(json_response, 'data[' + str(i) + '].first_name')
        print(first_name[0])
    


