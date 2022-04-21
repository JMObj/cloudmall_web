import time
from selenium import webdriver
from selenium.webdriver.common.touch_actions import TouchActions
from common.write_file import w_file
import re

text = 'https://www.cloudmall.ai/GB/zh-Hans/guestcheckout/success/20954389?method=paypal&PayerID=6R3CK6TPPYM62&st=Authorized&tx=8D558712NS8723606&cc=GBP&amt=0.29&cm=%7B%22order_id%22%3A%2220954389%22%2C%22payment_id%22%3A%22625124dda9456a0001309106%22%7D&payer_email=sisi.zeng%40imaygou.com&payer_id=6R3CK6TPPYM62&payer_status=VERIFIED&first_name=%E6%80%9D%E6%80%9D&last_name=%E6%9B%BE&address_name=hello%20world&address_street=1221%20Pershore%20Road&address_city=Birmingham&address_state=Berkshire&address_country_code=GB&address_zip=B30%202YT&residence_country=GB&txn_id=8D558712NS8723606&mc_currency=GBP&mc_gross=0.29&protection_eligibility=ELIGIBLE&payment_gross=0.29&payment_status=Authorized&pending_reason=authorization&payment_type=instant&handling_amount=0.00&shipping=0.00&item_name=CloudMall%2020954389&quantity=1&txn_type=web_accept&payment_date=2022-04-09T06%3A17%3A02Z&receiver_id=YR2X68TXA9MPU&notify_version=UNVERSIONED&custom=%7B%22order_id%22%3A%2220954389%22%2C%22payment_id%22%3A%22625124dda9456a0001309106%22%7D&verify_sign=AHWEskvAUTXOflW.y-IrG7c95Lt5ApD2dPtBj8P.7J4raTe-.-3A3Mr'
test_pattern = re.compile(r'[0-9]\d{7}')
prod_pattern = re.compile(r'[0-9]\d{6}')
order_number = test_pattern.search(text) or prod_pattern.search(text)
print(order_number.group(0))
# time_stamp = time.strftime('%Y-%m-%d', time.localtime(time.time()))
# print(time_stamp)
# w_file(time_stamp)


