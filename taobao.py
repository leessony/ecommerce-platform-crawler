import time

from crawler_tools import CrawlerTools


class Taobao:
    __LOGIN_URL = 'https://login.taobao.com/member/login.jhtml?from=taobaoindex&f=top&style=&sub=true&redirect_url=https%3A%2F%2Fmyseller.taobao.com%2Fhome.htm'
    __LOGIN_ID_XPATH = '//*[@id="fm-login-id"]'
    __LOGIN_PW_XPATH = '//*[@id="fm-login-password"]'
    __LOGIN_BTN_XPATH = '//*[@id="login-form"]/div[4]/button'

    tools = CrawlerTools()

    def login(self, id, pw):
        self.tools.get_driver.get(self.__LOGIN_URL)
        self.tools.get_driver.find_element_by_link_text('密码登录').click()

        time.sleep(3)
        self.tools.get_driver.find_element_by_xpath(self.__LOGIN_ID_XPATH).send_keys(id)
        time.sleep(10)
        self.tools.get_driver.find_element_by_xpath(self.__LOGIN_PW_XPATH).send_keys(pw)
        time.sleep(10)
        self.tools.get_driver.find_element_by_xpath(self.__LOGIN_BTN_XPATH).click()
