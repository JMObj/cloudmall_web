# # -*- coding:utf-8 -*-
# author='Yang Jia Ming';
# time: 2022/2/10 6:09 下午

from selenium.webdriver.common.by import By


class AddressLocators:
    # 添加地址页面姓名输入框
    address_name_iuput = (By.XPATH, '//*[@id ="receiver"]')
    # 添加地址页面手机号输入框
    address_mobileNumber_iuput = (By.XPATH, '//*[@id ="mobileNumber"]')
    # 添加地址页面街道输入框
    addres_street_input = (By.XPATH, '//*[@id ="street"]')
    # 添加地址页面城市输入框
    addres_city_input = (By.XPATH, '//*[@id ="city"]')
    # 添加地址页面省选择框
    addres_provinceSelect_choose = (By.XPATH, '//*[@id ="provinceSelect"]')
    # 美国地区选择省
    addres_US_provinceSelect = (By.XPATH, '//*[@title ="Arizona"]')
    # 英国地址省份输入框
    addres_GB_province = (By.XPATH, '//*[@id="province"]')
    # 添加地址页面邮编输入框
    addres_postcode_input = (By.XPATH, '//*[@id ="postcode"]')
    # 添加地址页面邮箱输入框
    addres_email_input = (By.XPATH, '//*[@id ="email"]')
    # 添加地址页面保存地址按钮
    addres_save_button = (By.XPATH, '//*[text()="保存"]')
    # 添加地址页面清空输入框按钮
    addres_clear_button = (By.XPATH, '//*[@src= "/static/media/clearIcon.ca3ffa67.svg"]')
    # 添加地址页面保存后二次确认弹窗
    addres_confirm_popups = (By.XPATH, '//*[text()="确认"]')
    # 添加地址页面es快速支付文案
    es_pay_text = (By.XPATH, '//*[@class="zoid-component-frame zoid-visible"]')
    # 添加地址页es支付按钮
    es_pay_button = (By.XPATH, '//*[@id="paypal-animation-container"]')


