from os import remove, path
from subprocess import run
from datetime import datetime

from app.Logger import LoggerConfig
from app.Email import Email


class Db:

    def __init__(self):
        self.__bkpFilename = f'bkp-{int(datetime.now().timestamp())}.sql.gz'
        self.__logger = LoggerConfig()
        self.__email = Email()

    def getBkpFilename(self):
        return self.__bkpFilename
        
    def makeDumpFile(self):
        cmd = f'mysqldump --defaults-file=.my.cnf --all-databases | gzip > \
            {self.__bkpFilename}'
        
        try:
            return run([cmd], check = True, shell = True)
        except Exception as err:
            self.removeDumpFile()
            self.__logger.log(err).error()
            self.__email.send('mysqldump err', err)
            exit(1)
        
    def removeDumpFile(self):
        if path.exists(self.__bkpFilename):
            remove(self.__bkpFilename)