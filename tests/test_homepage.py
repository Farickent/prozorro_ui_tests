import time
import pytest
from pom.homepage_navigation import HomePage_navg


@pytest.mark.usefixtures("setup")
class TestHomepage:

    def test_nav_links(self):
        homepage_nav = HomePage_navg(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        expected_links = homepage_nav.Nav_Linkl_Text
        print(expected_links)
        assert expected_links == actual_links, f"Актуальные получились вот такими:{actual_links}, поправь по братски!"
        for indx in range(3):
            homepage_nav.get_nav_links()[indx].click()
        time.sleep(2)






