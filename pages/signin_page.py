from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class SignInPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def enter_email(self, email):
        email_field = self.wait.until(lambda d: d.find_element(By.XPATH, "/html/body/div/div/div/form/div[1]/input"))
        email_field.clear()
        email_field.send_keys(email)

    def enter_password(self, password):
        password_field = self.driver.find_element(By.XPATH, "/html/body/div/div/div/form/div[2]/div[1]/input")
        password_field.clear()
        password_field.send_keys(password)

    def click_login(self):
        self.driver.find_element(By.XPATH, "/html/body/div/div/div/form/button").click()
        time.sleep(3)

    def get_error_messages(self):
        return self.driver.find_elements(By.CLASS_NAME, "text-red-500")
