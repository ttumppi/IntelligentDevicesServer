import smtplib, ssl
from email.mime.text import MIMEText

class EmailSender:

    def __init__ (self, loginEmail, password):
        self.port = 465
        self.password = password
        self.loginEmail = loginEmail

        self.context = ssl.create_default_context()

       

    def SendEmail(self, receiverEmail, message):
         
         with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
            server.login(self.loginEmail, self.password)
            server.sendmail(self.loginEmail, receiverEmail, message)