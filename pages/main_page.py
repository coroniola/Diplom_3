import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators
from seletools.actions import drag_and_drop
from selenium.webdriver.common.action_chains import ActionChains


class MainPage(BasePage):
    @allure.step("Переходим к конструктору")
    def navigate_to_constructor(self):
        constructor_button = self.wait_for_element_clickable(MainPageLocators.CONSTRUCTOR_BUTTON)
        if constructor_button.is_displayed() and constructor_button.is_enabled():
            actions = ActionChains(self.driver)
            actions.move_to_element(constructor_button).click().perform()
        else:
            raise Exception("Кнопка 'Конструктор' не видима или недоступна для клика")

    @allure.step("Переходим на страницу ленты заказов")
    def navigate_to_order_feed(self):
        list_orders = self.wait_for_element_visible(MainPageLocators.ORDER_FEED)
        self.driver.execute_script("arguments[0].click();", list_orders)

    @allure.step("Нажимаем на ингредиент")
    def click_to_ingredient(self):
        list_ingridients = self.wait_for_element_visible(MainPageLocators.INGREDIENT)
        self.driver.execute_script("arguments[0].click();", list_ingridients )


    @allure.step("Закрываем всплывающее окно")
    def close_popup(self):
        list_close_pop_up_button = self.wait_for_element_visible(MainPageLocators.POP_UP_CLOSE_BTN)
        self.driver.execute_script("arguments[0].click();", list_close_pop_up_button)


    @allure.step('Получаем текст информации об ингредиенте')
    def get_ingredient_info_text(self):
        return self.get_element_text(MainPageLocators.INGREDIENT_INFO)

    @allure.step("Получаем текст всплывающего окна оформления заказ")
    def get_order_popup_text(self):
        return self.get_element_text(MainPageLocators.POP_UP_ORDER)

    @allure.step("Получаем класс кнопки закрытия всплывающего окна")
    def get_popup_close_button_class(self):
        return self.get_attribute(MainPageLocators.POP_UP_CLOSE_BTN, "class")

    @allure.step("Добавляем ингредиент в конструктор")
    def add_ingredient_to_constructor(self):
        ingredient = self.wait_for_element_clickable(MainPageLocators.INGREDIENT)
        add_to_order = self.wait_for_element_clickable(MainPageLocators.BURGER_CONSTRUCTOR)
        drag_and_drop(self.driver, ingredient, add_to_order)

    @allure.step("Нажимаем на кнопку 'Оформить заказ'")
    def click_place_order_button(self):
        list_button_place_an_order = self.wait_for_element_visible(MainPageLocators.PLACE_ORDER)
        self.driver.execute_script("arguments[0].click();", list_button_place_an_order)

    @allure.step("Получаем количество ингредиентов")
    def get_ingredient_count(self):
        return self.get_element_text(MainPageLocators.INGREDIENT_COUNTER)


