from pages.locators.registration_page import RegisterFormLocators
from .base_page import BasePage


class RegistrationPage(BasePage):
    def should_be_registration_form(self):
        assert self.page.locator(
            *RegisterFormLocators.REGISTRATION_FROM_LINK).wait_for(), 'Registration form is not presented'
        assert self.page.locator(RegisterFormLocators.FORM_TITLE).text_content(), 'Title is not "Регистрация"'

    def register_new_client(self, email: str, name: str):
        email_form = self.page.locator(RegisterFormLocators.EMAIL_FORM_LINK)
        email_form.fill(email)
        name_form = self.page.locator(RegisterFormLocators.NAME_FORM_LINK)
        name_form.fill(name)
        submit_button = self.page.locator(RegisterFormLocators.SUBMIT_BUTTON_LINK)
        submit_button.click()

    def should_be_success_message(self):
        assert self.page.locator(
            RegisterFormLocators.SUCCESS_MESSAGE_LINK).wait_for(), 'Success message is not presented'

    def should_be_correct_email_in_success_message(self, qa_email):
        email_in_message = self.page.locator(RegisterFormLocators.SUCCESS_EMAIL_LINK)
        assert qa_email in email_in_message.text_content(), (
            f'QA email ({qa_email}) does not match email in the success message.'
            f'Given:'
            f'{email_in_message.text_content()}')

    def click_success_button(self):
        success_button = self.page.locator(RegisterFormLocators.SUCCESS_BUTTON_LINK)
        success_button.click()

    def should_be_error_notice(self):
        error_notice = self.page.locator(RegisterFormLocators.ERROR_NOTICE_LINK)
        assert error_notice, 'Error notice is not presented'
