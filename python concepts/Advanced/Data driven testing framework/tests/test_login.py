import pytest
from selenium import webdriver
from pages.loginpage import LoginPage
from utils.datareader import read_excel

# Path to test data file
filepath="D:\selenium_python\Python Concepts\Advanced\Data driven testing framework\data\ddt_data.xlsx"
sheetname="Sheet1"

@pytest.fixture
def setup():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach",True)
    driver = webdriver.Chrome(options=options)
    driver.get("https://practicetestautomation.com/practice-test-login/")  # Replace with your application URL
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.mark.parametrize("username,password,expected_result", read_excel(filepath, sheetname))
def test_login(setup, username, password, expected_result):
    driver = setup
    login_page = LoginPage(driver)
    login_page.login(username, password)

    # Example assertions
    if expected_result == "Success":
        assert "Dashboard" in driver.title  # Modify as per your application
    else:
        assert "Login" in driver.title
