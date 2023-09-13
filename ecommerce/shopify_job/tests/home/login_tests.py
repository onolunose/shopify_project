from pages.home.login_page import LoginPage
from utilities.teststatus import TestStatus
import unittest
import pytest
import utilities.custom_logger as cl
import logging


@pytest.mark.usefixtures("oneTimeSetUp", "setUp")
class LoginTests(unittest.TestCase):
    log = cl.customLogger(logging.DEBUG)

    @pytest.fixture(autouse=True)
    def setUpObject(self, oneTimeSetUp):
        """
        Setup objects for the test class.

        Args:
        - oneTimeSetUp: Fixture for setting up WebDriver instance.
        """
        self.lp = LoginPage(self.driver)
        self.ts = TestStatus(self.driver)

    @pytest.mark.run(order=1)
    def test_invalidLogin(self):
        """
        Test case to verify invalid login functionality.
        """
        self.log.info("*#" * 20)
        self.log.info("test_invalidLogin started")
        self.log.info("*#" * 20)

        # Perform logout and then attempt to login with incorrect credentials
        self.lp.logout()
        self.lp.login("abcdetest@gmail.com", "yyabc123ABC")

        # Verify that the password is incorrect and login is unsuccessful
        result1 = self.lp.incorrectPasswordVerified()
        result2 = self.lp.verifyLoginNotSuccessful()

        # Mark the results for reporting
        self.ts.mark(result1, "Incorrect Verification")
        print("Result2: " + str(result2))
        self.ts.markFinal("test_invalidLogin", result1, "Login Unsuccessful")

    @pytest.mark.run(order=2)
    def test_validLogin(self):
        """
        Test case to verify valid login functionality.
        """
        self.log.info("*##" * 30)
        self.log.info("test_validLogin started")
        self.log.info("*##" * 30)

        # Login with valid credentials and then logout
        self.lp.login("abcdetest@gmail.com", "abc123ABC")



        # Verify successful login
        result1 = self.lp.verifyLoginSuccessful
        result2 = self.lp.verifyLoginSuccessful2()

        # Mark the results for reporting
        print("Result1: " + str(result1))
        print("Result2: " + str(result2))
        self.ts.mark(result2, "Login Verification Successful")

    @pytest.mark.run(order=3)
    def test_logout(self):
        self.lp.logout()
        result3 = self.lp.verifyLogoutSuccessful()
        print("Result3: " + str(result3))
        self.ts.markFinal("test_invalidLogout", result3, "Logout Successful")
        #self.driver.quit()

