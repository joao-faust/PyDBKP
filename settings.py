from os import path, getenv

# app
BASE_DIR = path.dirname(path.abspath(__file__))
APP_NAME = str(getenv('APP_NAME'))

# drive
FOLDER_ID = str(getenv('FOLDER_ID'))

# email
RECIEVER_EMAIL = str(getenv('RECIEVER_EMAIL'))
SENDER_EMAIL = str(getenv('SENDER_EMAIL'))
SENDER_EMAIL_PASSWD = str(getenv('SENDER_EMAIL_PASSWD'))