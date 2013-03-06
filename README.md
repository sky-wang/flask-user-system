flask-user-system
=================

##use:
1. flask 
2. bootstrap
3. sqlalchemy

##fun:
1. reg
2. login
3. edit infomation
4. login out
5. change password
6. find password

===============

##说明
1. 程序采用python语言 ， 使用了flask网络框架 
2. 项目地址：https://github.com/Liuchang0812/flask-user-system 
3. 新浪云平台DEMO：http://lcusersystem.sinaapp.com/

##安装说明
1. 安装依赖环境：
```bash
   pip install -f requirements.txt
```
2. 配置相关参数
```bash
vi config.py #打开文件
DATABASE = 'sqlite:///db/database.db' #数据库文件
SECRET_KEY  = 'liuchang0812@gmail.com' #密匙
SMTP_HOST = 'smtp.qq.com' #smtp服务器
SMTP_PORT = '587'         #端口
SMTP_USER = 'xxxxxxxx@qq.com'#用户名
SMTP_PASS = 'xxxxxxxx' #密码

3. 运行初始化脚本
```bash
python init.py
```
4. 打开浏览器，输入地址







