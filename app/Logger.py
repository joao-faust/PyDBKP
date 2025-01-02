from os import path
from datetime import datetime


class LoggerConfig:

    def __init__(self):
        self.__dirname = 'logs'
        self.__filename = 'app'
        self.__fullpath = path.join(self.__dirname, self.__filename + '.log')

    def getFullpath(self):
        return self.__fullpath
    
    def log(self, msg: str):
        return _Logger(self, msg)
    

class _Logger:

    def __init__(self, config: LoggerConfig, msg: str):
        self.__config = config
        self.__msg = msg

    def __log(self, level: str):
        fullpath = self.__config.getFullpath()

        with open(fullpath, 'a') as f:
            now = datetime.now()
            log = f'[{now}][{level}] - {self.__msg}\n'
            f.write(log)

    def info(self):
        self.__log('INFO')

    def error(self):
        self.__log('ERROR')