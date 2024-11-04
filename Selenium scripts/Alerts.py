from selenium.webdriver.common.by import By
from selenium.webdriver.common.alert import Alert
import time
import drivers

# Initialize the WebDriver
driver_instance=drivers.drivers()
driver=driver_instance.chrome()
try:
    driver.get("https://the-internet.herokuapp.com/javascript_alerts")
    # Click on the button to trigger the alert
    driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Alert')]").click()

    # Wait for the alert to be present
    time.sleep(1)
    alert = Alert(driver)
    print("Alert text:", alert.text)

    # Accept the alert
    alert.accept()
    # Verify the result
    result_text = driver.find_element(By.ID, "result").text
    print(result_text)

    driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Confirm')]").click()
    #cancel alert
    alert.dismiss()
    print("alert dismissed")
    # Verify the result
    result_text = driver.find_element(By.ID, "result").text
    print(result_text)

    #prompt alert
    driver.find_element(By.XPATH, "//button[contains(text(), 'Click for JS Prompt')]").click()
    alert.send_keys("sadfkljsfkljaslkdfj")
    alert.accept()

    # Verify the result
    result_text = driver.find_element(By.ID, "result").text
    print(result_text)

finally:
    driver.quit()
