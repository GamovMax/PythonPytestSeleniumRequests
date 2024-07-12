import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


class TestStepik148:

    @pytest.fixture(autouse=True)
    def driver_setup_and_teardown(self):
        options = Options()
        options.add_argument("--no-sandbox")
        options.add_argument("--disable-dev-shm-usage")
        options.add_argument("--window-size=1920,1080")
        options.add_argument("--disable-blink-features=AutomationControlled")
        options.add_argument(
            "--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

        # Добавляем опции в браузер
        self.driver = webdriver.Chrome(options=options)
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        yield
        self.driver.close()
        self.driver.quit()

    def test_cookies_first(self):
        self.driver.get("https://www.google.com/")
        self.driver.add_cookie({
            'name': 'username',
            'value': 'user123'
        })
        self.driver.refresh()
        # Получаем куки "username"
        cookie = self.driver.get_cookie("username")
        # Проверяем, что куки "username" существует и ее значение соответствует "user123"
        assert cookie is not None
        assert cookie['value'] == 'user123'
        print("\n", self.driver.get_cookie("username"))

    def test_cookies_second(self):
        self.driver.get("https://www.google.com/")
        self.driver.add_cookie({
            'name': 'username',
            'value': 'user123'
        })
        self.driver.delete_cookie("username")
        self.driver.refresh()
        # Получаем куки "username"
        cookie = self.driver.get_cookie("username")
        # Проверяем, что куки "username" не существует
        assert cookie is None
