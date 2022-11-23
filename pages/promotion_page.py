from .base_page import BasePage
from .locators.promotion_page import PromotionPageLocators
import random
from playwright.sync_api import expect, Locator


class PromotionPage(BasePage):

    def should_be_visible_price(self):
        expect(self.page.locator(PromotionPageLocators.PRISE_TEXT_LINK)).to_be_visible()

    def should_be_start_and_end_of_promotion(self):
        start_of_promotion = self.page.locator(PromotionPageLocators.START_OF_PROMOTION_DATE_LINK)
        end_of_promotion = self.page.locator(PromotionPageLocators.END_OF_PROMOTION_DATE_LINK)
        expect(start_of_promotion).to_be_visible()
        expect(end_of_promotion).to_be_visible()

    def should_be_visible_photos(self):
        photo_slider = self.page.locator(PromotionPageLocators.PHOTO_SLIDER_LINK)
        expect(photo_slider).to_be_visible()

    def click_to_active_photo(self):
        active_photo = self.page.locator(PromotionPageLocators.ACTIVE_PHOTO_LINK)
        active_photo.click()

    def should_be_visible_popup_photos(self):
        expect(self.page.locator(PromotionPageLocators.POPUP_PHOTO_SLIDER_LINK)).to_be_visible()

    def should_be_visible_recommended_slider(self):
        recommended_slider = self.page.locator(PromotionPageLocators.RECOMMENDED_PROMOTIONS_SLIDER_LINK)
        recommended_slider.scroll_into_view_if_needed()
        expect(recommended_slider).to_be_visible()

    def get_random_promotion_from_recommended(self) -> Locator:
        recommended_list = self.page.locator(PromotionPageLocators.RECOMMENDED_PROMOTIONS)
        random_num = random.randint(1, (recommended_list.count() - 1))
        random_promotion = self.page.locator(PromotionPageLocators.RECOMMENDED_PROMOTIONS).nth(random_num)
        return random_promotion

    def should_be_visible_promotion_title(self):
        expect(self.page.locator(PromotionPageLocators.PROMOTION_TITLE)).to_be_visible()

    def should_be_visible_promotion_conditions(self):
        expect(self.page.get_by_text(PromotionPageLocators.PROMOTION_CONDITIONS_BUTTON))
        expect(self.page.locator(f'id={PromotionPageLocators.PROMOTION_CONDITIONS_TEXT}')).not_to_be_empty()

    def should_be_visible_promotion_description(self):
        expect(self.page.get_by_text(PromotionPageLocators.PROMOTION_DESCRIPTION_BUTTON))
        expect(self.page.locator(f'id={PromotionPageLocators.PROMOTION_DESCRIPTION_TEXT}')).not_to_be_empty()

    def go_to_description(self):
        description_button = self.page.locator('span').filter(
            has_text=PromotionPageLocators.PROMOTION_DESCRIPTION_BUTTON)
        description_button.click()
