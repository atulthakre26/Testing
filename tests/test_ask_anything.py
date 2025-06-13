from base.base_test import BaseTest
from pages.login_page import LoginPage
from pages.chat_page import ChatPage
import time

class AskAnythingTest(BaseTest):
    def setUp(self):
        super().setUp()
        self.login_page = LoginPage(self.driver, self.wait)
        self.chat_page = ChatPage(self.driver, self.wait)

        self.login_page.go_to_login()
        self.login_page.login("atulthakre511@gmail.com", "123456789")
        self.chat_page.wait_for_response()  # Wait until chat is ready

    def test_ask_valid_question(self):
        self.chat_page.send_question("What is the capital of India?")
        time.sleep(5)
        response = self.chat_page.wait_for_response()
        self.assertTrue(len(response.text.strip()) > 0)

    def test_ask_empty_question(self):
        self.chat_page.send_question("")
        time.sleep(5)
        responses = self.chat_page.get_all_responses()
        self.assertTrue(len(responses) < 2)

    def test_ask_gibberish_question(self):
        self.chat_page.send_question("asdlkjasd1234!@#$%^&*")
        time.sleep(5)
        response = self.chat_page.wait_for_response()
        self.assertTrue(len(response.text.strip()) > 0)

if __name__ == "__main__":
    import unittest
    unittest.main()
