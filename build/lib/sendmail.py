# -*- coding: utf-8 -*-
__author__ = 'liuchang'

from config import  SMTP_HOST , SMTP_PASS , SMTP_PORT , SMTP_USER
from smtplib import SMTP
import mimetypes
from email.mime.text import MIMEText



def sendmail(to , subject , body):
    msg = MIMEText(body)
    msg['From'] = SMTP_USER
    msg['To'] = to
    msg['Subject'] = subject
    smtp = SMTP()
    smtp.connect(SMTP_HOST)
    smtp.login(SMTP_USER,SMTP_PASS)
    smtp.sendmail(SMTP_USER,to,msg.as_string())
    smtp.quit()
    print 'send succsessful!'


#sendmail('liuchang0812@gmail.com','hello lc ,can you teach me Cplusplus','hello , this is a email send by python')