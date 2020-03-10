"""
File:__init__.py.py
Author:pink girl
Date:2020-03-10
Connect:1183652970@qq.com
Description:
"""

# 1）创建蓝图
from flask import Blueprint
todo = Blueprint('todo',__name__)
from . import view