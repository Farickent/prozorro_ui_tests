import pytest
from pom.homepage_navigation import HomePageNavg

@pytest.mark.usefixtures("setup")
class TestFilterTender:
    def test_filters_tender(self):
        global filter_batton_name
        actual_name_filter = ['за замовчуванням', 'дата публікації – новіші', 'дата публікації – старіші', 'зростання вартості', 'зменшення вартості']
        homepage_nav = HomePageNavg(self.driver)
        link = "https://staging.prozorro.gov.ua/search/tender"
        browser = homepage_nav.driver
        browser.get(link)
        homepage_nav.get_click_filter_name().click()
        for indx in range(1, 5):
            filter_batton_name = homepage_nav.get_filters_tender_text()
            filter_batton = homepage_nav.get_filters_tender()[indx].click()
            homepage_nav.get_click_filter_name().click()
        assert actual_name_filter == filter_batton_name, f"Название фильтров не совпадают, вот что нашло {filter_batton_name}"
