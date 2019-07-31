from selenium.webdriver import Chrome
from Base import InitiateDriver
from Library import ConfigReader
from Pages import RegistrationPage
import pytest

#data driven framework
def dataGenerator():
    li=[['uname1','pass1',['uname2','pass2'],'uname3','pass3']]
    return li


# Variable name is 'data' which is receiving value from method dataGenerator
@pytest.mark.parametrize('data',dataGenerator())
def test_ValidRegistration():
    driver=InitiateDriver.startBroswer()
    #driver.find_element_by_name(ConfigReader.fetchElementLocators('Registration','username_name')).send_keys("hello")
    #driver.find_element_by_name(ConfigReader.fetchElementLocators('Registration','email_name')).send_keys("abc")
    register=RegistrationPage.RegistrationClass(driver)
    register.enter_username('hello')
    #register.enter_email('abc')
    #driver.implicitly_wait(15)
    register.enter_email(data[0])
    register.enter_password(data[1])


    #driver.close()
