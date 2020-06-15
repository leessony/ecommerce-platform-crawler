from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
import pyperclip
from bs4 import BeautifulSoup


def clipboard_input(user_xpath, user_input):
    temp_user_input = pyperclip.paste()

    pyperclip.copy(user_input)
    driver.find_element_by_xpath(user_xpath).click()
    ActionChains(driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()

    pyperclip.copy(temp_user_input)
    time.sleep(1)


driver = webdriver.Firefox(executable_path='/Users/idonghoon/Downloads/geckodriver')

url = "https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsell.smartstore.naver.com%2F%23%2FnaverLoginCallback%3Furl%3Dhttps%253A%252F%252Fsell.smartstore.naver.com%252F%2523%252Fproducts%252Forigin-list"

driver.get(url)

login = {
    "id": "",
    "pw": ""
}

# 아이디와 비밀번호를 입력합니다.
time.sleep(1)
clipboard_input('//*[@id="id"]', login.get("id"))
time.sleep(1)
clipboard_input('//*[@id="pw"]', login.get("pw"))
driver.find_element_by_xpath('//*[@id="log.login"]').click()

# 브라우저 등록 클릭
driver.find_element_by_xpath('//*[@id="new.save"]').click()

# 판매중 상품 버튼 클릭
time.sleep(10)
driver.get('https://sell.smartstore.naver.com/#/products/origin-list')
driver.find_element_by_xpath('/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div/ui-view[1]/div[1]/ul/li[3]/a').click()

time.sleep(5)
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
textInfos = soup.select("a[target='_blank'].text-info")
for info in textInfos:
    print(info.text)
