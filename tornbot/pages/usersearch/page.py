# coding: utf-8

from ..base.page import BasePage
from .locators import LAST_PAGE


class UserSearchPage(BasePage):

    url = 'userlist.php'

    def crawl_users(self):
        # TODO: исправить чтобы все работало
        # last_page_url = self.driver.find_element(*LAST_PAGE).get_attribute(
        #     'href')
        # last_offset = last_page_url.split('#start=')[1]
        # user_agent = self.driver.execute_script("return navigator.userAgent")
        # process = CrawlerProcess({'USER_AGENT': user_agent})
        # process.crawl(UsersSpider, cookies=self.driver.get_cookies(),
        #               url=self.url, last_offset=last_offset,
        #               rfcv=self.driver.get_cookie('rfc_v').get('value'))
        # process.start()
        return
