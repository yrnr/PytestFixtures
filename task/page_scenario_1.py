from multiprocessing.util import sub_debug


class Page_Scenario_1:
    # test variables
    simple_form_demo_url = "simple-form-demo"
    welcome_text = "Welcome to LambdaTest"
    # elements
    LINK_TEXT_SIMPLE_FORM_DEMO = "Simple Form Demo"
    XPATH_USER_MESSAGE = "//input[@id='user-message' and @placeholder='Please enter your Message']"
    XPATH_WELCOME_MESSAGE = f"//label[contains(text(),'Your Message:')]/following-sibling::p[@id='message' and text()='{welcome_text}']"
    ID_SHOW_INPUT_BUTTON = "showInput"

class Page_Scenario_2:
    LINK_TEXT_DRAG_DROP_SLIDERS = "Drag & Drop Sliders"
    XPATH_DRAG_15_95_SLIDER = "//input[@type='range' and @value='15']"
    XPATH_RANGE_OUTPUT = "//output[@id='rangeSuccess']"

class Page_Scenario_3:
    # elements
    XPATH_NAME_FIELD = "//input[@id='name' and @placeholder='Name']"
    XPATH_EMAIL_FIELD = "//input[@placeholder='Email' and @name='email']"
    XPATH_PASSWORD_FIELD = "//input[@id='inputPassword4' and @name='password']"
    XPATH_COMPANY_FIELD = "//input[@id='company' and @name='company']"
    XPATH_WEBSITE_FIELD = "//input[@id='websitename' and @name='website']"
    XPATH_CITY_FIELD = "//input[@id='inputCity' and @name='city']"
    XPATH_ADD1_FIELD = "//input[@id='inputAddress1' and @name='address_line1']"
    XPATH_ADD2_FIELD = "//input[@id='inputAddress2' and @name='address_line2']"
    XPATH_STATE_FIELD = "//input[@id='inputState' and @placeholder='State']"
    XPATH_ZIP_FIELD = "//input[@id='inputZip' and @name='zip']"
    # more elements
    LINK_TEXT_INPUT_FORM_SUBMIT = "Input Form Submit"
    XPATH_BUTTON_SUBMIT = "//button[@type='submit' and text()='Submit']"
    XPATH_COUNTRY_DROPDOWN = "//select[@name='country']"
    XPATH_SUCCESS_MESSAGE = "//p[contains(@class, 'success-msg') and contains(text(),'we will get back')]"

    # test variables
    name = ("Subbu", XPATH_NAME_FIELD)
    email = ("subbu@owncompany.com", XPATH_EMAIL_FIELD)
    password = ("SubbuPswd", XPATH_PASSWORD_FIELD)
    company = ("owncompany", XPATH_COMPANY_FIELD)
    website = ("ownsite", XPATH_WEBSITE_FIELD)
    city = ("bigcity", XPATH_CITY_FIELD)
    addr1 = ("107, subbulane1", XPATH_ADD1_FIELD)
    addr2 = ("subbustreet1", XPATH_ADD2_FIELD)
    state = ("TX", XPATH_STATE_FIELD)
    zip_code = ("12345", XPATH_ZIP_FIELD)
    success_message = ("Thanks for contacting us, we will get back to you shortly.", XPATH_SUCCESS_MESSAGE)
    # more test variables
    validation_message = "Please fill out this field."
    country = 'United States'


