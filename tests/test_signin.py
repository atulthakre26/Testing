import pytest
from pages.signin_page import SignInPage

def test_valid_signin(setup):
    driver, wait = setup
    driver.get("https://demo.aceint.ai/auth/signin")
    signin = SignInPage(driver, wait)

    signin.enter_email("atulthakre511@gmail.com")
    signin.enter_password("123456789")
    signin.click_login()

  #  assert "AceInt" in driver.title

def test_invalid_password(setup):
    driver, wait = setup
    driver.get("https://demo.aceint.ai/auth/signin")
    signin = SignInPage(driver, wait)

    signin.enter_email("atulthakre511@gmail.com")
    signin.enter_password("wrongpass123")
    signin.click_login()

   # assert signin.get_error_messages()

def test_invalid_email_format(setup):
    driver, wait = setup
    driver.get("https://demo.aceint.ai/auth/signin")
    signin = SignInPage(driver, wait)

    signin.enter_email("invalidemail")
    signin.enter_password("somepass")
    signin.click_login()

   # assert signin.get_error_messages()

def test_empty_fields(setup):
    driver, wait = setup
    driver.get("https://demo.aceint.ai/auth/signin")
    signin = SignInPage(driver, wait)

    signin.click_login()

    #assert signin.get_error_messages()
