import allure

from pages.base_page import BasePage
from locators.personal_account_locators import PersonalAccountLocators


class RecoveryPasswordPage(BasePage):

    @allure.step("Ищем и нажимаем на ссылку Восстановить пароль")
    def navigate_to_password_recovery(self):
        self.click_element_when_clickable(PersonalAccountLocators.FORGOT_PASS_BTN)

    @allure.step("Вводим почту для восстановления пароля")
    def enter_recovery_email(self, email):
        self.input_text(PersonalAccountLocators.EMAIL_INPUT, email)

    @allure.step("Получение класса выделенного поля ввода пароля")
    def get_active_password_field_class(self):
        return self.get_attribute(PersonalAccountLocators.PASSWORD_ACTIVE, "class")
    @allure.step("Нажимаем на кнопку Восстановить")
    def click_recovery_button(self):
        list_recovery_button = self.wait_for_element_visible(PersonalAccountLocators.RECOVERY_PASS_BTN)
        self.execute_script("arguments[0].click();", list_recovery_button)

    @allure.step("Нажимаем на кнопку Показать пароль")
    def click_show_password_button(self):
        list_show_password_button = self.wait_for_element_visible(PersonalAccountLocators.SHOW_PASS_BTN)
        self.execute_script("arguments[0].click();", list_show_password_button)

