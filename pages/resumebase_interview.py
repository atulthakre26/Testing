from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os

class InterviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

    def click_technical_interview(self):
        self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//div[contains(text(),'Technical Interview')]"
        ))).click()

    def select_interview_type(self):
        self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//select"
        ))).click()
        self.driver.find_element(By.XPATH, "//option[2]").click()

    def upload_resume(self, file_path):
        full_path = os.path.abspath(file_path)
        upload_input = self.wait.until(EC.presence_of_element_located((
            By.XPATH, "//input[@type='file']"
        )))
        upload_input.send_keys(full_path)

    def start_interview(self):
        self.wait.until(EC.element_to_be_clickable((
            By.XPATH, "//form/button"
        ))).click()
