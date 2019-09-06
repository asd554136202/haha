import pymysql

host = 'localhost'
port = 3306
usr_account = 'root'
pwd = 'root'
db = 'edu'
sql = 'select * from xsmart_users where id = 64'
conn = pymysql.connect(host=host, port=port, user=usr_account, password=pwd, db=db)
cur = conn.cursor()
cur.execute(sql)
data = cur.fetchone()
print('data is', data)
