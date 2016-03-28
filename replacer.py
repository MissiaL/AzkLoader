# coding=utf-8

import os
import re
import sys
from configparser import ConfigParser

def replaceServerPort(port):
    serverBat = 'StartServer.bat'

    serverPort = 'set SERVER_PORT={}\n'.format(port.strip())
    reServerPort = re.compile('\Aset SERVER_PORT=')

    with open(serverBat, 'r') as bat:
        data = bat.readlines()

    serverPortFound = False

    serverBatNewConfig = []

    for line in data:
        if re.match(reServerPort, line):
            serverBatNewConfig.append(serverPort)
            serverPortFound = True
            continue
        serverBatNewConfig.append(line)

    if not serverPortFound:
        serverBatNewConfig.append(serverPort)
    os.remove(serverBat)
    with open(serverBat, 'w') as newBat:
        for line in serverBatNewConfig:
            newBat.write(line)

def replaceClientPort(port):
    clientConfig = 'Azk2Clnt.ini'
    config = ConfigParser()
    config.read(clientConfig)
    config.set('CORBA','Server','localhost:'+port)
    with open(clientConfig, 'w') as configfile:
        config.write(configfile)

def replaceAzkConfig(db):
    config = 'Azk2Server.properties'
    dburl = 'azk.db.url=jdbc:oracle:thin:@172.21.10.56:1521:support11\n'
    dbname = 'azk.db.user={}\n'.format(db.strip())
    dbpass = 'azk.db.password={}\n'.format(db.strip())
    dbtrace = 'azk.db.traceenabled=true\n'
    azklic = 'azk.license.name=bft.lic\n'

    reDbUrl = re.compile('\Aazk.db.url')
    reDbName = re.compile('\Aazk.db.user')
    reDbPass = re.compile('\Aazk.db.password')
    reDbTrace = re.compile('\Aazk.db.traceenabled')
    reAzkLic = re.compile('\Aazk.license.name')

    with open(config, 'r') as azkconfig:
        data = azkconfig.readlines()

    dbUrlFound = False
    dbNameFound = False
    dbPassFound = False
    dbTraceFound = False
    azkLicFound = False

    azkNewConfig = []
    for line in data:
        if re.match(reDbUrl, line):
            azkNewConfig.append(dburl)
            dbUrlFound = True
            continue
        if re.match(reDbName, line):
            azkNewConfig.append(dbname)
            dbNameFound = True
            continue
        if re.match(reDbPass, line):
            azkNewConfig.append(dbpass)
            dbPassFound = True
            continue
        if re.match(reAzkLic, line):
            azkNewConfig.append(azklic)
            azkLicFound = True
            continue
        if re.match(reDbTrace, line):
            azkNewConfig.append(dbtrace)
            dbTraceFound = True
            continue
        azkNewConfig.append(line)

    if not dbUrlFound:
        azkNewConfig.append(dburl)
    if not dbNameFound:
        azkNewConfig.append(dbname)
    if not dbPassFound:
        azkNewConfig.append(dbpass)
    if not dbTraceFound:
        azkNewConfig.append(dbtrace)
    if not azkLicFound:
        azkNewConfig.append(azklic)

    os.remove(config)
    with open(config, 'w') as newAzkConfig:
        for line in azkNewConfig:
            newAzkConfig.write(line)


def replaceGzConfig(db, dbtype):
    config = 'Server.properties'
    if dbtype in ('fb', 'firebird'):
        path = db.replace('\\', '\\\\')
        dburl = 'azk.db.url=jdbc:firebirdsql:localhost/3050:{}\n'.format(path)
        dbdriver = 'azk.db.driver=org.firebirdsql.jdbc.FBDriver\n'
        dbname = 'azk.db.user=SYSDBA\n'
        dbpass = 'azk.db.password=masterkey\n'
        dbaccessmode = 'azk.db.accessmode=interbase\n'
    elif dbtype in ('o', 'oracle'):
        dburl = 'azk.db.url=jdbc:oracle:thin:@172.21.10.56:1521:support11\n'
        dbdriver = 'azk.db.driver=oracle.jdbc.driver.OracleDriver\n'
        dbname = 'azk.db.user={}\n'.format(db.strip())
        dbpass = 'azk.db.password={}\n'.format(db.strip())
        dbaccessmode = 'azk.db.accessmode=oracle\n'
    else:
        sys.exit()
    dbtrace = 'azk.db.traceenabled=true\n'

    reDbUrl = re.compile('\Aazk.db.url')
    reDbName = re.compile('\Aazk.db.user')
    reDbPass = re.compile('\Aazk.db.password')
    reDbDriver = re.compile('\Aazk.db.driver')
    reDbAccessmode = re.compile('\Aazk.db.accessmode')
    reDbTrace = re.compile('\Aazk.db.traceenabled')

    with open(config, 'r') as azkconfig:
        data = azkconfig.readlines()

    dbUrlFound = False
    dbNameFound = False
    dbDriverFound = False
    dbAccessmodeFound = False
    dbPassFound = False
    dbTraceFound = False

    azkNewConfig = []
    for line in data:
        if re.match(reDbUrl, line):
            azkNewConfig.append(dburl)
            dbUrlFound = True
            continue
        if re.match(reDbDriver, line):
            azkNewConfig.append(dbdriver)
            dbDriverFound = True
            continue
        if re.match(reDbAccessmode, line):
            azkNewConfig.append(dbaccessmode)
            dbAccessmodeFound = True
            continue
        if re.match(reDbName, line):
            azkNewConfig.append(dbname)
            dbNameFound = True
            continue
        if re.match(reDbPass, line):
            azkNewConfig.append(dbpass)
            dbPassFound = True
            continue
        if re.match(reDbTrace, line):
            azkNewConfig.append(dbtrace)
            dbTraceFound = True
            continue
        azkNewConfig.append(line)

    if not dbUrlFound:
        azkNewConfig.append(dburl)
    if not dbNameFound:
        azkNewConfig.append(dbname)
    if not dbPassFound:
        azkNewConfig.append(dbpass)
    if not dbTraceFound:
        azkNewConfig.append(dbtrace)
    if not dbAccessmodeFound:
        azkNewConfig.append(dbaccessmode)
    if not dbDriverFound:
        azkNewConfig.append(dbdriver)

    os.remove(config)
    with open(config, 'w') as newAzkConfig:
        for line in azkNewConfig:
            newAzkConfig.write(line)


if __name__ == '__main__':
    os.chdir(r'E:\work\azk\2.38.2.89')
    replaceClientPort('2015')
