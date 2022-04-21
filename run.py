import pytest
import time

time_stamp = time.strftime('%Y-%m-%d-%H-%M-%S', time.localtime(time.time()))

# cloudmall 生产环境数据
cloud_mall_prod_data = {
    'Common_url': 'https://www.cloudmall.ai/',
    'client': 'cloudmall',
    'US_address_data': {
        # 美国地址收货地址
        'US_address_name': 'test',
        'US_address_phone': '123456',
        'US_address_street': 'Orr',
        'US_address_city': 'Dall',
        'US_address_postcode': '11111',
        'US_address_email': 'jiaming.yang@cloudmall.ai'
    },
    'GB_address_data': {
        # 英国地址收货地址
        'GB_address_name': 'test',
        'GB_address_phone': '123456',
        'GB_address_street': 'Orr',
        'GB_address_city': 'Dall',
        'GB_address_province': 'sdadsad',
        'GB_address_postcode': 'A00 0AA',
        'GB_address_email': 'jiaming.yang@cloudmall.ai'
    },
    'item_id': '9981835',
    'home_search_text': 'Shoes',
    'buy_also_buy_item': 44626278,
    'size_item': 44626278,
    'comment_item': 39592674,
    'video_item': 9386626,
    'US_coupon_text': 'testyjm11',
    'GB_coupon_text': 'testyjm15',
    'US_adyen_info': {
        'US_adyen_payment': '4336 6800 0926 7119',
        'US_adyen_name': 'test',
        'US_adyen_card_time': '10/22',
        'US_card_code': '766'
    },
    'US_paypal_info': {
        'paypal_email': 'sisi.zeng@imaygou.com',
        'paypal_password': 'Cloudmall0311'
    }
}

# haffprice 生产环境数据
haff_price_prod_data = {
    'Common_url': 'https://www.haffprice.com/',
    'client': 'haffprice',
    'US_address_data': {
        # 美国地址收货地址
        'US_address_name': 'test',
        'US_address_phone': '123456',
        'US_address_street': 'Orr',
        'US_address_city': 'Dall',
        'US_address_postcode': '11111',
        'US_address_email': 'jiaming.yang@cloudmall.ai'
    },
    'GB_address_data': {
        # 英国地址收货地址
        'GB_address_name': 'test',
        'GB_address_phone': '123456',
        'GB_address_street': 'Orsadr',
        'GB_address_city': 'Dadsadll',
        'GB_address_province': 'sdadsad',
        'GB_address_postcode': 'A00 0AA',
        'GB_address_email': 'jiaming.yang@cloudmall.ai'
    },
    'item_id': '9981835',
    'home_search_text': 'Shoes',
    'buy_also_buy_item': 44626278,
    'size_item': 44626278,
    'comment_item': 39592674,
    'video_item': 9386626,
    'US_coupon_text': 'testyjm11',
    'GB_coupon_text': 'testyjm15',
    'US_adyen_info': {
        'US_adyen_payment': '4336 6800 0926 7119',
        'US_adyen_name': 'test',
        'US_adyen_card_time': '10/22',
        'US_card_code': '766'
    },
    'US_paypal_info': {
        'paypal_email': 'sisi.zeng@imaygou.com',
        'paypal_password': 'Cloudmall0311'
    }
}

# haffprice 测试环境环境数据
haff_price_test_data = {
    'Common_url': 'https://nightly7.momoso.com/',
    'US_address_data': {
        # 美国地址收货地址
        'US_address_name': 'test',
        'US_address_phone': '123456',
        'US_address_street': 'Orr',
        'US_address_city': 'Dall',
        'US_address_postcode': '11111',
        'US_address_email': 'jiaming.yang@cloudmall.ai'
    },
    'GB_address_data': {
        # 英国地址收货地址
        'GB_address_name': 'test',
        'GB_address_phone': '123456',
        'GB_address_street': 'Orr',
        'GB_address_city': 'Dall',
        'GB_address_province': 'sdadsad',
        'GB_address_postcode': 'A00 0AA',
        'GB_address_email': 'jiaming.yang@cloudmall.ai'
    },
    'item_id': '9981835',
    'home_search_text': 'Shoes',
    'buy_also_buy_item': 44626278,
    'size_item': '44626278',
    'comment_item': '39592674',
    'video_item': '9386626',
    'US_coupon_text': 'testyjm141',
    'GB_coupon_text': 'testyjm141',
    'US_adyen_info': {
        'US_adyen_payment': '4111 1111 1111 1111',
        'US_adyen_name': 'test',
        'US_adyen_card_time': '03/30',
        'US_card_code': '737'
    },
    'US_paypal_info': {
        'paypal_email': 'paypal-buyer@momoso.com',
        'paypal_password': 'Fynv4k38'
    }
}


# 生产环境cloudmall
# data = cloud_mall_prod_data
# if __name__ == '__main__':
#     pytest.main(["-m","cloudmall","--reruns", "1", "--reruns-delay", "5",
#                       r"--html=Outputs/reports/resuit{}.html".format(time_stamp)])
# print('执行了cloudmall的用例')

# 生产环境haffprice
data = haff_price_prod_data
if __name__ == '__main__':
    pytest.main(["-m", "haffprice", "--reruns", "1", "--reruns-delay", "5",
             r"--html=Outputs/reports/resuit{}.html".format(time_stamp)])
print('haffprice的用例')
