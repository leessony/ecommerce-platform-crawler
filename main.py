from selenium import webdriver
import time
from bs4 import BeautifulSoup

from naver import Naver

n = Naver()

login = {
    "id": "",
    "pw": ""
}

n.login(login.get("id"), login.get("pw"))
products = n.get_products()

for p in products:
    print(p.text)
