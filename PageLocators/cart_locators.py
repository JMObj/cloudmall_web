# # -*- coding:utf-8 -*-
# author='Yang Jia Ming';
# time: 2022/2/10 4:39 下午
from selenium.webdriver.common.by import By

class CartLocators:
    '''
    购物车页面元素定位
    '''
    #购物车加购后的商品数量
    cart_shopping_number = (By.XPATH, '//*[text()=1 and @color="primary"]')

    #购物车列表编辑按钮
    cart_update_button = (By.XPATH, '//*[text()="编辑"]')
    #购物车列表删除购物车内商品按钮
    cart_delete_button = (By.XPATH, '//*[text()="删除"]')
    #购物车列表点击删除后二次确认弹窗按钮
    cart_delete_popups_button = (By.XPATH, '//*[text()="确认"]')

    #购物车商品列表结算
    cart_settlement = (By.XPATH,'//*[text()="去结算"]')