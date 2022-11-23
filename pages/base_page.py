import re

from .locators.base_page import BasePageLocators, CatalogLocators
from .locators.login_page import LoginFormLocators
from .locators.registration_page import RegisterFormLocators
from .locators.promotion_page import PromotionPageLocators
from playwright.sync_api import Page, expect, Locator, ElementHandle

import random


class BasePage:

    def __init__(self, page: Page, timeout_sec=20):
        self.context = page.context
        self.page = page
        self.page.set_default_timeout(timeout_sec * 1000)
        self.base_url = 'https://www.biglion.ru/'

    def open(self, url=None):
        if url:
            self.page.goto(url)
        else:
            self.page.goto(self.base_url)

    @staticmethod
    def click_to(selector):
        selector.click()

    def check_js_errors(self):
        pass

    def go_to_login_page(self):
        login_button_link = self.page.locator(BasePageLocators.LOGIN_BUTTON_LINK)
        login_button_link.click()
        login_form = self.page.locator(LoginFormLocators.LOGIN_FORM_LINK)
        expect(login_form).to_be_visible()

    def go_to_registration_page(self):
        registration_button_link = self.page.locator(BasePageLocators.REGISTRATION_BUTTON_LINK)
        registration_button_link.click()
        registration_form = self.page.locator(RegisterFormLocators.REGISTRATION_FROM_LINK)
        expect(registration_form).to_be_visible()

    def should_be_user_avatar(self):
        expect(self.page.locator(BasePageLocators.USER_AVATAR_LINK)).to_be_visible()

    def exit_reg_auth_form_page(self):
        exit_form_button = self.page.locator(RegisterFormLocators.EXIT_REG_AUTH_FORM_BUTTON)
        exit_form_button.click()

    def click_and_go_to_new_tab(self, locator: Locator):
        with self.context.expect_page() as new_tab_info:
            locator.click()
        new_tab = new_tab_info.value
        self.page = new_tab

    def get_random_promotion(self) -> Locator:
        promotions_on_page = self.page.locator(PromotionPageLocators.DEAL_ITEMS_LINK)
        random_num = random.randint(1, promotions_on_page.count())
        random_promotion = self.page.locator(PromotionPageLocators.DEAL_ITEMS_LINK + f'[{random_num}]')
        return random_promotion

    def go_to_section(self, section: str):
        section_button = self.page.locator(BasePageLocators.get_header_section_link(section))
        section_button.click()

    def search_click(self):
        self.page.locator(BasePageLocators.SEARCH_BUTTON_LINK).click()
        expect(self.page.locator(BasePageLocators.SEARCH_PRELOADER_LINK)).to_be_hidden()

    def enter_text_into_search(self, text: str):
        self.page.locator(BasePageLocators.SEARCH_INPUT_LINK).fill(text)


class Catalog(BasePage):
    @staticmethod
    def should_be_visible_promotion_price(promotion: Locator):
        price_locator = CatalogLocators.get_promotion_price_locator(promotion)
        expect(price_locator).to_be_visible()

    @staticmethod
    def should_be_visible_promotion_photo(promotion: Locator):
        price_locator = CatalogLocators.get_promotion_photo_locator(promotion)
        expect(price_locator).to_be_visible()

    @staticmethod
    def should_be_visible_promotion_discount(promotion: Locator):
        price_locator = CatalogLocators.get_promotion_discount_locator(promotion)
        expect(price_locator).to_be_visible()

    def change_sorting(self, sorting: str):
        sorting_list_button = self.page.locator(CatalogLocators.SORTING_LIST_LINK).get_by_role('button')
        sorting_list_button.click()
        sorting_button = self.page.locator(CatalogLocators.get_sorting_button_locator(sorting))
        sorting_button.click()
        expect(self.page.locator(BasePageLocators.OVERLAY_LINK)).to_be_hidden(timeout=10000)

    def check_sorting_by_cheap_first(self):
        service_promotions_list = self.page.locator(CatalogLocators.SERVICES_DEALS_LINK)
        price_list = service_promotions_list.locator("//span[@class='dc__price_new']")
        clean_price_list = [int((re.sub("[^0-9]", '', i))) for i in price_list.all_inner_texts()]
        assert clean_price_list == sorted(clean_price_list), 'Цена не по возрастанию'

    def check_sorting_by_expensive_first(self):
        service_promotions_list = self.page.locator(CatalogLocators.SERVICES_DEALS_LINK)
        price_list = service_promotions_list.locator("//span[@class='dc__price_new']")
        clean_price_list = [int((re.sub("[^0-9]", '', i))) for i in price_list.all_inner_texts()]
        assert clean_price_list == sorted(clean_price_list, reverse=True), 'Цена не по Убыванию'

    def check_sorting_in_n_pages(self, n: int):
        max_pages = int(self.page.locator(CatalogLocators.PAGINATION_LAST_PAGE).text_content().strip())
        next_page = self.page.locator(CatalogLocators.PAGINATION_NEXT_PAGE)
        if n <= max_pages:
            for _ in range(n):
                self.check_sorting_by_expensive_first()
                next_page.click()
        else:
            for _ in range(max_pages):
                self.check_sorting_by_expensive_first()
                next_page.click()

    def go_to_pagination_next_page(self):
        next_page_button = self.page.locator(CatalogLocators.PAGINATION_NEXT_PAGE)
        if next_page_button.is_visible():
            next_page_button.click()

    @staticmethod
    def get_promotion_title_from_catalog(locator: Locator) -> str:
        return str(locator.get_by_role('img').get_attribute('alt')).replace(u'\xa0', u' ')

    @staticmethod
    def get_promotion_href_link(promotion: Locator) -> str:
        return promotion.get_attribute('href')

    def check_promotion_after_search(self, href_link: str):
        promotion_on_page_link = self.page.locator(BasePageLocators.DEAL_ITEMS_LINK)
        expect(promotion_on_page_link).to_have_attribute('href', href_link)
