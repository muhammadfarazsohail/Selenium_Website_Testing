
from locator import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

# this checks for the page title


class MainPage(BasePage):

    # this method checks for the title of landonhotel.com
    def is_title_matches(self):
        return "Landon Hotel" in self.driver.title

    # this method clicks the down button on the site by finding using locator class
    def down_button(self):
        element = self.driver.find_element(*MainPageLocators.DOWN_BUTTON)
        element.click()

    # this method clicks the brand button that is landon hotel on the site by finding using locator class
    def brand_button(self):
        element = self.driver.find_element(*MainPageLocators.BRAND_BUTTON)
        element.click()

    # this method clicks the info button on the site by finding using locator class
    def info_button(self):
        element = self.driver.find_element(*MainPageLocators.INFO_BUTTON)
        element.click()

    # this method clicks the Rooms button on the site by finding using locator class
    def rooms_button(self):
        element = self.driver.find_element(*MainPageLocators.ROOMS_BUTTON)
        element.click()

    # this method clicks the dining button on the site by finding using locator class
    def dine_button(self):
        element = self.driver.find_element(*MainPageLocators.DINE_BUTTON)
        element.click()

    # this method clicks the events button on the site by finding using locator class
    def event_button(self):
        element = self.driver.find_element(*MainPageLocators.EVENT_BUTTON)
        element.click()

    # this method clicks the attractions button on the site by finding using locator class
    def attract_button(self):
        element = self.driver.find_element(*MainPageLocators.ATTRACT_BUTTON)
        element.click()

    # this method clicks the twitter icon button on the site by finding using locator class
    def twitter_button(self):
        element = self.driver.find_element(*MainPageLocators.TWITTER_BUTTON)
        element.click()

    # this method clicks the facebook icon button on the site by finding using locator class
    def fb_button(self):
        element = self.driver.find_element(*MainPageLocators.FB_BUTTON)
        element.click()

    # this method clicks the youtube icon button on the site by finding using locator class
    def yt_button(self):
        element = self.driver.find_element(*MainPageLocators.YT_BUTTON)
        element.click()
