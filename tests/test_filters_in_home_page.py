import time

import pytest
from pom.homepage_navigation import HomePageNavg

@pytest.mark.usefixtures("setup")
class TestFiltersHomepage:
    def test_filters_homepage(self):
        global name_filters
        actual_name_filters_homepage = ['Замовник', 'Учасник', 'Закупівельник', 'ДК021:2015', 'Статус', 'Вид закупівлі', 'Регіон', 'Очікувана вартість', 'Дати', 'Обґрунтування', 'Оцінка пропозицій', 'Умови оплати', 'Згорнути фільтри']
        homepage_nav = HomePageNavg(self.driver)
        link = "https://staging.prozorro.gov.ua/"
        browser = homepage_nav.driver
        browser.get(link)
        homepage_nav.get_nav_filters()[7].click()
        for indx in range(13):
            name_filters = homepage_nav.get_nav_filters_text()
            filters = homepage_nav.get_nav_filters()[indx].click()
        assert actual_name_filters_homepage == name_filters, f"Filters name is not correct{name_filters}"










