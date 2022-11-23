from pages.login_page import LoginPage
import pytest
import testit
from playwright.sync_api import Page
from dotenv import load_dotenv
import os


class TestLoginClient:
    load_dotenv()
    qa_email = os.getenv('QA_EMAIL')
    qa_password = os.getenv('QA_PASSWORD')

    @pytest.mark.skip
    @testit.labels('e2e', 'ui', 'auto')
    @testit.externalId(f'test_positive_login')
    def test_positive_login(self, page: Page):
        """Позитивный тест на аутентификацию пользователя с валидными данными"""
        page = LoginPage(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step('Открытие формы входа'):
            page.go_to_login_page()
            page.should_be_login_form()
        with testit.step('Ввод валидных данных в форму входа'):
            page.login_client(email=self.qa_email, password=self.qa_password)
            page.should_not_be_an_error()
        with testit.step('Должен быть аватар пользователя'):
            page.should_be_user_avatar()

    @pytest.mark.skip
    @testit.labels('e2e', 'ui', 'auto')
    @pytest.mark.parametrize("negative_email, negative_name", [
        ('invalid_user@biglion.su', "QAClient"),
    ])
    @testit.externalId(f'test_negative_login')
    def test_negative_login(self, page: Page, negative_email, negative_name):
        """Негативный тест на аутентификацию пользователя с использованием невалидных данных"""
        page = LoginPage(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step('Открытие формы входа'):
            page.go_to_login_page()
            page.should_be_login_form()
        with testit.step('Ввод невалидных данных в форму входа'):
            page.login_client(email=negative_email, password=negative_name)
        with testit.step('Должна быть ошибка "Пользователь с таким логином и паролем не найден"'):
            page.should_be_error_message_text("Пользователь с таким логином и паролем не найден")
