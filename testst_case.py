import requests
from selenium import webdriver

options = webdriver.ChromeOptions()
options.add_argument('--ignore-ssl-errors=yes')
options.add_argument('--ignore-certificate-errors')

driver = webdriver.Remote(command_executor='http://localhost:4444/wd/hub',
                          options=options)

uri_variable = "Napoleon"
url = ["https://www.wikipedia.org/"]



# if response.status_code == 200:
#     print("pass")
# if response.status_code == 404:
#     print("error")

# data = response.text
# print(data)

# docker run -d -p 4444:4444 -p 5900:5900 -v /dev/shm:/dev/shm selenium/standalone-chrome-debug