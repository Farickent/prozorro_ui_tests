import time
from pytest_check import check
import pytest
from pom.homepage_navigation import HomePageNavg


@pytest.mark.usefixtures("setup")
class TestHomepage:

    def test_nav_links(self):
        links = ["tender", "plan", "catalog"]
        homepage_nav = HomePageNavg(self.driver)
        actual_links = homepage_nav.get_nav_links_text()
        with check:
            assert ['Тендери', 'Плани', 'Кваліфікації до каталогу'] == actual_links, f"Актуальные получились вот такими:{actual_links}, is not correct!"
        for indx in range(3):
            homepage_nav.get_nav_links()[indx].click()
            homepage_nav.wait_for_url_contains(links[indx])
            with check:
                assert links[indx] in homepage_nav.driver.current_url, f"Link is not present in url {links[indx]}"
        for i in actual_links:
            print(i)









