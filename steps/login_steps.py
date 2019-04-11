@step('I open login page')
def step_impl(context):
    context.start_page.login()


@step('I login with "{username}" and "{password}"')
def step_impl(context, username, password):
    context.login_page.login(username, password)


@step('I am on main page')
def step_impl(context):
    assert (not context.main_page.is_home_tab_selected())
