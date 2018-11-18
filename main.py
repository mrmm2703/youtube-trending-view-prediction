import warnings
import time
import sys
import os.path
warnings.simplefilter(action='ignore', category=FutureWarning)

print "Importing machine learning modules..."
import csv
from sklearn.externals import joblib
from sklearn import linear_model
import numpy as np
print "Modules have been imported."
print ""

details = ([])
views = ([])
counter = 0

if os.path.isfile("model.joblib"):
    print "Found saved model."
    while(True):
        choice = raw_input("Do you want to used the model on disk (Y/N)? ")
        if choice.lower() == "y" or choice.lower() == "yes":
            print "Loading model..."
            reg = joblib.load("model.joblib")
            print "Model loaded."
            print ""
            break
        elif choice.lower() == "n" or choice.lower() == "no":
            print ""
            print "Reading database into memory..."
            time.sleep(0.2)
            with open('database.csv', 'rb') as csvfile:
                spamreader = csv.reader(csvfile)
                for row in spamreader:
                    counter = counter + 1
                    if counter == 1:
                        continue
                    details.append([row[8], row[9], row[10]])
                    views.append([row[7]])
            print "Read " + str(len(details)) + " records."
            print ""
            print "Learning data..."
            time.sleep(0.1)
            reg = linear_model.LinearRegression()
            reg.fit(details, views)
            print "Data learnt."
            while(True):
                choice = raw_input("Do you want save the model to disk (Y/N)? ")
                if choice.lower() == "y" or choice.lower() == "yes":
                    joblib.dump(reg, 'model.joblib')
                    print "Model saved to disk."
                    print ""
                    break
                elif choice.lower() == "n" or choice.lower() == "no":
                    print ""
                    break
                else:
                    print "Invalid choice. Try again"
                    print ""
            break
else:
    print "Model does not exist. Creating model..."
    print ""
    print "Reading database into memory..."
    time.sleep(0.2)
    with open('database.csv', 'rb') as csvfile:
        spamreader = csv.reader(csvfile)
        for row in spamreader:
            counter = counter + 1
            if counter == 1:
                continue
            details.append([row[8], row[9], row[10]])
            views.append([row[7]])

    print "Read " + str(len(details)) + " records."
    print ""
    print "Learning data..."
    time.sleep(0.1)
    reg = linear_model.LinearRegression()
    reg.fit(details, views)
    print "Data learnt."
    while(True):
        choice = raw_input("Do you want save the model to disk (Y/N)? ")
        if choice.lower() == "y" or choice.lower() == "yes":
            joblib.dump(reg, 'model.joblib')
            print "Model saved to disk."
            print ""
            break
        elif choice.lower() == "n" or choice.lower() == "no":
            print ""
            break
        else:
            print "Invalid choice. Try again"
            print ""

while(True):
    choice = raw_input("Press enter to continue with a prediction or type in exit to leave: ")
    if choice == "exit":
        print "Leaving..."
        sys.exit()
    elif choice == "":
        while(True):
            cLikes = raw_input("Enter the number of likes: ")
            try:
                cLikes = int(cLikes)
                break
            except:
                print "Incorrect value entered. Try again."
        while(True):
            cDislikes = raw_input("Enter the number of dislikes: ")
            try:
                cDislikes = int(cDislikes)
                break
            except:
                print "Incorrect value entered. Try again."
        while(True):
            cComments = raw_input("Enter the number of comments: ")
            try:
                cComments = int(cComments)
                print ""
                break
            except:
                print "Incorrect value entered. Try again."
        print "The predicted number of views is " + str(int(reg.predict([[cLikes, cDislikes, cComments]])[0][0]))
        print ""
    else:
        print "Invalid choice. Try again."
