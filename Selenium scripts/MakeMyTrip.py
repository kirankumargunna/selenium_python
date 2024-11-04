from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

options=webdriver.ChromeOptions()
options.add_experimental_option("detach",True)

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service,options=options)

driver.implicitly_wait(10)

url=r'https://www.makemytrip.com/'
driver.maximize_window()   #maximize window

driver.get(url) # open make my trip webpage

# close the sign in pop up
driver.find_element(By.CLASS_NAME,'commonModal__close').click()

# click on buses tab
driver.find_element(By.CLASS_NAME,'menu_Buses').click()

driver.find_element(By.ID,'fromCity').click()

wait = WebDriverWait(driver, 10)

input_element = wait.until(
    EC.visibility_of_element_located((By.CSS_SELECTOR, '.react-autosuggest__input.react-autosuggest__input--open')))

# Send keys to the input field
input_element.send_keys('hyderabad')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'.react-autosuggest__input.react-autosuggest__input--open').send_keys(Keys.DOWN)
driver.find_element(By.CSS_SELECTOR,'.react-autosuggest__input.react-autosuggest__input--open').send_keys(Keys.ENTER)

#driver.find_element(By.XPATH,"//input[@id='toCity']").click()
driver.find_element(By.CSS_SELECTOR,'.react-autosuggest__input.react-autosuggest__input--open').is_displayed()
driver.find_element(By.CSS_SELECTOR,'.react-autosuggest__input.react-autosuggest__input--open').send_keys('banglore')
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'.react-autosuggest__input.react-autosuggest__input--open').send_keys(Keys.DOWN)
driver.find_element(By.CSS_SELECTOR,'.react-autosuggest__input.react-autosuggest__input--open').send_keys(Keys.ENTER)

def convert_date(date_input):
    formats = [
        "%Y-%m-%d",        # 2024-11-30
        "%d/%m/%Y",        # 30/11/2024
        "%m-%d-%Y",        # 11-30-2024
        "%B %d, %Y",      # November 30, 2024
        "%b %d, %Y",      # Nov 30, 2024
        "%Y/%m/%d",       # 2024/11/30
        "%d %B %Y",       # 30 November 2024
        "%d %b %Y",       # 30 Nov 2024
        "%m/%d/%Y",       # 11/30/2024
        "%Y.%m.%d",       # 2024.11.30
        "%d-%m-%Y",       # 30-11-2024
        "%Y%m%d",         # 20241130
        "%A, %d %B %Y",   # Saturday, 30 November 2024
        "%a, %d %b %Y",   # Sat, 30 Nov 2024
        "%d %m %Y",       # 30 11 2024
        ]

    for fmt in formats:
        try:
            parsed_date=datetime.strptime(date_input,fmt)
            month_year = parsed_date.strftime("%B %Y")
            return parsed_date.strftime("%a %b %d %Y"), month_year

        except ValueError:
            continue
    return "invalid date format"

date, month_year = convert_date('25/01/2024')


elements = driver.find_elements(By.CSS_SELECTOR, ".DayPicker-Caption div")
for element in elements:
    while True:
        if month_year in  element.text:
            return True




driver.find_element(By.CLASS_NAME,'primaryBtn font24 latoBold widgetSearchBtn').click() #click on search


#driver.quit()