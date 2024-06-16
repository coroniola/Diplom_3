from selenium.webdriver.common.by import By

from locators.base_page_locators import BasePageLocators


class RecoveryPasswordPageLocators(BasePageLocators):
    FORGOT_PASS_BTN = (By.XPATH, ".//*[@href='/forgot-password']")
    RECOVERY_PASS_BTN = (By.XPATH, ".//*[text()='Восстановить']")
    EMAIL_INPUT = (By.XPATH, ".//*[@class='text input__textfield text_type_main-default']")
    LOGIN_BTN = (By.XPATH, ".//*[text()='Войти']")
    SAVE_BTN = (By.XPATH, ".//*[text()='Сохранить']")
    SHOW_PASS_BTN = (By.XPATH, ".//*[@class='input__icon input__icon-action']")