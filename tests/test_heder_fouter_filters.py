import time

import pytest
from pom.homepage_navigation import HomePageNavg

@pytest.mark.usefixtures("setup")
class TestHederFouterFilters:
    def test_heder_fouter_filters(self):
        global name_filters_hed_fout
        actual_name_heder_fouter_filters = ['Новини', 'Prozorro Market', 'Інфобокс', 'Стара версія пошуку', 'Тестування уповноважених осіб', 'Про нас', 'Bug bounty', 'Інформаційна безпека', 'Документи ДП "ПРОЗОРРО"', 'Подати офіційний лист з ЕЦП', 'Розвиток системи', 'Майданчики Prozorro', 'Дозорро', 'Друзі Prozorro', 'Prozorro Market інструмент ЦЗО', 'Митці', 'тест', 'Тестування УО', 'Моніторинг', 'Розробникам', 'Майданчикам', 'Захист учасників', 'Запитання та відповіді']
        homepage_nav = HomePageNavg(self.driver)
        link = "https://staging.prozorro.gov.ua/"
        browser = homepage_nav.driver
        browser.get(link)
        for indx in range(23):
            name_filters_hed_fout = homepage_nav.get_heder_fouter_links_text()
            links_hed_fut = homepage_nav.get_heder_fouter_links()[indx].click()
            time.sleep(1)
            browser.back()
        assert actual_name_heder_fouter_filters == name_filters_hed_fout, f"Названия изменились на вот такие {name_filters_hed_fout}, нужно смотреть!"
