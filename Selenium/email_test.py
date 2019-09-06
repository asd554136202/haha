import yagmail

user = 'asd554136202@163.com'
user_pwd = 'asd554136202'
user_host = 'smtp.163.com'
user_port = '465'
zj_mail = '554136202@qq.com'
# send = yagmail.SMTP(user=user, password=user_pwd, host=user_host, port=user_port)
body = '<h1>老板，这是我的测试报告</h1>'
send = yagmail.SMTP(user=user, password=user_pwd, host=user_host, port=user_port)

send.send(to=zj_mail, subject='自动化测试报告', contents=[body, './123.txt'])

print('发送成功')
