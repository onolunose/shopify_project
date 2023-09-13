import utilities.custom_logger as cl

import logging
from base.basepage import BasePage
from utilities.util import Util
from selenium.common.exceptions import*


class LoginPage(BasePage):
    """
            Initialize LoginPage class with driver instance and NavigationPage instance.

            Args:
            - driver: WebDriver instance.
            """


    log2 = Util()
    log = cl.customLogger(logging.DEBUG)

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver


    # Locators
    _log_out_confirm="//h1[contains(text(), 'logged')]" # the text is "You have successfully logged out"
    _confirm_order="//div//span[contains(text(), 'Order')]" # successfull login verification point or to click My store
    _confirmation_textmessage="A link to reset your password has been emailed to you.]"
    _change_email="//a[contains(text(), 'Change')]"
    _confirm_password_reset_link = "//p[contains(text(), 'emailed')]"
    _login_after_reset="//button[contains(text(), 'Log')]"
    _password_field_reset="//input[contains(@id, 'account_password')]"
    _return_to_login ="//a[contains(text(), 'Return')]"
    _reset_password ="//button[contains(text(), 'Reset')]"
    _incorrect_password="//span[contains(text(), 'Incorrect')]"
    _my_store = "(//p[contains(text(),'My Store')])"
    _log_out = "//span[normalize-space()='Log out']"
    _start_link="//div[1]//li[2]//a[contains(text(), 'Start free trial')]"
    _select_already="//span[contains(text(), 'I’m already selling online or in person')]"
    _select_starting="//span[contains(text(), 'just ')]"
    _online_store="//span[contains(text(), 'fully')]"
    _add_buy_button="//span[contains(text(), 'Add')]"
    _online_marketplace="//span[contains(text(), 'Amazon')]"
    _in_person="//span[contains(text(), 'pop-ups')]"
    _social_media="//span[contains(text(), 'Tik')]"
    _not_sure="//span[contains(text(), 'not')]"
    _skip_all="//span[contains(text(), 'All')]"
    _next1_button= "(//span[contains(text(), 'Next')])[1]"
    _skip="(//span[contains(text(), 'Skip')])[2]"
    _back="(//span[contains(text(), 'Back')])[1]"
   #WHAT DO YOU PLAN TO SELL PAGE
    _self_product="//span[contains(text(), 'by me')]"
    _drop_shipping="//span[contains(text(), 'Sourced')]"
    _print_on_product="//span[contains(text(), 'designs')]"
    _digital_products ="//span[contains(text(), 'digital')]"
    _services= "//span[contains(text(), 'Coaching')]"
    _decide_later= "//span[contains(text(), 'decide')]"
    _skip_all2="//span[contains(text(), 'All')]"
    _skip2="(//span[contains(text(), 'Skip')])[2]"
    _back2="(//span[contains(text(), 'Back')])[1]"
    _next_button2 ="//div[4]//span[@class='Polaris-Button__Text_yj3uv']"
    #"(//span[contains(text(), 'Next')])[1]"
    _france="// select[ @ id = 'country'] // option[ @ value = 'FR']"
    #_next_button3 = "(// span[contains(text(), 'Next')])[2]"
    _next_button3 = "(//span[contains(text(), 'Next')])[1]"
    _next_button4 = "(// span[contains(text(), 'Next')])[2]"
    _login_mainlink = "(//a[contains(text(), 'Log')])[1]"

    _login_link = "(//a[contains(text(), 'Log')])[1]"
    _email_field = "//input[@id='account_email']"

    _continue_IfLogin = "(//button[contains(text(), 'Continue')])[1]"
    _password_field = "//input[@id='account_password']"

    _login_in_after_password = "(//button[contains(text(), 'Log')])[1]"

    #_login_with_email ="Continue with email"  #link

    #_continue_IfEmail="(//span[contains(text(), 'Continue')])[1]"
    #_get_started= "(//a[contains(text(), 'Get')])[1]"



    _forget_password="Forgot password" #link
    _change_email="Change email"
    #AFTER LOGIN IT ALWAYS TAKE LIKE 3MINS FOR YOUR STORE TO BE BUILT
    #AFTER SUCCESFUL LOGIN A POP UP BOX DISPLAYED IT CAN BE CLOSE WITH X
    _my_store="(//p[contains(text(),'My Store')])"
    _log_out= "//span[normalize-space()='Log out']"
    _log_out_successful="//h1[@class='logout-hero__heading gutter-bottom--reset']"
    def clickStartFree(self):
        self.elementClick(self._start_link, locatorType="xpath")
    def selectAlready(self):
        self.elementClick(self._select_already, locatorType="xpath")
    def selectStarting(self):
        self.elementClick(self._select_starting, locatorType="xpath")
    def clickNext(self):
        self.elementClick(self._next1_button, locatorType="xpath")
    def onlineStore(self):
        self.elementClick(self._online_store, locatorType="xpath")
    def addBuyButton(self):
        self.elementClick(self._add_buy_button, locatorType="xpath")
    def onlineMarketplace(self):
        self.elementClick(self._online_marketplace, locatorType="xpath")
    def inPerson(self):
        self.elementClick(self._in_person, locatorType="xpath")
    def socialMedia(self):
        self.elementClick(self._social_media, locatorType="xpath")
    def notSure(self):
        self.elementClick(self._not_sure, locatorType="xpath")
    def nextButton2(self):
        self.elementClick(self._next_button2, locatorType="xpath")
    def selfProduct(self):
        self.elementClick(self._self_product, locatorType="xpath")
    def dropShipping(self):
        self.elementClick(self._drop_shipping, locatorType="xpath")
    def printProduct(self):
        self.elementClick(self._print_on_product, locatorType="xpath")
    def service(self):
        self.elementClick(self._services,locatorType="xpath")
    def digitalProduct(self):
        self.elementClick(self._digital_products, locatorType="xpath")
    def decideLater(self):
        self.elementClick(self._decide_later, locatorType="xpath")
    def nextButton3(self):
        self.elementClick(self._next_button3, locatorType="xpath")
    def selectCountry(self):
        self.elementClick(self._france, locatorType="xpath")
        self.log2.sleep(4)
    def nextButton4(self):
        self.elementClick(self._next_button4, locatorType="xpath")
    def loginMainLink(self):
        self.elementClick(self._login_mainlink, locatorType="xpath")
    def emailField(self):
        self.elementClick(self._email_field, locatorType="xpath")
    def enterEmail(self, email):
        self.sendKeys(email, self._email_field, locatorType="xpath")
    #def continueLogin(self):
        #self.elementClick(self._continue_IfLogin, locatorType="xpath")

    def passwordField(self):
        self.elementClick(self._password_field, locatorType="xpath")
    def enterPassword(self, password):
        self.sendKeys(password, self._password_field, locatorType="xpath")

    def clickLogin(self):
        self.elementClick(self._login_in_after_password, locatorType="xpath")



    def login(self, email="", password=""):
        """
                Perform login action.

                Args:
                - email (str): Email address for login.
                - password (str): Password for login.
                """
        self.clickStartFree()
        self.selectAlready()
        self.selectStarting()
        self.clickNext()
        self.onlineStore()
        self.addBuyButton()
        self.onlineMarketplace()

        self.socialMedia()
        self.notSure()
        self.log2.sleep(4)
        self.nextButton2()
        self.selfProduct()
        self.dropShipping()
        self.service()
        self.printProduct()

        self.digitalProduct()
        self.decideLater()

        self.nextButton3()
        # self.log2.sleep(4)
        #self.selectCountry()
        self.log2.sleep(4)
        select_country = self.waitForElement(locator=self._france,
                                             locatorType="xpath", pollFrequency=1)
        self.elementClick(element=select_country)
        self.log2.sleep(4)
        self.nextButton4()
        self.loginMainLink()
        self.log2.sleep(4)
        captcha_element=self.emailField()
        try:
            captcha_element = captcha_element
            if captcha_element:
                print("captcha element detected")
                input()
        except NoSuchElementException:
            pass
        #self.sendKeys(email="abcdetest@gmail.com")

        self.enterEmail(email)
        self.log2.sleep(10)
        continue_login = self.waitForElement(locator=self._continue_IfLogin,
                                                locatorType="xpath", pollFrequency=1)
        self.elementClick(element=continue_login)
        self.log2.sleep(10)
        #self.continueLogin()
        self.passwordField()


        self.log2.sleep(4)
        self.enterPassword(password)

        self.log2.sleep(4)
        # click_login = self.waitForElement(locator=self._login_in_after_password,timeout=2,
        #                                      locatorType="xpath", pollFrequency=1)
        #
        # self.elementClick(element=click_login)

        self.clickLogin()


    # try:
    #     captcha_element = driver.find_element_by_id("captcha")  # Adjust the selector as needed
    #     if captcha_element:
    #         print("Captcha detected! Please solve the captcha manually and then press Enter to continue.")
    #         input()  # Wait for user to press Enter
    # except NoSuchElementException:
    #     pass

    # def incorrectPassword(self):
    #     self.elementClick(self._incorrect_password, locatorType="xpath")
    #
    # def verifyLoginSuccessful(self):
    #     result_first=self.waitForElement(self._incorrect_password,
    #                                    locatorType="xpath")
    #     result = self.isElementPresent(locator=self._incorrect_password,
    #                                    locatorType="xpath")
    #     return result
    #
    def verifyLoginNotSuccessful(self):
        """
                Verify if login was not successful.

                Returns:
                - bool: True if login was not successful, False otherwise.
                """
        result_first = self.waitForElement(self._incorrect_password,
                                           locatorType="xpath")

        result = self.isElementPresent(locator=self._incorrect_password,
                                       locatorType="xpath")  # Here the result should output boolean value cos that what
                                                            #   our setResult method needs to fill the resultList.
        return result
    def incorrectPasswordVerified(self):
        result_first = self.waitForElement(self._incorrect_password,
                                           locatorType="xpath")
        element = result_first.text
        print("Actual text" + element)
        result = self.log2.verifyTextMatch(actualText=element, expectedText="Incorrect password")
        return result


    def verifyLoginTitle(self):
        return self.verifyPageTitle("shopify.com")
    def verifyLoginSuccessful(self):
        """
                Verify if login successful.

                Returns:
                - bool: True if login was successful, False otherwise.
                """
        result_first = self.waitForElement(self._confirm_order,
                                           locatorType="xpath")
        result = self.isElementPresent(locator=self._confirm_order,
                                       locatorType="xpath")
        return result
    def verifyLoginSuccessful2(self):


        result_first = self.waitForElement(self._my_store,
                                           locatorType="xpath")
        result = self.isElementPresent(locator=self._my_store,
                                       locatorType="xpath")
        return result

    def logout(self):

        #self.nav.navigateToUserSettings()
        logoutLinkElement = self.waitForElement(locator="(//p[contains(text(),'My Store')])",timeout=90,
                          locatorType="xpath", pollFrequency=1)
        self.elementClick(element=logoutLinkElement)
        self.elementClick(locator="//span[normalize-space()='Log out']",
                          locatorType="xpath")
    def verifyLogoutSuccessful(self):

        """
                Verify if logout was successful.

                Returns:
                - bool: True if logout was successful, False otherwise.
                """
        result_first = self.waitForElement(self._log_out_confirm,
                                           locatorType="xpath")
        result = self.log2.verifyTextMatch(actualText=self._log_out_confirm, expectedText="You have successfully logged out")
        return result
    #
    def clearFields(self):
        emailField = self.getElement(locator=self._email_field)
        emailField.clear()
        passwordField = self.getElement(locator=self._password_field)
        passwordField.clear()