from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class MainPageLocators(BasePageLocators):

    INGREDIENT = [By.XPATH, "//a[contains(@class, 'BurgerIngredient_ingredient_')][1]"]
    INGREDIENT_INFO = By.XPATH, ".//h2[text()= 'Детали ингредиента']"
    INGREDIENT_COUNTER = (By.XPATH, ".//ul[1]/a[1]/div[1]/p")
    PLACE_ORDER = (By.XPATH, ".//*[text()='Оформить заказ']")
    POP_UP_ORDER = (By.XPATH, ".//*[@class='undefined text text_type_main-medium mb-15']")
    POP_UP_ORDER_OPEN = (By.XPATH, ".//section[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    POP_UP_ORDER_CLOSE = (By.XPATH, './/div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]'
                                 '/following-sibling::button')
    POP_UP_CLOSE_BTN = (By.XPATH, ".//*[@class='Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK']")
    BURGER_CONSTRUCTOR = (By.XPATH, ".//*[@class='BurgerConstructor_basket__list__l9dp_']")