import pytest

from TestDatas import CommonData
from TestDatas import loginData
from PageObject.login_page import LoginPage
from PageObject.home_page import HomePage
from common.modus import roanom_eamil



class Testlogin:
    @pytest.mark.haffprice
    @pytest.mark.cloudmall
    @pytest.mark.usefixtures("init_driver")
    def test_login_success(self, init_driver):
        '''
        邮箱注册用例
        :param init_driver: 用例的前置与后置
        :return:
        '''
        LoginPage(init_driver).email_ragister_pass(roanom_eamil(), '123456')
        assert HomePage(init_driver).if_homepage_exist() is True

    # @data(*loginData.login_datas.cases)
    # @pytest.mark.usefixtures("init_driver")
    # @pytest.mark.parametrize("case",loginData.login_datas.cases)
    # def test_login_failed(self,case,init_driver):
    #     li = LoginPage(init_driver).login_not_pass_from(case["user_mobile"],case["user_pwd"],case["user_code"])
    #     assert case["ass"] == li

if __name__ == '__main__':
    pytest.main(["test_login.py"])
