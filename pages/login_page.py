import testit
from pages.locators.login_page import LoginFormLocators
from .base_page import BasePage
from playwright.sync_api import expect

class LoginPage(BasePage):

    def should_be_login_form(self):
        expect(self.page.locator(LoginFormLocators.LOGIN_FORM_LINK)).to_be_visible()
        expect(self.page.locator(LoginFormLocators.FORM_TITLE)).to_have_text('Вход')

    def login_client(self, email: str, password: str):
        email_form = self.page.locator(LoginFormLocators.LOGIN_FORM_LINK)
        email_form.fill(email)
        password_form = self.page.locator(LoginFormLocators.PASSWORD_FORM_LINK)
        password_form.fill(password)
        submit_button = self.page.locator(LoginFormLocators.SUBMIT_BUTTON_LINK)
        submit_button.click()

    def should_be_error_message_text(self, error_text):
        expect(self.page.locator(LoginFormLocators.ERROR_MESSAGE_LINK)).to_have_text(error_text)

    def should_not_be_an_error(self):
        expect(self.page.locator(LoginFormLocators.ERROR_MESSAGE_LINK)).not_to_be_visible()
