#/usr/bin/python
# -*- coding: UTF-8 -*-

import os
import sys
import argparse
import subprocess

import MySQLdb

# def _argparse():
#     parser = argparse.ArgumentParser(description='archive big tables')
#     parser.add_argument('--database',action='store',dest='database',required=True,help='dababase name')
#     parser.add_argument('--table',action='store',dest='table',required=True,help='table name')
#     return parser.parse_args()
def get_conn(**kwargs):
    conn = MySQLdb.connect(**kwargs)
    try:
        yield conn
    finally:
        conn.close()

def main():
    database='test_insert_data_db'
    table='test_insert_data_table'
    cmd = '/usr/local/mysql56/bin/mysqldump -h192.168.56.102 -P3306 -urepl -prepl {0} {1} > /tmp/{0}.{1}.sql'.format(database,table)
    os.system(cmd)

    conn = MySQLdb.connect(host='192.168.56.102', user='repl', passwd='repl', db='test_insert_data_db')
    cur=conn.cursor()
    cur.execute("select max(id) from {0}.{1} where id < 3678".format(database,table))
    res=cur.fetchall()
    max_id=int(res[0][0])
    print max_id
    i=1
    while i < round(max_id/10)+1:
        hh=cur.execute("delete from {0}.{1} where id <= {2} limit 10".format(database,table,max_id))
        i+=1
    # cur.execute("commit")
    conn.commit()

if __name__ == '__main__':
    main()
#test1
