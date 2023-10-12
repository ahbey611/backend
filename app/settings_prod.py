from app.settings import *

DEBUG = False

# TODO: 修改数据库连接的密码和 IP 地址
# 你的数据库使用账号 root（默认值），其密码为你的学号，数据库名称为 thss，使用端口3306（默认值）
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "NAME": "thss",
        "USER": "root",
        "PASSWORD": "2021080078",
        "HOST": "db",
        "PORT": "3306",
    }
}
