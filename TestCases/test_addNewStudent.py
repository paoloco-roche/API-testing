import requests
import jsonpath
import json

def test_add_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails"

    with open("C:\\software\\APIFramework\\TestCases\\postStudentDetails.json", 'r') as file:
        json_input = json.loads(file.read())
        file.close()

    response = requests.post(API_URL, json_input)
    print(response.text)

def test_get_student_data():
    API_URL = "http://thetestingworldapi.com/api/studentsDetails/147776"
    response = requests.get(API_URL)
    json_response = json.loads(response.text)
    id = jsonpath.jsonpath(json_response, 'data.id')
    assert id[0] == 147776

