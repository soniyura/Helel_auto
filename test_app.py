import requests
import pytest

# створення файлу логування
def save_data(data):
    with open("log.txt", "a") as f:
        f.write(data)

class TestSuite:
    #внесення даних в файл логування при старті
    def setup(self):
        save_data("started \n")

    # внесення даних в файл логування при в кінці
    def teardown(self):
        save_data("finidhed \n")

    def test_first_check(self):
        status = requests.get("https://google.com").status_code
        assert  status == 200

    def test_second_check(self):
        status = requests.get("https://google.com/_").status_code
        assert  status == 404