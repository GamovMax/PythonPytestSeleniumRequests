import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestStepik86:

    @pytest.fixture(autouse=True)
    def driver_setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()
        self.driver.quit()

    def test_demoqa(self):
        self.driver.get("https://demoqa.com/text-box")
        self.driver.find_element(By.CSS_SELECTOR, "div#userName-wrapper > div[class='col-md-9 col-sm-12'] > input").clear()
        self.driver.find_element(By.CSS_SELECTOR, "div#userName-wrapper > div[class='col-md-9 col-sm-12'] > input").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "div#userEmail-wrapper > div[class='col-md-9 col-sm-12'] > input").clear()
        self.driver.find_element(By.CSS_SELECTOR, "div#userEmail-wrapper > div[class='col-md-9 col-sm-12'] > input").send_keys("wqerwrq@dfsf.org")
        self.driver.find_element(By.CSS_SELECTOR, "div#currentAddress-wrapper > div[class='col-md-9 col-sm-12'] > textarea").clear()
        self.driver.find_element(By.CSS_SELECTOR, "div#currentAddress-wrapper > div[class='col-md-9 col-sm-12'] > textarea").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "div#permanentAddress-wrapper > div[class='col-md-9 col-sm-12'] > textarea").clear()
        self.driver.find_element(By.CSS_SELECTOR, "div#permanentAddress-wrapper > div[class='col-md-9 col-sm-12'] > textarea").send_keys("1")
        self.driver.find_element(By.CSS_SELECTOR, "button#submit").click()

    def test_herokuapp(self):
        self.driver.get("http://the-internet.herokuapp.com/status_codes")
        elements = self.driver.find_elements(By.XPATH, "//li/a")  # Находим все элементы
        for element in elements:  # Перебираем список элементов
            element.click()
            self.driver.back()
