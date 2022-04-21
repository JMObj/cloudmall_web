# # # -*- coding:utf-8 -*-
# # author='Yang Jia Ming';
# # time: 2022/2/11 5:19 下午
import pytest

from PageObject.order_page import OrderPage
from common.modus import roanom_eamil
from common.handle_log import do_log


class TestOrder:

    @pytest.mark.cloudmall
    @pytest.mark.usefixtures('init_driver')
    def test_us_guest_adyen_order(self, init_driver):
        '''
            美国未登录用户adyen下单用例
        '''
        assert OrderPage(init_driver).US_adyen_guest_order() is True

    @pytest.mark.haffprice
    @pytest.mark.usefixtures('init_driver')
    def test_us_guest_paypal_order(self, init_driver):
        '''
            美国未登录用户paypal下单用例
        '''
        assert OrderPage(init_driver).US_paypal_guest_order() is True


    @pytest.mark.usefixtures('init_driver')
    def test_us_user_adyen_order(self, init_driver):
        '''
            美国已登录用户adyen下单用例
        '''
        assert OrderPage(init_driver).US_adyen_user_order(roanom_eamil(), '123456') is True

    @pytest.mark.cloudmall
    @pytest.mark.usefixtures('GB_init_driver')
    def test_gb_user_paypal_order(self, GB_init_driver):
        '''
            英国已登录用户paypal下单用例
        '''
        assert OrderPage(GB_init_driver).GB_paypal_user_order(roanom_eamil(), '123456') is True


    @pytest.mark.usefixtures('GB_init_driver')
    def test_gb_user_es_order(self, GB_init_driver):
        '''
            英国已登录用户es下单用例
        '''
        assert OrderPage(GB_init_driver).GB_ES_paypal_user_order(roanom_eamil(), '123456') is True

    @pytest.mark.haffprice
    @pytest.mark.usefixtures('GB_init_driver')
    def test_gb_user_es_order(self, GB_init_driver):
        '''
            英国已登录用户adyen下单用例
        '''
        assert OrderPage(GB_init_driver).GB_adyen_user_order(roanom_eamil(), '123456') is True
#
#
if __name__ == '__main__':
    pytest.main(["test_order.py"])
