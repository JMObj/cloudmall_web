# # # -*- coding:utf-8 -*-
# # author='Yang Jia Ming';
# # time: 2022/1/7 12:08 下午
import pytest
from PageObject.home_page import Yml
# from TestDatas.CommonData import Common_url

class TestHome:
    @pytest.mark.haffprice
    @pytest.mark.cloudmall
    @pytest.mark.usefixtures('init_driver')
    def test_home_yml(self, init_driver):
        '''
        检测首页yml刷新
        :param init_driver: 用例的前置与后置
        :return:
        '''
        assert Yml(init_driver).home_yjm() is True

    @pytest.mark.haffprice
    @pytest.mark.cloudmall
    @pytest.mark.usefixtures('init_driver')
    def test_home_search(self, init_driver):
        '''
        首页关键字搜索，搜索的关键字默认为Shoes
        :param init_driver: 用例的前置与后置
        :return:
        '''
        assert Yml(init_driver).home_search() is True


if __name__ == '__main__':
    pytest.main(["test_home.py"])


