import pyperclip
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class CrawlerTools:
    # __CHROME_WEB_DRIVER_PATH = '/Users/idonghoon/Downloads/chromedriver'
    # __chrome_driver = webdriver.Chrome(executable_path=__CHROME_WEB_DRIVER_PATH)

    __GECKO_WEB_DRIVER_PATH = '/Users/idonghoon/Downloads/geckodriver'
    __gecko_driver = webdriver.Firefox(executable_path=__GECKO_WEB_DRIVER_PATH)

    __driver = __gecko_driver

    @property
    def get_driver(self):
        return self.__driver

    def clipboard_input(self, user_xpath, user_input):
        pyperclip.copy(user_input)
        self.__driver.find_element_by_xpath(user_xpath).click()
        ActionChains(self.__driver).key_down(Keys.COMMAND).send_keys('v').key_up(Keys.COMMAND).perform()
