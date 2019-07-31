from selenium.webdriver import Chrome

import time
import pytest

@pytest.fixture(scope="module")
def environment_setup():
    global driver
    path = "C:\\Users\\User\\Desktop\\Chrome WebDriver\\chromedriver_win32\\chromedriver.exe"
    driver = Chrome(executable_path=path)
    driver.get("http://www.thetestingworld.com/testings")
    driver.maximize_window()
    yield
    driver.implicitly_wait(15)
    driver.close()


def test_verify_registration(environment_setup):
    driver.find_element_by_xpath("//label[text()='Login']").click()
    driver.find_element_by_name("_txtUserName").send_keys("test")
    driver.find_element_by_name("_txtPassword").send_keys("test")
    driver.find_element_by_xpath("//input[@type='submit' and @value='Login']").click()
    driver.find_element_by_xpath("//a[contains(text(),'My Account')]").click()
    driver.find_element_by_xpath("//a[contains(text(),'Update')]").click()
    time.sleep(10)
    allwindows=driver.window_handles
    #print(allwindows)
    mainWin=""

    for win in allwindows:
        driver.switch_to.window(win)
        #print(driver.current_url)
        if(driver.current_url=='http://www.thetestingworld.com/testings/manage_customer.php'):
            driver.find_element_by_xpath("//button[text()='Start Download']").click()
            time.sleep(5)
            driver.close()
        elif(driver.current_url=='http://www.thetestingworld.com/testings/dashboard.php'):
            #mainwindow
            mainWin=win


    driver.switch_to.window(mainWin)
    print(driver.current_url)






