
import re
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, InvalidArgumentException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys  # Agrega esta línea
from selenium.webdriver.remote.webelement import WebElement  # Agrega esta línea


def initialize_webdriver(browser='chrome'):
    """
    Inicializa el controlador WebDriver para un navegador específico.

    :param browser: Navegador a utilizar ('chrome' o 'firefox'). Por defecto, se utiliza 'chrome'.
    :type browser: str
    :return: Instancia del controlador WebDriver configurado para el navegador especificado.
    :rtype: selenium.webdriver.WebDriver
    :raises ValueError: Si el navegador especificado no es compatible.
    
    Esta función inicializa el controlador WebDriver para el navegador indicado. 
    Si se proporciona 'chrome', se utilizará el controlador de Chrome, 
    y si se proporciona 'firefox', se utilizará el controlador de Firefox.

    Ejemplo de uso:
    
    >>> driver = initialize_webdriver()  # Utiliza Chrome por defecto
    >>> driver = initialize_webdriver('firefox')  # Utiliza Firefox
    >>> driver = initialize_webdriver('edge')  # Genera un ValueError ya que 'edge' no es compatible.
    """
    driver = None

    if browser.lower() == 'chrome':
        chrome_options = webdriver.ChromeOptions()

        # Descomenta la siguiente línea si deseas ejecutar en modo sin cabeza (headless)
        # chrome_options.add_argument('--headless')

        # Puedes agregar más opciones según sea necesario

        # Crea una instancia del controlador WebDriver de Chrome
        driver = webdriver.Chrome(options=chrome_options)
    elif browser.lower() == 'firefox':
        # Configuración para el controlador WebDriver de Firefox
        # Asegúrate de tener el geckodriver instalado y disponible en tu sistema
        driver = webdriver.Firefox()
    # Agrega más casos según sea necesario para otros navegadores

    if not driver:
        raise ValueError(f"Navegador no compatible: {browser}")

    return driver

def close_webdriver(driver):
    """
    Cierra el controlador WebDriver.

    :param driver: Instancia del controlador WebDriver que se debe cerrar.
    :type driver: selenium.webdriver.WebDriver
    :raises ValueError: Si la instancia del controlador WebDriver no es válida.

    Esta función cierra la instancia del controlador WebDriver proporcionada como argumento. 
    Asegúrate de llamar a esta función al finalizar tus pruebas o interacciones con el navegador
    para liberar recursos y cerrar la ventana del navegador.

    Ejemplo de uso:

    >>> driver = initialize_webdriver()
    >>> # Realiza operaciones con el controlador WebDriver
    >>> close_webdriver(driver)  # Cierra el controlador WebDriver al finalizar
    """
    # Agrega la lógica necesaria para cerrar el controlador WebDriver.
    if not isinstance(driver, webdriver.WebDriver):
        raise ValueError("La instancia del controlador WebDriver no es válida.")

    try:
        driver.quit()  # Cierra el navegador y libera los recursos
    except Exception as e:
        print(f"Error al cerrar el controlador WebDriver: {e}")

def wait_for_element(driver, by, value, timeout=10):
    """
    Espera hasta que un elemento esté presente en el DOM.

    :param driver: Instancia del controlador WebDriver.
    :type driver: selenium.webdriver.WebDriver
    :param by: Estrategia de búsqueda (por ejemplo, By.ID, By.XPATH).
    :type by: selenium.webdriver.common.by.By
    :param value: Valor del atributo usado por la estrategia de búsqueda.
    :type value: str
    :param timeout: Tiempo máximo de espera en segundos (por defecto, 10 segundos).
    :type timeout: int
    :return: Elemento web encontrado.
    :rtype: selenium.webdriver.remote.webelement.WebElement
    :raises TimeoutException: Si el elemento no está presente después del tiempo de espera.

    Esta función utiliza WebDriverWait para esperar hasta que un elemento esté presente en el DOM.
    Se especifica la estrategia de búsqueda (`by`) y el valor del atributo usado por esa estrategia (`value`).
    El tiempo máximo de espera se establece mediante el parámetro `timeout`.

    Ejemplo de uso:

    >>> from selenium.webdriver.common.by import By
    >>> from selenium.webdriver.support.ui import WebDriverWait
    >>> from selenium.webdriver.support import expected_conditions as EC
    >>>
    >>> driver = initialize_webdriver()
    >>> wait_for_element(driver, By.ID, 'element_id')  # Espera a que un elemento con ID 'element_id' esté presente.
    """

    wait = WebDriverWait(driver, timeout)
    return wait.until(EC.presence_of_element_located((by, value)))


def find_web_element(driver, css_id):
    """
    Encuentra un WebElement usando un tipo de selector y un selector específico.

    Args:
        driver (WebDriver): Instancia del controlador WebDriver.
        type_selector (str): Tipo de selector (por ejemplo, "id", "css", "xpath", etc.).
        selector (str): Valor del selector.

    Returns:
        WebElement: Elemento web encontrado o None si no se encuentra.

    Raises:
        ValueError: Si el tipo de selector no es válido.
    """
    selector_methods = {
        'id': 'By.ID',
        'name': 'By.NAME',
        'css': 'By.CSS_SELECTOR',
        'class': 'By.CLASS_NAME',
        'tag': 'By.TAG_NAME',
        'link': 'By.LINK_TEXT',
        'partial_link': 'By.PARTIAL_LINK_TEXT',
        'xpath': 'By.XPATH',
    }

    try:
        
        match = re.match(r'([a-zA-Z]+):(.+)', css_id)
        print(f"El selector es : {match}")
        # import pdb; pdb.set_trace()
        parts = css_id.split(":")

        if len(parts) != 2:
            raise ValueError(f'Formato incorrecto para se espera por ejemplo css:div[lo_que_sea] pero has informado css_id: {css_id}')

        type_selector, selector = parts
       
        print(f"type_selector {type_selector}, selector {selector}")

        #import pdb; pdb.set_trace()          
        
        if type_selector.lower() in selector_methods:
            webelement ='vacio'
            if type_selector.lower() == 'css':
                return driver.find_element(By.CSS_SELECTOR, selector)
            elif type_selector.lower() == 'id':
                return driver.find_element(By.ID, selector)
            elif type_selector.lower() == 'name':
                return driver.find_element(By.NAME, selector)
            elif type_selector.lower() == 'class':
                return driver.find_element(By.CLASS_NAME, selector)
            elif type_selector.lower() == 'tag':
                return driver.find_element(By.TAG_NAME, selector)
            elif type_selector.lower() == 'link':
                return driver.find_element(By.LINK_TEXT, selector)
            elif type_selector.lower() == 'partial_link':
                return driver.find_element(By.PARTIAL_LINK_TEXT, selector)
            
            return webelement
        else:
            raise ValueError(f'Tipo de selector no válido, se esperan [id,css,name...] pero has informado:  {type_selector}')

    except InvalidArgumentException as e:
        # Manejar la excepción de argumento no válido
        print(f"Error en el formato del selector: {e}")
        return None

    except NoSuchElementException as e:
        # Manejar la excepción de elemento no encontrado
        print(f"Elemento no encontrado: {type_selector}={selector}")
        return None

    except ValueError as e:
        # Manejar la excepción de formato incorrecto de css_id
        print(f"Error en el formato de css_id: {e}")
        return None

