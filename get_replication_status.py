import pymysql
from pymysql.cursors import DictCursor

#cursorclass=DictCursor indicates return results as a dictionary
conn = pymysql.connect(host='192.168.56.100',
                       port=3306,
                       user='repl',
                       password='repl',
                       database='test',
                       connect_timeout=10000,
                       cursorclass=DictCursor)

cur = conn.cursor()
cur.execute('show slave status')
res=cur.fetchall()
for row in res:
    print row['Slave_SQL_Running']
