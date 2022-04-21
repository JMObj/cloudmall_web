from selenium.webdriver.common.by import By

class HomeLocators:
    """
    首页元素定位
    """
    # 首页左上角菜单按钮
    home_menu =(By.XPATH,'//*[@id="root"]/div/div/div/div[2]/div/div[1]/div/div[1]/div/img')
    # 切换国家按钮
    home_country = (By.XPATH,'//*[@id="root"]/div/div/div/nav/div[3]/div[1]/div[7]/select')
    # 新人优惠券弹窗
    newcomer_coupons = (By.XPATH,'//*[text()="恭喜你"]')
    #首页yml刷新按钮，如果不存在就意味着最后一页
    Refresh_mark = (By.XPATH,'//*[@opacity="0"]/following-sibling::div[2]/div[2]')

    #首页弹窗
    home_popups = '//*[@src="/imgs/common/widgetClose.svg"]'


    #首页搜索按钮
    home_search = (By.XPATH,'//*[@id="root"]/div/div/div/div[2]/div/div[1]/a/img')
    #首页搜索输入框
    input_search = (By.XPATH,'//*[@type= "text"]')
    #首页搜索结果
    secarch_results = (By.XPATH,'//*[@src="/imgs/discount/addCart.svg"]')

