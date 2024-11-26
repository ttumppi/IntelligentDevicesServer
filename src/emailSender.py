import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:

    def __init__ (self, loginEmail, password):
        self.port = 465
        self.password = password
        self.loginEmail = loginEmail
        self.smtpServer = "smtp.gmail.com"
        self.context = ssl.create_default_context()

       

    def SendEmail(self, receiverEmail, message):
         
        msg = MIMEMultipart()
        msg["From"] = self.loginEmail
        msg["To"] = receiverEmail
        msg["Subject"] = "Doorbell notification"
        msg.attach(MIMEText(message, "plain"))

        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server:
            server.login(self.loginEmail, self.password)
            server.sendmail(self.loginEmail, receiverEmail, msg.as_string())