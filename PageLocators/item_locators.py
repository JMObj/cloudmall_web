# # -*- coding:utf-8 -*-
# author='Yang Jia Ming';
# time: 2022/1/12 6:36 下午

from selenium.webdriver.common.by import By


class ItemLocators:
    '''
    商品详情页元素定位
    '''
    #搜索buy_also_buy商品后列表展示
    buy_itmes_list = (By.XPATH,'//*[@data-bg="https://imgs.cloudmall.co/store/20210719/60f57bf32854336d8b07fed4.jpg!smallv4"]')
    #dp详情页buy also buy查看按钮
    related_products_button = (By.XPATH,'//*[text()="购买该物品的用户也可能购买"]/following-sibling::div')

    #商品详情查看商品规格
    item_specification= (By.XPATH,'//*[contains(text(),"Color")]')
    #商品规格尺码表按钮
    size_button = (By.XPATH,'//*[text()="尺码表"]')
    #尺码表详情页
    size_Details = (By.XPATH,'//h3[text()="How To Measure"]')


    #搜索评论商品后列表展示
    comment_items_list = (By.XPATH,'//*[@data-bg = "https://imgs.cloudmall.co/store/20210601/60b5ce77205a9f3dde99fcfe.jpg!largev3"]')
    #商品详情页打开评论
    item_comment = (By.XPATH,'//*[contains(text(),"用户评论")]')
    #评论列表页"所有"文案检测
    comment_list = (By.XPATH,'//*[contains(text(),"所有")]')

    #商品详情视频播放按钮
    item_video_button = (By.XPATH,'//*[@src = "/imgs/dp/item-video-play-icon.png"]')
    is_item_video_button = '//*[@src = "/imgs/dp/item-video-play-icon.png"]'
    #商品详情加购按钮
    item_add_cart_button = (By.XPATH, '//*[text()="加入购物车"]')
    #商品详情加购按钮
    item_add_on_button = (By.XPATH, '//*[text()="确定"]')
    #商品详情购物车图标
    item_shopping_cart_button = (By.XPATH, '//*[@src="/imgs/dp/dpCartIcon.svg" ]')

