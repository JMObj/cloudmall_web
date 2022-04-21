# # -*- coding:utf-8 -*-
# author='Yang Jia Ming';
# time: 2022/2/9 5:05 下午
import time

from PageLocators.home_locators import HomeLocators
from PageLocators.item_locators import ItemLocators
from selenium.webdriver.support.wait import WebDriverWait  # 等待引入的类
from selenium.webdriver.support import expected_conditions as EC  # 等待的条件
from common.basepage import BasePage
from TestDatas import CommonData
from run import data

class ItemPage(BasePage):

    '''
    商品对象
    '''
    def buy_also_buy(self):
        '''
        商品详情页查看Buy_also_buy是否正常，Buy_also_buy商品列表存在商品表示通过
        :return:
        '''
        # self.wait_ele_visible(HomeLocators.home_search, '首页搜索按钮')
        # self.ele_click(HomeLocators.home_search, '点击首页搜索按钮')
        # self.input_text(HomeLocators.input_search, '首页搜索输入框', f'{data.get("buy_also_buy_item")}')  # 输入buy_also_buy商品后点击搜索
        # self.key_board(HomeLocators.input_search, '首页搜索输入框', 1)
        # self.ele_click(ItemLocators.buy_itmes_list, '点击buy_also_buy商品进入详情页')
        self.driver.get(data.get("Common_url") + f'US/zh-Hans/item/{data.get("buy_also_buy_item")}')
        time.sleep(3)
        self.slide(0, 1500, 'buy_also_buy商品详情页滑动')
        self.ele_click(ItemLocators.related_products_button, '点击查看buy_also_buy商品列表按钮')
        try:
            self.wait_ele_visible(HomeLocators.secarch_results, 'buy_also_buy商品列表购物车图标')
            return True
        except:
            return False

    def item_size(self):
        '''
        商品详情页查看尺码表是否正常，尺码表商品列表存在文案How To Measure表示通过
        :return:
        '''
        # self.wait_ele_visible(HomeLocators.home_search, '首页搜索按钮')
        # self.ele_click(HomeLocators.home_search, '点击首页搜索按钮')
        # self.input_text(HomeLocators.input_search, '首页搜索输入框', 44626278)  # 输入尺码表商品后点击搜索
        # self.key_board(HomeLocators.input_search, '首页搜索输入框', 1)
        # self.ele_click(ItemLocators.buy_itmes_list, '点击尺码表商品进入详情页')
        self.driver.get(data.get("Common_url") + f'US/zh-Hans/item/{data.get("size_item")}')
        time.sleep(3)
        self.slide(0, 500, '商品详情页滑动')
        self.ele_click(ItemLocators.item_specification, '打开商品规格')
        self.ele_click(ItemLocators.size_button, '点击查看商品尺码表按钮')
        try:
            self.wait_ele_visible(ItemLocators.size_Details, '检测尺码表详情页How To Measure是否存在')
            return True
        except:
            return False

    def item_comment(self):
        '''
        商品详情页查看评论功能是否正常，尺码表商品列表存在文案How To Measure表示通过
        :return:
        '''
        # self.wait_ele_visible(HomeLocators.home_search, '首页搜索按钮')
        # self.ele_click(HomeLocators.home_search, '点击首页搜索按钮')
        # self.input_text(HomeLocators.input_search, '首页搜索输入框', 39592674)  # 输入尺码表商品后点击搜索
        # self.key_board(HomeLocators.input_search, '首页搜索输入框', 1)
        # self.ele_click(ItemLocators.comment_items_list, '点击评论商品进入详情页')
        self.driver.get(data.get("Common_url") + f'US/zh-Hans/item/{data.get("comment_item")}')
        time.sleep(3)
        self.slide(0, 500, '评论商品详情页滑动')
        self.ele_click(ItemLocators.item_comment, '商品详情页打开评论')
        try:
            self.wait_ele_visible(ItemLocators.comment_list, '检测评论详情页 所有 文案是否存在')
            return True
        except:
            return False

    def itme_video(self):
        '''
        商品详情页查看播放功能是否正常，点击播放按钮后，播放图标消失表示通过
        :return:
        '''
        self.driver.get(data.get("Common_url") + f'US/zh-Hans/item/{data.get("video_item")}')
        self.ele_click(ItemLocators.item_video_button, '点击视频播放按钮')
        try:
            time.sleep(1)
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(ItemLocators.is_item_video_button))
            return True
        except:
            return False
