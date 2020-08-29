from .base import *  # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',  # 连接的数据库类型
        'HOST': '192.168.25.130',  # 连接数据库的地址
        'PORT': 3306,  # 端口
        'NAME': 'typeidea',  # 数据库名称
        'USER': 'root',  # 用户
        'PASSWORD': 'Cmvcadmin2020!'  # 密码
    }
}
