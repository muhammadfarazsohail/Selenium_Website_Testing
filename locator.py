from selenium.webdriver.common.by import By

# this class holds all the paths and elements by their class names


class MainPageLocators(object):
    DOWN_BUTTON = (By.XPATH, "//a[contains(@href,'#welcome')]")
    BRAND_BUTTON = (By.CLASS_NAME, "brand")
    INFO_BUTTON = (By.CLASS_NAME, "info")
    ROOMS_BUTTON = (By.CLASS_NAME, "rooms")
    DINE_BUTTON = (By.CLASS_NAME, "dining")
    EVENT_BUTTON = (By.CLASS_NAME, "events")
    ATTRACT_BUTTON = (By.CLASS_NAME, "attractions")
    TWITTER_BUTTON = (By.XPATH, "//a[contains(@href,'https://twitter.com')]")
    FB_BUTTON = (By.XPATH, "//a[contains(@href,'http://www.facebook.com')]")
    YT_BUTTON = (By.XPATH, "//a[contains(@href,'http://www.youtube.com')]")
