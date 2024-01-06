from behave import given, when, then


@when('the user enters valid username and password')
def step_user_enters_valid_credentials(context):
    for row in context.table:
        context.login_page.enter_credentials(
            row["username_locator"],row["username_value"],
            row["password_locator"],row["password_value"]
        )

@when('the user clicks the login button "{button_locator}"')
def step_user_clicks_login_button(context, button_locator):
    context.login_page.click_login_button(button_locator)

@then('the user should be redirected to the home page')
def step_user_redirected_to_home_page(context):
    assert context.login_page.is_redirected_to_home()

#==========================================================================
