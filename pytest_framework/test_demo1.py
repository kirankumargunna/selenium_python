from selenium import webdriver

def test_lambdatest_playground():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://www.lambdatest.com/selenium-playground/")
  print("Title: ", driver.title)
@pytest.mark.smoke
def test2_lambdatest_ecommerce():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://ecommerce-playground.lambdatest.io/")
  print("Title: ", driver.title)

def test_RexWebsite():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://rexjones2.com")
  print("Title: ", driver.title)
  assert driver.title=="incorrect tilte ", "assertion failed due to data mismatch"

def test_google():
  driver = webdriver.Chrome()
  driver.maximize_window()
  driver.get("https://google.com")
  print("Title: ", driver.title)

