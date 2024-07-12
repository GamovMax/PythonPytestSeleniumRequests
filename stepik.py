import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStepik:

    @pytest.fixture(autouse=True)
    def driver_setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://testautomationpractice.blogspot.com/")
        yield
        self.driver.close()
        self.driver.quit()

    def test_translate(self):
        self.driver.find_element(By.CLASS_NAME, "wikipedia-icon")
        self.driver.find_element(By.ID, "Wikipedia1_wikipedia-search-input")
        self.driver.find_element("class name", "wikipedia-search-button")
        self.driver.find_element(By.TAG_NAME, "label")
