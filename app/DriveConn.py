from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive


class DriveConn:

    def getInstance(self):
        gauth = GoogleAuth()

        gauth.LoadCredentialsFile('credentials.txt')
        if gauth.credentials is None:
            gauth.LocalWebserverAuth()
        elif gauth.access_token_expired:
            gauth.Refresh()
        else:
            gauth.Authorize()
        gauth.SaveCredentialsFile('credentials.txt')

        return GoogleDrive(gauth)