# -*- coding: UTF-8 -*-
# time: 2019/9/2 下午9:53


# 创建蓝图对象
from flask import Blueprint

index_blu = Blueprint('index', __name__)

from . import  views