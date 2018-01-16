#/usr/bin/python
import MySQLdb
from MySQLdb.cursors import DictCursor

#cursorclass=DictCursor indicates return results as a dictionary
conn = pymysql.connect(host='127.0.0.1',
                       port=3306,
                       user='repl',
                       passwd='repllper',
                       cursorclass=DictCursor)

cur = conn.cursor()
cur.execute('show slave status')
res=cur.fetchall()
for row in res:
    if row['Slave_SQL_Running'] =='Yes' and row['Slave_IO_Running'] == 'Yes':
        print 1
    else:
        print 0
