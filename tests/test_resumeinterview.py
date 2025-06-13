from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.resumebase_interview import InterviewPage
import time

class AiInterviewTest(BaseTest):
    def test_start_interview(self):
        self.driver.get("https://demo.aceint.ai/")
        login_page = LoginPage(self.driver, self.wait)
        login_page.open()
        interview_page = InterviewPage(self.driver)

       
        login_page.login("atulthakre511@gmail.com", "123456789")

        interview_page.click_technical_interview()
        interview_page.select_interview_type()
        interview_page.upload_resume("C:/Users/HP/Downloads/AtulResume.pdf")
        interview_page.start_interview()

        time.sleep(30)  # Wait for interview session to load or complete actions

if __name__ == "__main__":
    import unittest
    unittest.main()
