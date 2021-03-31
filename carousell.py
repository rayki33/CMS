from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyautogui import write, press, click
from wc import *

import time

PATH = "./drivers/chromedriver"
FOLDER_PATH = "C:\\Users\\raychan\\Desktop\\inventory image - temp"


class Carousell:
    def __init__(self):
        self.username = "csdesign"
        self.password = "chk1q2w3e4r"

        self.options = Options()
        self.options.add_argument("user-data-dir=selenium")
        self.options.add_experimental_option('excludeSwitches', ['enable-logging'])
        self.options.add_experimental_option("detach", True)

        self.driver = webdriver.Chrome(PATH, options=self.options)
        self.actions = webdriver.ActionChains(self.driver)

    def login(self):
        self.driver.get("https://www.carousell.com.hk/sell")
        self.driver.find_element_by_xpath("//*[contains(text(), 'Log in') and @type='button' ]").click()

        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.password)

        self.element_locator = self.driver.find_element_by_xpath("//*[contains(text(), 'Log in') and @type='submit' ]")
        # self.element_locator.click()
        # actions.contextClick(elementLocator).perform()

    def sell(self, product_id):
        self.driver.get("https://www.carousell.com.hk/sell")
        select_photos_button = self.driver.find_element_by_xpath("//*[contains(text(), 'Select photos') and @type='button']")
        self.actions.click(select_photos_button).perform()
        time.sleep(3)

        self.input_filename(product_id)

    def input_filename(self, product_id):
        image_urls = get_image_url(product_id)
        for image_url in image_urls:
            print(image_url)
            write(f'"{image_url}"')
            press("enter")
            time.sleep(5)
            self.select_photos()

    def select_photos(self):
        select_photos_button = self.driver.find_element_by_xpath("//*[contains(text(), 'Select photos') and @type='button']")
        print(select_photos_button)
        self.actions.doubleClick(select_photos_button).perform()

    # select category
    def select_category(self):
        time.sleep(1.5)
        btn_category = self.driver.find_element_by_xpath("//*[contains(text(), 'Select a category')]")
        print(btn_category)
        btn_category.click()
        # for tab in range(0, 13):
        #     press("tab")


        # write("gadget")
        time.sleep(1)
        write("Electronics & Gadgets")