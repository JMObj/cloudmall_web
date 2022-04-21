# # -*- coding:utf-8 -*-
# author='Yang Jia Ming';
# time: 2022/2/10 5:53 下午

from selenium.webdriver.common.by import By


class OrderLocators:
    '''
    订单页面元素定位
    '''
    # 提交订单页面选择adyen支付
    order_anyen_pay = (By.XPATH, '//*[text()="Credit/Debit Card"]')
    # 美国地区提交订单页面需要支付金额
    order_US_amount = ('//*[contains(text(),"$") and @color="primary"]')
    #英国地区提交订单页面需要支付金额
    order_GB_amount = ('//*[contains(text(),"£") and @color="primary"]')
    order_card_ifame = ('//*[@title="Iframe for secured card number" and @class="js-iframe"]')
    # 提交订单页面adyen卡号输入框
    order_card_number_input = (By.XPATH, '//*[@id="encryptedCardNumber"]')
    # 提交订单页面adyen卡姓名输入框
    order_card_name_input = (By.XPATH, '//*[text()="卡名"]/preceding-sibling::input')
    # 提交订单页面adyen卡日期输入框
    order_card_time_input = (By.XPATH, '//*[@id="encryptedExpiryDate"]')
    # 提交订单页面adyen卡安全码输入框
    order_card_code_input = (By.XPATH, '//*[@id="encryptedSecurityCode"]')
    # 提交订单页面提交订单按钮
    continue_order_button = (By.XPATH, '//*[text()="继续"]')


    #提交订单页面选择paypal支付
    order_paypal_pay = (By.XPATH,'//*[text()="PayPal"]')
    #paypal登录页面邮箱输入框
    paypal_email = (By.XPATH,'//*[@id="email"]')
    #paypal登录页面下一步按钮
    paypal_Next_step_button = (By.XPATH,'//*[@id="btnNext"]')
    #paypal登录页面密码输入框
    paypal_password = (By.XPATH,'//*[@id="password"]')
    #paypal登录页面登录按钮
    paypal_login_button = (By.XPATH, '//*[@id="btnLogin"]')
    #paypal支付页面支付按钮
    pay_now_button = (By.XPATH,'//*[@id="payment-submit-btn"]')
    #paypal确认支付页面支付按钮
    pay_merchant_button = (By.XPATH,'//*[text()="Return to Merchant"]')
    #paypal登录账号后拒绝cookies管理按钮
    refuse_paypal_cookie_button = (By.XPATH,'//*[@id="bannerCloseButton"]')

    #用户支付成功后优惠券弹窗关闭按钮
    guest_order_coupon = (By.XPATH,'//*[text()="放弃优惠"]')

    #支付成功后订单号
    order_number = (By.XPATH,'//*[text()="支付成功"]/following-sibling::p')
    #已登录用户支付成功后支付成功文案
    pay_pass_text = (By.XPATH,'//*[text()="支付成功"]')