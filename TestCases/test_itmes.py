# # # -*- coding:utf-8 -*-
# # author='Yang Jia Ming';
# # time: 2022/2/9 5:54 下午
import pytest

from PageObject.items_page import ItemPage



class TestItmes:
    @pytest.mark.haffprice
    @pytest.mark.cloudmall
    @pytest.mark.usefixtures("init_driver")
    def test_buy_also_buy(self, init_driver):
        '''
        查看商品buy_also_buy展示是否正常
        :param init_driver: 用例的前置与后置
        :return:
        '''
        assert ItemPage(init_driver).buy_also_buy() is True

    @pytest.mark.haffprice
    @pytest.mark.cloudmall
    @pytest.mark.usefixtures("init_driver")
    def test_comment(self, init_driver):
        '''
        查看商品评论展示是否正常
        :param init_driver: 用例的前置与后置
        :return:
        '''
        assert ItemPage(init_driver).item_comment() is True

    @pytest.mark.haffprice
    @pytest.mark.cloudmall
    @pytest.mark.usefixtures("init_driver")
    def test_size(self, init_driver):
        '''
        查看商品尺码表展示是否正常
        :param init_driver: 用例的前置与后置
        :return:
        '''
        assert ItemPage(init_driver).item_size() is True

    @pytest.mark.haffprice
    @pytest.mark.cloudmall
    @pytest.mark.usefixtures("init_driver")
    def test_video(self, init_driver):
        '''
        查看商品详情页视频播放是否正常
        :param init_driver: 用例的前置与后置
        :return:
        '''
        assert ItemPage(init_driver).itme_video() is False


if __name__ == '__main__':
    pytest.main(["test_itmes.py"])