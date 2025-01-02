from pydrive.drive import GoogleDrive
from sys import exit
from os import getenv
from datetime import datetime

from app.Db import Db
from app.Logger import LoggerConfig
from app.Email import Email


class DriveBkp:

    def __init__(self, drive: GoogleDrive):
        self.__drive = drive
        self.__folderId = str(getenv('FOLDER_ID'))
        self.__db = Db()
        self.__logger = LoggerConfig()
        self.__email = Email()
        
    def db(self):
        bkpFilename = self.__db.getBkpFilename()

        self.__db.makeDumpFile()
    
        file = self.__drive.CreateFile({
            'parents': [{'id': self.__folderId}]
        })
        file.SetContentFile(bkpFilename)

        self.__db.removeDumpFile()

        try:
            file.Upload()
        except Exception as err:
            self.__logger.log(err).error()
            self.__email.send('drive upload err', err)
            exit(1)

        now = datetime.now().strftime('%Y-%m-%d at %H:%M:%S')
        successMsg = f'The backup was performed with the name {bkpFilename} on {now}'
        self.__logger.log(successMsg).info()
        self.__email.send('bkp', successMsg)