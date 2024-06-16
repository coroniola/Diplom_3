from selenium.webdriver.common.by import By
from locators.base_page_locators import BasePageLocators


class OrderPageLocators(BasePageLocators):
    ORDERS = (By.XPATH, ".//*[@class='OrderFeed_list__OLh59']")
    POP_UP_WINDOW_ORDER = (By.XPATH, ".//*[@class='Modal_modal_opened__3ISw4 Modal_modal__P3_V5']")
    NUM_ORDER = (By.XPATH, ".//*[@class='Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text "
                           "text_type_digits-large mb-8']")
    ORDER_N1 = By.XPATH, ".//div[contains(@class, 'OrderHistory_dataBox')]"
    ORDER_INFO = By.XPATH, "//p[text()= 'Cостав']"
    ALL_ORDERS = (By.XPATH, ".//p[text() = 'Выполнено за все время:']/following-sibling::p[@class = "
                            "'OrderFeed_number__2MbrQ text text_type_digits-large']")
    TODAY_ORDERS = (By.XPATH, "//div[last()]/p[@class='OrderFeed_number__2MbrQ text text_type_digits-large']")
    ORDER_IN_PROGRESS = (By.XPATH, "//ul[contains(@class, 'ListReady')]/li")
    ORDER_FEED_HEADER = (By.XPATH, '//h1[text()="Лента заказов"]')
    ORDER_NUMBER = (By.XPATH, ".//*[text()='#0{num_order}']")