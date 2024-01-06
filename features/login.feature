Feature: Login functionality on the specified URL

  Background: Browse to main page
    Given I browse to page "https://www.saucedemo.com/"
  
  Scenario: User logs in with valid credentials
    
    When I type 'standard_user' in webelement css:input[id='user-name']
    When I type 'secret_sauce' in webelement css:input[placeholder='Password']
    When I click on webelement "id:login-button"
    
  
  Scenario: User logs in using only username
    When I type 'standard_user' in webelement css:input[id='user-name']
    When I click on webelement "id:login-button"
    Then webelement css:h3[data-test='error'] is visible
    Then webelement css:h3[data-test='error'] has exactly the text 'Epic sadface: Password is required'

    Scenario: User logs in using wrong credentials
    When I type 'standard_user' in webelement css:input[id='user-name']
    When I type 'bad_password' in webelement css:input[placeholder='Password']
    When I click on webelement "id:login-button"
    Then webelement css:h3[data-test='error'] is visible
    Then webelement css:h3[data-test='error'] has exactly the text 'Epic sadface: Username and password do not match any user in this service'  

#    Then I pause the browser

#    When the user enters valid username and password
#      | username_locator             | username_value | password_locator                       | password_value |
#      | id:=user-name | your_username | css:input[placeholder='Password'] | your_password |
#    And the user clicks the login button "css:a[href^='/styled/auth/basic-auth-results.html']"
#    Then the user should be redirected to the home page
