from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

class ChatPage:
    def __init__(self, driver, wait):
        self.driver = driver
        self.wait = wait

    def send_question(self, text):
        input_box = self.wait.until(EC.visibility_of_element_located((By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/main/div/div/div[2]/form/textarea")))
        input_box.send_keys(text)
        input_box.send_keys(Keys.ENTER)

    def wait_for_response(self):
        return self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[2]/div/main/div/div/div/main/div/div/div[2]/form/textarea")
        ))

    def get_all_responses(self):
        return self.driver.find_elements(By.XPATH, "//div[contains(@class,'message')]")
