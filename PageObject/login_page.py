import time

from selenium.webdriver.support.wait import WebDriverWait  #等待引入的类
from selenium.webdriver.support import expected_conditions as EC #等待的条件
from selenium.webdriver.remote.webdriver import WebDriver

from PageLocators.login_locators import LoginLocators
from PageLocators.home_locators import HomeLocators
from common.basepage import BasePage

class LoginPage(BasePage):
    """
    登录注册用例
    """

    def email_ragister_pass(self,user_eamil,user_password,user_name = 'test'):
        '''
        邮箱注册登录
        :param user_eamil
        :param user_password: 密码
        :param user_name: 验证码
        :return:
        '''
        self.wait_ele_visible(HomeLocators.home_menu,'首页菜单按钮')
        self.ele_click(HomeLocators.home_menu,'点击首页菜单按钮')
        self.ele_click(LoginLocators.login_or_register_button,'点击首页登录注册按钮')
        time.sleep(1)
        self.ele_click(LoginLocators.email_button,'选择邮箱注册')
        self.input_text(LoginLocators.email_enter,'邮箱注册输入框',user_eamil)
        self.ele_click(LoginLocators.email_ragister_button,'输入邮箱后的注册按钮')
        self.input_text(LoginLocators.name_enter,'邮箱注册姓名输入框',user_name)
        self.input_text(LoginLocators.password_enter,'邮箱注册密码输入框',user_password)
        self.ele_click(LoginLocators.save_button,'邮箱注册输入完所填的信息后的保存按钮')







