import pytest
import requests


@pytest.mark.slow
@pytest.mark.all
def test_requests(message):
    url = "https://google.com"
    resource = requests.get(url).status_code
    with pytest.raises(ZeroDivisionError):
        var = 1 / 0
    assert resource == 200, f"failed with {url}"


"""мітка для запуску тестів, ми можемо обирати якийсь конкретний набір тестів 
при запуску обираючи метку, а мітку  ми можемо поставити на декількох тестах,
команда бля запуску - pytest test_requests.py -s -m all
де all це якась мітка  яка стоїть на певних тестах"""


@pytest.mark.parametrize("url", ["https://google.com",
                                 "https://vikipedia.com",
                                 "https://wikipedia.com",
                                 "https://google.com/_"])
@pytest.mark.smoke
@pytest.mark.multy
@pytest.mark.all
def test_requests_200(url):
    resource = requests.get(url).status_code
    assert resource == 200, f"failed with {url}"


@pytest.mark.smoke
@pytest.mark.all
def test_standalone(message, generator_0):
    assert message + generator_0 > 210
