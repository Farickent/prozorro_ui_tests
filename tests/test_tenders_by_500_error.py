
from pytest_check import check
import pytest
from pom.Items_in_page import Items_in_page

@pytest.mark.usefixtures("tenders")
class TestTenders:
    def test_tenders(self):
        tenders = Items_in_page(self.driver)
        id_tenders = []
        link = "https://staging.prozorro.gov.ua/search/tender"
        browser = tenders.driver
        browser.get(link)
        for indx in range(20):
            tenders_item = tenders.get_carta()
            tenders_item[indx].click()
            CBD_id = tenders.is_visible("css", "div[class=tender--head--inf]")
            CBD_id = CBD_id.text
            id_tenders.append(CBD_id)
            browser.back()
            with check:
                assert len(CBD_id) >= 58, f"тендер не открылся {CBD_id}"
        for i in id_tenders:
            print(i)





