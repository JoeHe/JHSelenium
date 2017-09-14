from jh.pages import HomePage
#from jh.utils import utils
from jh.setting import LoginIdentify

class LoginPage(object):
    def __init__(self, driver):
        self.driver = driver
        self.driver.open(LoginIdentify.url)
        if(self.driver.get_title() != "登录你的 Microsoft 帐户"):
            raise Exception("This is not Login page!!!")

    def input_name(self, usrname):
        self.driver.type(LoginIdentify.user_name, usrname)

    def input_pwd(self, pwd):
        self.driver.type(LoginIdentify.pwd, pwd)

    def submit(self):
        return HomePage.HomePage(self.driver)

