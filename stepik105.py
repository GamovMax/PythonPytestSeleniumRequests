import os
import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By


class TestStepik105:

    @pytest.fixture(autouse=True)
    def driver_setup_and_teardown(self):
        options = Options()
        preferences = {
            "download.default_directory": os.path.join(os.getcwd(), "downloads")
        }
        options.add_experimental_option("prefs", preferences)
        # Добавляем опции в браузер
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()
        self.driver.quit()

    def test_demoqa(self):
        self.driver.get("https://demoqa.com/upload-download")
        # Записываем поле ввода в переменную
        upload_file_field = self.driver.find_element(By.CSS_SELECTOR, "input#uploadFile")
        # Загружаем картинку
        upload_file_field.send_keys(os.path.join(os.getcwd(), "iceberg.jpg"))
        time.sleep(5)

    def test_herokuapp(self):
        self.driver.get("http://the-internet.herokuapp.com/download")
        elements = self.driver.find_elements(By.CSS_SELECTOR, "div.example>a")  # Находим все элементы
        for element in elements:  # Перебираем список элементов
            element.click()
