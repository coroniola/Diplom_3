import allure

from constants.urls import Urls
from pages.recovery_password_page import RecoveryPasswordPage


class TestsPasswordRecovery:
    @allure.title('Тест: Проверка перехода на страницу восстановления пароля')
    @allure.description(
        'Проверяет, что при клике на ссылку "Забыли пароль?" пользователь переходит на страницу восстановления пароля.')
    def test_navigate_to_password_recovery_page(self, driver):
        password_recovery_page = RecoveryPasswordPage(driver)
        password_recovery_page.navigate_to_url(Urls.LOGIN)
        password_recovery_page.navigate_to_password_recovery()
        current_url = password_recovery_page.get_current_url()
        assert current_url == Urls.FORGOT_PASSWORD

    @allure.title('Тест: Ввод почты и клик по кнопке «Восстановить»')
    @allure.description(
        'Проверяет, что пользователь может ввести email и нажать кнопку "Восстановить пароль", после чего переходит на страницу сброса пароля.')
    def test_recover_password(self, driver, user):
        password_recovery_page = RecoveryPasswordPage(driver)
        password_recovery_page.navigate_to_url(Urls.FORGOT_PASSWORD)
        password_recovery_page.enter_recovery_email(user["email"])
        password_recovery_page.click_recovery_button()
        password_recovery_page.wait_for_url(Urls.RESET_PASSWORD)
        current_url = password_recovery_page.get_current_url()
        assert current_url == Urls.RESET_PASSWORD

    @allure.title('Тест: Клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его.')
    @allure.description(
        'Проверяет, что при клике на кнопку "Показать пароль" на странице восстановления пароля, поле ввода пароля подсвечивается.')
    def test_highlight_password_field(self, driver, user):
        password_recovery_page = RecoveryPasswordPage(driver)
        password_recovery_page.navigate_to_url(Urls.FORGOT_PASSWORD)
        password_recovery_page.enter_recovery_email(user["email"])
        password_recovery_page.click_recovery_button()
        password_recovery_page.click_show_password_button()
        result = password_recovery_page.get_active_password_field_class()
        assert "status_active" in result