from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def go_to_login(self):
        self.driver.get("https://demo.aceint.ai/auth/signin")

    def login(self, email, password):
        self.wait.until(EC.visibility_of_element_located((By.XPATH, "//input[@type='email']"))).send_keys(email)
        self.driver.find_element(By.XPATH, "//input[@type='password']").send_keys(password)
        self.driver.find_element(By.XPATH, "//button[contains(text(),'Sign In')]").click()
