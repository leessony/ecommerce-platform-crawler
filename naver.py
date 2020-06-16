import time

from bs4 import BeautifulSoup

from crawler_tools import CrawlerTools


class Naver:
    __LOGIN_URL = 'https://nid.naver.com/nidlogin.login?url=https%3A%2F%2Fsell.smartstore.naver.com%2F%23%2FnaverLoginCallback%3Furl%3Dhttps%253A%252F%252Fsell.smartstore.naver.com%252F%2523%252Fproducts%252Forigin-list'
    __LOGIN_ID_XPATH = '//*[@id="id"]'
    __LOGIN_PW_XPATH = '//*[@id="pw"]'
    __LOGIN_BTN_XPATH = '//*[@id="log.login"]'

    __REGISTER_BROWSER_BTN_XPATH = '//*[@id="new.save"]'

    __PRODUCT_MANAGE_URL = 'https://sell.smartstore.naver.com/#/products/origin-list'
    __PRODUCT_ON_SALE_LIST_BTN_XPATH = '/html/body/ui-view[1]/div[3]/div/div[3]/div/ui-view/div/ui-view[1]/div[1]/ul/li[3]/a'
    __PRODUCT_LIST_QUERY_SELECTOR = "a[target='_blank'].text-info"

    tools = CrawlerTools()

    def login(self, id, pw):
        self.tools.get_driver.get(self.__LOGIN_URL)

        time.sleep(1)
        self.tools.clipboard_input(self.__LOGIN_ID_XPATH, id)
        time.sleep(1)
        self.tools.clipboard_input(self.__LOGIN_PW_XPATH, pw)
        self.tools.get_driver.find_element_by_xpath(self.__LOGIN_BTN_XPATH).click()

        # 브라우저 등록 클릭
        self.tools.get_driver.find_element_by_xpath(self.__REGISTER_BROWSER_BTN_XPATH).click()

    def get_products(self):
        # 판매중 상품 버튼 클릭
        time.sleep(12)
        self.tools.get_driver.get(self.__PRODUCT_MANAGE_URL)
        self.tools.get_driver.find_element_by_xpath(
            self.__PRODUCT_ON_SALE_LIST_BTN_XPATH
        ).click()

        time.sleep(1)
        html = self.tools.get_driver.page_source
        soup = BeautifulSoup(html, 'html.parser')
        return soup.select(self.__PRODUCT_LIST_QUERY_SELECTOR)
