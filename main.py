from dotenv import load_dotenv
load_dotenv()

from app.DriveConn import DriveConn
from app.DriveBkp import DriveBkp

if __name__ == '__main__':
    driveConn = DriveConn()
    drive = driveConn.getInstance()

    driveBkp = DriveBkp(drive)
    driveBkp.db()