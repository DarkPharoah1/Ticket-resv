#reqd library
import random
import time
import sys
from datetime import datetime
from datetime import date

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

print("YOU CAN DO THE FOLLOWING WORK HERE: ")
time.sleep(1)
print("1)Booking")
time.sleep(1)
print("2)Cancellation")
time.sleep(1)
print("3)Exit")
Booking = "Booking"
Cancellation = "Cancellation"
Exit = "Exit"
time.sleep(1)
work = input("Enter work: ")
if work == Booking:
#info about the destination
    today = date.today()
    date1 = input("Enter date in dd-mm-yyyy format: ")
    date2 = datetime.strptime(date1, "%d-%m-%Y").date()
    while date2 <= today:
        if date2 <= today:
            print("Date cannot be earlier than today.")
            date1 = input("Enter date in dd-mm-yyyy format: ")
            date2 = datetime.strptime(date1, "%d-%m-%Y").date()
            if date2 > today:
                fdate = date2

    if date2 > today:
        fdate = date2
    print("Date has been noted.")

    print("CHOOSE DESTINATION: ")
    time.sleep(1)
    print("Bangalore")
    time.sleep(1)
    print("Kolkata")
    time.sleep(1)
    print("Mumbai")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

    Bangalore = 'Bangalore'
    Kolkata = 'Kolkata'
    Mumbai = 'Mumbai'

    time.sleep(1)
    des = input("ENTER DESTINATION: ")
    #input data bout states in this indent block
    if des == Bangalore:
        time.sleep(1)
        print("Available flights: ")
        time.sleep(1)
        print("OPTION#1 @ Rs.1000")
        time.sleep(1)
        print("OPTION#2 @ Rs.2000")
        OPTION1 = "OPTION1"
        OPTION2 = 'OPTION2'
        option = input("Flight chosen: ")
        #input flight data in this indent block
        if option == OPTION1:
            print("OPTION1 chosen.")
            print("This airline supports snacks.")
            print("Do you want snack for additional Rs. 500?(Yes/No)")
            Yes = "Yes"
            No = "No"
            food = input("Food: ")
            if food == Yes:
                print("Ok")
                print("Total stands at Rs 1500")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

            elif food == No:
                print("OK")
                print("Total stands at Rs. 1000")
        if option == OPTION2:
            print("OPTION2 chosen")
            print("This airline does not support snacks")
            pay2 = 2000
    if des == Kolkata:
        time.sleep(1)
        print("OPTION#3 @Rs. 3000")
        time.sleep(1)
        print("OPTION#4 @Rs. 2500")
        print("Both flights offer no snacks")
        OPTION3 = "OPTION3"
        OPTION4 = 'OPTION4'
        option = input("Flight chosen: ")

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

    n = int(input("ENTER NUMBER OF PERSON: "))
    if des == Bangalore:
        if option == OPTION1:
            if food == Yes:
                gt = n * 1500
            if food == No:
                gt = n * 1000
        elif option == OPTION2:
            gt = n * 2000
    if des == Kolkata:
        if option == OPTION3:
            gt = n * 3000
        if option == OPTION4:
            gt = n * 2500

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

    if des == Mumbai:
        time.sleep(1)
        print("Available flights: ")
        time.sleep(1)
        print("OPTION#5 @ Rs.5000")
        time.sleep(1)
        print("OPTION#6 @ Rs.6000")
        print("OPTION6 offers snacks @Rs 1000.")
        OPTION5 = "OPTION5"
        OPTION6 = 'OPTION6'
        option = input("Flight chosen: ")
        if des == Mumbai:
            if option == OPTION5:
                gt = 5000 * n
            elif option == OPTION6:
                food = input("Snacks required(Yes/No): ")
                Yes = 'Yes'
                No = 'No'
                if food == Yes:
                    gt = 7000 * n
                if food == No:
                    gt = 6000 * n



    dict1 = {}

    for i in range(n):
        x = input("ENTER NAME: ")
        y = random.randrange(0, 99999)
        z = int(input("ENTER CONTACT NUMBER: "))

        dict1[x] = y, z, des, fdate, option

    print("CHECK VALUES: ")
    print("Your Grand Total stands at:", gt)
    print('FORMAT: Name, ID number, Destination, Date, Flight')
    print("USER'S INFO", dict1)
    sys.stdout = open("test.txt", "a+")
    print('FORMAT: Name, ID number, Phone Number, Destination, Date, Flight')
    print(dict1)
    print("Amount Due:", gt)
    sys.stdout.close()

    sys.stdout = open("Backup.txt", "a+")
    print('FORMAT: Name, ID number, Destination, Date, Flight')
    print(dict1)
    print("Amount Due:", gt)
    sys.stdout.close()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------

if work == Cancellation:
    dummy = input("Enter ID number: ")
    with open("test.txt", "r+") as f:
        new_f = f.readlines()
        f.seek(0)
        for line in new_f:
            if dummy not in line:
                f.write(line)
        f.truncate()
    print("Ok, your booking has been cancelled.")

    with open("Backup.txt", "r+") as g:
        new_g = g.readlines()
        g.seek(0)
        for line in new_g:
            if dummy not in line:
                g.write(line)
        g.truncate()

#--------------------------------------------------------------------------------------------------------------------------------------------------------------
elif work == "Exit":
    print("Thank you.")
#--------------------------------------------------------------------------------------------------------------------------------------------------------------
