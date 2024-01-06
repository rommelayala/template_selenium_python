from selenium.webdriver.common.by import By
from my_app.utils.webdriver_utils import wait_for_element

class HomePage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "url_de_tu_aplicacion/home"

    def open(self):
        self.driver.get(self.url)

    def has_welcome_message(self):
        # Verifica si hay un mensaje de bienvenida en la página de inicio
        welcome_message = wait_for_element(self.driver, By.ID, "welcome-message", timeout=5)
        return welcome_message is not None and welcome_message.is_displayed()
