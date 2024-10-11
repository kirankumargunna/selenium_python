from selenium import webdriver

# initilize browser
driver= webdriver.Chrome()

# navigate to url
driver.get('https://www.pythontutorial.net/')

# close the browser
driver.quit()