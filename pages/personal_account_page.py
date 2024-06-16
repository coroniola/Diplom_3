import allure

from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


class PersonalAccountPage(BasePage):

    @allure.step("Нажимаем на кнопку Личный кабинет")
    def go_to_personal_account(self):
        self.click_element_when_clickable(PersonalAccountLocators.ACCOUNT_BUTTON)

    @allure.step("Авторизация")
    def login_account(self, data):
        self.input_text(PersonalAccountLocators.LOGIN_EMAIL_INPUT, data["email"])
        self.input_text(PersonalAccountLocators.LOGIN_PASSWORD_INPUT, data["password"])
        enter_to_account_button = self.wait_for_element_clickable(PersonalAccountLocators.LOGIN_BTN)
        self.execute_script("arguments[0].click();", enter_to_account_button)

    @allure.step("Переходим в историю")
    def go_to_order_history(self):
        list_history = self.wait_for_element_visible(PersonalAccountLocators.ORDER_HISTORY)
        self.execute_script("arguments[0].click();", list_history)

    @allure.step("Ищем и нажимаем на кнопку Выход из аккаунта")
    def logout_account(self):
        self.click_element_when_clickable(PersonalAccountLocators.LOGOUT_BTN)

    @allure.step("Получаем аттрибут кнопки история заказов")
    def get_the_order_history_button_attribute(self):
        return self.get_attribute(PersonalAccountLocators.ORDER_HISTORY, "aria-current")

    @allure.step("Ищем кнопку войти в аккаунт")
    def find_login_button(self):
        return self.wait_for_element_clickable(PersonalAccountLocators.LOGIN_BTN)

