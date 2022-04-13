from bace.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from bace.utlis import Utils


class TestTenders(SeleniumBase):

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.__search_result_tenders: str = "ul.search-result__list>li"

    def get_nav_tenders(self) ->List[WebElement]:
        return  self.are_visible("css", self.__search_result_tenders, "Tenders visible in prozorro search only 20 item")

    def get_nav_tenders_text(self) -> str:
        nav_links_tender = self.get_nav_tenders()
        nav_links_tender_text = self.get_text_from_webelements(nav_links_tender)
        return Utils.join_strings(nav_links_tender_text)

    def get_nav_tenders_by_name(self, name) -> WebElement:
        elements = self.get_nav_tenders()
        return self.get_element_by_text(elements, name)