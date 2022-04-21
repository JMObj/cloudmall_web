import sys

from selenium.webdriver.support.wait import WebDriverWait  # 等待引入的类
from selenium.webdriver.support import expected_conditions as EC  # 等待的条件
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.touch_actions import TouchActions
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import TimeoutException
import time
import datetime

from common.handle_log import do_log
# from common.win_up_file import upload
from common.dir_config import screenshot_dir


class BasePage:
    '''
    对Selenium中的元素操作方法进行第二次封装加上日志，失败截图
    '''

    def __init__(self, driver: WebDriver):
        self.driver = driver

    def wait_ele_visible(self, loc, img_doc,  time_out=20, poll_frequency=0.5):
        '''
        等待元素可见，默认等待时间为20秒，默认每隔0.5秒刷新一次
        :param loc: 查找的元素
        :param img_doc: 页面的名称
        :param time_out: 等待的时长
        :param poll_frequency: 刷新的时长
        :return:
        '''
        do_log.info("{}等待{}元素".format(img_doc, loc))
        new_time = datetime.datetime.now()  # 开始等待时间
        start_time = new_time.strftime("%Y--%m--%d %H:%M:%S")
        do_log.info("{}等待开始时间{}:".format(img_doc, start_time))
        try:
            WebDriverWait(self.driver, time_out, poll_frequency).until(EC.visibility_of_element_located(loc))
        except:
            do_log.exception("{}等待{}元素失败".format(img_doc, loc))
            self._save_page_shot(img_doc)
        else:
            old_time = datetime.datetime.now()  # 等待结束时间
            end_time = old_time.strftime("%Y--%m--%d %H:%M:%S")
            do_log.info("{}等待结束时间{}:".format(img_doc, end_time))



    def wait_ele_visible_tow(self, loc, img_doc, time_out=20, poll_frequency=0.5):
        '''
        等待元素是否在dom树中可见，默认等待时间为20秒，默认每隔0.5秒刷新一次
        :param loc: 查找的元素
        :param img_doc: 页面的名称
        :param time_out: 等待的时长
        :param poll_frequency: 刷新的时长
        :return:
        '''
        do_log.info("{}等待{}元素可见".format(img_doc, loc))
        new_time = datetime.datetime.now()  # 开始等待时间
        start_time = new_time.strftime("%Y--%m--%d %H:%M:%S")
        do_log.info("{}等待起止时间{}:".format(img_doc, start_time))
        # try:
        WebDriverWait(self.driver, time_out, poll_frequency).until(EC.presence_of_element_located(loc))
        # except:
        #     do_log.exception("{}等待{}元素失败".format(img_doc, loc))
        #     raise
        # else:
        #     old_time = datetime.datetime.now()  # 等待结束时间
        #     end_time = old_time.strftime("%Y--%m--%d %H:%M:%S")
        #     do_log.info("{}等待结束时间{}:".format(img_doc, end_time))

    def ele_click(self, loc, img_doc, time_out=20, poll_frequency=0.5):
        '''
        点击元素
        :param loc: 查找的元素
        :param img_doc: 页面的名称
        :param time_out: 等待的时长
        :param poll_frequency: 刷新的时长
        :return:
        '''
        do_log.info("{}点击{}元素".format(img_doc, loc))
        try:
            self.wait_ele_visible(loc, img_doc, time_out, poll_frequency)
            self.driver.find_element(*loc).click()
        except:
            do_log.exception("{}点击{}元素失败".format(img_doc, loc))
            self._save_page_shot(img_doc)
            raise

    def input_text(self, loc, img_doc, text, time_out=20, poll_frequency=0.5):
        '''
                对文本框输入并点击
                :param loc: 查找的元素
                :param img_doc: 页面的名称
                :param test: 输入的内容
                :param time_out: 等待的时长
                :param poll_frequency: 刷新的时长
                :return:
                '''
        do_log.info("{}对{}输入{}".format(img_doc, loc, text))
        try:
            self.wait_ele_visible(loc, img_doc, time_out, poll_frequency)
            self.driver.find_element(*loc).send_keys(text)
        except:
            do_log.exception("{}对{}元素输入{}失败".format(img_doc, loc, text))
            self._save_page_shot(img_doc)
            raise

    def select_cike(self, loc, img_doc, select_text, time_out=20, poll_frequency=0.5):
        '''
        对sleect列表点击
        :param loc: 列表元素名称
        :param img_doc: 页面名称
        :param time_out: 等待时长
        :param poll_frequency: 刷新时间
        select_text :选择的文本
        :return:
        '''
        do_log.info("{}对{}选择了{}".format(img_doc, loc, select_text))
        try:
            self.wait_ele_visible(loc, img_doc, time_out, poll_frequency)
            select_ele = self.driver.find_element(*loc)
            s = Select(select_ele)
            s.select_by_visible_text(select_text)
        except:
            do_log.exception("{}选择{}失败".format(img_doc, select_text))
            self._save_page_shot(img_doc)
            raise

    def mouse(self, loc, img_doc, cli=True, time_out=20, poll_frequency=0.5):
        '''
                对元素鼠标悬浮并点击
                :param loc: 查找的元素
                :param img_doc: 页面的名称
                :param time_out: 等待的时长
                :param poll_frequency: 刷新的时长
                :param cli: 如果为True执行悬浮并点击，如果为False执行悬浮
                :return:
                '''

        if cli == True:
            do_log.info("{}对{}悬浮鼠标并点击".format(img_doc, loc))
            try:
                self.wait_ele_visible_tow(loc, img_doc, time_out, poll_frequency)
                webdriver.ActionChains(self.driver).move_to_element(self.driver.find_element(*loc)).click(
                    self.driver.find_element(
                        *loc)).perform()
            except:
                do_log.exception("{}对{}元素鼠标悬浮并点击失败".format(img_doc, loc))
                self._save_page_shot(img_doc)
                raise
        elif cli == False:
            do_log.info("{}对{}悬浮鼠标".format(img_doc, loc))
            try:
                self.wait_ele_visible_tow(loc, img_doc, time_out, poll_frequency)
                webdriver.ActionChains(self.driver).move_to_element(self.driver.find_element(*loc)).perform()
            except:
                do_log.exception("{}对{}元素鼠标悬浮并点击失败".format(img_doc, loc))
                self._save_page_shot(img_doc)
                raise

    # def up_file(self, path, img_doc):
    #     '''
    #             对文本框点击并输入
    #             :param loc: 查找的元素
    #             :param img_doc: 页面的名称
    #             :param time_out: 等待的时长
    #             :param poll_frequency: 刷新的时长
    #             :return:
    #             '''
    #     do_log.info("在{}上传文件".format(img_doc))
    #     try:
    #         upload(path)
    #     except:
    #         do_log.exception("{}上传文件失败".format(img_doc))
    #         self._save_page_shot(img_doc)
    #         raise

    def get_text(self, loc, img_doc, time_out=20, poll_frequency=0.5):
        '''
                获取元素文本
                :param loc: 查找的元素
                :param img_doc: 页面的名称
                :param time_out: 等待的时长
                :param poll_frequency: 刷新的时长
                :return:
                '''
        do_log.info("{}对{}获取文本属性".format(img_doc, loc))

        try:
            self.wait_ele_visible(loc, img_doc, time_out, poll_frequency)
            value = self.driver.find_element(*loc).text
        except:
            do_log.exception("{}对{}元素鼠标悬浮并点击失败".format(img_doc, loc))
            self._save_page_shot(img_doc)
            raise
        else:
            return value

    def get_window_handles(self):
        '''
        :return:获取当前页面所有窗口的对象
        '''
        do_log.info("获取当前所有的窗口")
        try:
            wins = self.driver.window_handles
        except:
            pass
        else:
            do_log.info("当前所有窗口是{}".format(wins))
            return wins

    def switch_to_new_window(self):
        '''
        :return: 切换到最新的窗口
        '''
        time.sleep(2)
        wins = self.get_window_handles()
        do_log.info("切换到了最新的窗口{}".format(wins[-1]))
        try:
            self.driver.switch_to.window(wins[-1])
        except:
            pass

    def slide(self, x, y, img_doc):
        '''
        H5页面滑动
        列子
        s = "window.scrollBy(0,500)"  # 向下滑动500个像素
        js = "window.scrollBy(0,-500)"　# 向上滚动500个像素
        js = "window.scrollBy(500,0)"  # 向右滑动500个像素
        js = "window.scrollBy(-500,0)"　# 向左滚动500个像素
        img_doc：页面名称
        :return:
        '''
        do_log.info("{}页面滑动".format(img_doc))
        try:
            Action = TouchActions(self.driver)
            Action.scroll(x, y).perform()
        except:
            do_log.error("{}页面滑动失败".format(img_doc))
            raise

    def key_board(self, loc, img_doc, key_board_type, time_out=20, poll_frequency=0.5):
        '''

        :param loc:元素定位
        :param img_doc: 输入的回车页面
        :param key_board_type:
        1 为回车键输入
        :param time_out:最长等待时间
        :param poll_frequency: 刷新时间时长
        :return:
        '''
        if key_board_type == 1:
            do_log.info("{}键盘输入回车".format(img_doc))
            try:
                self.wait_ele_visible_tow(loc, img_doc, time_out, poll_frequency)
                self.driver.find_element(*loc).send_keys(Keys.ENTER)
            except:
                raise

    def ifarme_window(self, loc):
        '''
        定位到ifame窗口
        :param loc:
        :return:
        '''
        try:
            self.driver.switch_to.frame(loc)
        except:
            raise

    def clear_input(self, loc, img_doc, time_out=20, poll_frequency=0.5):
        '''
        清空输入框
        :param loc:
        :param img_loc:
        :param time_out:
        :param poll_frequency:
        :return:
        '''
        try:
            self.wait_ele_visible(loc, img_doc, time_out, poll_frequency)
            self.driver.find_element(*loc).clear()
        except:

            do_log.exception(f'清空{loc}输入框失败\n')
            do_log.exception('清空{}输入框失败'.format(loc))
            raise

    def _save_page_shot(self, img_doc):
        '''
        用例失败后保存截图到文件中
        :param img_doc:页面名称与元素定位名称
        :return:
        '''
        timestamp = time.time()
        file_name = "{}_{}.png".format(img_doc, timestamp)
        try:
            self.driver.save_screenshot(screenshot_dir + '/' + file_name)

        except:
            do_log.exception("{}截图保存失败".format(img_doc))
        else:
            do_log.info("截图成功保存在{}目录".format(screenshot_dir + '/' + file_name))


if __name__ == '__main__':
    option = webdriver.ChromeOptions()  # 调用了newsession这个接口
    driver = webdriver.Chrome(options=option)
    driver.get(
        'https://www.google.com.hk/search?q=selenium+%E5%90%91%E4%B8%8B%E6%BB%91%E5%8A%A8&newwindow=1&ei=yB7MYbevOZj8wQP14IDQBA&start=10&sa=N&ved=2ahUKEwi3s_aFzoj1AhUYfnAKHXUwAEoQ8NMDegQIARBG&biw=1920&bih=1001&dpr=1')
    ls = BasePage(driver)
    time.sleep(10)
    print('开始滑动')
    driver.execute_script("window.scrollBy(0,1000)")
    # ls.slide(0,700,'百度首页')
    # xp = (By.XPATH, '//span[@id = "s-usersetting-top"]')
    # ls.mouse(xp, "百度首页设置", cli=False)
    time.sleep(10)
    driver.quit()
