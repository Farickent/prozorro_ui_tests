import time

import pytest
from pom.homepage_navigation import HomePageNavg

@pytest.mark.usefixtures("setup")
class TestItemOwner:
    def test_item_owner(self):
        global actual_item_name_text
        homepage_nav = HomePageNavg(self.driver)
        link = "https://staging.prozorro.gov.ua/"
        browser = homepage_nav.driver
        browser.get(link)
        actual_item_name = ['Будівництво', 'Медицина', 'Меблі', "Комп'ютерна техніка", 'Канцелярія та госптовари', 'Транспорт та запчастини', 'Енергетика, нафтопродукти та паливо', 'Метали', 'Комунальне та побутове обслуговування', 'Навчання та консалтинг', 'Нерухомість', 'Сільське господарство', 'Одяг, взуття та текстиль', 'Промислове обладнання та прилади', 'Харчування', 'Поліграфія', 'Науково-дослідні роботи', 'Різні послуги та товари']
        for indx in range(18):
            actual_item_name_text = homepage_nav.get_category_owners_text()
            item_owner = homepage_nav.get_category_owners()[indx].click()
            item_owner_onclick = homepage_nav.get_category_owners()[indx].click()
        assert actual_item_name == actual_item_name_text, f"Айтемы для заказчика поменялись на вот такие {actual_item_name_text}"

