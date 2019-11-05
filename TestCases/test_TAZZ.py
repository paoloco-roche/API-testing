import requests
import json
import jsonpath
import pytest

#API url


@pytest.mark.Smoke

def test_TAZZ_bif():
    url = "http://dtumvims10.dtu.roche.com:8000/tazz/?FIF=/PSAD/images/TAZZ_Test/VT0000000723_CD68.bif&&TILE=5,0,0,512,512&RETURN=PNG"

    #1. open the file
    response = requests.get(url)

    #2. validate response code
    assert response.status_code == 200

    #3. Verify content
    assert response.headers['Content-Type'] == 'image/png'
    assert response.headers['Content-Length'] == '395111'

    #4. future, create image diff
    

def xtest_TAZZ_ndpi_thumbnail():
    url = "http://sunusimgbld05.sun.roche.com:8000/tazz/?FIF=/PSAD/images/TAZZ_Test/OS-2.ndpi&THUMBNAIL=0,0&RETURN=JPG"

    #1. open the file
    response = requests.get(url)

    #2. validate response code
    assert response.status_code == 200

    #3. Verify content
    assert response.headers['Content-Type'] == 'image/png'
    assert response.headers['Content-Length'] == '395111'

    #4. future, create image diff


    


