from selenium.webdriver.common.by import By
import time

class SignupPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def open_signup_page(self):
        self.driver.get("https://demo.aceint.ai/auth/signup")

    def enter_first_name(self, first_name):
        self.wait.until(lambda d: d.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[1]/div[1]/input")).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[1]/div[2]/input").send_keys(last_name)

    def enter_email(self, email):
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[2]/input").send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/div[3]/div/input").send_keys(password)

    def click_signup_button(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div[2]/div/form/button").click()
        time.sleep(2)

    def get_error_messages(self):
        return self.driver.find_elements(By.CLASS_NAME, "text-red-500")
