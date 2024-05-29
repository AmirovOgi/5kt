from page_objects.base_page import base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class main_page(base_page):
    search = (By.CSS_SELECTOR, "input.form-control.form-control-lg")
    button_search = (By.CSS_SELECTOR, "button.btn.btn-light.btn-lg")

    macbook = (By.LINK_TEXT, "MacBook")
    droptablet = (By.LINK_TEXT, "Планшеты")
    droptelephone = (By.LINK_TEXT, "Телефоны")

    iphone = (By.LINK_TEXT, "iPhone")
    samsung = (By.LINK_TEXT, "Samsung Galaxy Tab 10.1")

    def enter(self):
        self.action.send_keys(Keys.CONTROL).send_keys(Keys.ENTER).perform()
