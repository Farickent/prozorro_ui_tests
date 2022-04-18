from bace.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List

class HomePageNavg(SeleniumBase):


    __ui_tabs: str = "li[class*=tab]"
    Nav_Linkl_Text = "Тендери,Плани,Кваліфікації до каталогу"
    __ui_filters: str = "label.filter-btn"
    __heder_foyter_links: str = "span[class*=link__wrapper]"
    __category_owners: str = "li[class*=category-purchases__list]"

    def get_category_owners(self) -> List[WebElement]:
        return self.are_visible("css", self.__category_owners, "Visible 18 item for owner")

    def get_category_owners_text(self):
        category_filter = self.get_category_owners()
        category_filter_text = self.get_text_from_webelements(category_filter)
        return category_filter_text


    def get_heder_fouter_links(self) -> List[WebElement]:
        return self.are_visible("css", self.__heder_foyter_links, "Visible 23 item header+fouter")

    def get_heder_fouter_links_text(self):
        heder_filter = self.get_heder_fouter_links()
        heder_filter_text = self.get_text_from_webelements(heder_filter)
        return heder_filter_text


    def get_nav_filters(self) -> List[WebElement]:
        return self.are_preset("css", self.__ui_filters, "Name filters in tenders")

    def get_nav_filters_text(self):
        nav_filters = self.get_nav_filters()
        nav_filters_text = self.get_text_from_webelements(nav_filters)
        return nav_filters_text


    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible("css", self.__ui_tabs, "Header Navigation Links by Prozzoro" )

    def get_nav_links_text(self):
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return nav_links_text

    def get_nav_link_by_name(self, name) ->WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements,name)






