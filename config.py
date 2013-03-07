# -*- coding: utf-8 -*-
__author__ = 'liuchang'
import sae.const
DB = sae.const.MYSQL_DB      # 数据库名
USER = sae.const.MYSQL_USER    # 用户名
PASS = sae.const.MYSQL_PASS    # 密码
HOST = sae.const.MYSQL_HOST    # 主库域名（可读写）
PORT = sae.const.MYSQL_PORT    # 端口，类型为<type 'str'>，请根据框架要求自行转换为int

DATABASE = 'mysql://%s:%s@%s:%d/%s' %(USER,PASS,HOST,int(PORT),DB)
SECRET_KEY  = 'liuchang0812@gmail.com'
SMTP_HOST = 'smtp.qq.com'
SMTP_PORT = '587'
SMTP_USER = '757695453@qq.com'
SMTP_PASS = 'daydayupup'
