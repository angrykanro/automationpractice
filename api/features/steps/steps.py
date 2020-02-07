from behave import given, when, then, step
from selene.support.shared import browser
from selene.api import *

BASE_URL = 'http://automationpractice.com/index.php'
SIGN_IN_PATH = 'controller=my-account'

REGISTRATION_EMAIL = 'mailfortesting13@mailfortestingonly.com'
REGISTRATION_FIRST_NAME = 'tester'
REGISTRATION_LAST_NAME = 'tester'
REGISTRATION_PASSWORD = 'tdlpswd!777531'
REGISTRATION_ADDRESS = 'Tester Street 85'
REGISTRATION_STATE = "24"
REGISTRATION_ZIP = '54545'
REGISTRATION_PHONE_NUMBER = '1234567890'

SIGN_IN_EMAIL = 'mailfortesting@mailfortestingonly.com'
SIGN_IN_PASSWORD = 'tdlpswd!777531'

@given(u'I am logged in')
def step_impl(context):
    context.browser.open_url("{}?{}".format(BASE_URL, SIGN_IN_PATH))
    s("#email").should(be.visible).set_value(SIGN_IN_EMAIL)
    s("#passwd").should(be.visible).set_value(SIGN_IN_PASSWORD)
    s("#SubmitLogin").click()

# @given(u'I am in Landing page')
# def step_impl(context):
#     s("#header_logo").click()

# @when(u'I select Search menu')
# def step_impl(context):
#     s("#search_query_top").click()

# @when(u'I enter ​{searchTerm}')
# def step_impl(context, searchTerm):
#     s("#search_query_top").set_value(searchTerm)

# @when(u'I click on Search button')
# def step_impl(context):
#     s(".button-search").click()

# @when(u'only 1 result is found')
# def step_impl(context):
#     s("#heading-counter").should(have.text("1 result has been found."))

# @when(u'I select the item')
# def step_impl(context):
#     s(".product-container .product_img_link").click()

# @when(u'item description and condition is displayed')
# def step_impl(context):
#     s("#short_description_content").should(be.visible)
#     s("#product_condition").should(be.visible)

# @when(u'I change quantity to 2')
# def step_impl(context):
#     s(".product_quantity_up").click()

# @when(u'I set size to S')
# def step_impl(context):
#     # s(".attribute_fieldset .attribute_label").should(be.visible)

# @when(u'I select Add to cart')
# def step_impl(context):
    

# @when(u'item is successfully added to cart')
# def step_impl(context):
    

# @when(u'I click on Proceed to checkout button')
# def step_impl(context):
    

# @then(u'Shopping cart summary page is opened')
# def step_impl(context):
  

# @then(u'correct description is specified')
# def step_impl(context):
    
# @then(u'amount is correctly calculated')
# def step_impl(context):
   


# @then(u'Proceed to checkout button is visible')
# def step_impl(context):
    
# @when(u'I click on BEST SELLERS button')
# def step_impl(context):
    

# @when(u'I select first item from list')
# def step_impl(context):
    

# @when(u'item description and condition is displayed')
# def step_impl(context):
    

# @when(u'I set size to L')
# def step_impl(context):
    

# @when(u'I set color to Green')
# def step_impl(context):
    

# @when(u'I click on Add to wishlist button')
# def step_impl(context):
    

# @when(u'I open My Whishlist page')
# def step_impl(context):
   

# @when(u'I click on My Wishlist (the one automatically created)')
# def step_impl(context):
   

# @then(u'My Wishlist item are visible')
# def step_impl(context):
    

# @then(u'correct wishlist item preferences is displayed')
# def step_impl(context):
   

@given(u'I am in Sign In page')
def step_impl(context):
    context.browser.open_url("{}?{}".format(BASE_URL, SIGN_IN_PATH))
    s("#email_create").should(be.visible)

@when(u'I enter {email} in Create New Account section')
def step_impl(context, email):
    s("#email_create").set_value(email).press_enter()
    s("#account-creation_form").should(be.visible)

@when(u'I enter valid account details({firstname}, {lastname})')
def step_impl(context, firstname, lastname):
    s("#customer_firstname").set_value(firstname)
    s("#customer_lastname").set_value(lastname)
    s("#passwd").set_value(REGISTRATION_PASSWORD)
    s("#address1").set_value(REGISTRATION_ADDRESS)
    s("#city").set_value(REGISTRATION_LAST_NAME)
    s("#id_state").click()
    s("#id_state>option[value='" + REGISTRATION_STATE + "']").click()
    s("#postcode").set_value(REGISTRATION_ZIP)
    s("#phone_mobile").set_value(REGISTRATION_PHONE_NUMBER)

@when(u'click on Register button')
def step_impl(context):
    s("#submitAccount").click()

@when(u'My Account page is opened')
def step_impl(context):
    s(".page-heading").should(be.visible)
    s('.info-account').should(have.text('Welcome to your account. Here you can manage all of your personal information and orders.'))
    

@when(u'I click on My Personal Information button')
def step_impl(context):
    s(".myaccount-link-list>li>a[title='Information']").click()

@then(u'Your Personal Information page is opened')
def step_impl(context):
    s('.page-subheading').should(have.text('YOUR PERSONAL INFORMATION'))

@then(u'correct personal information({email}, {firstname}, {lastname}) is displayed')
def step_impl(context, email, firstname, lastname):
    s("#firstname").should(have.value(firstname))
    s("#lastname").should(have.value(lastname))
    s("#email").should(have.value(email))