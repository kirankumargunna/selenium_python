from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
from datetime import datetime, timedelta
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



source=input("enter source :")
destination=input("enter destination :")
#Date_of_travel=input("enter date :")
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



def is_valid_date(user_date):
    """
    Check if the user-provided date is within the range of 3 months from today's date.
    """
    today = datetime.today()
    three_months_later = today + timedelta(days=90)  # Approximate 3 months as 90 days

    # Check if the input date is within the range of today and 3 months from now
    if today <= user_date <= three_months_later:
        return True
    return False



def get_date_of_travel():
    """
    Prompt the user to input a valid date within the next 3 months in various formats.
    """
    while True:
        Travel_date=input("enter date of journey(less than 3 months from today) : ")

        converted_date, month_year = convert_date(Travel_date)

        if converted_date == "invalid date format":
            print("Invalid date format. Please try again.")
            continue

        # Convert string to datetime object for range check
        user_date = datetime.strptime(converted_date, "%a %b %d %Y")

        if is_valid_date(user_date):
            print(f"Valid date entered: {converted_date}")
            return converted_date, month_year
        else:
            print("The date is outside the allowed range (next 3 months). Please try again.")

date, month_year = get_date_of_travel()
print(date,month_year)
#***********************************script starts *********************

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
input_element.send_keys(source)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'.react-autosuggest__input.react-autosuggest__input--open').send_keys(Keys.DOWN)
driver.find_element(By.CSS_SELECTOR,'.react-autosuggest__input.react-autosuggest__input--open').send_keys(Keys.ENTER)

#driver.find_element(By.XPATH,"//input[@id='toCity']").click()
driver.find_element(By.CSS_SELECTOR,'.react-autosuggest__input.react-autosuggest__input--open').is_displayed()
driver.find_element(By.CSS_SELECTOR,'.react-autosuggest__input.react-autosuggest__input--open').send_keys(destination)
time.sleep(1)
driver.find_element(By.CSS_SELECTOR,'.react-autosuggest__input.react-autosuggest__input--open').send_keys(Keys.DOWN)
driver.find_element(By.CSS_SELECTOR,'.react-autosuggest__input.react-autosuggest__input--open').send_keys(Keys.ENTER)


element_found= False
while element_found==False:
    try:
        # Try to locate the element with the provided XPath
        element = driver.find_element(By.XPATH, f"//div[@class='DayPicker-Caption']/div[text()='{month_year}']")
        element_found= True  # Return True if the element is found

    except Exception as e:
        # If the element is not found, print an error and continue to the next iteration
        print(f"Element not found, retrying... {e}")
        next_month=driver.find_element(By.XPATH,"//span[@role='button' and @class='DayPicker-NavButton DayPicker-NavButton--next']")
        next_month.click()
        next_month.click()

driver.find_element(By.XPATH,f"//div[@role='gridcell' and @class='DayPicker-Day' and @aria-label='{date}']").click()

driver.find_element(By.CSS_SELECTOR,'.primaryBtn.font24.latoBold.widgetSearchBtn').click() #click on search


driver.quit()