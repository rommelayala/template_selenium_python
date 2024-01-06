from selenium.webdriver.common.by import By
from my_app.utils.webdriver_utils import wait_for_element

class LoginPage:
    def __init__(self, driver):
        super().__init__(driver)
        self.url = ""

    def open(self, url):
        self.url = url
        super().open()

    def enter_credentials(self, username_locator, username_value, password_locator, password_value):
        self.enter_text(username_locator, username_value)
        self.enter_text(password_locator, password_value)

    def submit_login(self, button_locator):
        login_button = wait_for_element(self.driver, By.XPATH, "//button[@type='submit']")

        self.click_element(button_locator)

    def is_redirected_to_home(self):
        # Verifica si el usuario está en la página de inicio después del inicio de sesión
        return "home" in self.driver.current_url.lower()
