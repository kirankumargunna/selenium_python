import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import time



class TestWebPage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        """This method runs once for the entire class before any tests."""
        print("setUpClass: Preparing test setup (e.g., initializing the browser)")
        options=webdriver.ChromeOptions()
        options.add_experimental_option("detach",True)
        cls.driver = webdriver.Chrome(options=options)
        cls.driver.maximize_window()  # Optional: Maximize the window

    def setUp(self):
        """This method runs before each test method."""
        print("setUp: Navigating to the website")
        self.driver.get("https://www.google.com")  # Example: Navigate to Google's homepage

    def test_title(self):
        """Test case to check the page title."""
        print("test_title: Checking the page title")
        self.assertEqual(self.driver.title, "Google")

    def test_search_box_exists(self):
        """Test case to check if the search box exists."""
        print("test_search_box_exists: Checking if the search box is present")
        search_box = self.driver.find_element(By.NAME, "q")
        self.assertTrue(search_box.is_displayed(), "Search box is not displayed")

    def test_search_functionality(self):
        """Test case to check if search functionality works."""
        print("test_search_functionality: Searching for Selenium WebDriver")
        search_box = self.driver.find_element(By.NAME, "q")
        search_box.send_keys("Selenium WebDriver")
        search_box.send_keys(Keys.RETURN)  # Press Enter
        time.sleep(2)  # Wait for the results to load (not recommended in real tests)
        self.assertIn("Selenium", self.driver.title)  # Check if title contains "Selenium"

    def test_element_visibility(self):
        """Test case to check visibility of a specific element."""
        print("test_element_visibility: Checking visibility of 'Google Search' button")
        search_button = self.driver.find_element(By.NAME, "btnK")
        self.assertTrue(search_button.is_displayed(), "'Google Search' button is not visible")

    def tearDown(self):
        """This method runs after each test method."""
        print("tearDown: Cleaning up after the test")
        # In this case, no cleanup is necessary after each test, but you can clear cookies, reset state, etc.
        pass

    @classmethod
    def tearDownClass(cls):
        """This method runs once after all tests are finished."""
        print("tearDownClass: Closing the browser")
        cls.driver.quit()  # Close the browser after all tests are complete

# Ensure the script runs only if executed directly
if __name__ == "__main__":
    unittest.main()
