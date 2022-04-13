import time
import pytest
from pom.tenders_navigation import TestTenders


@pytest.mark.usefixtures("tenders")
class TenderTest:

    def test_tender_link(self):
        homepage_nav = TestTenders(self.driver)
        for indx in range(20):
            homepage_nav.get_nav_tenders()[indx].click()
        time.sleep(10)