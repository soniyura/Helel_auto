import requests
from assertpy import assert_that

urls = ("https://www.google.com/s", "https://www.google.com/", "https://www.google.com/f")


def logs(url):
    print(f"URL : {url}")


# for url in urls:
#     resourse = requests.get(url)
#     assert resourse == 200, logs(url)
#     #assert_that(resourse,"massege").is_equal_to(200)


def url_check(var):
    resourse = requests.get(var)
    resourse = resourse.status_code
    if resourse == 200:
        return 1
    else:
        return 3


for i in urls:
    print(url_check(i))


def test_url_check(data="https://www.google.com/"):
    assert url_check(data) == 1


def test_url_check(data="https://www.google.com/s"):
    assert url_check(data) == 3
