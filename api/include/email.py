import smtplib
from email.mime.text import MIMEText

#第三方SMTP服务
mail_host = "smtp.qq.com"
mail_user = "wsyjlly@foxmail.com"
mail_pass = "授权码"

sender = "wsyjlly@foxmail.com"
receiver = "wsyjlly@foxmail.com"

message = MIMEText("你好，世界！")
message["From"] = sender
message["To"] = receiver
message["Subject"] = "一起嗨吧！"

def send_email():
    try:
        server = smtplib.SMTP()
        server.connect(mail_host)
        server.login(mail_user,mail_pass)
        server.sendmail(sender,receiver,message.as_string())
        server.close()
        print("邮件发送成功!")
    except Exception as e:
        print("邮件发送失败!",e)

if __name__ == '__main__':
    send_email()