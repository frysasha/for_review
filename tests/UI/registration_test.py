from pages.registration_page import RegistrationPage
import time
import testit
import pytest
from playwright.sync_api import Page


class TestUserRegistrate:
    """Позитивный и негативные тесты на регистрацию.
    В поле email должны присутствовать символы '@' и '.'
    В поле имени должны быть только буквы"""
    positive_email = 'QA_Client_' + str(time.strftime('%d.%b_%H.%M')) + '@biglion.ru'
    positive_name = 'QA_Client'

    @pytest.mark.skip
    @testit.labels('e2e', 'ui', 'auto')
    @testit.externalId(f'test_positive_registration')
    def test_positive_registration(self, page: Page):
        """Позитивный тест на регистрацию пользователя"""
        page = RegistrationPage(page)
        with testit.step('Открытие страницы'):
            page.open()
        with testit.step('Открытие формы регистрации'):
            page.go_to_registration_page()
            page.should_be_registration_form()
        with testit.step('Ввод валидных данных в форму регистрации'):
            page.register_new_client(self.positive_email, self.positive_name)
            page.should_be_success_message()
            page.should_be_correct_email_in_success_message(self.positive_email)
            page.click_success_button()
        with testit.step('Проверка наличия аватара пользователя'):
            page.should_be_user_avatar()

    @pytest.mark.skip
    @testit.labels('e2e', 'ui', 'auto')
    @pytest.mark.parametrize("negative_email, negative_name", [
        ('QA_Client@biglion', "QAClient"),
    ])
    @testit.externalId(f'test_negative_registration')
    def test_negative_registration(self, page: Page, negative_email, negative_name):
        """Негативный тест на регистрацию пользователя"""
        page = RegistrationPage(page)
        with testit.step('Открытие страницы'):
            page.open()
        with testit.step('Открытие формы регистрации'):
            page.go_to_registration_page()
            page.should_be_registration_form()
        with testit.step('Ввод невалидных данных в форму регистрации'):
            page.register_new_client(negative_email, negative_name)
        with testit.step('Должна быть ошибка "Неверно заданы входные параметры"'):
            page.should_be_error_notice()
