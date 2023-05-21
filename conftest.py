import pytest
import requests
from random import randint

@pytest.fixture
def message():
    print("initial test run")
    yield 100
    print("finalization")

@pytest.fixture
def generator_0():
    return randint(100, 200)