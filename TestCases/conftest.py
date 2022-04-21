import time

from selenium import webdriver
import pytest
from TestDatas import CommonData
from PageLocators.home_locators import HomeLocators
from common.basepage import BasePage
from common.handle_log import do_log
from selenium.webdriver.common.touch_actions import TouchActions
from run import data


# @pytest.fixture(scope = "class")
# def init_class():
#     do_log.info("=================这个是类的前置==================")
#     yield
#     do_log.info("=================这个是类的后置==================")



def suspondWindowHandler(brower):
    #处理普通弹窗
    suspondWindow = brower.find_element_by_xpath(HomeLocators.home_popups)
    suspondWindow.click()
    do_log.info('关闭普通弹窗')


@pytest.fixture
def init_driver():
    '''
    常规用例前置/后置
    :return:
    '''
    try:
        mobile_emulation = {"deviceName": "iPhone X"}
        options = webdriver.ChromeOptions()
        options.add_argument("--auto-open-devtools-for-tabs")
        options.add_experimental_option('mobileEmulation', mobile_emulation)
        options.add_experimental_option('w3c', False)
        options.add_argument("--kiosk")
        driver = webdriver.Chrome(options=options)
        driver.get(data.get('Common_url'))
        # driver.get(CommonData.Common_url.site_url)
        drivers = BasePage(driver)
        time.sleep(3)
        try:
            suspondWindowHandler(driver)
        except Exception as e:
            drivers.ele_click(HomeLocators.home_menu, '首页左上角菜单按钮')
            Action = TouchActions(driver)
            Action.scroll(0, 1000).perform()
            time.sleep(1)
            drivers.ele_click(HomeLocators.home_country,'国家列表')
            drivers.select_cike(HomeLocators.home_country, '国家列表', 'United States')
            time.sleep(3)
        else:
            drivers.ele_click(HomeLocators.home_menu, '首页左上角菜单按钮')
            Action = TouchActions(driver)
            Action.scroll(0, 1000).perform()
            time.sleep(1)
            drivers.ele_click(HomeLocators.home_country, '国家列表')
            drivers.select_cike(HomeLocators.home_country, '国家列表', 'United States')
            time.sleep(3)
        try:
            suspondWindowHandler(driver)
        except Exception as e:
            # do_log.info('未找到首页弹窗')
            yield driver
        else:
            yield driver
    finally:
        driver.quit()

@pytest.fixture
def GB_init_driver():
    '''
    GB下单用例前置/后置
    :return:
    '''
    try:
        mobile_emulation = {"deviceName": "iPhone X"}
        options = webdriver.ChromeOptions()
        options.add_argument("--auto-open-devtools-for-tabs")
        options.add_experimental_option('mobileEmulation', mobile_emulation)
        options.add_experimental_option('w3c', False)
        options.add_argument("--kiosk")
        driver = webdriver.Chrome(options=options)
        driver.get(data.get('Common_url'))
        # driver.get(CommonData.Common_url.site_url)
        drivers = BasePage(driver)
        time.sleep(3)
        try:
            suspondWindowHandler(driver)
        except Exception as e:
            drivers.ele_click(HomeLocators.home_menu, '首页左上角菜单按钮')
            Action = TouchActions(driver)
            Action.scroll(0, 1000).perform()
            time.sleep(1)
            drivers.ele_click(HomeLocators.home_country,'国家列表')
            drivers.select_cike(HomeLocators.home_country, '国家列表', 'United Kingdom')
            time.sleep(3)
        else:
            drivers.ele_click(HomeLocators.home_menu, '首页左上角菜单按钮')
            Action = TouchActions(driver)
            Action.scroll(0, 1000).perform()
            time.sleep(1)
            drivers.ele_click(HomeLocators.home_country, '国家列表')
            drivers.select_cike(HomeLocators.home_country, '国家列表', 'United Kingdom')
            time.sleep(3)
        try:
            suspondWindowHandler(driver)
        except Exception as e:
            yield driver
        else:
            yield driver
    finally:
        driver.quit()