from .base_page import BasePageLocators


class RegisterFormLocators(BasePageLocators):
    EMAIL_FORM_LINK = "//input[@data-qa='email_input']"
    NAME_FORM_LINK = "//input[@data-qa='name_input']"
    REGISTRATION_FROM_LINK = "//div[@data-qa='auth_form']"
    EXIT_REG_AUTH_FORM_BUTTON = "//div[@data-qa='auth_close']"
    SUCCESS_MESSAGE_LINK = "//h2[@data-qa='success_title']"
    SUCCESS_EMAIL_LINK = "//p[@data-qa='success_body']"
    SUCCESS_BUTTON_LINK = "//button[@data-qa='success_button']"
    FORM_TITLE = "//h2[@data-qa='auth_title']"
    ERROR_NOTICE_LINK = "//div[@data-qa='auth_notice']/p"