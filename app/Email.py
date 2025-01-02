from smtplib import SMTP
from os import getenv

from app.Logger import LoggerConfig


class Email:

    def __init__(self):
        self.__sender = str(getenv('SENDER_EMAIL'))
        self.__senderPasswd = str(getenv('SENDER_EMAIL_PASSWD'))
        self.__reciever = str(getenv('RECIEVER_EMAIL'))
        self.__appName = str(getenv('APP_NAME'))
        self.__host = 'smtp.gmail.com'
        self.__port = 587
        self.__logger = LoggerConfig()

        # create email session
        self.__session = SMTP(self.__host, self.__port)
        self.__session.starttls()
        self.__session.login(self.__sender, self.__senderPasswd)

    def send(self, title: str, body: str):
        message = f'Subject: {self.__appName} - {title}\n\n{body}'.encode('utf-8')

        try:
            self.__session.sendmail(self.__sender, self.__reciever, message)
        except Exception as err:
            self.__logger.log(err).error()
