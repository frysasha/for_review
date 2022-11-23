from playwright.sync_api import Page
import testit
from pages.promotion_page import PromotionPage
import pytest


class TestViewPromotion:

    @testit.workItemIds(16)
    @testit.labels('e2e', 'ui', 'auto')
    @testit.externalId(f'test_user_can_see_price')
    def test_user_can_see_price(self, page: Page):
        """Пользователь заходит в рандомную акцию и видит цену купона"""
        page = PromotionPage(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step('Получение рандомной акции'):
            promotion = page.get_random_promotion()
        with testit.step(f'Открытие акции {promotion.get_attribute("href")}'):
            page.click_and_go_to_new_tab(promotion)
        with testit.step('Должна быть видна цена купона'):
            page.should_be_visible_price()

    @testit.workItemIds(23)
    @testit.labels('e2e', 'ui', 'auto')
    @testit.externalId(f'test_user_can_see_start_and_end_of_promotion')
    def test_user_can_see_start_and_end_of_promotion(self, page: Page):
        """Пользователь заходит в рандомную акцию и видит даты начала и окончания акции"""
        page = PromotionPage(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step('Получение рандомной акции'):
            promotion = page.get_random_promotion()
        with testit.step(f'Открытие акции {promotion.get_attribute("href")}'):
            page.click_and_go_to_new_tab(promotion)
        with testit.step('Должны быть видны даты начала и окончания акции'):
            page.should_be_start_and_end_of_promotion()

    @testit.workItemIds(21)
    @testit.labels('e2e', 'ui', 'auto')
    @testit.externalId(f'test_user_can_see_promotion_photos')
    def test_user_can_see_promotion_photos(self, page: Page):
        """Пользователь заходит в рандомную акцию и видит фотографии акции"""
        page = PromotionPage(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step('Получение рандомной акции'):
            promotion = page.get_random_promotion()
        with testit.step(f'Открытие акции {promotion.get_attribute("href")}'):
            page.click_and_go_to_new_tab(promotion)
        with testit.step('Должны быть видны фотографии акции'):
            page.should_be_visible_photos()
        with testit.step('Открытие и просмотр фотографий'):
            page.click_to_active_photo()
            page.should_be_visible_popup_photos()

    @testit.workItemIds(53)
    @testit.labels('e2e', 'ui', 'auto')
    @testit.externalId(f'test_user_can_see_recommended_section')
    def test_user_can_see_recommended_section(self, page: Page):
        """Пользователь заходит в рандомную акцию и видит секцию "Вам может понравиться" в конце страницы"""
        page = PromotionPage(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step('Получение рандомной акции'):
            promotion = page.get_random_promotion()
        with testit.step(f'Открытие акции {promotion.get_attribute("href")}'):
            page.click_and_go_to_new_tab(promotion)
        with testit.step('Должна быть видна секция "Вам может понравиться"'):
            page.should_be_visible_recommended_slider()
        with testit.step('Получение акции из рекоментаванных'):
            promotion = page.get_random_promotion_from_recommended()
        with testit.step(f'Открытие акции из рекомендованных'):
            page.click_and_go_to_new_tab(promotion)
        with testit.step(f'Должно быть видно название акции {page.page.url}'):
            page.should_be_visible_promotion_title()

    @testit.workItemIds(89)
    @testit.labels('e2e', 'ui', 'auto')
    @testit.externalId(f'test_user_can_see_promotion_conditions')
    def test_user_can_see_promotion_conditions(self, page: Page):
        """Пользователь заходит в рандомную акцию и видит условия акции"""
        page = PromotionPage(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step('Получение рандомной акции'):
            promotion = page.get_random_promotion()
        with testit.step(f'Открытие акции {promotion.get_attribute("href")}'):
            page.click_and_go_to_new_tab(promotion)
        with testit.step('Должны быть видны условия акции'):
            page.should_be_visible_promotion_conditions()

    @testit.workItemIds(90)
    @testit.labels('e2e', 'ui', 'auto')
    @testit.externalId(f'test_user_can_see_promotion_description')
    def test_user_can_see_promotion_description(self, page: Page):
        """Пользователь заходит в рандомную акцию и видит описание акции"""
        page = PromotionPage(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step('Получение рандомной акции'):
            promotion = page.get_random_promotion()
        with testit.step(f'Открытие акции {promotion.get_attribute("href")}'):
            page.click_and_go_to_new_tab(promotion)
        with testit.step(f'Переход в "Описание"'):
            page.go_to_description()
        with testit.step('Должно быть видно описание акции'):
            page.should_be_visible_promotion_conditions()
