from page_objects.base_page import base_page
from selenium.webdriver.common.by import By

class reg_page(base_page):
    INPUT_LOGIN = (By.CSS_SELECTOR, "#input-username")
    INPUT_PASSWORD = (By.CSS_SELECTOR, "#input-password")
    NEXT = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[1]/div[1]/div[1]/div[1]/div[2]/form[1]/div[3]/button[1]")

    def login(self):
        self._input(reg_page.INPUT_LOGIN, "user")
        self._input(reg_page.INPUT_PASSWORD, "bitnami")
        self.click(reg_page.NEXT)
