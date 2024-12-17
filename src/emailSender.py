import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailSender:

    def __init__ (self, loginEmail, password):
        self.port = 465
        self.password = password
        self.loginEmail = loginEmail
        self.smtpServer = "smtp.gmail.com" # What email address to use
        self.context = ssl.create_default_context() # Create encrypted space to send emails

       

    def SendEmail(self, receiverEmail, message):
         
        msg = MIMEMultipart()  # Create different parts of the email, "subject", "Sender", "Receiver"
        msg["From"] = self.loginEmail
        msg["To"] = receiverEmail
        msg["Subject"] = "Doorbell notification"
        msg.attach(MIMEText(message, "plain"))

        with smtplib.SMTP_SSL("smtp.gmail.com", self.port, context=self.context) as server: # Opens connection to email sending server tool
            server.login(self.loginEmail, self.password)
            server.sendmail(self.loginEmail, receiverEmail, msg.as_string())