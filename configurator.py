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
