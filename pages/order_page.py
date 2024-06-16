import time

import allure
from selenium.webdriver.common.by import By

from locators.order_page_locators import OrderPageLocators
from pages.base_page import BasePage


class OrderPage(BasePage):

    @allure.step("Нажимаем по заказ")
    def click_to_order(self):
        list_button_order = self.wait_for_element_visible(OrderPageLocators.ORDERS)
        self.execute_script("arguments[0].click();", list_button_order)

    @allure.step("Получаем номер заказа")
    def get_num_order(self):
        self.wait_for_element_clickable(OrderPageLocators.NUM_ORDER)
        self.wait_for_text_not_in_element(OrderPageLocators.NUM_ORDER, '9999')
        return self.get_element_text(OrderPageLocators.NUM_ORDER)

    @allure.step("Получем количество заказов за сегодня")
    def get_today_orders_count(self):
        return self.get_element_text(OrderPageLocators.TODAY_ORDERS)

    @allure.step("Получаем количество всех заказов")
    def get_total_orders_count(self):
        return self.get_element_text(OrderPageLocators.ALL_ORDERS)

    @allure.step("Получаем заказы в работе")
    def get_in_progress_orders(self):
        self.wait_for_element_clickable(OrderPageLocators.ORDER_IN_PROGRESS)
        self.wait_for_text_not_in_element(OrderPageLocators.ORDER_IN_PROGRESS, 'Все текущие заказы готовы!')
        return self.get_element_text(OrderPageLocators.ORDER_IN_PROGRESS)

    @allure.step("Ищем элемент по номеру заказа")
    def find_element_by_order_number(self, num_order):
        str_num_order = OrderPageLocators.ORDER_NUMBER
        str_num_order = (str_num_order[0], str_num_order[1].format(num_order=num_order))
        return self.wait_for_element_clickable(str_num_order)

    @allure.step('Получаем текст информации о заказе')
    def get_order_info(self):
        self.click_element(OrderPageLocators.ORDER_N1)
        return self.get_element_text(OrderPageLocators.ORDER_INFO)

    def get_counter_value(self, counter):
        self.wait_for_element_visible(OrderPageLocators.ORDER_FEED_HEADER)
        return self.get_element_text(counter)