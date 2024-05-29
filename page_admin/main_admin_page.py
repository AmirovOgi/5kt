from page_objects.base_page import base_page
from selenium.webdriver.common.by import By


class main_admin_page(base_page):
    MENU_CATALOG = (By.CSS_SELECTOR, "#menu-catalog")
    LI_CATEGORIES = (By.LINK_TEXT, "Categories")
    LI_PRODUCTS = (By.LINK_TEXT, "Products")