from firebaseAPI import FirebaseDB 
import os.path

firebaseDB = None

def Start():

    filepath = ""

    while (True):
        filepath = input("Please write the path to the sdk key JSON file:    ")
    
        if (os.path.isfile(filepath) == False):
            print(f'File {filepath} could not be found, please try again')

        break
    
    firebaseDB = FirebaseDB(filepath)


