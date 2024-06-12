from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class FlaskTest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_example(self):
        driver = self.driver
        driver.get("http://localhost:5000")
        self.assertIn("Hello, World!", driver.page_source)

    def tearDown(self):
        self.driver.close()

if __name__ == "__main__":
    unittest.main()
