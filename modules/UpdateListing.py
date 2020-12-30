from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

options = Options()
# options.add_argument("--start-maximized");
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("./drivers/chromedriver", options=options)
wait = WebDriverWait(driver, 5)
# actions = webdriver.ActionChains(driver)


def login(username,password):
    driver.get("https://hk.pinkoi.com/login#signin")
    searchBox = driver.find_element_by_xpath("//*[@id='login-app']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/label[1]/input[1]")
    searchBox.send_keys(username)
    passwordBox = driver.find_element_by_xpath("//*[@id='login-app']/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/label[1]/input[1]")
    passwordBox.send_keys(password + Keys.RETURN)


def go_to_listing(productID):
    #go to the product on admin page
    time.sleep(1)
    driver.get("https://www.pinkoi.com/panel/listings/"+ productID +"/edit")


def close_popup_window():
    #close popup window
    time.sleep(3)
    popupWindow = driver.find_element_by_class_name("modal-close")
    # print(bool(popupWindow))

    if popupWindow:
        popupWindow.click()
        # print("close popup window")
    # else:
    #     print("No popup window")


def edit_options():
    time.sleep(1)
    # hide bottom panel
    bottom_action_panel = driver.find_element_by_class_name("m-react-bottom-action-panel")
    driver.execute_script("arguments[0].setAttribute('style','visibility: hidden;')", bottom_action_panel)

    editOption_txt = driver.find_element_by_xpath("//*[contains(text(), '修改規格')]")

    actions = webdriver.ActionChains(driver)
    actions.click(editOption_txt).perform()

def close_program():
    #close windows
    time.sleep(5)
    driver.close()


def update_options(option):
    time.sleep(3)
    actions = webdriver.ActionChains(driver)

    # remove old options
    option_text_fields = driver.find_elements_by_css_selector("html > body > div:nth-of-type(9) > div > div:nth-of-type(2) > div > div:nth-of-type(2) > div > div > div > div > div:nth-of-type(2) > div > div > div > label > input")
    row = 0
    while row < 100 :
        # actions.move_to_element(option_text_fields[0])
        actions.click(option_text_fields[0]).perform()
        # actions.double_click(option_text_fields[0]).click().perform()
        # option_text_fields[0].send_keys(Keys.DELETE)
        actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
        option_text_field_value = option_text_fields[0].get_attribute("value")

        # check if the field is empty
        if bool(option_text_field_value) == False:
            break
        row += 1


    # add new options
    i = 0

    while i < len(option):
        actions.send_keys(option[i][0] + Keys.TAB)
        i += 1



    # click confirm
    confirm_button = driver.find_element_by_xpath("//*[contains(text(), '套用規格')]")
    actions.move_to_element(confirm_button).click().perform()
    time.sleep(2)

    # confirm_button_again = driver.find_element_by_xpath("//*[contains(text(), '套用規格')]")
    confirm_button_again = driver.find_element(By.CSS_SELECTOR,".m-react-dialog .m-br-button--primary")
    confirm_button_again.click()

    # print("confirm_button: ",confirm_button)
    # print("confirm_button_again: ",confirm_button_again)


def show_bottom_panel():
    time.sleep(0.5)
    bottom_action_panel = driver.find_element_by_class_name("m-react-bottom-action-panel")
    driver.execute_script("arguments[0].setAttribute('style','visibility: visible;')", bottom_action_panel)

def confirm_changes():
    time.sleep(1)
    preview_product_btn = driver.find_element(By.CSS_SELECTOR,".action-panel .m-br-button--primary")
    preview_product_btn.click()
    time.sleep(2)
    save_changes_btn = driver.find_element(By.CSS_SELECTOR,".action-panel .m-br-button--primary")
    save_changes_btn.click()

    # print("preview_product_btn: ",preview_product_btn)
    # print("save_changes_btn: ",save_changes_btn)

def close_update_complete_popup_window():
    time.sleep(8)
    popup_close_btn = driver.find_element(By.CSS_SELECTOR,".m-react-modal .m-br-button--secondary")

    # print("popup_close_btn: ",popup_close_btn)
    popup_close_btn.click()

def update_option_sku(sku):
    actions = webdriver.ActionChains(driver)
    time.sleep(1)
    input_SKU_txtbox = driver.find_element(By.CSS_SELECTOR,".m-react-listing-variation-table .g-form-input")
    # print(sku)
    actions.reset_actions()
    actions.move_to_element(input_SKU_txtbox).click().key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).send_keys(sku).perform()
    # breakpoint()


#### The Main Program ####
def update_listing(listingIDs,phonecases):

    print("Running...")
    login("csdesign","cp1q2w3e4r")

    listing_num = 0
    while listing_num < len(listingIDs):
        go_to_listing(listingIDs[listing_num,0])

        # if listing_num == 0:
        #      close_popup_window()

        edit_options()

        update_options(phonecases)
        update_option_sku(listingIDs[listing_num,1])

        show_bottom_panel()
        confirm_changes()
        print("Listing #", listing_num + 1, ": ", listingIDs[listing_num,0] ," completed.")
        print("SKU #", listing_num + 1, ": ", listingIDs[listing_num,1] ," completed.")

        close_update_complete_popup_window()


        listing_num += 1
        time.sleep(5)
    close_program()
    print("Done!")
