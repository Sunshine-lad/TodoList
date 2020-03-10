"""
File:__init__.py.py
Author:pink girl
Date:2020-03-10
Connect:1183652970@qq.com
Description:
"""
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from config import config

bootstrap = Bootstrap()
db = SQLAlchemy()
mail = Mail()

# 把创建app这块封装成一个函数
def create_app(config_name='development'):
    """
    默认创建开发环境的app对象
    :param config_name:
    :return:
    """
    app = Flask(__name__)

    """
    config = {
   'development': DevelopmentConfig,
   'testing': TestingConfig,
   'production': ProductionConfig,
   'default': DevelopmentConfig
    }
    """
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    mail.init_app(app)
    db.init_app(app)

# if __name__ == '__main__':
#     app = create_app('testing')
#     app.run()
#     app1 = create_app()             #括号里面不写，表示默认是开发环境
#     app.run()

# 3）注册蓝图,和app关联在一起
    from app.auth import auth
    app.register_blueprint(auth, url_prefix='/auth')
    # 这里的url_prefix='/auth'表示的是网页运行时的前缀，不想要的时候可以去掉

    from app.todo import todo
    app.register_blueprint(todo,url_prefix='/todo')
    return app