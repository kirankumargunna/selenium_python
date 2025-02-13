from selenium import webdriver

def test_login():
    driver=webdriver.Chrome()
    driver.maximize_window()
    driver=driver.get("https://ecommerce-playground.lambdatest.io/")
    return driver

