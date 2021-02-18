from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from pyautogui import write, press, click

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

        self.driver = webdriver.Chrome(PATH, options=self.options)
        self.actions = webdriver.ActionChains(self.driver)
        self.image_files = [("AP2C-EB-01AG.jpg", "AP2C-EB-01DR.jpg")]

    def login(self):
        self.driver.get("https://www.carousell.com.hk/sell")
        self.driver.find_element_by_xpath("//*[contains(text(), 'Log in') and @type='button' ]").click()

        self.driver.find_element_by_xpath("//input[@name='username']").send_keys(self.username)
        self.driver.find_element_by_xpath("//input[@name='password']").send_keys(self.password)

        self.driver.find_element_by_xpath("//*[contains(text(), 'Log in') and @type='submit' ]").click()

    def sell(self):
        self.driver.get("https://www.carousell.com.hk/sell")
        select_photos = self.driver.find_element_by_xpath("//*[contains(text(), 'Select photos') and @type='button']")
        self.actions.click(select_photos).perform()
        time.sleep(3)

        self.input_filename()

    def input_filename(self):
        new_folder_path = '"' + FOLDER_PATH + '"'
        write(new_folder_path)
        press('enter')
        time.sleep(2)

        for image_file in self.image_files[0]:
            new_file = '"' + image_file + '"'
            write(new_file)
            write(" ")
        press('enter')

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