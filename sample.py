import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver import ActionChains, Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=options)

driver.implicitly_wait(10)

driver.get("https://chorusqa.cogninelabs.com/")
print(driver.title)
driver.maximize_window()
time.sleep(5)
driver.find_element(By.XPATH, "//input[@type='email']").send_keys("tejaswini.voora@cognine.com")
driver.implicitly_wait(3)
driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
time.sleep(3)
driver.find_element(By.NAME, "passwd").send_keys("Deepveer@0")
driver.find_element(By.ID, "idSIButton9").click()
time.sleep(3)
driver.find_element(By.ID, "KmsiCheckboxField").click()
driver.implicitly_wait(3)
driver.find_element(By.ID, "idSIButton9").click()
driver.implicitly_wait(3)
driver.find_element(By.CLASS_NAME, "ic-title").click()
driver.implicitly_wait(5)
iframe_element = driver.find_element(By.XPATH, "//iframe[@id='undefined']")
driver.switch_to.frame(iframe_element)
action = ActionChains(driver)
action.move_to_element(driver.find_element(By.XPATH,"//div[@class='sidebar close']"))
action.perform()
driver.find_element(By.ID, "Practice").click()
driver.find_element(By.ID, "addOrUpdatePractice").click()
driver.find_element(By.ID, "PracticeName").send_keys("Python2")
driver.find_element(By.CLASS_NAME, "chosen-search-input").click()
driver.find_element(By.CLASS_NAME, "chosen-search-input").send_keys("Kiran Gunna")
driver.find_element(By.CLASS_NAME, "active-result").click()
driver.find_element(By.ID, "PracticeManagementEmail").click()
driver.find_element(By.ID, "PracticeManagementEmail").send_keys("tejaswini.voora@cognine.com")
driver.find_element(By.ID, "PracticeGroupEmail").send_keys("tejaswini.voora@cognine.com")
driver.find_element(By.ID, "PracticeGroupEmail").send_keys(Keys.ENTER)
time.sleep(3)
#button = driver.find_element(By.XPATH, "//button[@id='SaveData']")
button = driver.find_element(By.ID, "SaveData")
button.click()