import pandas as pd
import numpy as np
import time
#Guest database
hotel_guest={"NAME":["Ramin Ahmed", "Aman Gupta", "Vineeta Singh", "Namita Thapar", "Anupam Mittal", "Ashneer Grover", "Peyush Bansal", "Ghazal Alagh", "Ranjit Singh", "John Alexander", "Ketan Roy", "Jatin Roy", "Amit Jayan", "Devika Kumar", "Ashwin Ram", "Ram Kapoor", "Nikhil Sharma", "Sanya Singh", "Robin Singh"], "ROOM":[211, 215, 216, 217, 218, 219, 220, 221, 121, 314, 223, 224, 115, 119, 307, 321, 104, 229, 228], "TYPE":["Suite", "Suite", "Suite", "Suite", "Suite", "Suite", "Suite", "Suite", "Single", "Deluxe", "Suite", "Suite", "Single", "Single", "Deluxe", "Deluxe", "Single", "Suite", "Suite"], "STAY":["02/01/2022", "02/01/2022", "02/02/2022", "02/01/2022", "02/01/2022","02/01/2022", "02/01/2022", "02/01/2022", "25/01/2022", "28/01/2022", "25/01/2022", "25/01/2022", "10/01/2022", "14/01/2022", "14/02/2022","09/01/2022", "10/02/2022", "10/01/2022", "10/01/2022"], "END":["02/02/2022", "07/02/2022", "07/02/2022", "07/02/2022", "07/02/2022", "07/02/2022", "07/02/2022", "07/02/2022", "27/02/2022", "01/02/2022", "09/02/2022", "09/02/2022", "15/01/2022", "15/01/2022", "21/02/2022", "11/01/2022", "17/02/2022", "17/02/2022", "17/02/2022"]}
guest=pd.DataFrame(hotel_guest)

#Employee database
hotel_emp={"ECODE":[11, 12, 13, 14, 15, 16, 20, 21, 22, 23, 24, 25, 26, 30, 31, 32, 33, 34, 35, 36, 40, 41, 42, 43, 44, 50, 51, 52, 53, 54, 55, 56, 57, 58],"ENAME":["Tanmay", "Rohit", "Rajesh", "Sam", "Priyanka", "Kavya", "Manav", "Neha", "Mark", "Sabu", "Amit", "Ranjan", "Bobby", "Mohit", "Ram", "Saurab", "Sonam", "Arjun", "Mansi", "Bhushan", "Kirti", "Micheal", "Sam", "Robin", "Chetna", "Bhavya", "Shruti", "Aman", "Jeet", "Ritik", "Manasvi", "Saraansh", "Raghu", "Sanya"], "DEPT": ["Front Desk", "Front Desk", "Front Desk", "Front Desk", "Front Desk", "Front Desk", "Admin", "Admin", "Admin", "Admin", "Admin", "Admin", "Admin", "Service", "Service", "Service", "Service", "Service", "Service", "Service", "Kitchen", "Kitchen", "Kitchen", "Kitchen", "Kitchen", "IT & Network", "IT & Network", "IT & Network", "IT & Network", "IT & Network", "IT & Network", "IT & Network", "IT & Network", "IT & Network"]}
emp=pd.DataFrame(hotel_emp)

#Application Start
print('***Welcome To Hotel Management System***')
print()
def menu():
    print('''What would like to do?

1-Check Rooms Occupied
2-Employees Present
3-New Check in
4-Remove Guest''')
print()

#Taking Input for the desired operation to be done
menu()
a=int(input("Please Enter your desired option-"))
while a !=0:
    if a==1:
        total_rooms=len(guest)
        print(total_rooms, "are currently occupied of the total 50")
        print()
        time.sleep(2)
        print("Go back to menu? Y/N")
        b=input("")
        #Returning back to the menu screen
        menu()
        a=int(input("Please enter your desired option: "))
        print()
        time.sleep(2)
   
    elif a==2:
        total_emp=len(emp)
        print(total_emp, "are present today.")
        print()
        time.sleep(2)
        print("Go back to menu? Y/N")
        b=input("")
        menu()
        a=int(input("Please enter your desired option: "))
        print()
        time.sleep(2)
    elif a==3:
        name=input("Enter Guest Name= ")
        typ=input("Enter room type= ")
        start=input("Enter Check in date= ")
        end=input("Enter check out date= ")
        num=input("Enter Room no= ")
        #Placing the input given by the user to add to the database
        df2 = {'NAME': name, "ROOM":num, "TYPE": typ, "STAY":start, "END":end}
        guest=guest.append(df2, ignore_index = True)
        #Printing the updated guestlist to see if the changes have taken place
        print("UPDATED GUESTLIST")
        print(guest)
        print()
        time.sleep(2)
        print("Go back to menu? Y/N")
        b=input("")
        menu()
        a=int(input("Please enter your desired option: "))
        print()
        time.sleep(2)
    elif a==4:
        nam=int(input("Enter guest no: "))
        guest.drop(1)
        print(guest)
        print()
        time.sleep(2)
        print("Go back to menu? Y/N")
        b=input("")
        menu()
        a=int(input("Please enter your desired option: "))
        print()
        time.sleep(2)
    else:
        print("WRONG INPUT, Please try Again")
        print()
        time.sleep(2)
        menu()
        a=int(input("Please enter your desired option: "))
        print()
    
