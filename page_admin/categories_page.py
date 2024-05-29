from page_objects.base_page import base_page
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


class categories_page(base_page):
    Main_Page = (By.LINK_TEXT, "Categories")
    LI_GENERAL = (By.LINK_TEXT, "General")
    LI_DATA = (By.LINK_TEXT, "Data")
    LI_SEO = (By.LINK_TEXT, "SEO")
    LI_DESIGN = (By.XPATH, "//body/div[@id='container']/div[@id='content']/div[2]/div[1]/div[2]/form[1]/ul[1]/li[4]/a[1]")
    BUTTON_ADD_NEW_CATEGORIES = (By.CSS_SELECTOR, "a.btn.btn-primary:nth-child(2)")
    INPUT_CATEGORY_NAME = (By.CSS_SELECTOR, "#input-name-1")
    INPUT_META_TAG_TITLE = (By.CSS_SELECTOR, "#input-meta-title-1")
    INPUT_META_TAG_DESCRIPTION = (By.CSS_SELECTOR, "#input-meta-description-1")
    INPUT_META_TAG_KEYWORDS = (By.CSS_SELECTOR, "#input-meta-keyword-1")
    BUTTON_SAVE_CATEGORY = (By.CSS_SELECTOR, "button.btn.btn-primary:nth-child(1)")
    SELECT_PARENT = (By.CSS_SELECTOR, "#input-parent")
    OPTION_PARENT = (By.PARTIAL_LINK_TEXT, "--- None -")
    INPUT_FILTER = (By.CSS_SELECTOR, "#input-filter")
    INPUT_COLUMNS = (By.CSS_SELECTOR, "#input-column")
    INPUT_SORT_ORDER = (By.CSS_SELECTOR, "#input-sort-order")
    INPUT_STATUS = (By.CSS_SELECTOR, "#input-status")
    SELECT_LAYOUT_OVERRIDE = (By.XPATH, "//tbody/tr[1]/td[2]/select[1]")
    INPUT_KEYWORD = (By.CSS_SELECTOR, "#input-keyword-0-1")
    
    def downArrow(self):
        self.action.send_keys(Keys.CONTROL).send_keys(Keys.ARROW_DOWN).perform()
        self.logger.info("Press 'Down'")
        return self

    def create_categories(self, name: str, mtt: str, mtd: str, mtk: str, parent=None):
        self.click(self.BUTTON_ADD_NEW_CATEGORIES)

        self.write(self.INPUT_CATEGORY_NAME, name)
        self.write(self.INPUT_META_TAG_TITLE, mtt+name)
        self.write(self.INPUT_META_TAG_DESCRIPTION, mtd+name)
        self.write(self.INPUT_META_TAG_KEYWORDS, mtk+name)

        self.click(self.LI_DATA)

        if parent is not None:
            self.write(self.SELECT_PARENT, parent)
            self.click((By.LINK_TEXT, parent))
        else:
            self.click(self.SELECT_PARENT)
            self.click(self.OPTION_PARENT)

        self.click(self.LI_SEO)
        self.write(self.INPUT_KEYWORD, name.lower()+"test")

        self.click(self.LI_DESIGN)
        self.click(self.SELECT_LAYOUT_OVERRIDE)

        for _ in range(7):
            self.downArrow()

        self.click(self.BUTTON_SAVE_CATEGORY)
        self.click(self.Main_Page)
