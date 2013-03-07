# -*- coding: utf-8 -*-
__author__ = 'liuchang'
import sae.mail
from config import  SMTP_HOST , SMTP_PASS , SMTP_PORT , SMTP_USER
from smtplib import SMTP
import mimetypes
from email.mime.text import MIMEText



def sendmail(to , subject , body):
    sae.mail.send_mail(to,subject,body,(SMTP_HOST,SMTP_PORT,SMTP_USER,SMTP_PASS,True)) ;

#sendmail('liuchang0812@gmail.com','hello lc ,can you teach me Cplusplus','hello , this is a email send by python')