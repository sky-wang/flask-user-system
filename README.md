flask-user-system
=================


##说明
1. 程序采用python语言 ， 使用了flask网络框架 
2. 项目地址：https://github.com/Liuchang0812/flask-user-system 
3. 新浪云平台DEMO：http://1.lcusersystem.sinaapp.com/

##安装说明
1. 安装依赖环境：
```bash
   pip install -f requirements.txt
```
2. 配置相关参数

```python
   vi config.py 
   DATABASE = 'sqlite:///db/database.db' #数据库文件
   SECRET_KEY  = 'liuchang0812@gmail.com' #密匙
   SMTP_HOST = 'smtp.qq.com' #smtp服务器
   SMTP_PORT = '587'         #端口
   SMTP_USER = 'xxxxxxxx@qq.com'#用户名
   SMTP_PASS = 'xxxxxxxx' #密码
```

3. 运行初始化脚本

```bash
python init.py
python myapp.py
```

4. 打开浏览器，输入地址 http://127.0.0.1:5000






