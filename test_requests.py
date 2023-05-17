import pytest
import requests

def test_requests():
    url = "https://google.com"
    resource = requests.get(url)
    assert resource == 200, f"failed with {url}"