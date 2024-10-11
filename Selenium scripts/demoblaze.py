import time
import pyautogui
from selenium import webdriver
from selenium.common import NoSuchElementException, TimeoutException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.alert import Alert

username=input("enter username")
password=input('enter password')
service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.maximize_window()

def signup():
    try:
        if driver.find_element(By.ID,'signin2').is_displayed():
            driver.find_element(By.ID,'signin2').click()
        if driver.find_element(By.ID,'signInModalLabel').is_displayed():
            print("sign popup displayed ")
        else:
            print("sign up pop up not displayed ")
        # type username
        driver.find_element(By.ID, 'sign-username').clear()
        driver.find_element(By.ID,'sign-username').send_keys(username)
        # type password
        driver.find_element(By.ID, 'sign-password').clear()
        driver.find_element(By.ID,'sign-password').send_keys(password)
        # click signup
        driver.find_element(By.XPATH,"//button[@class='btn btn-primary' and text()='Sign up']"). click()
        alert=Alert(driver)
        if alert.text=="This user already exist":
            print('this user already exist try with different username')
            alert.accept()
            signup()
        elif alert.text=="Sign up successful.":
            print("sucessfully created user")
            alert.accept()
    except NoSuchElementException as e:
        print(f"Error: Element not found. {e}")
    except TimeoutException as e:
        print(f"Error: Loading took too much time! {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        # Close the browser
        driver.quit()

def login():
    try:
        if driver.find_element(By.ID,'login2').is_displayed():
            driver.find_element(By.ID,'login2').click()
        if driver.find_element(By.ID, 'logInModalLabel').is_displayed():
            print("login page displayed ")
        else:
            print("login page not displayed ")
            # type username
            driver.find_element(By.ID, 'loginusername').clear()
            driver.find_element(By.ID, 'loginusername').send_keys(username)
            # type password
            driver.find_element(By.ID, 'loginpassword').clear()
            driver.find_element(By.ID, 'loginpassword').send_keys(password)
            # click signup
            driver.find_element(By.XPATH, "//button[@class='btn btn-primary' and text()='Log in']").click()
            alert = Alert(driver)
            if alert.text == "User does not exist.":
                print('invalid username and password try with valid username and password')
                alert.accept()
                login()
            elif alert.text == "Sign up successful.":
                print("sucessfully created user")
                alert.accept()



def main():
    url=r"https://www.demoblaze.com/"
    driver.get(url)
    time.sleep(3)
    signup()
    login()

main()
