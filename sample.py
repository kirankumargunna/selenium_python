# import time
# from selenium import webdriver
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# from selenium.webdriver import ActionChains, Keys
# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.common.by import By

# options=webdriver.ChromeOptions()
# options.add_experimental_option("detach",True)

# service=Service(ChromeDriverManager().install())
# driver=webdriver.Chrome(service=service,options=options)

# driver.implicitly_wait(10)

# driver.get("https://chorusqa.cogninelabs.com/")
# print(driver.title)
# driver.maximize_window()
# time.sleep(5)
# driver.find_element(By.XPATH, "//input[@type='email']").send_keys("tejaswini.voora@cognine.com")
# driver.implicitly_wait(3)
# driver.find_element(By.XPATH, "//input[@id='idSIButton9']").click()
# time.sleep(3)
# driver.find_element(By.NAME, "passwd").send_keys("Deepveer@0")
# driver.find_element(By.ID, "idSIButton9").click()
# time.sleep(3)
# driver.find_element(By.ID, "KmsiCheckboxField").click()
# driver.implicitly_wait(3)
# driver.find_element(By.ID, "idSIButton9").click()
# driver.implicitly_wait(3)
# driver.find_element(By.CLASS_NAME, "ic-title").click()
# driver.implicitly_wait(5)
# iframe_element = driver.find_element(By.XPATH, "//iframe[@id='undefined']")
# driver.switch_to.frame(iframe_element)
# action = ActionChains(driver)
# action.move_to_element(driver.find_element(By.XPATH,"//div[@class='sidebar close']"))
# action.perform()
# driver.find_element(By.ID, "Practice").click()
# driver.find_element(By.ID, "addOrUpdatePractice").click()
# driver.find_element(By.ID, "PracticeName").send_keys("Python2")
# driver.find_element(By.CLASS_NAME, "chosen-search-input").click()
# driver.find_element(By.CLASS_NAME, "chosen-search-input").send_keys("Kiran Gunna")
# driver.find_element(By.CLASS_NAME, "active-result").click()
# driver.find_element(By.ID, "PracticeManagementEmail").click()
# driver.find_element(By.ID, "PracticeManagementEmail").send_keys("tejaswini.voora@cognine.com")
# driver.find_element(By.ID, "PracticeGroupEmail").send_keys("tejaswini.voora@cognine.com")
# driver.find_element(By.ID, "PracticeGroupEmail").send_keys(Keys.ENTER)
# time.sleep(3)
# #button = driver.find_element(By.XPATH, "//button[@id='SaveData']")
# button = driver.find_element(By.ID, "SaveData")
# button.click()






import time
from selenium import webdriver
from selenium.webdriver.common.by import By

# Configure WebDriver
options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)  # Keep browser open after execution
driver = webdriver.Chrome(options=options)

try:
    # Navigate to the webpage
    driver.get("https://the-internet.herokuapp.com/checkboxes")

    # ===== Assertions =====
    # Assert the page title
    expected_title = "The Internet"
    actual_title = driver.title
    assert actual_title == expected_title, f"Page title mismatch! Expected: '{expected_title}', Found: '{actual_title}'"

    # Assert the current URL
    expected_url = "https://the-internet.herokuapp.com/checkboxes"
    actual_url = driver.current_url
    assert actual_url == expected_url, f"URL mismatch! Expected: '{expected_url}', Found: '{actual_url}'"

    # Assert that the header is visible and contains correct text
    header = driver.find_element(By.TAG_NAME, "h3")
    assert header.is_displayed(), "Header is not visible"
    expected_header_text = "Checkboxes"
    assert header.text == expected_header_text, f"Header text mismatch! Expected: '{expected_header_text}', Found: '{header.text}'"

    # Locate checkboxes
    checkboxes = driver.find_elements(By.CSS_SELECTOR, "input[type='checkbox']")
    assert len(checkboxes) == 2, f"Expected 2 checkboxes, but found {len(checkboxes)}"

    # ===== Assertions on Checkboxes =====
    # Assert the initial state of the first checkbox (should be unchecked)
    assert not checkboxes[0].is_selected(), "First checkbox should be unchecked by default"

    # Assert the initial state of the second checkbox (should be checked)
    assert checkboxes[1].is_selected(), "Second checkbox should be checked by default"

    # ===== Interact with Checkboxes =====
    # Check the first checkbox
    checkboxes[0].click()
    time.sleep(1)  # Simulate a slight delay for interaction

    # Assert the first checkbox is now checked
    assert checkboxes[0].is_selected(), "First checkbox should be checked after clicking"

    # Uncheck the second checkbox
    checkboxes[1].click()
    time.sleep(1)

    # Assert the second checkbox is now unchecked
    assert not checkboxes[1].is_selected(), "Second checkbox should be unchecked after clicking"

    # ===== Additional Validations =====
    # Assert that both checkboxes are visible
    assert checkboxes[0].is_displayed(), "First checkbox is not visible"
    assert checkboxes[1].is_displayed(), "Second checkbox is not visible"

    # Assert that the input elements are enabled (interactable)
    assert checkboxes[0].is_enabled(), "First checkbox is not enabled"
    assert checkboxes[1].is_enabled(), "Second checkbox is not enabled"

    print("All assertions passed successfully!")

finally:
    # Close the browser
    driver.quit()
