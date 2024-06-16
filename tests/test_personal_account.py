import allure

from constants.urls import Urls
from pages.personal_account_page import PersonalAccountPage


class TestsPersonalAccount:
    @allure.title('Тест: Проверка перехода в личный кабинет')
    @allure.description('Проверяет, что пользователь может перейти в личный кабинет с главной страницы.')
    def test_go_to_personal_account(self, driver):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.navigate_to_url(Urls.BASE_URL)
        personal_account_page.go_to_personal_account()
        personal_account_page.wait_for_url(Urls.LOGIN)
        current_url = personal_account_page.get_current_url()
        assert current_url == Urls.LOGIN

    @allure.title('Тест: Проверка перехода в историю заказов')
    @allure.description('Проверяет, что пользователь может перейти в историю заказов после авторизации в личном кабинете.')
    def test_navigate_to_order_history(self, driver, user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.navigate_to_url(Urls.LOGIN)
        personal_account_page.login_account(user)
        personal_account_page.go_to_personal_account()
        personal_account_page.go_to_order_history()
        result = personal_account_page.get_the_order_history_button_attribute()
        assert result == "page"

    @allure.title('Тест: Проверка выхода из аккаунта')
    @allure.description('Проверяет, что пользователь может выйти из своего аккаунта и вернуться на страницу авторизации.')
    def test_logout_account(self, driver, user):
        personal_account_page = PersonalAccountPage(driver)
        personal_account_page.navigate_to_url(Urls.LOGIN)
        personal_account_page.login_account(user)
        personal_account_page.go_to_personal_account()
        personal_account_page.logout_account()
        assert personal_account_page.find_login_button()