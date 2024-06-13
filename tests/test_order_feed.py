import allure
import pytest
from constants.urls import Urls
from pages.order_page import OrderPage
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage
from locators.order_page_locators import OrderPageLocators


class TestOrderFeed:
    @allure.title('Тест: Открытие всплывающего окна с деталями заказа')
    @allure.description('Проверяет, что при клике на заказ открывается всплывающее окно с деталями заказа')
    def test_open_order_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to_url(Urls.BASE_URL)
        main_page.navigate_to_order_feed()
        order_page = OrderPage(driver)
        order_page.click_to_order()
        assert order_page.get_order_info() == 'Cостав'

    @allure.title('Тест: Отображение заказов пользователя в ленте заказов')
    @allure.description(
        'Проверяет, что заказы пользователя из раздела "История заказов" отображаются на странице "Лента заказов"')
    def test_user_orders_displayed_in_order_feed(self, driver, user):
        order_page = OrderPage(driver)
        order_page.navigate_to_url(Urls.LOGIN)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.login_account(user)
        main_page = MainPage(driver)
        main_page.add_ingredient_to_constructor()
        main_page.click_place_order_button()
        order_number = order_page.get_num_order()
        main_page.close_popup()
        main_page.navigate_to_order_feed()
        order_page = OrderPage(driver)
        feed_orders = order_page.get_num_order()
        assert str(order_number) in feed_orders, 'Заказ пользователя не отображается в Ленте заказов'
        personal_account_page.go_to_personal_account()
        personal_account_page.go_to_order_history()
        assert order_page.find_element_by_order_number(
            order_number), 'Заказ пользователя не отображается в Истории заказов'


    @allure.title('Тест: Отображение номера заказа в разделе "В работе" после оформления')
    @allure.description('Проверяет, что после оформления заказа его номер появляется в разделе "В работе"')
    def test_order_number_displayed_in_in_progress_section(driver, user):
        main_page = MainPage(driver)
        main_page.navigate_to_url(Urls.LOGIN)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.login_account(user)
        main_page.add_ingredient_to_constructor()
        main_page.click_place_order_button()
        order_page = OrderPage(driver)
        order_num = order_page.get_num_order()
        main_page.close_popup()
        order_page.navigate_to_url(Urls.FEED)
        in_progress_orders = order_page.get_in_progress_orders()
        assert f"0{order_num}" in in_progress_orders, "Номер заказа не отображается в разделе 'В работе'"


    @allure.title('Тест: Увеличение счетчика "Выполнено за сегодня" при создании нового заказа')
    @allure.description('Проверяет, что при создании нового заказа счетчик "Выполнено за сегодня" увеличивается')
    @pytest.mark.parametrize('counter', [OrderPageLocators.TODAY_ORDERS, OrderPageLocators.ALL_ORDERS])
    def test_daily_completed_orders_counter_increase(self, driver, user, counter):
        order_page = OrderPage(driver)
        order_page.navigate_to_url(Urls.FEED)
        result1 = order_page.get_counter_value(OrderPageLocators.TODAY_ORDERS)
        order_page.navigate_to_url(Urls.LOGIN)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.login_account(user)
        main_page = MainPage(driver)
        main_page.add_ingredient_to_constructor()
        main_page.click_place_order_button()
        order_page.navigate_to_url(Urls.FEED)
        result2 = order_page.get_counter_value(counter)
        assert int(result2) > int(result1)

