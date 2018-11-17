import warnings
import time
import sys
warnings.simplefilter(action='ignore', category=FutureWarning)

print "Importing machine learning modules..."
import csv
from sklearn import linear_model
import numpy as np
print "Modules have been imported."
print ""

details = ([])
views = ([])
counter = 0

recordNo = ""
while(True):
    recordNo = raw_input("How many records to learn from (number or infinity): ")
    if recordNo == "infinity":
        break
    try:
        recordNo = int(recordNo)
        break
    except:
        print "Incorrect value entered. Enter a number or infinity."


print "Reading data into memory..."
time.sleep(0.2)
with open('database.csv', 'rb') as csvfile:
    spamreader = csv.reader(csvfile)
    for row in spamreader:
        counter = counter + 1
        if counter == 1:
            continue
        details.append([row[8], row[9], row[10]])
        views.append([row[7]])
        if recordNo == "infinity":
            continue
        else:
            if counter == int(recordNo) + 1:
                break
print "Read " + str(len(details)) + " records."
print ""
print "Learning data..."
reg = linear_model.LinearRegression()
reg.fit(details, views)
print "Data learnt."
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
