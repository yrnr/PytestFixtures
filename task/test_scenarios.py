import pytest
from time import sleep
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from .page_scenarios import Page_Scenario_1 as ps1
from .page_scenarios import Page_Scenario_2 as ps2
from .page_scenarios import Page_Scenario_3 as ps3

@pytest.mark.usefixtures("setup_browser")
class Test_Scenarios:

    @pytest.mark.timeout(30)
    def test_scenario_1(self):
        self.driver.get('https://www.lambdatest.com/selenium-playground')
        self.driver.find_element(By.LINK_TEXT, ps1.LINK_TEXT_SIMPLE_FORM_DEMO).click()
        assert ps1.simple_form_demo_url in self.driver.current_url
        self.driver.find_element(By.XPATH, ps1.XPATH_USER_MESSAGE).send_keys(ps1.welcome_text)
        self.driver.find_element(By.ID, ps1.ID_SHOW_INPUT_BUTTON).click()
        assert ps1.welcome_text == self.driver.find_element(By.XPATH, ps1.XPATH_WELCOME_MESSAGE).text
    
    @pytest.mark.timeout(90)
    def test_scenario_2(self):
        self.driver.get('https://www.lambdatest.com/selenium-playground')
        self.driver.find_element(By.LINK_TEXT, ps2.LINK_TEXT_DRAG_DROP_SLIDERS).click()
        ddslider = self.driver.find_element(By.XPATH, ps2.XPATH_DRAG_15_95_SLIDER)
        for i in range(80):
            ddslider.send_keys(Keys.ARROW_RIGHT)
        ddoutput = self.driver.find_element(By.XPATH, ps2.XPATH_RANGE_OUTPUT).text
        assert int(ddoutput) == 95

    @pytest.mark.timeout(50)
    def test_scenario_3(self):
        self.driver.get('https://www.lambdatest.com/selenium-playground')
        self.driver.find_element(By.LINK_TEXT, ps3.LINK_TEXT_INPUT_FORM_SUBMIT).click()
        self.driver.find_element(By.XPATH, ps3.XPATH_BUTTON_SUBMIT).click()
        validation_msg = self.driver.find_element(By.XPATH, ps3.XPATH_NAME_FIELD).get_property('validationMessage')
        assert ps3.validation_message in validation_msg
        self.driver.find_element(By.XPATH, ps3.name[1]).send_keys(ps3.name[0])
        self.driver.find_element(By.XPATH, ps3.email[1]).send_keys(ps3.email[0])
        self.driver.find_element(By.XPATH, ps3.password[1]).send_keys(ps3.password[0])
        self.driver.find_element(By.XPATH, ps3.company[1]).send_keys(ps3.company[0])
        self.driver.find_element(By.XPATH, ps3.website[1]).send_keys(ps3.website[0])
        self.driver.find_element(By.XPATH, ps3.city[1]).send_keys(ps3.city[0])
        self.driver.find_element(By.XPATH, ps3.addr1[1]).send_keys(ps3.addr1[0])
        self.driver.find_element(By.XPATH, ps3.addr2[1]).send_keys(ps3.addr2[0])
        self.driver.find_element(By.XPATH, ps3.state[1]).send_keys(ps3.state[0])
        self.driver.find_element(By.XPATH, ps3.zip_code[1]).send_keys(ps3.zip_code[0])
        country_select = Select(self.driver.find_element(By.XPATH, ps3.XPATH_COUNTRY_DROPDOWN))
        country_select.select_by_visible_text(ps3.country)
        self.driver.find_element(By.XPATH, ps3.XPATH_BUTTON_SUBMIT).click()
        assert self.driver.find_element(By.XPATH, ps3.success_message[1]).text == ps3.success_message[0]

