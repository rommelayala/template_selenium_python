from my_app.utils.webdriver_utils import initialize_webdriver, close_webdriver

def before_all(context):
    # Configuración global antes de ejecutar cualquier escenario
    browser = context.config.userdata.get("navegador", "chrome")
    context.driver = initialize_webdriver(browser)

def after_all(context):
    # Limpieza global después de ejecutar todos los escenarios
    context.driver.quit()
