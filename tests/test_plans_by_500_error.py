from pytest_check import check
import pytest
from pom.Items_in_page import Items_in_page


@pytest.mark.usefixtures("plans")
class TestPlans:
    def test_plans(self):
        tenders = Items_in_page(self.driver)
        id_plans = []
        link = "https://staging.prozorro.gov.ua/search/plan"
        browser = tenders.driver
        browser.get(link)
        for indx in range(20):
            tenders_item = tenders.get_carta()
            tenders_item[indx].click()
            CBD_id = tenders.is_visible("css", "div[class=tender--head--inf]")
            CBD_id = CBD_id.text
            id_plans.append(CBD_id)
            browser.back()
            with check:
                assert len(CBD_id)>5, f"тендер не открылся {CBD_id}"
        for i in id_plans:
            print(i)
