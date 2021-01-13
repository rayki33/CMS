from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("./drivers/chromedriver", options=options)
actions = webdriver.ActionChains(driver)

def login(username,password):
    driver.get("https://www.carousell.com.hk/csdesign/")
    driver.find_element_by_xpath("//*[contains(text(), 'Sell')]").click()

    time.sleep(2)
    txtLogin = driver.find_element(By.LINK_TEXT, "Log in")
    actions.context_click(txtLogin).perform()

login("csdesign","chk1q2w3e4r")
print("Done")
