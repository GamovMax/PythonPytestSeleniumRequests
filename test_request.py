import pytest
import requests


class TestAPI:

    @pytest.fixture(autouse=True)
    def browser_setup_and_teardown(self):
        # Установка базового URL для API
        self.base_url = "https://jsonplaceholder.typicode.com"
        yield

    def test_get_first(self):
        # Выполнение GET-запроса к API
        response = requests.get(self.base_url + "/posts/1")

        # Проверка статус-кода ответа
        status_code = response.status_code
        print("\n\ntest_get_first\nStatus code:", status_code)

    def test_get_second(self):
        # Отправляем GET-запрос на /posts/1 и ожидаем HTTP-код 200
        response = requests.get(self.base_url + "/posts/1")
        response.raise_for_status()  # Проверка статус-кода ответа

    def test_get_third(self):
        # Отправляем GET-запрос на /posts/1 и проверяем, что userId равен 1
        response = requests.get(self.base_url + "/posts/1")
        json_response = response.json()
        assert json_response["userId"] == 1

    def test_post(self):
        # Отправляем POST-запрос на /posts и проверяем, что возвращается HTTP-код 201 (Created)
        response = requests.post(self.base_url + "/posts", json={"title": "foo", "body": "bar", "userId": 1})
        response.raise_for_status()  # Проверка статус-кода ответа

    def test_del(self):
        # Отправка DELETE запроса
        response = requests.delete(self.base_url + "/posts/1")
        # Проверка статус-кода ответа
        response.raise_for_status()

    def test_put(self):
        request_data = {"title": "New Title", "body": "New Body", "userId": 1}

        response = requests.put(self.base_url + "/posts/1", json=request_data)
        response.raise_for_status()  # Проверка статус-кода ответа

    def test_get_json(self):
        response = requests.get(self.base_url + "/posts/1")

        json_response = response.json()
        print("\n\ntest_get_json\nJson:",json_response)

    def test_option(self):
        response = requests.options(self.base_url + "/posts")

        print("\n\ntest_option\nResponse code:", response.status_code)
        print("Allowed methods:", response.headers.get("Allow"))

    def test_head(self):
        response = requests.head(self.base_url + "/posts")

        print("\n\ntest_head\nResponse code:", response.status_code)
        print("Content-Type:", response.headers.get("Content-Type"))
        print("Response time:", response.elapsed.total_seconds() * 1000, "ms")

    def test_patch(self):
        request_data = {"title": "Updated title"}

        response = requests.patch(self.base_url + "/posts/1", json=request_data)

        print("\n\ntest_patch\nResponse code:", response.status_code)
        print("Response body:", response.text)
