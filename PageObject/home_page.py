import datetime

from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.wait import WebDriverWait  # 等待引入的类
from selenium.webdriver.support import expected_conditions as EC  # 等待的条件
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.touch_actions import TouchActions

import time

from PageLocators.home_locators import HomeLocators
from common.basepage import BasePage
from common.handle_log import do_log
from run import data


class HomePage:
    def __init__(self, driver: WebDriver):
        self.driver = driver

    def if_homepage_exist(self):
        '''
        注册成功后断言新人优惠券弹窗是否存在
        :return:存在返回True 不存在返回False
        '''
        try:
            WebDriverWait(self.driver, 20).until(EC.visibility_of_element_located(HomeLocators.newcomer_coupons))
        except:
            return False
        else:
            return True


class Yml(BasePage):

    def home_yjm(self):
        '''
        检测首页yml滑动
        :return:
        '''
        # try:
        time.sleep(2)
        for x in range(3):
            num = 0
            while True:
                Action = TouchActions(self.driver)
                Action.scroll(1, 1500).perform()
                # self.slide(1, 500, '首页yml滑动')
                try:
                    # new_time = datetime.datetime.now()  # 开始等待时间
                    # start_time = new_time.strftime("%Y--%m--%d %H:%M:%S")
                    # do_log.info(f'开始等待时间{start_time}')
                    # WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(HomeLocators.Refresh_mark))
                    self.wait_ele_visible_tow(HomeLocators.Refresh_mark, '首页yml刷新图标',time_out=4)
                    # old_time = datetime.datetime.now()  # 等待结束时间
                    # end_time = old_time.strftime("%Y--%m--%d %H:%M:%S")
                    # do_log.info(f'结束等待时间{end_time}')
                    # WebDriverWait(self.driver, 3).until(EC.visibility_of_element_located(HomeLocators.Refresh_mark))
                    break
                except TimeoutException:
                    num += 1
                    if num == 5:
                        return False
            if x == 2:
                return True

    def home_search(self):
        '''
        首页搜索商品，商品数大于1则通过
        :return:
        '''
        self.wait_ele_visible(HomeLocators.home_search, '首页搜索按钮')
        self.ele_click(HomeLocators.home_search, '点击首页搜索按钮')
        self.input_text(HomeLocators.input_search, '首页搜索输入框', 'Shoes')  # 输入女鞋后点击搜索
        self.key_board(HomeLocators.input_search, '首页搜索输入框', 1)
        try:
            self.wait_ele_visible(HomeLocators.secarch_results, '首页搜索结果购物车图标')
            # li = self.driver.find_element_by_xpath(HomeLocators.secarch_result).get_attribute('innerHTML') #获取有多少个搜索结果
            # do_log.info("搜索列表返回的结果是{}".format(li))
            # flsg = len(li)
            # if flsg < 1:
            #     do_log.error('结果返回不大于0，返回结果为{}'.format(flsg))
            return True
        except:
            return False
