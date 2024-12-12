from firebaseAPI import FirebaseDB 
from emailSender import EmailSender
from client import HttpClient
import os.path
import sys
import time
import msvcrt
import re
import getpass

client = None
emailSender = None

emailReceiver = ""

def CreateDatabaseConnection():

    global client

    client = HttpClient("localhost", "8080", VisitorAddedListener)
    client.Start()

def WaitForShutdown():


    
    while (input("Press S to shutdown") != "S"):
        time.sleep(10)
   




def SetupEmailSender():
    global emailSender
    global emailReceiver

    email = ""
    password = ""

    emailReceiver = input("Input email of receiver of notifications: ")

    email = input("Input login email used as sender:  ")

    password = getpass.getpass("Please input password for sender account:  ")

    emailSender = EmailSender(email, password)



def VisitorAddedListener(visitorMessage):
    emailSender.SendEmail(emailReceiver, f'You have a visit. message:  {visitorMessage}')
    print(f"Sending message : {visitorMessage}")

CreateDatabaseConnection()

SetupEmailSender()



WaitForShutdown()
client.Shutdown()

print("Shutting down")