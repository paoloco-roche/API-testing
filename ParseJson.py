import json
import requests
import jsonpath

odics='{"k1": "val1", "k2":"k2"}'

json_result = json.loads(odics)

print(json_result)
print(json_result['k1'])

#reqres
base_url = "https://reqres.in/"
relative_url = "https://reqres.in/api/users?page=2"

response = requests.get(relative_url)

#displays response code eg. 200
print(response)

#displays response content
print(response.content)

#status code
print(response.status_code)
assert response.status_code == 200

#response headers
print(response.headers)
##response headers Date, Server
print(response.headers.get('Date'))
print(response.headers.get('Server'))

#response cookies
print(response.cookies)

#elapsed time --notes
print(response.elapsed)

#parse response to json format
json_response = json.loads(response.text)
print(json_response)

#fetch using json path
pages = jsonpath.jsonpath(json_response, 'total_pages')
print(pages[0])

#fetch array in json
first_name = jsonpath.jsonpath(json_response, 'data[0].first_name')
print(first_name[0])


#url for tazz
def getScanDate(tazz_url):
    response = requests.get(tazz_url)
    json_response = json.loads(response.text)
    print(json_response)
    scan_date = jsonpath.jsonpath(json_response, 'iScan.ScanDate')
    if scan_date:
        return scan_date[0]
    else:
        return None

#requests with parameters
param = {'name': 'testingworld', 'email':'testingworld@gmail.com', 'number':'+91 123'}
response = requests.get('https://httpbin.org/get', params=param)
print(response.text)

