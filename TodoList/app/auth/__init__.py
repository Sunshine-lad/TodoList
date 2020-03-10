"""
File:__init__.py.py
Author:pink girl
Date:2020-03-10
Connect:1183652970@qq.com
Description:
"""
from flask import  Blueprint
# 1). 创建蓝图
auth = Blueprint('auth', __name__)

#注意;导入包的实质是执行里面的__init__.py文件
from . import view

