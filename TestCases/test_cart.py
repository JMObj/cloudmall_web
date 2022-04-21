# # -*- coding:utf-8 -*-
# author='Yang Jia Ming';
# time: 2022/2/10 5:19 下午
import pytest

from PageObject.cart_page import CartPage

class TestCart:
    '''
    购物车用例
    '''
    @pytest.mark.haffprice
    @pytest.mark.cloudmall
    @pytest.mark.usefixtures('init_driver')
    def test_cart_add_item(self,init_driver):
        '''
        添加商品到购物车
        :return:
        '''
        assert CartPage(init_driver).add_item() is True

    @pytest.mark.haffprice
    @pytest.mark.cloudmall
    @pytest.mark.usefixtures('init_driver')
    def test_cart_delete_item(self, init_driver):
        '''
        添加商品到购物车后删除商品
        :return:
        '''
        assert CartPage(init_driver).delete_item() is True

if __name__ == '__main__':
    pytest.main(["test_cart.py"])