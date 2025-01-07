from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
from sys import exit
from os import path

from app.Logger import LoggerConfig
from app.Email import Email
from settings import BASE_DIR


class DriveConn:

    def __init__(self):
        self.__logger = LoggerConfig()
        self.__email = Email()

    def getInstance(self):
        gauth = GoogleAuth()

        credentiasFilePath = path.join(BASE_DIR, 'credentials.txt')

        try:
            gauth.LoadCredentialsFile(credentiasFilePath)
            if gauth.credentials is None:
                gauth.LocalWebserverAuth()
            elif gauth.access_token_expired:
                gauth.Refresh()
            else:
                gauth.Authorize()
            gauth.SaveCredentialsFile(credentiasFilePath)
        except Exception as err:
            self.__logger.log(err).error()
            self.__email.send('drive conn err', err)
            exit(1)
        
        return GoogleDrive(gauth)