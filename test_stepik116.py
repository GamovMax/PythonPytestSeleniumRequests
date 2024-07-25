import pytest
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


class TestStepik116:

    @pytest.fixture(autouse=True)
    def driver_setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://chercher.tech/practice/explicit-wait-sample-selenium-webdriver")
        yield
        self.driver.close()
        self.driver.quit()

    def test_chercher(self):
        self.wait = WebDriverWait(self.driver, 15, poll_frequency=1)

        self.driver.find_element("id", "populate-text").click()
        CHANGE_TEXT_BUTTON = ("css selector", "h2#h2")
        self.driver.find_element(*CHANGE_TEXT_BUTTON)
        self.wait.until(EC.text_to_be_present_in_element(CHANGE_TEXT_BUTTON, "Selenium Webdriver"))  # Ждем пока текст в элементе не сменится на указанный

        self.driver.find_element("id", "display-other-button").click()
        DISPLAY_BUTTON = ("id", "hidden")
        self.wait.until(EC.visibility_of_element_located(DISPLAY_BUTTON))  # Ждем пока элемент станет видимым

        self.driver.find_element("id", "enable-button").click()
        ENABLE_BUTTON = ("id", "disable")
        self.wait.until(EC.element_to_be_clickable(ENABLE_BUTTON))  # Ждем пока кнопка станет кликабельной

        self.driver.find_element("id", "alert").click()
        self.wait.until(EC.alert_is_present())  # Ждем появления всплывающего окна (алерта(Alert))
