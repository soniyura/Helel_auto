import pytest
import requests
from random import randint

@pytest.fixture
def message():
    print("initial test run")
    return 100

@pytest.fixture
def generator_0():
    return randint(100, 200)