source = int(input("Enter your source Station:"))
destination = int(input("Enter your destination Station:"))
if source == 1000 and destination == 1001:
    print("Ticket Fair is Rs.20/person")
elif source == 1002 and destination == 1003:
    print("Ticket Fair is Rs.30/person")
elif source == 1004 and destination == 1005:
    print("Ticket Fair is Rs.60/person")
elif source == 1006 and destination == 1007:
    print("Ticket Fair is Rs.80/person")
elif source == 1009 and destination == 1010:
    print("Ticket Fair is Rs.90/person")
else:
    print("Invalid stations")
member = int(input("How many members? "))
if source == 1000 and destination == 1001:
    fair = 20
elif source == 1002 and destination == 1003:
        fair = 30
elif source == 1004 and destination == 1005:
        fair = 60
elif source == 1006 and destination == 1007:
        fair = 80
elif source == 1009 and destination == 1010:
        fair = 90
print("Total fair is Rs.", fair * member)
payment = input("you want to book and pay? (yes/no): ")
if payment == "yes":
        print("Your ticket is booked successfully!")
else:
        print("Your transaction is cancelled")
