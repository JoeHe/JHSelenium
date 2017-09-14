import unittest
from jh.pages import LoginPage
from jh.utils import utils
from  jh.pages import HomePage


class TestBing(unittest.TestCase):
    def test_login(self):
        driver = utils.Utils(browser="ff")
        loginpage = LoginPage.LoginPage(driver)
        loginpage.input_name("kyle")
        loginpage.input_pwd("abc")
        homepage = loginpage.submit()

