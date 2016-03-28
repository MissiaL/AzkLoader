# coding=utf-8
import codecs
import os
from configparser import ConfigParser, NoOptionError

config = '''[database]
user =
password =
sid =
server =
[dialog]
;Папка, куда скачиваются сборки
path = E:\\work\\azk
port = 2015
; Путь к архиватору 7z
7z = C:\Program Files\7-Zip\7z.exe
[azkfin]
;Пути, где хранятся сборки АЦК-Финансы
path1 = //srv-fs-azkbuild/azkf/builds/azk2
path2 = //Srv-build1/build/AZK/builds
report1 = //srv-fs-azkbuild/azkf/builds/reports
report2 = //Srv-build1/build/Reports
'''


class Configurator:
    def __init__(self):
        self.Config = ConfigParser()
        if not os.path.exists('config.cfg'):
            with codecs.open('config.cfg', 'w', encoding='utf8') as c:
                c.write(config)
        self.Config.read('config.cfg')

    def getoption(self, section, option):
        if self.Config.has_section(section):
            if self.Config.has_option(section, option):
                return self.Config.get(section, option)
            else:
                return
        return

    def getdbparam(self):
        if self.Config.has_section('database'):
            server = self.Config.get('database', 'server')
            sid = self.Config.get('database', 'sid')
            user = self.Config.get('database', 'user')
            password = self.Config.get('database', 'password')
            return server, sid, user, password
        else:
            raise NoOptionError
