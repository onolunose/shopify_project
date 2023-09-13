import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.common.exceptions import*

class HomePage():
    def login_test(self):
        baseURL = "https://shopify.com/"
        driver = webdriver.Firefox()
        driver.fullscreen_window()
        driver.get(baseURL)
        driver.implicitly_wait(10)
        dd=ActionChains(driver)

        _my_store = "(//p[contains(text(),'My Store')])"
        _log_out = "//span[normalize-space()='Log out']"

        _login_mainlink = "(//a[contains(text(), 'Log')])[1]"
        _login_link = "(//button[contains(text(), 'Log')])[1]"
        _email_field = "//input[@id='account_email']"
        _continue_IfLogin = "(//button[contains(text(), 'Continue')])[1]"
        _password_field = "//input[@id='account_password']"
        _login_in_after_password = "(//button[contains(text(), 'Log')])[1]"

        _self_product = "//span[contains(text(), 'by me')]"
        _drop_shipping = "//span[contains(text(), 'Sourced')]"
        _print_on_product = "//span[contains(text(), 'designs')]"
        _digital_products = "//span[contains(text(), 'digital')]"
        _services = "//span[contains(text(), 'Coaching')]"
        _decide_later = "//span[contains(text(), 'decide')]"
        _next_button2 = "(//span[contains(text(), 'Next')])[1]"
        _france = "// select[ @ id = 'country'] // option[ @ value = 'FR']"
        _next_button3 ="(// span[contains(text(), 'Next')])[2]"
        _login_link = "//div[1]//li[2]//a[contains(text(), 'Start free trial')]"
        _skip_all = "navigation-skip-all-button"
        _select_starting = "//span[contains(text(), 'just ')]"
        _online_store = "//span[contains(text(), 'fully')]"
        _add_buy_button = "//span[contains(text(), 'Add')]"
        _online_marketplace = "//span[contains(text(), 'Amazon')]"
        _in_person = "//span[contains(text(), 'pop-ups')]"
        _social_media = "//span[contains(text(), 'Tik')]"
        _not_sure = "//span[contains(text(), 'not')]"
        # _select_already = "//input[@id=':r4:']"
        # _login_link = "//li[1]//a[contains(text(), 'Log In')]"
        # _email_field = "//input[@id='usernameOrEmail']"
        _self_product = "//span[contains(text(), 'by me')]"
        _drop_shipping = "//span[contains(text(), 'Sourced')]"
        _print_on_product = "//span[contains(text(), 'designs')]"
        _digital_products = "//span[contains(text(), 'digital')]"
        _services = "//span[contains(text(), 'Coaching')]"
        _decide_later = "//span[contains(text(), 'decide')]"
        # _login_button = "//button[contains(text(), 'Continue')]"
        # _password_field = "//input[@id='password']"
        # _login_pass="//div/button[contains(text(),'Log In')]"
        # _assert_button = "//ul//li[(@id='wp-admin-bar-my-account')]"
        _back = "//div[3]//span[@class='Polaris-Button__Text_yj3uv Polaris-Button--removeUnderline_adav6'][contains(text(),'Back')]"
        _next_button = "//div[4]//span[@class='Polaris-Button__Text_yj3uv']"
        _select_already = "//span[contains(text(), 'I’m already selling online or in person')]"
        _select_starting = "//span[contains(text(), 'just ')]"

        elementByXPath = driver.find_element(By.XPATH, _login_link)
        time.sleep(4)

        elementByXPath.click()
        #
        element2= driver.find_element(By.XPATH, _select_already)
        # ddd=print(elementBy)
        # wait = WebDriverWait(driver, 10)
        # element2 = driver.find_element(By.LINK_TEXT, _select_already)
        # time.sleep(5)
        ele=element2.text
        # driver.execute_script("arguments[0].scrollIntoView();", element2)
        element2.click()
        print(ele)

        element29 = driver.find_element(By.XPATH, _select_starting)
        # ddd=print(elementBy)
        # wait = WebDriverWait(driver, 10)
        # element2 = driver.find_element(By.LINK_TEXT, _select_already)
        # time.sleep(5)
        elect = element2.text
        # driver.execute_script("arguments[0].scrollIntoView();", element2)
        element29.click()
        print(elect)

        element3 = driver.find_element(By.XPATH, _next_button )
        # ddd=print(elementBy)
        # wait = WebDriverWait(driver, 10)
        # element2 = driver.find_element(By.LINK_TEXT, _select_already)
        # time.sleep(5)
        eles = element3.text
        # driver.execute_script("arguments[0].scrollIntoView();", element2)
        element3.click()
        print(eles)
        time.sleep(5)

        driver.find_element(By.XPATH, _online_store).click()
        time.sleep(4)
        driver.find_element(By.XPATH, _add_buy_button).click()
        time.sleep(4)
        driver.find_element(By.XPATH, _online_marketplace).click()
        time.sleep(4)
        driver.find_element(By.XPATH,  _in_person ).click()
        time.sleep(4)

        driver.find_element(By.XPATH,  _social_media ).click()
        time.sleep(4)
        lop=driver.find_element(By.XPATH,  _not_sure )
        eles45 = lop.text
        # driver.execute_script("arguments[0].scrollIntoView();", element2)
        lop.click()
        print(eles45)
        time.sleep(4)


        element34 = driver.find_element(By.XPATH, _next_button)
        # ddd=print(elementBy)
        # wait = WebDriverWait(driver, 10)
        # element2 = driver.find_element(By.LINK_TEXT, _select_already)
        # time.sleep(5)
        eles4 = element34.text
        # driver.execute_script("arguments[0].scrollIntoView();", element2)
        element34.click()
        print(eles4)

        driver.find_element(By.XPATH, _self_product).click()
        time.sleep(4)
        driver.find_element(By.XPATH, _drop_shipping).click()
        time.sleep(4)

        driver.find_element(By.XPATH, _print_on_product).click()
        time.sleep(4)
        driver.find_element(By.XPATH, _services).click()
        time.sleep(4)
        driver.find_element(By.XPATH, _digital_products).click()
        time.sleep(4)
        driver.find_element(By.XPATH, _decide_later).click()
        time.sleep(4)
        driver.find_element(By.XPATH, _next_button2).click()
        time.sleep(4)
        driver.find_element(By.XPATH, _france).click()
        time.sleep(4)
        driver.find_element(By.XPATH, _next_button3).click()
        time.sleep(4)
        driver.find_element(By.XPATH, _login_mainlink).click()
        time.sleep(4)
        email=driver.find_element(By.XPATH, _email_field)
        email.click()
        time.sleep(2)
        email.send_keys("abcdetest@gmail.com")
        time.sleep(2)
        driver.find_element(By.XPATH, _continue_IfLogin).click()
        time.sleep(4)
        pass_word = driver.find_element(By.XPATH, _password_field)
        pass_word.click()
        time.sleep(2)
        pass_word.send_keys("abc123ABC")
        time.sleep(2)
        driver.find_element(By.XPATH, _login_in_after_password).click()
        time.sleep(4)

        wait = WebDriverWait(driver, timeout=250,
                             poll_frequency=1,
                             ignored_exceptions=[NoSuchElementException,
                                                 ElementNotVisibleException,
                                                 ElementNotSelectableException])
        element = wait.until(EC.presence_of_element_located((By.XPATH, _my_store)))
        element.click()
        time.sleep(4)
        driver.find_element(By.XPATH, _log_out).click()

        driver.quit()

run_tests = HomePage()
run_tests.login_test()