from selenium import webdriver
from socket import *

def web_otvet():
    driver = webdriver.Chrome()
    p = input('url\n')
    driver.get(p)
    s = socket.socket()
    s.connect(p, 8080)