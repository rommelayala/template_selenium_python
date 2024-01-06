mi_proyecto/
|-- setup.py
|-- requirements.txt
|-- mi_app/
|   |-- __init__.py
|   |-- pages/
|   |   |-- __init__.py
|   |   |-- base_page.py
|   |   |-- home_page.py
|   |   |-- login_page.py
|   |-- utils/
|       |-- __init__.py
|       |-- webdriver_utils.py
|-- features/
|   |-- login.feature
|   |-- home_page.feature
|-- steps/
|   |-- __init__.py
|   |-- login_steps.py
|   |-- home_page_steps.py
|-- environment.py (pending)

Ejecutar los test eligiendo el browser
behave --tags=navegador_chrome

Debug in python
import pdb; pdb.set_trace()
n - next
s - entra en el funcion actual
c - continue
l - muestra el codigo fuente
p - print variables ( ejemplo: p selector )

Generacion de documentacion
https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration
pip install sphinx
sphinx-quickstart
en la raiz del proyecto se genera un archivo config.py agregar esta line 
extensions = [
    # ...
    'sphinx.ext.autodoc',
    # ...
]

desde el root del proyecto ejecutar ()
$ make html

esto genera la documentacion en formato html en _build/html/index.html.

para regenerar la documentacion volver a ejecutar make html


Existing steps
    
    Given I browse to page "https://www.saucedemo.com/"
    When I type 'standard_user' in webelement css:input[id='user-name']
    When I type 'secret_sauce' in webelement css:input[placeholder='Password']
    When I click on webelement "id:login-button"
    Then I pause the browser

Pendientes
Login a esta pagin a "https://testpages.eviltester.com/styled/auth/basic-auth-test.html"

en este step When I type 'standard_user' in webelement css:input[id='user-name'] hay que tratar todo el string css:input[...] tal como este otro string 'standard_user'

implementar metodos usando tablas 
    When the user enters valid username and password
      | username_locator | username_value | password_locator                  | password_value |
      | id:=user-name    | your_username  | css:input[placeholder='Password'] | your_password  |
    And the user clicks the login button "css:a[href^='/styled/auth/basic-auth-results.html']"
    Then the user should be redirected to the home page
