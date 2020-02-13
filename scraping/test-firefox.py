
import selenium
from selenium import webdriver

options = webdriver.FirefoxOptions()
options.add_argument('-headless')
options.log.level = "trace"
wdriver = selenium.webdriver.Firefox(options=options)
wdriver.implicitly_wait(10)

wdriver.get('https://www.google.com')
print(wdriver.page_source)
wdriver.close()