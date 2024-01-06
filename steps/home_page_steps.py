# home_page_steps.py

from behave import given, when, then

from my_app.pages.base_page import BasePage
from my_app.pages.home_page import HomePage


@given('the user is on the home page')
def step_user_on_home_page(context):
    context.home_page = HomePage()
    context.home_page.open()

@then('the user should see a welcome message')
def step_user_sees_welcome_message(context):
    assert context.home_page.has_welcome_message()

#===================================================

@given('I browse to page "{url}"')
def step_i_browse_to_web_page(context, url):
    """
    Abre una página web especificada.

    :param context: Contexto del escenario de Behave.
    :type context: behave.runner.Context
    :param url: URL de la página web a la que navegar.
    :type url: str
    """
    context.base_page = BasePage(context.driver)
    context.base_page.open(url)

@then('I pause the browser')
def step_i_pause_browser(context):
    """
    Pausa la ejecución y espera a que el usuario presione una tecla.

    :param context: Contexto del escenario de Behave.
    :type context: behave.runner.Context
    """
    context.base_page = BasePage(context.driver)
    context.base_page.pause_until_keypress()

@when('I click on webelement "{css_id}"')
def step_click_on_webelement(context, css_id):
    """
    Realiza un clic en un elemento web específico.

    :param context: Contexto del escenario de Behave.
    :type context: behave.runner.Context
    :param css_id: Identificador CSS del elemento web.
    :type css_id: str
    """
    context.base_page = BasePage(context.driver)
    # import pdb; pdb.set_trace()
    context.base_page.click_web_element(css_id)

@when('I type {text} in webelement {css_id}')
def step_i_type_in_weblement(context, text, css_id):
    """
    Escribe texto en un elemento de entrada web.

    :param context: Contexto del escenario de Behave.
    :type context: behave.runner.Context
    :param text: Texto a escribir en el elemento de entrada web.
    :type text: str
    :param css_id: Identificador CSS del elemento de entrada web.
    :type css_id: str
    """
    context.base_page = BasePage(context.driver)
    context.base_page.send_text_to_input(text, css_id)

@then('webelement {css_id} is visible')
def step_weblement_is_visible(context, css_id ):
    """
    Verifica si un elemento web es visible.

    :param context: Contexto del escenario de Behave.
    :type context: behave.runner.Context
    :param css_id: Identificador CSS del elemento web.
    :type css_id: str
    """
    context.base_page = BasePage(context.driver)
    assert context.base_page.is_visible(css_id) == True

@then('webelement {css_id} has exactly the text {text}')
def step_webelement_has_exactly_text(context,css_id, text):
    """
    Verifica si un elemento web tiene exactamente el texto especificado.

    :param context: Contexto del escenario de Behave.
    :type context: behave.runner.Context
    :param css_id: Identificador CSS del elemento web.
    :type css_id: str
    :param text: Texto esperado en el elemento web.
    :type text: str
    """
    #css:h3[data-test=\'error\']
    context.base_page = BasePage(context.driver)
    feature_text = text.replace("'","")
    webelement_text = context.base_page.get_text_webelement(css_id)
    #print(f"El contenido del text es-> {text}")
    assert feature_text == webelement_text, f"El texto esperado '{feature_text}' no coincide con el texto real '{webelement_text}'"



