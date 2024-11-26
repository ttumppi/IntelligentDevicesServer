from firebaseAPI import FirebaseDB 
import os.path
import sys
import time
import msvcrt

firebaseDB = None

def Start():

    filepath = ""

    while (True):
        filepath = input("Please write the path to the sdk key JSON file:    ")
    
        if (os.path.isfile(filepath) == False):
            print(f'File {filepath} could not be found, please try again')
            continue

        break
    
    firebaseDB = FirebaseDB(filepath)

def RunServer():

    print ("Press s to shutdown")
    while (True):

        

        if msvcrt.kbhit():  # Check if a key is pressed
            user_input = msvcrt.getch().decode("utf-8")  # Read the keypress
            if user_input == "s":
                 break
        time.sleep(0.1)

Start()

RunServer()

print("Shutting down")