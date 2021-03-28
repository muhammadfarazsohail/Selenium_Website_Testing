import unittest
from unittest.main import main
from selenium import webdriver
import page
import time


class LandonHotelSearch(unittest.TestCase):
    """test class to show how page object works"""

    def setUp(self):
        self.driver = webdriver.Chrome(
            "C:\Program Files (x86)\chromedriver.exe")
        self.driver.get("https://landonhotel.com")

    # this method tests the title page of the site
    def test_title(self):

        # Load the main page. In this case the home page of landonhotel.com.
        main_page = page.MainPage(self.driver)

        # Checks if the word "Landon Hotel" is in title
        assert main_page.is_title_matches(), "landonhotel.com title doesn't match."

    # this method clicks all the navigation buttons
    def test_button_clicks(self):
        # Load the main page. In this case the home page of landonhotel.com.
        main_page = page.MainPage(self.driver)
        # this portion executes the buttons found on the landon hotel navigation bar
        main_page.brand_button()
        main_page.info_button()
        main_page.rooms_button()
        main_page.dine_button()
        main_page.event_button()
        main_page.attract_button()

    # this method tests the down arrow on the top of the page
    def test_link_down(self):
        # Load the main page. In this case the home page of landonhotel.com.
        main_page = page.MainPage(self.driver)
        # this line executes the down button press method in page.py
        main_page.down_button()

    def test_link_twitter(self):
        # Load the main page. In this case the home page of landonhotel.com.
        main_page = page.MainPage(self.driver)
        # this line executes the twitter icon button press method in page.py
        main_page.twitter_button()

    def test_link_facebook(self):
        # Load the main page. In this case the home page of landonhotel.com.
        main_page = page.MainPage(self.driver)
        # this line executes the facebook icon button press method in page.py
        main_page.fb_button()

    def test_link_youtube(self):
        # Load the main page. In this case the home page of landonhotel.com.
        main_page = page.MainPage(self.driver)
        # this line executes the youtube icon button press method in page.py
        main_page.yt_button()

    # this is the last method used for closing things, in this case close the driver
    def tearDown(self):
        time.sleep(8)
        self.driver.close()


# this is the main method which runs all the tests in the file
if __name__ == "__main__":
    unittest.main()
