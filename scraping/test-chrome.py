import selenium
from selenium import webdriver
from selenium.webdriver import Chrome

options = webdriver.ChromeOptions()
options.add_argument('--headless')
options.add_argument('--no-sandbox')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--disable-setuid-sandbox')
wdriver = webdriver.Chrome('chromedriver',options=options)
wdriver.implicitly_wait(10)

wdriver.get('https://www.google.com')
print(wdriver.page_source)
wdriver.close()
