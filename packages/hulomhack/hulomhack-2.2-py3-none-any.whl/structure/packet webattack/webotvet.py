from selenium import webdriver

def web_otvet():
    driver = webdriver.Chrome()
    p = input('url\n')
    driver.get(p)