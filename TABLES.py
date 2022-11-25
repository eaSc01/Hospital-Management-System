import mysql.connector as c

con=c.connect(host="localhost",
              user="root",
              passwd=input("ENTER YOUR MYSQL PASSWORD:"),
              database="hospital_management")

cursor=con.cursor()

a=int(input("TABLE CREATER 1.1\nENTER COMMAND\nENTER 1 TO CREATE TABLES\nENTER 2 TO DELETE TABLES\nENTER 3 TO QUIT\n\nENTER 4 FOR UPDATE LOG\nwaiting for command\n\nENTER COMMAND:"))
if a==1:
    t1=int(input("THIS PROGRAM CREATES MYSQL TABLES\nENTER 1 TO CREATE STAFF TABLE\nENTER 2 TO CREATE PATIENTS TABLE\nENTER 3 TO CREATE AMBULANCE TABLE\nwaiting for your command\n\nENTER YOUR COMMAND:"))
    if t1==1:
        query="CREATE TABLE STAFF(ID integer PRIMARY KEY,Name varchar(100),FNAME varchar(100),Date_of_joining varchar(10),Designation varchar(100),Salary integer,DOB varchar(100),NATIONALITY varchar(100),CONTACT varchar(100))"
        cursor.execute(query)
        con.commit()
        print("STAFF TABLE CREATED SUCCESSFULLY!")
    elif t1==2:
        query="CREATE TABLE patients(PIT integer PRIMARY KEY,NAME varchar(100),FNAME varchar(100),HEALTH_ISSUE varchar(100),DURATION integer,STATUS varchar(100),CONTACT varchar(100),NATIONALITY varchar(100),DOB varchar(10),BILL integer)"
        cursor.execute(query)
        con.commit()
        print("PATIENTS TABLE CREATED SUCCESSFULLY!")
    elif t1==3:
        query="CREATE TABLE AMBULANCES(ANO integer PRIMARY KEY,VEHICLE_NUMBER varchar(100),CAPACITY integer,FACILITIES varchar(100))"
        cursor.execute(query)
        con.commit()
        print("AMBULANCE TABLE CREATED SUCCESSFULLY!")
    else:
        print("INVALID COMMAND")
    
elif a==2:
    d1=int(input("THIS PROGRAM DELETES MYSQL TABLES\nENTER 1 TO DELETE STAFF TABLE\nENTER 2 TO DELETE PATIENTS TABLE\nENTER 3 TO DELETE AMBULANCE TABLE\nwaiting for your command\n\nENTER YOUR COMMAND:"))
    if d1==1:
        query="DROP TABLE STAFF"
        cursor.execute(query)
        con.commit()        
        print("DATA DELETED SUCCESSFULLY!")
    elif d1==2:
        query="DROP TABLE patients"
        cursor.execute(query)
        con.commit()
        print("DATA DELETED SUCCESSFULLY!")
    elif d1==3:
        query="DROP TABLE AMBULANCES"
        cursor.execute(query)
        con.commit()
        print("DATA DELETED SUCCESSFULLY!")
    else:
        print("INVALID COMMAND")

elif a==3:
    exit()

elif a==4:
    print("VERSION 1.0\nLAUNCHED ON 7 MARCH 2022\nFIRST VERSION OF THE TABLE CREATER\nABLE TO CREATE AND DELETE STAFF/PATIENTS/AMBULANCES TABLES\n\nVERSION 1.1\nLAUNCHED ON 2 APRIL 2022\nUPDATED CHARACTER SIZE OF COLUMNS TO '100'\nADDED UPDATE LOG\nBUGS FIXED")
    x=int(input("ENTER ANY NUMBER TO QUIT:"))
    if x==int:
        exit()
else:
    print("INVALID COMMAND")

#______________________________________________________________________________________________________________________________________________________________________________________________________________________________
#END OF FILE    
    
    

   
