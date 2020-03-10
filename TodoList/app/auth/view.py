"""
File:view.py
Author:pink girl
Date:2020-03-10
Connect:1183652970@qq.com
Description:
"""
# 2)应用蓝图，管理路由

from app.auth import auth
# @app.route('/') 因为创建的是auth蓝图，所以就用auth来管理子模块儿view.py文件
@auth.route('/')
def index():
    return 'Index'

@auth.route('/register')
def register():
    return 'register'

@auth.route('/login')
def login():
    return 'login'

@auth.route('/logout')
def logout():
    return 'logout'

