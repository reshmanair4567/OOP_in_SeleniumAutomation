from selenium.webdriver import Chrome
from selenium.webdriver import Firefox
#to read library file here
from Library import ConfigReader

def startBroswer():
    global driver
    if ConfigReader.readConfigData('Details','Application_URL')=="Chrome":
        path = "C:\\Users\\User\\Desktop\\Chrome WebDriver\\chromedriver_win32\\chromedriver.exe"
        driver=Chrome(executable_path=path)
    elif ConfigReader.readConfigData('Details','Application_URL')=="Firefox":
        path = "C:\\Program Files\\Mozilla Firefox\\firefox.exe"
        driver=Firefox(executable_path=path)
    else:
        path = "C:\\Users\\User\\Desktop\\Chrome WebDriver\\chromedriver_win32\\chromedriver.exe"
        driver=Chrome(executable_path=path)


    driver.get(ConfigReader.readConfigData('Details','Application_URL'))
    driver.implicitly_wait(15)
    driver.maximize_window()
    return driver


def closeBrowser():
    driver.close()

