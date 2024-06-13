import allure

from constants.urls import Urls
from pages.main_page import MainPage
from pages.personal_account_page import PersonalAccountPage



class TestsMainPage:

    @allure.title('Тест Переход на страницу заказов по нажатию кнопки "Лента заказов"')
    @allure.description('Проверка перехода по клику на «Лента заказов»')
    def test_navigate_to_order_feed(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to_url(Urls.BASE_URL)
        main_page.navigate_to_order_feed()
        current_url = main_page.get_current_url()
        assert current_url == Urls.FEED

    @allure.title('Тест Переход в конструктор')
    @allure.description('Проверка перехода по клику на «Конструктор»')
    def test_navigate_to_constructor(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to_url(Urls.LOGIN)
        main_page.navigate_to_constructor()
        current_url = main_page.get_current_url()
        assert current_url == Urls.BASE_URL


    @allure.title('Тест Открытие всплывающего окна с деталями об ингридиенте')
    @allure.description(
        'Проверка, что при клике на ингредиент открывается всплывающее окно с соответствующими деталями')
    def test_open_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to_url(Urls.BASE_URL)
        main_page.click_to_ingredient()
        assert main_page.get_ingredient_info_text() == "Детали ингредиента"

    @allure.title('Тест закрытия всплывающего окна с деталями')
    @allure.description(
        'Проверка, что при клике на кнопку закрытия всплывающее окно с деталями ингредиента успешно закрывается')
    def test_close_ingredient_details_popup(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to_url(Urls.BASE_URL)
        main_page.click_to_ingredient()
        main_page.close_popup()
        result = main_page.get_popup_close_button_class()
        assert "opened" not in result

    @allure.title('Тест: Проверка счетчика ингредиентов в конструкторе')
    @allure.description(
        'Проверяет, что при перетаскивании ингредиента в конструктор, счетчик ингредиентов отображает корректное значение')
    def test_verify_ingredient_counter(self, driver):
        main_page = MainPage(driver)
        main_page.navigate_to_url(Urls.BASE_URL)
        main_page.add_ingredient_to_constructor()
        result = main_page.get_ingredient_count()
        assert result == "2"

    @allure.title('Тест: Оформление заказа')
    @allure.description(
        'Проверка, что авторизованный пользователь может успешно оформить заказ')
    def test_checkout(self, driver, user):
        main_page = MainPage(driver)
        main_page.navigate_to_url(Urls.LOGIN)
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.login_account(user)
        main_page = MainPage(driver)
        main_page.add_ingredient_to_constructor()
        main_page.click_place_order_button()
        result = main_page.get_order_popup_text()
        assert result == "идентификатор заказа"