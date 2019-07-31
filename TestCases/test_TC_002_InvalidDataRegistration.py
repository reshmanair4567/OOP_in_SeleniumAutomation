from Base import InitiateDriver
#for elements
from Library import ConfigReader
from Pages import RegistrationPage

def test_registration_invalid_data():
    driver=InitiateDriver.startBroswer()
    register = RegistrationPage.RegistrationClass(driver)
    register.enter_password('password')
    driver.implicitly_wait(15)
    driver.close()


