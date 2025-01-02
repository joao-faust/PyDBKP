from os import remove, path
from subprocess import getstatusoutput
from datetime import datetime


class Db:

    def __init__(self):
        self.__bkpFilename = self.__buildBkpFilename() 

    def __buildBkpFilename(self):
        ct = datetime.now()
        ts = int(ct.timestamp())
        return f'bkp-{ts}.sql.gz'

    def getBkpFilename(self):
        return self.__bkpFilename
        
    def makeDumpFile(self):
        cmd = f'mysqldump --defaults-file=./.my.cnf --all-databases | gzip > {self.__bkpFilename}'
        res = getstatusoutput(cmd)
        
        if len(res) > 1 and res[1] != '':
            self.removeDumpFile()
            print(res[1])
            return False
        return True
        
    def removeDumpFile(self):
        if path.exists(self.__bkpFilename) is False:
            return False
        remove(self.__bkpFilename)
        return True