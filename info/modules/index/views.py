# -*- coding: UTF-8 -*-
# time: 2019/9/2 下午10:11
from . import index_blu


# 测试
@index_blu.route('/')
def index():
    return '<h1>index-text</h1>'