# coding=utf-8
import cx_Oracle

def getDbShemaList(server, sid, user, password):
    dsn_tns = cx_Oracle.makedsn(server, 1521, sid)
    con = cx_Oracle.connect(user, password, dsn_tns, mode=cx_Oracle.SYSDBA)
    cur = con.cursor()
    cur.execute('''
    select u.name, U.EXT_USERNAME, D.CREATED from user$ u
    inner join dba_users d on u.name=d.username
    where D.ACCOUNT_STATUS='OPEN'
    and d.username not in ('DBSNMP', 'SYS', 'SYSTEM', 'SYSMAN', 'SCOTT')
    order by u.name asc''')
    return cur
