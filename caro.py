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
    driver.get("https://www.carousell.com.hk/sell")
    txtLogin = driver.find_element_by_xpath("//*[contains(text(), 'Log in') and @type='button' ]")
    txtLogin.click()
    # actions.move_to_element(txtLogin).click().perform()



    # print(txtLogin)
    # actions.click(txtLogin).perform()


def close_program(countdown):
    #close windows
    time.sleep(countdown)
    driver.close()


login("csdesign","chk1q2w3e4r")
print("Done and close browswer in 3s")
close_program(3)
