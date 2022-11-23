from pages.base_page import BasePageLocators


class PromotionPageLocators(BasePageLocators):
    PRISE_TEXT_LINK = "//span[@class='aside__price_text']"
    OLD_PRISE_TEXT_LINK = "//span[@class='aside__price_old']"
    BUY_BUTTON_LINK = "//a[@class='aside__btn-buy']"
    DEAL_OFFER_TITLE_TEXT_LINK = "//h1[@class='deal-offer__title']"
    PHOTO_SLIDER_LINK = "//div[@class='slider-popup deal-offer__slider']"
    CONDITIONS_TEXT_LINK = "//li[@id='do-conditions']/div"
    START_OF_PROMOTION_DATE_LINK = \
        "//li[@class='deal-offer__info_date_item']/span[text()='Начало действия']/following-sibling::p"
    END_OF_PROMOTION_DATE_LINK = \
        "//li[@class='deal-offer__info_date_item']/span[text()='Окончание действия']/following-sibling::p"
    POPUP_PHOTO_SLIDER_LINK = \
        "//div[@class='ui__slider swiper-container swiper-container-horizontal swiper-container-autoheight']"
    ACTIVE_PHOTO_LINK = "//div[@class='swiper-slide swiper-slide-active']"
    RECOMMENDED_PROMOTIONS_SLIDER_LINK = \
        "//div[@class='swiper-container deal-offer__recommended_slider swiper-container-horizontal']/div"
    RECOMMENDED_PROMOTIONS = "//div[starts-with(@class, 'card-item swiper-slide')]"
    PROMOTION_TITLE = "//h1[@class='deal-offer__title']"
    PROMOTION_CONDITIONS_BUTTON = 'Условия'
    PROMOTION_CONDITIONS_TEXT = 'do-conditions'
    PROMOTION_DESCRIPTION_BUTTON = 'Описание'
    PROMOTION_DESCRIPTION_TEXT = 'do-description'