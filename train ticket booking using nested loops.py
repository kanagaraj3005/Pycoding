import datetime
import random
import string
while True:
    print("Welcome to Train ticket booking portal!")
    print("Available stations: 1. egmore,2. tambaram,3. chengalpattu,4. villupuram,5. cuddalore")    
    s = input("Enter your source station(in lower case only):")
    d = input("Enter your destination station(in lower case only):")
    fare = None
    if s == "egmore" and d == "tambaram":
        fare = 20
    elif s == "egmore" and d == "chengalpattu":
        fare = 30
    elif s == "egmore" and d == "villupuram":
        fare = 45
    elif s == "egmore" and d == "cuddalore":
        fare = 65
    elif s == "cuddalore" and d == "egmore":
        fare = 65
    elif s == "villupuram" and d == "egmore":
        fare = 45
    elif s == "chengalpattu" and d == "egmore":
        fare = 30
    elif s == "tambaram" and d == "egmore":
        fare = 20
    elif s == "tambaram" and d == "chengalpattu":
        fare = 25
    elif s == "tambaram" and d == "villupuram":
        fare = 40
    elif s == "tambaram" and d == "cuddalore":
        fare = 60
    elif s == "cuddalore" and d == "tambaram":
        fare = 60
    elif s == "villupuram" and d == "tambaram":
        fare = 40
    elif s == "chengalpattu" and d == "tambaram":
        fare = 25
    elif s == "chengalpattu" and d == "villupuram":
        fare = 30
    elif s == "chengalpattu" and d == "cuddalore":
        fare = 45
    elif s == "cuddalore" and d == "chengalpattu":
        fare = 45
    elif s == "villupuram" and d == "chengalpattu":
        fare = 25
    elif s == "villupuram" and d == "cuddalore":
        fare = 20
    elif s == "cuddalore" and d == "villupuram":
        fare = 20
    else:
        print("invalid stations")
        continue
    print(f"Ticket fare is Rs.{fare}/person")
    member = int(input("How many members?:"))
    total = fare * member
    print("Total fare is Rs.",total, "/-")
    payment = input("Do you want to book and pay?(yes/no):")
    if  payment.lower() == "yes":
        booking_datetime = datetime.datetime.now()
        formatted_datetime = booking_datetime.strftime("%Y-%m-%d %H:%M:%S")
        reference_number = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    
    print("Your ticket is booked successfully!")
    print("Total Amount:Rs.", total, "/-")
    print("Booking Date and Time:", formatted_datetime)
    print("Reference Number:", reference_number)
    break

else:
            print("Sorry!,your transaction is cancelled.")
            
       
