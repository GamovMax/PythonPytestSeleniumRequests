import pytest
from selenium import webdriver


class TestStepik157:

    @pytest.fixture(autouse=True)
    def driver_setup_and_teardown(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.implicitly_wait(10)
        self.driver.get("https://demoqa.com/selectable")
        yield
        self.driver.close()
        self.driver.quit()

    def test_demoqa(self):
        self.driver.find_element("id", "demo-tab-grid").click()
        self.driver.find_element("css selector", "div#row1>li:nth-child(1)").click()
        self.driver.find_element("css selector", "div#row2>li:nth-child(2)").click()
        self.driver.find_element("css selector", "div#row3>li:nth-child(3)").click()

        assert "active" in self.driver.find_element("css selector", "div#row1>li:nth-child(1)").get_attribute("class"), "\n\nЧек-бокс 'One' не выбран\n\n"
        assert "active" in self.driver.find_element("css selector", "div#row2>li:nth-child(2)").get_attribute("class"), "\n\nЧек-бокс 'Five' не выбран\n\n"
        assert "active" in self.driver.find_element("css selector", "div#row3>li:nth-child(3)").get_attribute("class"), "\n\nЧек-бокс 'Nine' не выбран\n\n"

        self.driver.find_element("css selector", "div#row1>li:nth-child(1)").click()
        self.driver.find_element("css selector", "div#row2>li:nth-child(2)").click()
        self.driver.find_element("css selector", "div#row3>li:nth-child(3)").click()

        assert "active" not in self.driver.find_element("css selector", "div#row1>li:nth-child(1)").get_attribute("class"), "\n\nЧек-бокс 'One' выбран\n\n"
        assert "active" not in self.driver.find_element("css selector", "div#row2>li:nth-child(2)").get_attribute("class"), "\n\nЧек-бокс 'Five' выбран\n\n"
        assert "active" not in self.driver.find_element("css selector", "div#row3>li:nth-child(3)").get_attribute("class"), "\n\nЧек-бокс 'Nine' выбран\n\n"
