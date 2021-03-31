import pandas as pd
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
import time

# import clipboard

PINKOI_USERNAME = "csdesign"
PINKOI_PASSWORD = "cp1q2w3e4r"

options = Options()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome("./drivers/chromedriver", options=options)
actions = webdriver.ActionChains(driver)


def hide_bottom_action_panel():
    bottom_action_panel = driver.find_element_by_class_name("m-react-bottom-action-panel")
    driver.execute_script("arguments[0].setAttribute('style','visibility: hidden;')", bottom_action_panel)


class Pinkoi:
    def __init__(self):
        self.listing_data = "./data/pinkoi-listing-phonecase.csv"
        self.phone_case_model = "./data/phone-glossy.csv"
        self.phone_case_listings = "./data/pinkoi-listing-phonecase.csv"

    def get_product_list_to_update(self):
        # read order csv file

        # with open(self.listing_data,'rb') as f:
        #     result = chardet.detect(f.read())
        #     df = pd.read_csv(self.listing_data, encoding=result['encoding'], sep='\t', quotechar='"')

        df = pd.read_csv(self.listing_data, encoding="utf_8")
        df.to_dict()
        return df

    def login(self, username, password):
        driver.get("https://hk.pinkoi.com/login#signin")
        search_box = driver.find_element_by_xpath(
            "//*[@id='login-app']/div[1]/div[1]/div[1]/form[1]/div[1]/div[1]/label[1]/input[1]")
        search_box.send_keys(username)
        password_box = driver.find_element_by_xpath(
            "//*[@id='login-app']/div[1]/div[1]/div[1]/form[1]/div[2]/div[1]/label[1]/input[1]")
        password_box.send_keys(password + Keys.RETURN)

    def go_to_listing(self, pinkoi_listing_id):
        # go to the product in admin page
        time.sleep(1)
        driver.get("https://www.pinkoi.com/panel/listings/" + pinkoi_listing_id + "/edit")

    def select_edit_options(self):
        time.sleep(1)
        hide_bottom_action_panel()
        edit_option_text = driver.find_element_by_xpath("//*[contains(text(), '修改規格')]")
        actions.move_to_element(edit_option_text).click().perform()

    def show_bottom_action_panel(self):
        bottom_action_panel = driver.find_element_by_class_name("m-react-bottom-action-panel")
        driver.execute_script("arguments[0].setAttribute('style','visibility: visible;')", bottom_action_panel)

    def remove_previous_options(self):
        input_box = driver.find_element_by_css_selector(".m-react-listing-custom-variation-inputs .g-form-input")
        input_box_value = input_box.get_attribute("value")

        actions.click(input_box).perform()
        # actions.move_to_element(input_box).context_click().perform()
        # actions.move_to_element(input_box).double_click().perform()

        while input_box_value:
            actions.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).send_keys(Keys.DELETE).perform()
            input_box_value = input_box.get_attribute("value")

    def get_phone_case(self):
        df = pd.read_csv(self.phone_case_model)
        phone_cases = [item for item in df["Model"]]
        return phone_cases

    def add_phone_models(self):
        phone_cases = self.get_phone_case()

        for phone_case in phone_cases[:3]:
            print(phone_case)
            # clipboard.copy(phone_case)
            # actions.key_down(Keys.CONTROL).send_keys("V").key_up(Keys.CONTROL).send_keys(Keys.TAB)
            actions.send_keys(phone_case).send_keys(Keys.TAB)

        actions.perform()

    def press_apply_changes(self):
        time.sleep(1)
        driver.find_element_by_xpath("//*[contains(text(), '套用規格')]").click()
        time.sleep(2)
        driver.find_element_by_css_selector(".dialog-actions .m-br-button--primary").click()

    def confirm_changes(self):
        time.sleep(1)
        preview_product_btn = driver.find_element_by_css_selector(".action-panel .m-br-button--primary")
        preview_product_btn.click()
        time.sleep(2)
        save_changes_btn = driver.find_element_by_css_selector(".action-panel .m-br-button--primary")
        save_changes_btn.click()

    def close_update_complete_popup_window(self):
        time.sleep(5)
        popup_close_btn = driver.find_element_by_css_selector(".m-react-modal .m-br-button--secondary")
        popup_close_btn.click()

    def close_windows(self, second=3):
        # close windows
        time.sleep(second)
        driver.close()

    def update_option_sku(self, sku):
        # sku_text_box = driver.find_element_by_css_selector(".m-react-text-field .g-form-input-wrapper .g-form-input")
        # actions.send_keys(sku)
        pass

    def update_phone_models(self):
        self.login(PINKOI_USERNAME, PINKOI_PASSWORD)
        product_list = self.get_product_list_to_update()

        self.go_to_listing(product_list.loc[0]['listing_id'])
        self.select_edit_options()
        self.remove_previous_options()

        self.add_phone_models()
        self.press_apply_changes()
        self.update_option_sku()

        self.show_bottom_action_panel()
        self.confirm_changes()
        self.close_update_complete_popup_window()
        # self.close_windows()


pk = Pinkoi()
# pk.update_phone_models()
pk.update_phone_models()
