from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

import argparse

parser = argparse.ArgumentParser(description='Select action')
parser.add_argument("-login", "--login", action="store_true", help="login to Carousell")
parser.add_argument("-sell", "--sell", action="store_true", help="add a listing")

args = parser.parse_args()

options = Options()

options.add_argument("user-data-dir=selenium")
options.add_experimental_option('excludeSwitches', ['enable-logging'])
PATH = "./drivers/chromedriver"
driver = webdriver.Chrome(PATH, options=options)

actions = webdriver.ActionChains(driver)


def login(username, password):
    driver.get("https://www.carousell.com.hk/sell")
    driver.find_element_by_xpath("//*[contains(text(), 'Log in') and @type='button' ]").click()

    driver.find_element_by_xpath("//input[@name='username']").send_keys(username)
    driver.find_element_by_xpath("//input[@name='password']").send_keys(password)

    driver.find_element_by_xpath("//*[contains(text(), 'Log in') and @type='submit' ]").click()


def sell():
    driver.get("https://www.carousell.com.hk/sell")
    select_photos = driver.find_element_by_xpath("//*[contains(text(), 'Select photos') and @type='button']")
    # print(select_photos)
    actions.click(select_photos).perform()
    # fileInput.sendKeys("C:/Users/raychan/Desktop/tmp/82-super-foods02-01.jpg")


def close_program(countdown):
    # close windows
    time.sleep(countdown)
    driver.close()


if args.login:
    login("csdesign", "chk1q2w3e4r")

if args.sell:
    sell()

else:
    print("Goodbye")
    close_program(3)
