# # -*- coding:utf-8 -*-
# author='Yang Jia Ming';
# time: 2022/3/28 3:06 下午

from common.dir_config import order_number


def w_file(content):
    '''
    写入文件
    :param content: 写入的内容
    :return:
    '''
    with open(order_number, mode='a') as filename:
        filename.write(content)
        filename.write('\n')  #换行