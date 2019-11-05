from selenium.webdriver import Chrome
import pytest

a = 100

@pytest.mark.skip("don't want to execute on current buid")
def test_registration_valid_data():
    path = "C:\\Users\\cop\\Downloads\\Software\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")

@pytest.mark.skipif(a>100, reason = "don't want to execute on current buid")
def test_registration_valid_data2():
    path = "C:\\Users\\cop\\Downloads\\Software\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")

def test_registration_invalid_data():
    path = "C:\\Users\\cop\\Downloads\\Software\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()

@pytest.mark.Smoke
def test_registration_smoke1():
    path = "C:\\Users\\cop\\Downloads\\Software\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()
    
@pytest.mark.Smoke
def test_registration_smoke2():
    path = "C:\\Users\\cop\\Downloads\\Software\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()