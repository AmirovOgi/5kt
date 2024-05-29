import time, allure
from conftest import *
from page_objects.main_page import main_page
from page_admin.product_page import product_page
from page_admin.reg_page import reg_page
from page_admin.main_admin_page import main_admin_page
from page_admin.categories_page import categories_page

@allure.feature("Create Categories")
@allure.title("Creating new categories 'Devices'")
def test_1(driver):
    driver.get("http://localhost/administration")   
    reg_page(driver).login()
    main_admin_page(driver).click(main_admin_page.MENU_CATALOG)
    main_admin_page(driver).click(main_admin_page.LI_CATEGORIES)

    categories_page(driver).create_categories("Devices", "META_TAG_TITLE", "META_TAG_DESCRIPTION", "META_TAG_KEYWORDS")
    categories_page(driver).create_categories("mouse", "META_TAG_TITLE", "META_TAG_DESCRIPTION", "mousess", "Devices")
    categories_page(driver).create_categories("keyboard", "META_TAG_TITLE", "META_TAG_DESCRIPTION", "keyboardd", "Devices")

@allure.feature("Add products")
@allure.title("Creating 4 new products in 'Devices'")
def test_2(driver):
    driver.get("http://localhost/administration")
    reg_page(driver).login()
    main_admin_page(driver).click(main_admin_page.MENU_CATALOG)
    main_admin_page(driver).click(main_admin_page.LI_PRODUCTS)
    product_page(driver).add_product([
        ["Mouse", "model_mouse", "1"], 
        ["Keyboard", "keyboard_model", "0"]
    ])
    time.sleep(2)

@allure.feature("Checking products")
@allure.title("Checking all products in main page")
def test_3(driver):
    main_page(driver).write(main_page.search, "mouse")
    main_page(driver).enter()
    main_page(driver).write(main_page.search, "keyboard")
    main_page(driver).enter()

@allure.feature("Delete products")
@allure.title("Deleting 2 products")
def test_4(driver):
    driver.get("http://localhost/administration")
    reg_page(driver).login()
    main_admin_page(driver).click(main_admin_page.MENU_CATALOG)
    main_admin_page(driver).click(main_admin_page.LI_PRODUCTS)
    product_page(driver).delete_product(["Mouse", "model_mouse", "1"])
    product_page(driver).delete_product(["Keyboard", "keyboard_model", "0"])
    time.sleep(2)

@allure.feature("Checking products")
@allure.title("Checking all products in main page")
def test_5(driver):
    main_page(driver).write(main_page.search, "mouse")
    main_page(driver).enter()
    main_page(driver).write(main_page.search, "keyboard")
    main_page(driver).enter()