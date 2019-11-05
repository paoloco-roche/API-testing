import requests
import json
import jsonpath
import pytest

#API url
url = "https://reqres.in/api/users"

@pytest.fixture
def start_exec():
    global file_path
    file_path = 'C:\\software\\APIFramework\\reqres\\CreateUser.json'

@pytest.mark.Smoke
@pytest.mark.Sanity
def test_create_new_user(start_exec):

    #1. open the file
    with open(file_path, 'r') as input:
        json_input = input.read()
        input.close()

    #2. parse as json format
    request_json = json.loads(json_input)

    #3. post request with Json Input body
    response = requests.post(url, request_json)

    #4. validate response code
    assert response.status_code == 201

    #5. parse reponse to Json Format
    response_json = json.loads(response.text)

    #6. pick id from json path
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])


@pytest.mark.Smoke
def test_create_other_user(start_exec):

    #1. open the file
    with open(file_path, 'r') as input:
        json_input = input.read()
        input.close()

    #2. parse as json format
    request_json = json.loads(json_input)

    #3. post request with Json Input body
    response = requests.post(url, request_json)

    #4. validate response code
    assert response.status_code == 201

    #5. parse reponse to Json Format
    response_json = json.loads(response.text)

    #6. pick id from json path
    id = jsonpath.jsonpath(response_json, 'id')
    print(id[0])

