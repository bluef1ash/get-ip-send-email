import re
from datetime import datetime
from os import getenv, path

import requests
import yagmail
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger


def send_mail(new_ip):
    """
    发送电子邮件
    :param new_ip: 最新的IP地址
    :return:
    """
    if isinstance(content, str):
        c = content.replace('#{ip}', new_ip)
    elif isinstance(content, list):
        c = []
        for data in content:
            if isinstance(data, str):
                c.append(data.replace('#{ip}', new_ip))
    else:
        c = new_ip
    print('开始发送邮件\n')
    yagmail.SMTP(user=username, password=password, host=host, port=port).send(to, subject, c)
    print('发送成功\n')


def check_ip():
    """
    检测最新IP地址
    :return:
    """
    if path.exists(ip_file_path):
        file = open(ip_file_path)
        old_ip = file.read()
        file.close()
    else:
        old_ip = ''
    new_ip = requests.request('GET', 'https://ip.3322.org', headers={'User-agent': 'Mozilla/5.0 (Windows NT 10.0; '
                                                                                   'Win64; x64) AppleWebKit/537.36 ('
                                                                                   'KHTML, like Gecko) '
                                                                                   'Chrome/42.0.2311.135 '
                                                                                   'Safari/537.36 Edge/12.10240'}).text
    new_ip = re.compile(r'[\n\s\t\r]').sub('', new_ip)
    print(datetime.now(), '，检测到IP地址是：', new_ip, '\n')
    if old_ip != new_ip:
        send_mail(new_ip)
    file = open(ip_file_path, 'w')
    file.write(new_ip)
    file.close()


if __name__ == '__main__':
    host = getenv('SEND_EMAIL_HOST')
    if not host:
        raise RuntimeError('发送邮件服务器地址（SMTP）不能为空！')
    username = getenv('SEND_EMAIL_USERNAME')
    if not username:
        raise RuntimeError('发送邮件服务器用户名不能为空！')
    password = getenv('SEND_EMAIL_PASSWORD')
    if not password:
        raise RuntimeError('发送邮件服务器密码不能为空！')
    to = getenv('SEND_EMAIL_TO')
    if to is None:
        raise RuntimeError('接收邮箱不能为空！')
    port = getenv('SEND_MAIL_PORT')
    if not port:
        port = 587
    subject = getenv('SEND_EMAIL_SUBJECT')
    if subject is None:
        subject = '系统变更IP地址'
    content = getenv('SEND_EMAIL_CONTENT')
    if not content:
        content = '变更IP地址为：<span style="color:#FF0000;font-weight:bold;">#{ip}</span>'
    cron_expression = getenv('SEND_EMAIL_CRON_EXPRESSION')
    if not cron_expression:
        cron_expression = '0 */1 * * *'
    ip_file_path = './ip.txt'
    scheduler = BlockingScheduler()
    scheduler.add_job(check_ip, CronTrigger.from_crontab(cron_expression, 'Asia/Shanghai'),
                      next_run_time=datetime.now())
    scheduler.start()
