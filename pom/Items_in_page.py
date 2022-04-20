from bace.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List
from bace.utlis import Utils
class Items_in_page(SeleniumBase):

    __search_result_tenders = "ul.search-result__list>li"
    __carta = "div[class*=search-result-card] a"
    __id_item_in_page = "div[class=tender--head--inf]"

    def __init__(self, driver):
        super().__init__(driver)
        self.get_id_item_in_page = None



    def get_nav_tenders(self) ->List[WebElement]:
        return self.are_visible("css", self.__search_result_tenders, "Tenders visible in prozorro search only 20 item")

    def get_nav_tenders_text(self) -> str:
        nav_links_tender = self.get_nav_tenders()
        nav_links_tender_text = self.get_text_from_webelements(nav_links_tender)
        return Utils.join_strings(nav_links_tender_text)

    def get_nav_tenders_by_name(self, name) -> WebElement:
        elements = self.get_nav_tenders()
        return self.get_element_by_text(elements, name)

    def get_carta(self) -> List[WebElement]:
        return self.are_preset("css", self.__carta)

    def get_id_item(self) -> WebElement:
        items = self.is_visible("css", self.__id_item_in_page)
        return self.get_id_item_in_page(items)





