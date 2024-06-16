from selenium.webdriver.common.by import By


class BasePageLocators:

    ACCOUNT_BUTTON = (By.XPATH, ".//*[text()='Личный Кабинет']")
    LOGIN_EMAIL_INPUT = (By.XPATH, ".//*[@name='name']")
    ORDER_FEED = By.XPATH, '//p[text()="Лента Заказов"]/parent::a'
    PASSWORD_ACTIVE = (
        By.XPATH, ".//*[@class='input pr-6 pl-6 input_type_text input_size_default input_status_active']")
    LOGIN_PASSWORD_INPUT = (By.XPATH, ".//*[@name='Пароль']")
    CONSTRUCTOR_BUTTON = (By.XPATH, ".//*[text()='Конструктор']")

