import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from pages.signup_page import SignupPage

class SignupTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 10)
        self.signup_page = SignupPage(self.driver, self.wait)
        self.signup_page.open_signup_page()

    def tearDown(self):
        self.driver.quit()

    def test_valid_signup(self):
        self.signup_page.enter_first_name("Atul")
        self.signup_page.enter_last_name("Thakre")
        self.signup_page.enter_email("atul_auto_test@example.com")  # Change this to unique each time
        self.signup_page.enter_password("StrongPassword123")
        self.signup_page.click_signup_button()

        # Assertion depends on expected behavior (success redirect, message, etc.)
       # self.assertIn("signin", self.driver.current_url.lower())  # or check for success message

    def test_signup_with_empty_fields(self):
        self.signup_page.click_signup_button()
        errors = self.signup_page.get_error_messages()
      #  self.assertGreater(len(errors), 0, "Expected error messages for empty fields")

    def test_signup_with_invalid_email(self):
        self.signup_page.enter_email("invalidemail")
        self.signup_page.click_signup_button()
        errors = self.signup_page.get_error_messages()
        #self.assertGreater(len(errors), 0)

if __name__ == "__main__":
    unittest.main()
