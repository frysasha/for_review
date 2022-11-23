from playwright.sync_api import Locator


class BasePageLocators:
    LOGIN_BUTTON_LINK = "//a[text()='Вход']"
    REGISTRATION_BUTTON_LINK = "//a[text()='Регистрация']"
    CHATS_BUTTON_LINK = "//button[@class='chats__button']"
    SUBMIT_BUTTON_LINK = "//button[@data-qa='submit']"
    USER_AVATAR_LINK = "//div[@class='user__avatar']"
    RECAPTCHA_LINK = "//div[@id='rc-imageselect']"
    DEALS_LIST_LINK = "//div[@class='h__deals_list']"
    #DEAL_ITEMS_LINK = "(//div[@class='card-item h__deals_list_item']/a[starts-with(@href, '/deals/')])"
    DEAL_ITEMS_LINK = "(//div[starts-with(@class, 'card-item ')]/a[starts-with(@href, '/deals/')])"
    HEADER_SERVICES_LINK = "//a[@href='/services/' and @class='header__nav_top_link']"
    HEADER_TOURS_LINK = "//a[@href='/tours/' and @class='header__nav_top_link']"
    HEADER_SERVICES_GOODS_LINK = "//a[@href='/services/goods/' and @class='header__nav_top_link']"
    OVERLAY_LINK = "//div[@class='lion__overlay bservices__preloader']"
    SEARCH_BUTTON_LINK = "//button[@data-qa='search_button']"
    SEARCH_INPUT_LINK = "//input[@data-qa='search_input']"
    SEARCH_PRELOADER_LINK = '//div[@class="search__preloader"]'

    @staticmethod
    def get_header_section_link(section: str) -> str:
        return f"//a[@href='{section}' and @class='header__nav_top_link']"


class CatalogLocators(BasePageLocators):
    SORTING_LIST_LINK = "//div[@class='bservices__sort']"
    SERVICES_DEALS_LINK = "//div[@class='card-item item bservices__deals_item']"
    PAGINATION_NEXT_PAGE = "(//*[@class='bgln__icon pagination__item_arrow'])[2]"
    PAGINATION_PREV_PAGE = "(//*[@class='bgln__icon pagination__item_arrow'])[1]"
    PAGINATION_LAST_PAGE = "//li[@class='pagination__item -last']"

    @staticmethod
    def get_sorting_button_locator(sorting_str: str) -> str:
        return f"//li[starts-with(text(), '{sorting_str}')]"

    @staticmethod
    def get_promotion_price_locator(promotion) -> Locator:
        return promotion.locator('//following-sibling::div').locator("//span[@class='dc__price_new']")

    @staticmethod
    def get_promotion_photo_locator(promotion: Locator) -> Locator:
        return promotion.locator('//img')

    @staticmethod
    def get_promotion_discount_locator(promotion: Locator) -> Locator:
        return promotion.locator("//span[@class='card-item__discount']")
