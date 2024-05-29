from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class base_page:
    def __init__(self, driver, wait=10):
        self.driver = driver
        self.logger = driver.logger
        self.wait = WebDriverWait(self.driver, wait)
        self.action = ActionChains(self.driver)
        self.class_name = self.__class__.__name__
        self.logger.info(f"{self.class_name} initialized")

    def element_name(self, element):
        for name, value in vars(self.__class__).items():
            if isinstance(value, (list, tuple)) and element in value:
                return f"{name}[{value.index(element)}]"
            elif value == element:
                return name
        return str(element)

    def find_element(self, element_locator):
        try:
            element = self.wait.until(EC.presence_of_element_located(element_locator))
            self.logger.info(f"Found element {element_locator}")
            return element
        except Exception as e:
            self.logger.error(f"finding element: {e}")
            return None

    def click(self, element_locator):
        try:
            element = self.find_element(element_locator)
            if element is None:
                raise Exception("Element not found")
            element_name = self.element_name(element_locator)
            self.wait.until(EC.element_to_be_clickable(element_locator)).click()
            self.logger.info(f"{self.class_name}: Clicked on '{element_name}'")
        except Exception as e:
            self.logger.error(f"clicking element: {e}")
        return self

    def write(self, element_locator, value):
        self.click(element_locator)
        self._input(element_locator, value)
        return self

    def _input(self, element_locator, value, bool=False):
        try:
            element = self.find_element(element_locator)
            if element is None:
                raise Exception("Element not found")
            element_name = self.element_name(element_locator)
            element.clear()
            element.send_keys(value)
            self.logger.info(f"{self.class_name}: Cleared and wrote '{value}' to '{element_name}'")
        except Exception as e:
            self.logger.error(f"inputting to element: {e}")
        return self
