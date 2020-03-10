"""
File:view.py
Author:pink girl
Date:2020-03-10
Connect:1183652970@qq.com
Description:
"""
# 2)应用蓝图
from app.todo import todo

#/todo/add/
@todo.route('/add/')
def add():
    return 'todo add'

#/todo/delete/
@todo.route('/delete/')
def deleate():
    return 'todo delete'


