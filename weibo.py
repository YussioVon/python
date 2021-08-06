#!/usr/bin/python
#coding:utf-8
# @Time : 2021/8/5 10:57
# @Author :Yussio
# @FileName : weibo
import smtplib
from email.mime.text import MIMEText

import requests
from bs4 import BeautifulSoup


def get_content():
    data = {
        'cata':'realtimehot'
    }
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }
    try:
        res = requests.get('http://s.weibo.com/top/summary?', params=data, headers=headers)
        if res.status_code == 200:
            html = res.text
            soup = BeautifulSoup(html, 'lxml')
            tr = soup.find(id='pl_top_realtimehot').find_all('tr', class_="")
            hotSearch = ""

        for i, item in enumerate(tr):
            if i > 0:
                title = item.find('a').get_text()
                url = "https://s.weibo.com" + item.find('a').attrs['href']
                hot = item.find('span').get_text()
                id = item.find('td', class_="td-01 ranktop").get_text()
                hotSearch += '<p>'+id + '\t' + title + "\t"+  hot+'</p>' +'<a href={url}>'.format(url=url)+url+'</a>'+"\n"
        print(hotSearch)
        return hotSearch
    except:
        print("访问失败")


def send_mail(message):
    mail_host = 'smtp.qq.com'
    mail_user = '986285415'
    mail_pass = 'snuttcqakjnobaie'

    # 发送方，可以自己给自己发
    sender = '986285415@qq.com'

    # 邮件接受方邮箱地址，可多写
    receivers = [
        '986285415@qq.com','731812309@qq.com','fyx98628@163.com'
    ]

    # 邮件内容设置，将第一个参数修改成你要发送的内容即可
    message = MIMEText(message, 'html', 'utf-8')
    # 邮件主题
    message['Subject'] = '微博热搜,请查收'
    # 发送方信息
    message['From'] = mail_user+"<"+sender+">"
    # 接受方信息
    message['To'] = receivers[0]

    try:
        smtpObj = smtplib.SMTP_SSL(mail_host)
        # 登录到服务器
        smtpObj.login(mail_user, mail_pass)
        # 发送
        smtpObj.sendmail(
            sender, receivers, message.as_string())
        # 退出
        smtpObj.quit()
        print('success')
    except smtplib.SMTPException as e:
        print('error', e)  # 打印错误

if __name__ == '__main__':
    # get_content()
    res = get_content()
    send_mail(res)