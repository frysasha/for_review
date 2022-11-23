import pytest
from playwright.sync_api import Page
import testit
from pages.base_page import Catalog
import time


class TestBasePageViewCatalog:
    @testit.workItemIds(30)
    @testit.externalId('test_user_can_see_price_photo_discount')
    @testit.labels('e2e', 'ui', 'auto')
    def test_user_can_see_price_photo_discount(self, page: Page):
        """Пользователь заходит на главную страницу и видит фото, цену, скидку акции"""
        page = Catalog(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step('Получение рандомной акции'):
            promotion = page.get_random_promotion()
        with testit.step(f'Должна быть видна цена акции {promotion.get_attribute("href")} из каталога'):
            page.should_be_visible_promotion_price(promotion)
        with testit.step(f'Должна быть видна фото акции {promotion.get_attribute("href")} из каталога'):
            page.should_be_visible_promotion_photo(promotion)
        with testit.step(f'Должна быть видна скидка акции {promotion.get_attribute("href")} из каталога'):
            page.should_be_visible_promotion_discount(promotion)

    @testit.workItemIds(32)
    @testit.externalId(f'test_user_can_change_sorting_in_catalog')
    @testit.labels('e2e', 'ui', 'auto')
    @pytest.mark.parametrize("section", [
        '/services/', '/tours/', '/services/goods/'])
    @pytest.mark.parametrize('sorting', [
        ["Выбор пользователей", "Сначала дешёвые", "Сначала дорогие", "Новые",
         "Лидеры продаж", "Без сортировки"]])
    def test_user_can_change_sorting_in_catalog(self, section: str, sorting: list, page: Page):
        """Пользователь заходит в разделы 'Услуги', 'Туры', 'Товары по купонам' и меняет сортировку акций на
        'Выбор пользователей', 'Сначала дешёвые', 'Сначала дорогие', 'Новые', 'Лидеры продаж', 'Без сортировки'"""
        page = Catalog(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step(f'Переход в раздел {section} по ссылке в хедере'):
            page.go_to_section(section)
        for sort in sorting:
            with testit.step(f'Выбор сортировки {sort}'):
                page.change_sorting(sort)

    @testit.workItemIds(72)
    @testit.externalId(f'test_check_sorting_by_cheap_first')
    @testit.labels('e2e', 'ui', 'auto')
    @pytest.mark.parametrize("section", [
        '/services/', '/tours/', '/services/goods/'])
    def test_check_sorting_by_cheap_first(self, section: str, page: Page):
        """Проверка работы сортировки 'Сначала дешёвые' в разделах Услуги, Туры, Товары по купонам"""
        page = Catalog(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step(f'Переход в раздел {section} по ссылке в хедере'):
            page.go_to_section(section)
        with testit.step('Выбор сортировки "Сначала дешёвые"'):
            page.change_sorting('Сначала дешёвые')
        for i in range(1, 6):
            with testit.step(f'Проверка сортировки на странице №{i}'):
                page.check_sorting_by_cheap_first()
                page.go_to_pagination_next_page()

    @testit.workItemIds(71)
    @testit.externalId(f'test_check_sorting_by_expensive_first')
    @testit.labels('e2e', 'ui', 'auto')
    @pytest.mark.parametrize("section", [
        '/services/', '/tours/', '/services/goods/'])
    def test_check_sorting_by_expensive_first(self, section: str, page: Page):
        """Проверка работы сортировки 'Сначала дорогие' в разделе Услуги, Туры, Товары по купонам"""
        page = Catalog(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step(f'Переход в раздел {section} по ссылке в хедере'):
            page.go_to_section(section)
        with testit.step('Выбор сортировки "Сначала дорогие"'):
            page.change_sorting('Сначала дорогие')
        for page_num in range(1, 6):
            with testit.step(f'Проверка сортировки на странице №{page_num}'):
                page.check_sorting_by_expensive_first()
                page.go_to_pagination_next_page()

    @testit.workItemIds(86)
    @testit.externalId(f'test_check_sorting_by_user_choice')
    @testit.labels('e2e', 'ui', 'auto')
    @pytest.mark.parametrize("section", [
        '/services/', '/tours/', '/services/goods/'])
    def test_check_sorting_by_user_choice(self, section: str, page: Page):
        """Проверка работы сортировки 'Выбор пользователей' в разделе Услуги, Туры, Товары по купонам"""
        page = Catalog(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step(f'Переход в раздел {section} по ссылке в хедере'):
            page.go_to_section(section)
        with testit.step('Выбор сортировки "Выбор пользователей"'):
            page.change_sorting('Выбор пользователей')
        # TODO: Сделать проверку сортировки

    @testit.workItemIds(56)
    @testit.externalId(f'test_promotion_search')
    @testit.labels('e2e', 'ui', 'auto')
    def test_promotion_search(self, page: Page):
        """Поиск акции через поисковую строку"""
        page = Catalog(page)
        with testit.step(f'Открытие главной страницы {page.base_url}'):
            page.open()
        with testit.step('Получение рандомной акции'):
            promotion = page.get_random_promotion()
            promotion_title = page.get_promotion_title_from_catalog(promotion)
            promotion_href_link = page.get_promotion_href_link(promotion)
        with testit.step(f'Ввод названия случайной акции в поисковую строку - {promotion_title}'):
            page.enter_text_into_search(promotion_title)
        with testit.step('Нажать кнопку поиск'):
            page.search_click()
        with testit.step('Проверка, что найдена введённая акция в поисковую строку'):
            page.check_promotion_after_search(promotion_href_link)
