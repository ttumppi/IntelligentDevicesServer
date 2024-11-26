import firebase_admin
from firebase_admin import credentials, db
import smtplib
from email.mime.text import MIMEText




class FirebaseDB:

    def __init__(self, pathToServiceAccountFile):

        self.cred = credentials.Certificate(pathToServiceAccountFile)
        firebase_admin.initialize_app(self.cred, {
            'databaseURL': 'https://intelligentdevicescourse-default-rtdb.europe-west1.firebasedatabase.app/'
})