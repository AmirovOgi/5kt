from page_objects.base_page import base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from random import randint 
import time

class product_page(base_page):
    LI_DATA = (By.LINK_TEXT, "Data")
    LI_SEO = (By.LINK_TEXT, "SEO")
    LI_LINK = (By.LINK_TEXT, "Links")
    LI_GENERAL = (By.LINK_TEXT, "General")
    MAIN_PAGE_PRODUCT = (By.LINK_TEXT, "Products")
    BUTTON_FILTER = (By.CSS_SELECTOR, "#button-filter")
    INPUT_PRODUCT_NAME = (By.CSS_SELECTOR, "#input-name")
    CHECKBOX = (By.XPATH, "//tbody/tr[1]/td[1]/input[1]")
    BUTTON_DELETE = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/button[3]")
    BUTTON_ADD_NEW_PRODUCT = (By.CSS_SELECTOR, "a.btn.btn-primary:nth-child(2)")
    INPUT_PRODUCT_NAME_1 = (By.CSS_SELECTOR, "#input-name-1")
    INPUT_META_TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title-1")
    INPUT_META_TAG_DESCRIPTION = (By.CSS_SELECTOR, "#input-meta-description-1")
    INPUT_META_TAG_KEYWORDS = (By.CSS_SELECTOR, "#input-meta-keyword-1")
    BUTTON_SAVE_PRODUCT = (By.CSS_SELECTOR, "button.btn.btn-primary:nth-child(1)")
    INPUT_MODEL = (By.CSS_SELECTOR, "#input-model")
    INPUT_KEYWORD = (By.CSS_SELECTOR, "#input-keyword-0-1")
    INPUT_CHOICE_CATEGORIES = (By.CSS_SELECTOR, "#input-category")
    SELECT_DEVICES = (By.XPATH, "//a[contains(text(),'Devices')]")

    def tab(self):
        self.action.send_keys(Keys.TAB).perform()
        self.logger.info("Press 'TAB'")

    def enter(self):
        self.action.send_keys(Keys.ENTER).perform()
        self.logger.info("Press 'TAB'")

    def add_product(self, arr):
        for element in arr:
            name = element[0]
            model = element[1]
            full_name = name + " " + model

            self.click(self.BUTTON_ADD_NEW_PRODUCT)
            self.write(self.INPUT_PRODUCT_NAME_1, full_name)
            self.write(self.INPUT_META_TAG_TITLE, name)
            self.click(self.LI_DATA)
            self.write(self.INPUT_MODEL, model)
            self.click(self.LI_LINK)

            if element[2] == "1":
                self.write(self.INPUT_CHOICE_CATEGORIES, "mouse")
            elif element[2] == "0":
                self.write(self.INPUT_CHOICE_CATEGORIES, "keyboard")
            else:
                self.write(self.INPUT_CHOICE_CATEGORIES, "Devices")
            
            time.sleep(0.5)
            self.tab()
            self.enter()
            self.click(self.LI_SEO)
            
            keyword = ""
            for _ in range(len(name)):
                keyword += name.replace(" ", "")[randint(0, len(name)-1)]

            self.write(self.INPUT_KEYWORD, keyword)
            self.click(self.BUTTON_SAVE_PRODUCT)
            self.click(self.MAIN_PAGE_PRODUCT)

    def find_product_arr(self, arr):
        for element in arr:
            name = element[0]
            model = element[1]

            self.click(self.MAIN_PAGE_PRODUCT)
            self.write(self.INPUT_PRODUCT_NAME, name)
            self.write(self.INPUT_MODEL, model)
            self.click(self.BUTTON_FILTER)

    def accept_alert(self):
        alert = self.driver.switch_to.alert
        alert.accept()

    def find_product_name(self, name, model):
        self.click(self.MAIN_PAGE_PRODUCT)
        self.write(self.INPUT_PRODUCT_NAME, name)
        self.write(self.INPUT_MODEL, model)
        self.click(self.BUTTON_FILTER)

    def delete_product(self, arr):
        self.find_product_name(arr[0], arr[1])
        self.click(self.CHECKBOX)
        self.click(self.BUTTON_DELETE)
        self.accept_alert()
