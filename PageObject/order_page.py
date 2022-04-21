# # -*- coding:utf-8 -*-
# author='Yang Jia Ming';
# time: 2022/2/11 3:56 下午
import time
import re

from PageLocators.item_locators import ItemLocators
from PageLocators.cart_locators import CartLocators
from PageLocators.address_locators import AddressLocators
from PageLocators.coupon_locators import CouponLocators
from PageLocators.order_locators import OrderLocators
from PageLocators.login_locators import LoginLocators
from PageLocators.home_locators import HomeLocators
from selenium.webdriver.support.wait import WebDriverWait  # 等待引入的类
from selenium.webdriver.support import expected_conditions as EC  # 等待的条件
from common.basepage import BasePage
from common.write_file import w_file
from TestDatas import CommonData
from common.handle_log import do_log
from run import data


class OrderPage(BasePage):
    '''
    下单页面对象
    '''
    time_stamp = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time()))

    def suspondWindowHandler(self):
        '''
        处理下单过程中可能会出现的弹窗
        :return:
        '''
        # 下单成功后出现的优惠券弹窗
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderLocators.guest_order_coupon))
            self.ele_click(OrderLocators.guest_order_coupon, '支付成功后点击优惠券弹窗关闭按钮')
        except BaseException:
            pass

        # 注册后出现的新人优惠券
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(HomeLocators.newcomer_coupons))
            self.ele_click(HomeLocators.newcomer_coupons, '首页关闭新人优惠券')
        except BaseException:
            pass

        # 注册后首页普通弹窗的
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(HomeLocators.home_popups))
            # self.wait_ele_visible(HomeLocators.home_popups, '首页检查弹窗出现',is_screenshot=False,time_out=5)
            self.ele_click(HomeLocators.home_popups, '关闭首页弹窗')
        except BaseException:
            pass
        # paypal支付成功后二次确认弹窗
        try:
            WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(OrderLocators.pay_merchant_button))
            # self.wait_ele_visible(OrderLocators.pay_merchant_button, 'paypal支付页面等待确认支付按钮出现')
            self.ele_click(OrderLocators.pay_merchant_button, 'paypal支付页面等待确认支付按钮出现')
        except:
            pass

    def guest_adyen_order(self):
        '''
        adyen未登录用户下单
        :return:
        '''
        self.driver.get(data.get("Common_url") + f'US/zh-Hans/item/{data.get("item_id")}')
        self.ele_click(ItemLocators.item_add_cart_button, '商品详情页点击加购按钮')
        self.ele_click(ItemLocators.item_add_on_button, '选择商品后点击确认按钮')
        self.ele_click(ItemLocators.item_shopping_cart_button, '商品详情点击购物车按钮')
        self.ele_click(CartLocators.cart_settlement, '购物车列表选择测品去结算')
        self.input_text(AddressLocators.address_name_iuput, '订单页面添加地址姓名输入',
                        data.get('US_address_data').get('US_address_name'))
        self.input_text(AddressLocators.address_mobileNumber_iuput, '订单页面添加地址手机号输入',
                        data.get('US_address_data').get('US_address_phone'))
        self.input_text(AddressLocators.addres_street_input, '订单页面添加地址街道输入',
                        data.get('US_address_data').get('US_address_street'))
        self.input_text(AddressLocators.addres_city_input, '订单页面添加地址城市输入',
                        data.get('US_address_data').get('US_address_city'))
        self.ele_click(AddressLocators.addres_provinceSelect_choose, '订单页面添加地址省选择')
        self.ele_click(AddressLocators.addres_US_provinceSelect, '订单页面添加地址选择指定的省')
        self.input_text(AddressLocators.addres_postcode_input, '订单页面添加地址输入邮编',
                        data.get('US_address_data').get('US_address_postcode'))
        self.input_text(AddressLocators.addres_email_input, '订单页面添加地址输入邮箱',
                        data.get('US_address_data').get('US_address_email'))
        self.ele_click(AddressLocators.addres_save_button, '订单页面地址保存按钮')
        self.ele_click(AddressLocators.addres_confirm_popups, '订单页面保存地址二次确认')
        self.wait_ele_visible(CouponLocators.order_coupon_exchange_button, '等待优惠券兑换框出现')
        time.sleep(1)
        self.ele_click(CouponLocators.order_coupon_exchange_button, '订单页面点击优惠券兑换')
        self.input_text(CouponLocators.order_coupon_input, '订单页面优惠券兑换码输入框', data.get('US_coupon_text'))
        self.ele_click(CouponLocators.order_coupon_confirm, '订单页面输入优惠券兑换码后点击兑换按钮')
        self.ele_click(CouponLocators.order_eie_coupon, '订单页面优惠券兑换成功后确定按钮')
        self.ele_click(CouponLocators.order_choose_coupon, '订单页面选择对应的优惠券')
        time.sleep(3)
        self.ele_click(OrderLocators.order_anyen_pay, '提交订单页面选择adyen支付')
        self.slide(0, -1000, '提交订单页面向上滑动')
        amount = self.driver.find_element_by_xpath(OrderLocators.order_US_amount).text
        if float(amount[1:]) > 0.01 and float(amount[1:]) < 1.00:
            self.slide(0, 1000, '提交订单页面向下滑动')
            self.ifarme_window(0)
            self.input_text(OrderLocators.order_card_number_input, '订单页面卡号输入',
                            data.get('US_adyen_info').get('US_adyen_payment'))
            self.driver.switch_to.default_content()
            time.sleep(3)
            self.input_text(OrderLocators.order_card_name_input, '订单页面姓名输入',
                            data.get('US_adyen_info').get('US_adyen_name'))
            self.ifarme_window(1)
            time.sleep(3)
            self.input_text(OrderLocators.order_card_time_input, '订单页面日期输入框',
                            data.get('US_adyen_info').get('US_adyen_card_time'))
            self.driver.switch_to.default_content()
            time.sleep(3)
            self.ifarme_window(2)
            self.input_text(OrderLocators.order_card_code_input, '订单页面安全码输入框',
                            data.get('US_adyen_info').get('US_card_code'))
            self.driver.switch_to.default_content()
            self.ele_click(OrderLocators.continue_order_button, '订单页面提交订单按钮')
            self.suspondWindowHandler()
            order_number_url = self.driver.current_url
            test_pattern = re.compile(r'[0-9]\d{8}')
            prod_pattern = re.compile(r'[0-9]\d{7}')
            order_number = test_pattern.findall(order_number_url) or prod_pattern.findall(order_number_url)
            do_log.info(f'{self.time_stamp} 站点{data.get("client")}美国地区未登录用户adyen支付的订单号:{order_number}')
            order_file = f'{self.time_stamp} 站点{data.get("client")}美国地区未登录用户adyen支付的订单号:{order_number}'
            w_file(order_file)
            return True
        else:
            do_log.error("订单金额小于0.01或者大于1，无法支付订单")
            return False

    def user_adyen_order(self):
        '''
        US国家adyen已登录用户下单
        :return:
        '''
        self.driver.get(data.get("Common_url") + f'US/zh-Hans/item/{data.get("item_id")}')
        self.ele_click(ItemLocators.item_add_cart_button, '商品详情页点击加购按钮')
        self.ele_click(ItemLocators.item_add_on_button, '选择商品后点击确认按钮')
        self.ele_click(ItemLocators.item_shopping_cart_button, '商品详情点击购物车按钮')
        self.ele_click(CartLocators.cart_settlement, '购物车列表选择测品去结算')
        self.wait_ele_visible(AddressLocators.address_name_iuput, '等待姓名输入框出现')
        self.ele_click(AddressLocators.address_name_iuput, '点击添加地址页清空姓名输入框')
        self.ele_click(AddressLocators.addres_clear_button, '清空姓名输入框')
        self.input_text(AddressLocators.address_name_iuput, '订单页面添加地址姓名输入',
                        data.get('US_address_data').get('US_address_name'))
        self.input_text(AddressLocators.address_mobileNumber_iuput, '订单页面添加地址手机号输入',
                        data.get('US_address_data').get('US_address_phone'))
        self.input_text(AddressLocators.addres_street_input, '订单页面添加地址街道输入',
                        data.get('US_address_data').get('US_address_street'))
        self.input_text(AddressLocators.addres_city_input, '订单页面添加地址城市输入',
                        data.get('US_address_data').get('US_address_city'))
        self.ele_click(AddressLocators.addres_provinceSelect_choose, '订单页面添加地址省选择')
        self.ele_click(AddressLocators.addres_US_provinceSelect, '订单页面添加地址选择指定的省')
        self.input_text(AddressLocators.addres_postcode_input, '订单页面添加地址输入邮编',
                        data.get('US_address_data').get('US_address_postcode'))
        self.ele_click(AddressLocators.addres_email_input, '点击邮箱输入框')
        self.ele_click(AddressLocators.addres_clear_button, '清空邮箱输入框')
        self.input_text(AddressLocators.addres_email_input, '订单页面添加地址输入邮箱',
                        data.get('US_address_data').get('US_address_email'))
        self.ele_click(AddressLocators.addres_save_button, '订单页面地址保存按钮')
        self.ele_click(AddressLocators.addres_confirm_popups, '订单页面保存地址二次确认')
        self.wait_ele_visible(CouponLocators.order_coupon_exchange_button, '等待订单页面点击优惠券兑换按钮')
        self.ele_click(CouponLocators.order_coupon_exchange_button, '订单页面点击优惠券兑换')
        self.input_text(CouponLocators.order_coupon_input, '订单页面优惠券兑换码输入框', data.get('US_coupon_text'))
        self.ele_click(CouponLocators.order_coupon_confirm, '订单页面输入优惠券兑换码后点击兑换按钮')
        self.ele_click(CouponLocators.order_eie_coupon, '订单页面优惠券兑换成功后确定按钮')
        self.ele_click(CouponLocators.order_choose_coupon, '订单页面选择对应的优惠券')
        time.sleep(3)
        self.ele_click(OrderLocators.order_anyen_pay, '提交订单页面选择adyen支付')
        self.slide(0, -1000, '提交订单页面向上滑动')
        amount = self.driver.find_element_by_xpath(OrderLocators.order_US_amount).text
        if float(amount[1:]) > 0.01 and float(amount[1:]) < 1.00:
            self.slide(0, 1000, '提交订单页面向下滑动')
            self.ifarme_window(0)
            self.input_text(OrderLocators.order_card_number_input, '订单页面卡号输入',
                            data.get('US_adyen_info').get('US_adyen_payment'))
            self.driver.switch_to.default_content()
            time.sleep(3)
            self.input_text(OrderLocators.order_card_name_input, '订单页面姓名输入',
                            data.get('US_adyen_info').get('US_adyen_name'))
            self.ifarme_window(1)
            time.sleep(3)
            self.input_text(OrderLocators.order_card_time_input, '订单页面日期输入框',
                            data.get('US_adyen_info').get('US_adyen_card_time'))
            self.driver.switch_to.default_content()
            time.sleep(3)
            self.ifarme_window(2)
            self.input_text(OrderLocators.order_card_code_input, '订单页面安全码输入框',
                            data.get('US_adyen_info').get('US_card_code'))
            self.driver.switch_to.default_content()
            self.ele_click(OrderLocators.continue_order_button, '订单页面提交订单按钮')
            # self.wait_ele_visible(CouponLocators.order_done_button, '点击支付成功后的完成按钮')
            self.suspondWindowHandler()
            order_number_url = self.driver.current_url
            test_pattern = re.compile(r'[0-9]\d{8}')
            prod_pattern = re.compile(r'[0-9]\d{7}')
            order_number = test_pattern.findall(order_number_url) or prod_pattern.findall(order_number_url)
            do_log.info(f'{self.time_stamp} 站点{data.get("client")}美国地区已登录用户adyen支付的订单号:{order_number}')
            order_file = f'{self.time_stamp} 站点{data.get("client")}美国地区已登录用户adyen支付的订单号:{order_number}'
            w_file(order_file)
            return True
        else:
            do_log.error("订单金额小于0.01或者大于1，无法支付订单")
            return False

    def guest_paypal_order(self):
        '''
        paypal US未登录用户paypal下单
        :return:
        '''
        self.driver.get(data.get("Common_url") + f'US/zh-Hans/item/{data.get("item_id")}')
        self.ele_click(ItemLocators.item_add_cart_button, '商品详情页点击加购按钮')
        self.ele_click(ItemLocators.item_add_on_button, '选择商品后点击确认按钮')
        self.ele_click(ItemLocators.item_shopping_cart_button, '商品详情点击购物车按钮')
        self.ele_click(CartLocators.cart_settlement, '购物车列表选择测品去结算')
        self.input_text(AddressLocators.address_name_iuput, '订单页面添加地址姓名输入',
                        data.get('US_address_data').get('US_address_name'))
        self.input_text(AddressLocators.address_mobileNumber_iuput, '订单页面添加地址手机号输入',
                        data.get('US_address_data').get('US_address_phone'))
        self.input_text(AddressLocators.addres_street_input, '订单页面添加地址街道输入',
                        data.get('US_address_data').get('US_address_street'))
        self.input_text(AddressLocators.addres_city_input, '订单页面添加地址城市输入',
                        data.get('US_address_data').get('US_address_city'))
        self.ele_click(AddressLocators.addres_provinceSelect_choose, '订单页面添加地址省选择')
        self.ele_click(AddressLocators.addres_US_provinceSelect, '订单页面添加地址选择指定的省')
        self.input_text(AddressLocators.addres_postcode_input, '订单页面添加地址输入邮编',
                        data.get('US_address_data').get('US_address_postcode'))
        self.input_text(AddressLocators.addres_email_input, '订单页面添加地址输入邮箱',
                        data.get('US_address_data').get('US_address_email'))
        self.ele_click(AddressLocators.addres_save_button, '订单页面地址保存按钮')
        self.ele_click(AddressLocators.addres_confirm_popups, '订单页面保存地址二次确认')
        self.wait_ele_visible(CouponLocators.order_coupon_exchange_button, '等待优惠券兑换框出现')
        time.sleep(1)
        self.ele_click(CouponLocators.order_coupon_exchange_button, '订单页面点击优惠券兑换')
        self.input_text(CouponLocators.order_coupon_input, '订单页面优惠券兑换码输入框', data.get('US_coupon_text'))
        self.ele_click(CouponLocators.order_coupon_confirm, '订单页面输入优惠券兑换码后点击兑换按钮')
        self.ele_click(CouponLocators.order_eie_coupon, '订单页面优惠券兑换成功后确定按钮')
        self.ele_click(CouponLocators.order_choose_coupon, '订单页面选择对应的优惠券')
        time.sleep(3)
        self.slide(0, -1000, '提交订单页面向上滑动')
        amount = self.driver.find_element_by_xpath(OrderLocators.order_US_amount).text
        if float(amount[1:]) > 0.01 and float(amount[1:]) < 1.00:
            self.slide(0, 1000, '提交订单页面向下滑动')
            self.ele_click(OrderLocators.order_paypal_pay, '订单页面选择paypal支付方式支付')
            self.ele_click(OrderLocators.continue_order_button, 'paypal确定支付')
            self.wait_ele_visible(OrderLocators.paypal_email, '等待paypal登录页面账号输入框出现')
            self.input_text(OrderLocators.paypal_email, 'paypal登录页面账号输入',
                            data.get('US_paypal_info').get('paypal_email'))
            self.ele_click(OrderLocators.paypal_Next_step_button, 'paypal输入账号后点击下一步按钮')
            self.input_text(OrderLocators.paypal_password, 'paypal登录页面密码输入',
                            data.get('US_paypal_info').get('paypal_password'))
            self.ele_click(OrderLocators.paypal_login_button, 'paypal登录页面登录按钮')
            self.slide(0, 1000, 'paypal支付页面向下滑动')
            self.wait_ele_visible(OrderLocators.pay_now_button, 'paypal支付页面等待支付按钮出现')
            self.ele_click(OrderLocators.pay_now_button, '点击订单页面提交订单按钮')
            self.suspondWindowHandler()
            self.wait_ele_visible(OrderLocators.pay_pass_text, 'paypal支付后等待支付成功文案出现')
            order_number_url = self.driver.current_url
            test_pattern = re.compile(r'[0-9]\d{7}')
            prod_pattern = re.compile(r'[0-9]\d{6}')
            order_number = test_pattern.search(order_number_url) or prod_pattern.search(order_number_url)
            do_log.info(f'{self.time_stamp} 站点{data.get("client")}美国地区未登录用户paypal支付的订单号:{order_number_url}')
            order_file = f'{self.time_stamp} 站点{data.get("client")}美国地区未登录用户paypal支付的订单号:{order_number.group(0)}'
            w_file(order_file)
            return True
        else:
            do_log.error("订单金额小于0.01或者大于1，无法支付订单")
            return False

    def user_paypal_order(self):
        '''
        英国地区paypal已登录用户下单
        :return:
        '''
        self.driver.get(data.get("Common_url") + f'US/zh-Hans/item/{data.get("item_id")}')
        self.ele_click(ItemLocators.item_add_cart_button, '商品详情页点击加购按钮')
        self.ele_click(ItemLocators.item_add_on_button, '选择商品后点击确认按钮')
        self.ele_click(ItemLocators.item_shopping_cart_button, '商品详情点击购物车按钮')
        self.ele_click(CartLocators.cart_settlement, '购物车列表选择测品去结算')
        self.ele_click(AddressLocators.address_name_iuput, '点击姓名输入框')
        self.ele_click(AddressLocators.addres_clear_button, '清空姓名输入框')
        self.input_text(AddressLocators.address_name_iuput, '订单页面添加地址姓名输入',
                        data.get('GB_address_data').get('GB_address_name'))
        self.input_text(AddressLocators.address_mobileNumber_iuput, '订单页面添加地址手机号输入',
                        data.get('GB_address_data').get('GB_address_phone'))
        self.input_text(AddressLocators.addres_street_input, '订单页面添加地址街道输入',
                        data.get('GB_address_data').get('GB_address_street'))
        self.input_text(AddressLocators.addres_city_input, '订单页面添加地址城市输入',
                        data.get('GB_address_data').get('GB_address_city'))
        self.input_text(AddressLocators.addres_GB_province, '订单页面添加地址选择指定的省',
                        data.get('GB_address_data').get('GB_address_province'))  # 英国地区输入省
        self.input_text(AddressLocators.addres_postcode_input, '订单页面添加地址输入邮编',
                        data.get('GB_address_data').get('GB_address_postcode'))
        self.ele_click(AddressLocators.addres_email_input, '点击邮箱输入框')
        self.ele_click(AddressLocators.addres_clear_button, '清空邮箱输入框')
        self.input_text(AddressLocators.addres_email_input, '订单页面添加地址输入邮箱',
                        data.get('GB_address_data').get('GB_address_email'))
        self.ele_click(AddressLocators.addres_save_button, '订单页面地址保存按钮')
        self.ele_click(AddressLocators.addres_confirm_popups, '订单页面保存地址二次确认')
        self.wait_ele_visible(CouponLocators.order_coupon_exchange_button, '等待订单页面点击优惠券兑换按钮')
        time.sleep(3)
        self.ele_click(CouponLocators.order_coupon_exchange_button, '订单页面点击优惠券兑换')
        self.input_text(CouponLocators.order_coupon_input, '订单页面优惠券兑换码输入框',
                        data.get('GB_coupon_text'))
        self.ele_click(CouponLocators.order_coupon_confirm, '订单页面输入优惠券兑换码后点击兑换按钮')
        self.ele_click(CouponLocators.order_eie_coupon, '订单页面优惠券兑换成功后确定按钮')
        self.ele_click(CouponLocators.order_choose_coupon, '订单页面选择对应的优惠券')
        time.sleep(2)
        self.slide(0, -1000, '提交订单页面向上滑动')
        amount = self.driver.find_element_by_xpath(OrderLocators.order_GB_amount).text
        if float(amount[1:]) > 0.01 and float(amount[1:]) < 1.00:
            self.slide(0, 1000, '提交订单页面向下滑动')
            self.ele_click(OrderLocators.order_paypal_pay, '订单页面选择paypal支付方式支付')
            self.ele_click(OrderLocators.continue_order_button, 'paypal确定支付')
            self.wait_ele_visible(OrderLocators.paypal_email, '等待paypal登录页面账号输入框出现')
            self.input_text(OrderLocators.paypal_email, 'paypal登录页面账号输入',
                            data.get('US_paypal_info').get('paypal_email'))
            self.ele_click(OrderLocators.paypal_Next_step_button, 'paypal输入账号后点击下一步按钮')
            self.input_text(OrderLocators.paypal_password, 'paypal登录页面密码输入',
                            data.get('US_paypal_info').get('paypal_password'))
            self.ele_click(OrderLocators.paypal_login_button, 'paypal登录页面登录按钮')
            self.slide(0, 1000, 'paypal支付页面向下滑动')
            self.wait_ele_visible(OrderLocators.pay_now_button, 'paypal支付页面等待支付按钮出现')
            self.ele_click(OrderLocators.pay_now_button, '点击订单页面提交订单按钮')
            self.suspondWindowHandler()
            self.wait_ele_visible(OrderLocators.pay_pass_text, 'paypal支付后等待支付成功文案出现')
            order_number_url = self.driver.current_url
            test_pattern = re.compile(r'[0-9]\d{7}')
            prod_pattern = re.compile(r'[0-9]\d{6}')
            order_number = test_pattern.search(order_number_url) or prod_pattern.search(order_number_url)
            do_log.info(f'{self.time_stamp} 站点{data.get("client")}英国地区已登录用户paypal支付的订单号:{order_number_url}')
            order_file = f'{self.time_stamp} 站点{data.get("client")}英国地区已登录用户paypal支付的订单号:{order_number.group(0)}'
            w_file(order_file)
            return True
        else:
            do_log.error("订单金额小于0.01或者大于1，无法支付订单")
            return False

    def user_es_paypal_order(self):
        '''
        英国地区es已登录用户下单
        :return:
        '''
        self.driver.get(data.get("Common_url") + f'US/zh-Hans/item/{data.get("item_id")}')
        self.ele_click(ItemLocators.item_add_cart_button, '商品详情页点击加购按钮')
        self.ele_click(ItemLocators.item_add_on_button, '选择商品后点击确认按钮')
        self.ele_click(ItemLocators.item_shopping_cart_button, '商品详情点击购物车按钮')
        self.ele_click(CartLocators.cart_settlement, '购物车列表选择测品去结算')
        self.wait_ele_visible(AddressLocators.es_pay_text, '等待es快速支付文案出现', time_out=300)
        self.driver.switch_to.frame(self.driver.find_element_by_class_name('zoid-component-frame'))
        time.sleep(5)
        es_pay_button = self.driver.find_element_by_class_name('paypal-button-label-container')
        self.driver.execute_script("arguments[0].click();", es_pay_button)  # 使用js点击快捷支付按钮
        self.get_window_handles()
        self.switch_to_new_window()
        self.wait_ele_visible(OrderLocators.paypal_email, '等待paypal登录页面账号输入框出现')
        self.input_text(OrderLocators.paypal_email, 'paypal登录页面账号输入',
                        data.get('US_paypal_info').get('paypal_email'))
        self.ele_click(OrderLocators.paypal_Next_step_button, 'paypal输入账号后点击下一步按钮')
        self.input_text(OrderLocators.paypal_password, 'paypal登录页面密码输入',
                        data.get('US_paypal_info').get('paypal_password'))
        self.ele_click(OrderLocators.paypal_login_button, 'paypal登录页面登录按钮')
        self.slide(0, 1000, 'paypal支付页面向下滑动')
        # self.wait_ele_visible(OrderLocators.refuse_paypal_cookie_button,'等待paypal登录账号后拒绝cookies管理按钮',time_out=60)
        # self.ele_click(OrderLocators.refuse_paypal_cookie_button,'点击paypal登录账号后拒绝cookies管理按钮')
        self.wait_ele_visible(OrderLocators.pay_now_button, 'paypal支付页面等待支付按钮出现')
        self.ele_click(OrderLocators.pay_now_button, '点击订单页面提交订单按钮')
        self.suspondWindowHandler()

        self.switch_to_new_window()
        self.wait_ele_visible(AddressLocators.address_name_iuput, '等待姓名输入框出现')
        self.ele_click(AddressLocators.address_name_iuput, '点击姓名输入框')
        self.ele_click(AddressLocators.addres_clear_button, '清空姓名输入框')
        self.input_text(AddressLocators.address_name_iuput, '订单页面添加地址姓名输入',
                        data.get('GB_address_data').get('GB_address_name'))
        time.sleep(2)
        self.input_text(AddressLocators.address_mobileNumber_iuput, '订单页面添加地址手机号输入',
                        data.get('GB_address_data').get('GB_address_phone'))
        # self.input_text(AddressLocators.addres_street_input, '订单页面添加地址街道输入',
        #                 data.get('GB_address_data').get('GB_address_street'))
        # self.input_text(AddressLocators.addres_city_input, '订单页面添加地址城市输入',
        #                 data.get('GB_address_data').get('GB_address_city'))
        # self.input_text(AddressLocators.addres_GB_province, '订单页面添加地址选择指定的省',
        #                 data.get('GB_address_data').get('GB_address_province'))  # 英国地区输入省
        # self.ele_click(AddressLocators.addres_clear_button, '清空邮编输入框')
        # self.input_text(AddressLocators.addres_postcode_input, '订单页面添加地址输入邮编',
        #                 data.get('GB_address_data').get('GB_address_postcode'))
        self.ele_click(AddressLocators.addres_email_input, '点击邮箱输入框')
        time.sleep(1)
        self.ele_click(AddressLocators.addres_clear_button, '清空邮箱输入框')
        self.input_text(AddressLocators.addres_email_input, '订单页面添加地址输入邮箱',
                        data.get('GB_address_data').get('GB_address_email'))
        self.ele_click(AddressLocators.addres_save_button, '订单页面地址保存按钮')
        # self.ele_click(AddressLocators.addres_confirm_popups, '订单页面保存地址二次确认')
        time.sleep(1)
        self.wait_ele_visible(CouponLocators.order_coupon_exchange_button, '等待订单页面点击优惠券兑换按钮')
        self.ele_click(CouponLocators.order_coupon_exchange_button, '订单页面点击优惠券兑换')
        self.input_text(CouponLocators.order_coupon_input, '订单页面优惠券兑换码输入框',
                        data.get('GB_coupon_text'))
        self.ele_click(CouponLocators.order_coupon_confirm, '订单页面输入优惠券兑换码后点击兑换按钮')
        self.ele_click(CouponLocators.order_eie_coupon, '订单页面优惠券兑换成功后确定按钮')
        self.ele_click(CouponLocators.order_choose_coupon, '订单页面选择对应的优惠券')
        self.slide(0, -1000, '提交订单页面向上滑动')
        amount = self.driver.find_element_by_xpath(OrderLocators.order_GB_amount).text
        if float(amount[1:]) > 0.01 and float(amount[1:]) < 1.00:
            self.slide(0, 1000, '提交订单页面向下滑动')
            self.ele_click(OrderLocators.order_paypal_pay, '订单页面选择paypal支付方式支付')
            self.ele_click(OrderLocators.continue_order_button, 'paypal确定支付')
            self.suspondWindowHandler()
            self.wait_ele_visible(OrderLocators.pay_pass_text, 'paypal支付后等待支付成功文案出现')
            order_number_url = self.driver.current_url
            test_pattern = re.compile(r'[0-9]\d{7}')
            prod_pattern = re.compile(r'[0-9]\d{6}')
            # order_number = test_pattern.findall(order_number_url) or prod_pattern.findall(order_number_url)
            order_number = test_pattern.search(order_number_url) or prod_pattern.search(order_number_url)
            do_log.info(f'{self.time_stamp} 站点{data.get("client")}英国地区未登录用户EC支付的订单号:{order_number_url}')
            order_file = f'{self.time_stamp} 站点{data.get("client")}英国地区未登录用户EC支付的订单号:{order_number.group(0)}'
            w_file(order_file)
            return True
        else:
            do_log.error("订单金额小于0.01或者大于1，无法支付订单")
            return False

    def gb_user_adyen_order(self):
        '''
           GB国家adyen已登录用户下单
           :return:
        '''
        self.driver.get(data.get("Common_url") + f'US/zh-Hans/item/{data.get("item_id")}')
        self.ele_click(ItemLocators.item_add_cart_button, '商品详情页点击加购按钮')
        self.ele_click(ItemLocators.item_add_on_button, '选择商品后点击确认按钮')
        self.ele_click(ItemLocators.item_shopping_cart_button, '商品详情点击购物车按钮')
        self.ele_click(CartLocators.cart_settlement, '购物车列表选择测品去结算')
        self.ele_click(AddressLocators.address_name_iuput, '点击姓名输入框')
        self.ele_click(AddressLocators.addres_clear_button, '清空姓名输入框')
        self.input_text(AddressLocators.address_name_iuput, '订单页面添加地址姓名输入',
                        data.get('GB_address_data').get('GB_address_name'))
        self.input_text(AddressLocators.address_mobileNumber_iuput, '订单页面添加地址手机号输入',
                        data.get('GB_address_data').get('GB_address_phone'))
        self.input_text(AddressLocators.addres_street_input, '订单页面添加地址街道输入',
                        data.get('GB_address_data').get('GB_address_street'))
        self.input_text(AddressLocators.addres_city_input, '订单页面添加地址城市输入',
                        data.get('GB_address_data').get('GB_address_city'))
        self.input_text(AddressLocators.addres_GB_province, '订单页面添加地址选择指定的省',
                        data.get('GB_address_data').get('GB_address_province'))  # 英国地区输入省
        self.input_text(AddressLocators.addres_postcode_input, '订单页面添加地址输入邮编',
                        data.get('GB_address_data').get('GB_address_postcode'))
        self.ele_click(AddressLocators.addres_email_input, '点击邮箱输入框')
        self.ele_click(AddressLocators.addres_clear_button, '清空邮箱输入框')
        self.input_text(AddressLocators.addres_email_input, '订单页面添加地址输入邮箱',
                        data.get('GB_address_data').get('GB_address_email'))
        self.ele_click(AddressLocators.addres_save_button, '订单页面地址保存按钮')
        self.ele_click(AddressLocators.addres_confirm_popups, '订单页面保存地址二次确认')
        self.wait_ele_visible(CouponLocators.order_coupon_exchange_button, '等待订单页面点击优惠券兑换按钮')
        time.sleep(3)
        self.ele_click(CouponLocators.order_coupon_exchange_button, '订单页面点击优惠券兑换')
        self.input_text(CouponLocators.order_coupon_input, '订单页面优惠券兑换码输入框',
                        data.get('GB_coupon_text'))
        self.ele_click(CouponLocators.order_coupon_confirm, '订单页面输入优惠券兑换码后点击兑换按钮')
        self.ele_click(CouponLocators.order_eie_coupon, '订单页面优惠券兑换成功后确定按钮')
        self.ele_click(CouponLocators.order_choose_coupon, '订单页面选择对应的优惠券')
        time.sleep(3)
        self.ele_click(OrderLocators.order_anyen_pay, '提交订单页面选择adyen支付')
        self.slide(0, -1000, '提交订单页面向上滑动')
        amount = self.driver.find_element_by_xpath(OrderLocators.order_GB_amount).text
        if float(amount[1:]) > 0.01 and float(amount[1:]) < 1.00:
            self.slide(0, 1000, '提交订单页面向下滑动')
            self.ifarme_window(0)
            self.input_text(OrderLocators.order_card_number_input, '订单页面卡号输入',
                            data.get('US_adyen_info').get('US_adyen_payment'))
            self.driver.switch_to.default_content()
            time.sleep(3)
            self.input_text(OrderLocators.order_card_name_input, '订单页面姓名输入',
                            data.get('US_adyen_info').get('US_adyen_name'))
            self.ifarme_window(1)
            time.sleep(3)
            self.input_text(OrderLocators.order_card_time_input, '订单页面日期输入框',
                            data.get('US_adyen_info').get('US_adyen_card_time'))
            self.driver.switch_to.default_content()
            time.sleep(3)
            self.ifarme_window(2)
            self.input_text(OrderLocators.order_card_code_input, '订单页面安全码输入框',
                            data.get('US_adyen_info').get('US_card_code'))
            self.driver.switch_to.default_content()
            self.ele_click(OrderLocators.continue_order_button, '订单页面提交订单按钮')
            # self.wait_ele_visible(CouponLocators.order_done_button, '点击支付成功后的完成按钮')
            self.suspondWindowHandler()
            order_number_url = self.driver.current_url
            test_pattern = re.compile(r'[0-9]\d{8}')
            prod_pattern = re.compile(r'[0-9]\d{7}')
            order_number = test_pattern.findall(order_number_url) or prod_pattern.findall(order_number_url)
            do_log.info(f'{self.time_stamp} 站点{data.get("client")}英国地区已登录用户adyen支付的订单号:{order_number_url}')
            order_file = f'{self.time_stamp} 站点{data.get("client")}英国地区已登录用户adyen支付的订单号:{order_number}'
            w_file(order_file)
            return True
        else:
            do_log.error("订单金额小于0.01或者大于1，无法支付订单")
            return False

    def US_adyen_guest_order(self):
        '''
        美国未登录用户adyen支付方式下单
        '''
        return self.guest_adyen_order()

    def US_paypal_guest_order(self):
        '''
        美国未登录paypal用户下单
        '''
        return self.guest_paypal_order()

    def US_adyen_user_order(self, user_eamil, user_password, user_name='test'):
        '''
        美国已登录用户adyen支付方式下单
        :return:
        '''
        self.wait_ele_visible(HomeLocators.home_menu, '首页菜单按钮')
        self.ele_click(HomeLocators.home_menu, '点击首页菜单按钮')
        time.sleep(1)
        self.ele_click(LoginLocators.login_or_register_button, '点击首页登录注册按钮')
        time.sleep(3)
        self.ele_click(LoginLocators.email_button, '选择邮箱注册')
        self.input_text(LoginLocators.email_enter, '邮箱注册输入框', user_eamil)
        time.sleep(1)
        self.ele_click(LoginLocators.email_ragister_button, '输入邮箱后的注册按钮')
        self.input_text(LoginLocators.name_enter, '邮箱注册姓名输入框', user_name)
        self.input_text(LoginLocators.password_enter, '邮箱注册密码输入框', user_password)
        self.ele_click(LoginLocators.save_button, '邮箱注册输入完所填的信息后的保存按钮')
        time.sleep(3)
        self.suspondWindowHandler()
        return self.user_adyen_order()

    def GB_paypal_user_order(self, user_eamil, user_password, user_name='test'):
        '''
        英国已登录用户paypal支付方式下单
        :return:
        '''
        self.wait_ele_visible(HomeLocators.home_menu, '首页菜单按钮')
        self.ele_click(HomeLocators.home_menu, '点击首页菜单按钮')
        self.ele_click(LoginLocators.login_or_register_button, '点击首页登录注册按钮')
        time.sleep(1)
        self.ele_click(LoginLocators.email_button, '选择邮箱注册')
        self.input_text(LoginLocators.email_enter, '邮箱注册输入框', user_eamil)
        self.ele_click(LoginLocators.email_ragister_button, '输入邮箱后的注册按钮')
        self.input_text(LoginLocators.name_enter, '邮箱注册姓名邮箱注册密码输入框输入框', user_name)
        self.input_text(LoginLocators.password_enter, '邮箱注册密码输入框', user_password)
        self.ele_click(LoginLocators.save_button, '邮箱注册输入完所填的信息后的保存按钮')
        time.sleep(3)
        self.suspondWindowHandler()
        return self.user_paypal_order()

    def GB_ES_paypal_user_order(self, user_eamil, user_password, user_name='yjm'):
        '''
        英国已登录用户es支付方式下单
        :return:
        '''
        self.wait_ele_visible(HomeLocators.home_menu, '首页菜单按钮')
        self.ele_click(HomeLocators.home_menu, '点击首页菜单按钮')
        self.ele_click(LoginLocators.login_or_register_button, '点击首页登录注册按钮')
        time.sleep(1)
        self.ele_click(LoginLocators.email_button, '选择邮箱注册')
        self.input_text(LoginLocators.email_enter, '邮箱注册输入框', user_eamil)
        self.ele_click(LoginLocators.email_ragister_button, '输入邮箱后的注册按钮')
        self.input_text(LoginLocators.name_enter, '邮箱注册姓名邮箱注册密码输入框输入框', user_name)
        self.input_text(LoginLocators.password_enter, '邮箱注册密码输入框', user_password)
        self.ele_click(LoginLocators.save_button, '邮箱注册输入完所填的信息后的保存按钮')
        time.sleep(3)
        self.suspondWindowHandler()
        return self.user_es_paypal_order()

    def GB_adyen_user_order(self, user_eamil, user_password, user_name='yjm'):
        '''
        英国已登录用户adyen支付方式下单
        :return:
        '''
        self.wait_ele_visible(HomeLocators.home_menu, '首页菜单按钮')
        self.ele_click(HomeLocators.home_menu, '点击首页菜单按钮')
        self.ele_click(LoginLocators.login_or_register_button, '点击首页登录注册按钮')
        time.sleep(1)
        self.ele_click(LoginLocators.email_button, '选择邮箱注册')
        self.input_text(LoginLocators.email_enter, '邮箱注册输入框', user_eamil)
        self.ele_click(LoginLocators.email_ragister_button, '输入邮箱后的注册按钮')
        self.input_text(LoginLocators.name_enter, '邮箱注册姓名邮箱注册密码输入框输入框', user_name)
        self.input_text(LoginLocators.password_enter, '邮箱注册密码输入框', user_password)
        self.ele_click(LoginLocators.save_button, '邮箱注册输入完所填的信息后的保存按钮')
        time.sleep(3)
        self.suspondWindowHandler()
        return self.gb_user_adyen_order()
