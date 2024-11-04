from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import drivers

# Initialize the WebDriver
driver_instance=drivers.drivers()
driver=driver_instance.chrome()
try:
    driver.get("https://the-internet.herokuapp.com/windows")
    original_window = driver.current_window_handle

    # Click to open a new window
    driver.find_element(By.LINK_TEXT, "Click Here").click()
    time.sleep(2)  # Wait for the new window to open

    # Switch to the new window
    for handle in driver.window_handles:
        if handle != original_window:
            driver.switch_to.window(handle)
            break

    print("New window title:", driver.title)

    # Close the new window and switch back
    driver.close()
    driver.switch_to.window(original_window)

    print("Original window title:", driver.title)

finally:
    driver.quit()
