from firebaseAPI import FirebaseDB 
from emailSender import EmailSender
import os.path
import sys
import time
import msvcrt
import re
import getpass

firebaseDB = None
emailSender = None

emailReceiver = ""

def CreateDatabaseConnection():

    global firebaseDB

    filepath = ""

    while (True):
        filepath = input("Please write the path to the sdk key JSON file:    ")
    
        if (os.path.isfile(filepath) == False):
            print(f'File {filepath} could not be found, please try again')
            continue

        break
    
    firebaseDB = FirebaseDB(filepath, True)

def WaitForShutdown():


    
    print ("Press s to shutdown")
    while (True):

        

        if msvcrt.kbhit():  # Check if a key is pressed
            user_input = msvcrt.getch().decode("utf-8")  # Read the keypress
            if user_input == "s":
                 break
        time.sleep(0.1)




def SetupEmailSender():
    global emailSender
    global emailReceiver

    email = ""
    password = ""

    emailReceiver = input("Input email of receiver of notifications: ")

    email = input("Input login email used as sender:  ")

    password = getpass.getpass("Please input password for sender account:  ")

    emailSender = EmailSender(email, password)

def RegisterVisitorAddedEventListener():
    firebaseDB.RegisterListenerForReceivedVisitors(VisitorAddedListener)

def VisitorAddedListener(visitor):
    emailSender.SendEmail(emailReceiver, f'You have a visit from {visitor}')

CreateDatabaseConnection()

SetupEmailSender()

RegisterVisitorAddedEventListener()

WaitForShutdown()

print("Shutting down")