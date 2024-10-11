from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By


service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

url=r"https://opensource-demo.orangehrmlive.com/auth/login"
driver.get(url)  #opens OrangeHRM login page
driver.implicitly_wait(5)
# find web element
username=driver.find_element(By.CL,"#app > div.orangehrm-login-layout > div > div.orangehrm-login-container > div > div.orangehrm-login-slot > div.orangehrm-login-form > form > div:nth-child(2) > div > div:nth-child(2) > input")
print(username)
username.
driver.find_element(By.CSS_SELECTOR