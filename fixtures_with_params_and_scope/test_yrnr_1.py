import os
import sys
import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.relative_locator import with_tag_name, locate_with
from selenium.webdriver.firefox.service import Service as FirefoxService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope='class')
def setup_ff(request):
    lambdatest_usr = os.getenv('LT_USER')
    lambdatest_key = os.getenv('LT_ACCESS_KEY')
    desired_capabilities ={
        "single_test": {
        "browserName": "Firefox",
        "browserVersion": "104.0",
        "LT:Options": {
          "username": "iamramuhere",
          "accessKey": "96pQHvrEYTbumnaMY7svaferQRhvdYSknl49M9mPJv59hxpfi9",
          "geoLocation": "MX",
          "visual": True,
          "video": True,
          "platformName": "Windows 10",
          "timezone": "UTC-05:00",
          "build": "yrnr_ff",
          "project": "Untitled",
          "console": "true",
          "w3c": True,
          "plugin": "python-pytest"
          }
        }
    }
    desired_capabilities["single_test"]["LT:Options"].update(
    {"username":lambdatest_usr, "accessKey":lambdatest_key})

    ff_options = webdriver.FirefoxOptions()
    ff_options.set_capability('LT:Options', desired_capabilities)
    driver = webdriver.Remote(
        command_executor= f"http://{lambdatest_usr}:{lambdatest_key}@hub.lambdatest.com:80/wd/hub",
        options= ff_options
    )
    # driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    request.cls.driver = driver
    yield
    # tearDown runs after each test case
    driver.quit()

@pytest.fixture(scope='class')
def setup_chrome(request):
    lambdatest_usr = os.getenv('LT_USER')
    lambdatest_key = os.getenv('LT_ACCESS_KEY')
    desired_capabilities = {
      "single_test": {
      "browserName": "Chrome",
      "browserVersion": "105.0",
      "LT:Options": {
        "geoLocation": "IN",
        "visual": True,
        "video": True,
        "platformName": "Windows 10",
        "timezone": "UTC+05:30",
        "project": "Untitled",
        "name": "test_yrnr_1",
        "tags": ["yrnr"],
        "console": True,
        "terminal": True,
        "networkThrottling": "DSL",
        "w3c": True,
        "plugin": "python-pytest"
      }
      }
    }
    desired_capabilities["single_test"]["LT:Options"].update(
    {"username":lambdatest_usr, "accessKey":lambdatest_key})
  
    chrome_options = webdriver.ChromeOptions()
    chrome_options.set_capability('LT:Options', desired_capabilities)
    driver = webdriver.Remote(
        command_executor= f"http://{lambdatest_usr}:{lambdatest_key}@hub.lambdatest.com:80/wd/hub",
        options= chrome_options
    )
    # driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    request.cls.driver = driver
    yield
    # tearDown runs after each test case
    driver.quit()

@pytest.mark.usefixtures("setup_chrome")
class Test_Yrnr_1:
   
    def test_unit_user_should_able_to_add_item_cr(self):
        # try:
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        # self.driver.get('https://maps.google.com/')
        self.driver.maximize_window()
        
        self.driver.find_element(By.NAME, "li1").click()
        self.driver.find_element(By.NAME, "li2").click()
 
        title = "Sample page - lambdatest.com"
        assert title == self.driver.title
 
        sample_text = "Happy Testing CR at LambdaTest"
        email_text_field = self.driver.find_element(By.ID, "sampletodotext")
        email_text_field.send_keys(sample_text)
        sleep(5)
 
        self.driver.find_element(By.ID, "addbutton").click()
        sleep(5)
 
        output_str = self.driver.find_element(By.NAME, "li6").text
        print(output_str)
 
        sleep(2)
 

@pytest.mark.usefixtures("setup_ff")
class Test_Yrnr_2:
   
    def test_unit_user_should_able_to_add_item_ff(self):
        # try:
        self.driver.get('https://lambdatest.github.io/sample-todo-app/')
        # self.driver.get('https://maps.google.com/')
        self.driver.maximize_window()
        
        self.driver.find_element(By.NAME, "li3").click()
        self.driver.find_element(By.NAME, "li4").click()
 
        title = "Sample page - lambdatest.com"
        assert title == self.driver.title
 
        sample_text = "Happy Testing FF at LambdaTest"
        email_text_field = self.driver.find_element(By.ID, "sampletodotext")
        email_text_field.send_keys(sample_text)
        sleep(5)
 
        self.driver.find_element(By.ID, "addbutton").click()
        sleep(5)
 
        output_str = self.driver.find_element(By.NAME, "li6").text
        print(output_str)
 
        sleep(2)
