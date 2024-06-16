from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:
    def __init__(self, driver):
        driver.implicitly_wait(10)
        self.driver = driver

    def navigate_to_url(self, url):
        return self.driver.get(url)

    def wait_for_element_visible(self, locator):
        return WebDriverWait(self.driver, 10).until(ec.visibility_of_element_located(locator))

    def get_current_url(self):
        return self.driver.current_url

    def wait_for_url(self, url, time=10):
        return WebDriverWait(self.driver, time).until(ec.url_to_be(url))

    def click_element(self, locator):
        element = self.wait_for_element_visible(locator)
        ActionChains(self.driver).click(element).perform()

    def wait_for_element_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator))

    def wait_for_text_not_in_element(self, locator, template, time=10):
        return WebDriverWait(self.driver, time).until_not(ec.text_to_be_present_in_element(locator, template))

    def click_element_when_clickable(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).click()

    def input_text(self, locator, text, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).send_keys(text)

    def get_attribute(self, locator, attribute, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).get_attribute(attribute)

    def get_element_text(self, locator, time=10):
        return WebDriverWait(self.driver, time).until(ec.element_to_be_clickable(locator)).text


    def wait_url_changes(self, url):
        WebDriverWait(self.driver, 20).until(expected_conditions.url_changes(url))

    def move_to_and_click(self, element):
        actions = ActionChains(self.driver)
        actions.move_to_element(element).click().perform()

    def execute_script(self, script, *args):
        return self.driver.execute_script(script, *args)


