from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from my_app.utils.webdriver_utils import find_web_element


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
            self.url = url
            try:
                self.driver.get(url)
            except TimeoutException:
                raise TimeoutException(f"Exception")

    def wait_for_element(self, by, value, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.presence_of_element_located((by, value)))
        except TimeoutException:
            raise TimeoutException(f"Elemento no encontrado: {by}={value}")

    def click_element(self, by, value, timeout=10):
        element = self.wait_for_element(by, value, timeout)
        element.click()

    def enter_text(self, by, value, text, timeout=10):
        element = self.wait_for_element(by, value, timeout)
        element.clear()
        element.send_keys(text)

#===================================================================================================

    def i_browse_to_web_page(self, url, timeout=10):
        """
        Navega a una página web específica.

        :param url: URL de la página web a la que navegar.
        :type url: str
        :param timeout: Tiempo máximo de espera en segundos para cargar la página.
                        Por defecto, se establece en 10 segundos.
        :type timeout: int
        :raises TimeoutException: Si la página no se carga dentro del tiempo especificado.
        """
        try:
            self.driver.get(url)
        except TimeoutException:
            raise TimeoutException(f"Exception")

    def pause(self, seconds):
        """
        Pausa la ejecución de las pruebas durante el número especificado de segundos.

        :param seconds: Número de segundos para pausar la ejecución.
        :type seconds: int
        """
        time.sleep(seconds)

    def pause_until_keypress(self):
        """
        Pausa la ejecución hasta que se presione una tecla.
        """
        input(f"Press key to continue....")

    def click_web_element(self, css_id):
        """
        Realiza un clic en un elemento web específico.

        :param css_id: Identificador CSS del elemento web.
        :type css_id: str
        """
        webelement = find_web_element(self.driver, css_id)
        print(f"Clicking on web_element....")
        webelement.click()

    def send_text_to_input(self, text, css_id):
        """
        Escribe texto en un elemento de entrada web.

        :param text: Texto a escribir en el elemento de entrada web.
        :type text: str
        :param css_id: Identificador CSS del elemento de entrada web.
        :type css_id: str
        """
        webelement = find_web_element(self.driver, css_id)
        text_without_starting_ending_quotes = text.replace("'","")
        print(f"Sending text to input....{text_without_starting_ending_quotes}")
        webelement.send_keys(text_without_starting_ending_quotes)

    def is_visible(self, css_id):
        """
        Verifica si un elemento web es visible.

        :param css_id: Identificador CSS del elemento web.
        :type css_id: str
        :return: True si el elemento es visible, False de lo contrario.
        :rtype: bool
        """
        webelement = find_web_element(self.driver, css_id)
        return webelement.is_displayed()
    
    def get_text_webelement(self,css_id):
        """
        Obtiene el texto de un elemento web.

        :param css_id: Identificador CSS del elemento web.
        :type css_id: str
        :return: Texto del elemento web.
        :rtype: str
        """
        #import pdb; pdb.set_trace()
        webelement = find_web_element(self.driver, css_id)
        return webelement.text



