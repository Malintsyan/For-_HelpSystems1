from selenium import webdriver
from selenium.webdriver.common.by import By
import pytest
from x_path import X_path


def find_element(text_from_amazon):
    i = "iPhone"
    if i in text_from_amazon:
        return i


class TestIPhon:
    @pytest.fixture()
    def test_amazon(self):
        self.driver = webdriver.Chrome()
        self.driver.get(X_path.amazon)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.search_input = self.driver.find_element(By.XPATH, X_path.input_search_text)
        self.search_input.send_keys('iPhone')
        self.search_click = self.driver.find_element(By.XPATH, X_path.click_search)
        self.search_click.click()
        yield
        self.driver.close()
        self.driver.quit()

    def test_first(self, test_amazon):
        element1 = self.driver.find_element(By.XPATH, X_path.element1_text).text
        check_word = find_element(element1)
        assert check_word == "iPhone"

    def test_second(self, test_amazon):
        element2 = self.driver.find_element(By.XPATH, X_path.element2_text).text
        check_word = find_element(element2)
        assert check_word == "iPhone"

    def test_third(self, test_amazon):
        element3 = self.driver.find_element(By.XPATH, X_path.element3_text).text
        check_word = find_element(element3)
        assert check_word == "iPhone"
