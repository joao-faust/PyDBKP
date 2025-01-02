from dotenv import dotenv_values
config = dotenv_values('.env')

from app.DriveConn import DriveConn
from app.DriveBkp import DriveBkp


if __name__ == '__main__':
    driveConn = DriveConn()
    drive = driveConn.getInstance()

    FOLDER_ID = config['FOLDER_ID']
    try:
        driveBkp = DriveBkp(drive, FOLDER_ID)
        driveBkp.db()
    except TypeError as msg:
        print(msg)