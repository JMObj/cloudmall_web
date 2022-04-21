# # -*- coding:utf-8 -*-
# author='Yang Jia Ming';
# time: 2021/12/29 2:49 下午
import random
def roanom_eamil():
    '随机生成一个qq邮箱'
    num = ''
    for i in range(6):
        n = str(random.randint(1,9))
        num += n
    eamil = num + '@qq.com'
    return eamil

