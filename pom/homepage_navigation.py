from bace.seleniumbase import SeleniumBase
from selenium.webdriver.remote.webelement import WebElement
from typing import List

from bace.utlis import Utils


class HomePage_navg(SeleniumBase):

    def __init__(self, driver):
        super(). __init__(driver)
        self.driver = driver
        self.__ui_tabs: str = "uL.tabs>li"
        self.Nav_Linkl_Text = "Тендери,Плани,Кваліфікації до каталогу"


    def get_nav_links(self) -> List[WebElement]:
        return self.are_visible("css", self.__ui_tabs, "Header Navigation Links by Prozzoro" )

    def get_nav_links_text(self) -> str:
        nav_links = self.get_nav_links()
        nav_links_text = self.get_text_from_webelements(nav_links)
        return Utils.join_strings(nav_links_text)

    def get_nav_link_by_name(self, name) ->WebElement:
        elements = self.get_nav_links()
        return self.get_element_by_text(elements,name)






