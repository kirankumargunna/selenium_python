from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)

url=r'https://www.makemytrip.com/'
driver.maximize_window()
driver.get(url) # open make my trip webpage
driver.find_element(By.CLASS_NAME,'commonModal__close').click()
driver.find_element(By.CLASS_NAME,'menu_Buses').click() # click on buses tab
element = driver.find_element(By.ID,'fromCity').click()
driver.find_element(By.CLASS_NAME,'react-autosuggest__input react-autosuggest__input--open').send_keys('hyderabad')
driver.find_element(By.CLASS_NAME,'react-autosuggest__input react-autosuggest__input--open').send_keys(Keys.DOWN)
driver.find_element(By.CLASS_NAME,'react-autosuggest__input react-autosuggest__input--open').send_keys(Keys.ENTER)

driver.find_element(By.ID,'toCity').click()
driver.find_element(By.CLASS_NAME,'react-autosuggest__input react-autosuggest__input--open').send_keys('banglore')
driver.find_element(By.CLASS_NAME,'react-autosuggest__input react-autosuggest__input--open').send_keys(Keys.DOWN)
driver.find_element(By.CLASS_NAME,'react-autosuggest__input react-autosuggest__input--open').send_keys(Keys.ENTER)

driver.find_element((By.CLASS_NAME,'react-autosuggest__input react-autosuggest__input--open').send_keys('banglore')) # enter source of journey
driver.find_element(By.CLASS_NAME,'primaryBtn font24 latoBold widgetSearchBtn').click() #click on search



import array
array.array