# 定时获取IP地址并发送邮件提醒

使用Docker，Cron定时，使用前请先配置环境变量

Docker Hub镜像搜索：[get-ip-send-email](https://hub.docker.com/repository/docker/bluef1ash/get-ip-send-email)

#### 运行命令

```shell
docker run -d -e SEND_EMAIL_HOST=xxx.xxx.xxx \
              -e SEND_EMAIL_USERNAME=xxx \
              -e SEND_EMAIL_PASSWORD=xxx \
              -e SEND_EMAIL_TO=abc@def.com bluef1ash/get-ip-send-email:latest
```

### 环境变量列表

```shell
SEND_EMAIL_HOST            # 发送邮件服务器地址（SMTP）；必选
SEND_EMAIL_USERNAME        # 发送邮件服务器用户名；必选
SEND_EMAIL_PASSWORD        # 发送邮件服务器密码；必选
SEND_MAIL_PORT             # 发送邮件服务器端口号；默认587；可选
SEND_EMAIL_TO              # 接收邮箱地址；必选
SEND_EMAIL_SUBJECT         # 发送邮件主题；可选
SEND_EMAIL_CONTENT         # 发送邮件内容，内容需要添加“#{ip}”标识符，用来替换自动获取到的IP地址
                           # 支持多条、HTML标签、附件
                           # 例如：['<span style="color:#FF0000;font-weight:bold;">发送内容</span>',
                           #       'https://www.baidu.com/a.pdf']
                           # 可选
SEND_EMAIL_CRON_EXPRESSION # Cron表达式；可选
```

### Cron表达式

```
例子：

    每月的最后1天

    0 0 L * * *

说明：

*    *    *    *    *
-    -    -    -    -
|    |    |    |    |
|    |    |    |    +----- 星期 (0 -  7) (星期天为0或者7) 或者 sun,mon,tue,wed,thu,fri,sat
|    |    |    +---------- 月份 (1 - 12) 或者 jan,feb,mar,apr ...
|    |    +--------------- 天   (1 - 31)
|    +-------------------- 小时 (0 - 23)
+------------------------- 分钟 (0 - 59)
```
