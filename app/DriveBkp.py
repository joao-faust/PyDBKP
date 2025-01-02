from pydrive.drive import GoogleDrive

from app.Db import Db


class DriveBkp:

    def __init__(self, drive: GoogleDrive, folderId: str):
        if drive is None:
            raise TypeError('The drive instance is None')

        self.__drive = drive
        self.__folderId = folderId
        self.__db = Db()
        
    def db(self):
        if self.__db.makeDumpFile() is False:
            return
    
        file = self.__drive.CreateFile({
            'parents': [{'id': self.__folderId}]
        })
        file.SetContentFile(self.__db.getBkpFilename())
        file.Upload()

        if self.__db.removeDumpFile() is False:
            return