import os
import smtplib
import sys
import cgi
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import email.encoders

def sendmail(toaddr, name):
    em = 'yourownchatbot@gmail.com'
    text = 'Ваш заказ готов!'

    fromaddr = "yourownchatbot@gmail.com"
    mypass = "qwertyuiop21"
    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = 'Доставка еды'
    body = name + "! " + "\n\n\n"+str(text)
    msg.attach(MIMEText(body, 'plain'))
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(fromaddr, mypass)
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
