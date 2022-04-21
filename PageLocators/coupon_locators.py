# # -*- coding:utf-8 -*-
# author='Yang Jia Ming';
# time: 2022/2/10 6:32 下午

from selenium.webdriver.common.by import By

class CouponLocators:
    '''
    优惠券兑换页面
    '''
    # 订单页面优惠券兑换按钮
    order_coupon_exchange_button = (By.XPATH, '//*[text()="使用优惠码或优惠券"]')
    # 订单页面优惠券兑换码输入框
    order_coupon_input = (By.XPATH, '//*[@name="coupon_code_input"]')
    # 订单页面输入兑换码后兑换按钮
    order_coupon_confirm = (By.XPATH, '//*[text()="兑换"]')
    # 订单页面兑换优惠券后点击使用优惠券
    order_eie_coupon = (By.XPATH, '//*[@src = "/imgs/checkout/finger.svg"]')
    # 订单页面兑换优惠券后选择可用的优惠券
    order_choose_coupon = (By.XPATH,'//*[text()="详情" and @color="emphatic"]/parent::button/preceding-sibling::p')
    # 兑换优惠券后关闭优惠券列表按钮
    order_coupon_closure = (By.XPATH, '//*[@src="/imgs/common/crossIcon.svg"]')
    #支付成功成功页面完成按钮
    order_done_button = (By.XPATH, '//*[text()="完成"]')
