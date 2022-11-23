from .base_page import BasePageLocators


class LoginFormLocators(BasePageLocators):
    LOGIN_FORM_LINK = "//input[@data-qa='login_input']"
    PASSWORD_FORM_LINK = "//input[@data-qa='password_input']"
    REMINDER_BUTTON_LINK = "//a[@data-qa='reminder_link']"
    FORM_TITLE = "//h2[@data-qa='auth_title']"
    ERROR_MESSAGE_LINK = "//*[@data-qa='auth_notice']/p"
