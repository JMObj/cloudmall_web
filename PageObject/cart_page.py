# # -*- coding:utf-8 -*-
# author='Yang Jia Ming';
# time: 2022/2/10 4:49 下午
import time

from PageLocators.item_locators import ItemLocators
from PageLocators.cart_locators import CartLocators
from selenium.webdriver.support.wait import WebDriverWait  # 等待引入的类
from selenium.webdriver.support import expected_conditions as EC  # 等待的条件

from common.basepage import BasePage
from TestDatas import CommonData
from run import data
from common.handle_log import do_log

class CartPage(BasePage):
    '''
    购物车对象
    '''
    def add_item(self):
        '''
        加购一件商品后查看购物车是否正常展示
        :return:
        '''
        # self.driver.get(data.get('Common_url')+ f'US/zh-Hans/item/{data.get("test_item")}')
        self.driver.get(data.get('Common_url') + f'US/zh-Hans/item/{data.get("item_id")}')
        self.ele_click(ItemLocators.item_add_cart_button,'商品详情页点击加购按钮')
        self.ele_click(ItemLocators.item_add_on_button,'选择商品后点击确认按钮')
        self.ele_click(ItemLocators.item_shopping_cart_button,'商品详情点击购物车按钮')
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(CartLocators.cart_shopping_number))
            return True
        except:
            return False

    def delete_item(self):
        '''
        加购一件商品后在购物车删除该商品是否正常展示
        '''
        self.driver.get(data.get('Common_url') + f'US/zh-Hans/item/{data.get("item_id")}')
        # self.driver.get(CommonData.Common_url.site_url + f'US/zh-Hans/item/{9981835}')
        self.ele_click(ItemLocators.item_add_cart_button, '商品详情页点击加购按钮')
        self.ele_click(ItemLocators.item_add_on_button, '选择商品后点击确认按钮')
        self.ele_click(ItemLocators.item_shopping_cart_button, '商品详情点击购物车按钮')
        time.sleep(3)
        self.ele_click(CartLocators.cart_update_button, '购物车列表编辑按钮')
        self.ele_click(CartLocators.cart_delete_button, '购物车列表删除按钮')
        self.ele_click(CartLocators.cart_delete_popups_button,'删除商品后二次确认')
        time.sleep(4)
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(CartLocators.cart_shopping_number))
            # self.wait_ele_visible(CartLocators.cart_shopping_number,'检测购物车商品数量是否为1',time_out=5)
        except:
            return True
        else:
            return False