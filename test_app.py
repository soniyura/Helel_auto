import requests
import pytest


# створення файлу логування
def save_data(data):
    with open("log.txt", "a") as f:
        f.write(data)


class TestSuite:
    def setup_class(self):
        self.variable = []
        print("test started")

    def teardown_class(self):
        save_data(str(self.variable))

    # внесення даних в файл логування при старті
    def setup_method(self):
        save_data("started \n")

    # внесення даних в файл логування при в кінці
    def teardown_method(self):
        save_data("finished \n")

    def test_first_check(self):
        status = requests.get("https://google.com").status_code
        self.variable.append(status)
        assert status == 200

    def test_second_check(self):
        status = requests.get("https://google.com/_").status_code
        self.variable.append(status)
        assert status == 404

    def test_third_check(self):
        status = requests.get("https://wikipedia.com").status_code
        self.variable.append(status)
        assert status == 200