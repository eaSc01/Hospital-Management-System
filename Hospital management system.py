import mysql.connector as c

con=c.connect(host="localhost",
              user="root",
              passwd=input("ENTER YOUR MYSQL PASSWORD:"),
              database="hospital_management")

#ENTER YOUR HOST, USER & PASSWORD ABOVE!
# A database named as "hospital_management" must be already created before running this code!
# with following tables= STAFF, patients, AMBULANCES.

#built on Python IDLE 3.10.2 AND MySQL 8.0


#WELCOME TO HOSPITAL MANAGEMENT SYSTEM
#TERM-II PROJECT


print("HOSPITAL MANAGEMENT 1.0\nHERE YOU CAN ADD, EDIT AND FETCH DATA OF OUR HOSPITAL\n_\n")

print("ENTER COMMAND\nENTER 1 TO ADD, FETCH or EDIT STAFF ENTERIES\nENTER 2 TO ADD, FETCH or EDIT PATIENT ENTERIES\nENTER 3 TO ADD, FETCH or EDIT AMBULANCE ENTERIES\nENTER 4 TO CLOSE PROGRAM\n\nENTER 0 TO OPEN UPDATE LOGS\nwaiting for your command...")

cursor=con.cursor()
ch=int(input("ENTER YOUR COMMAND:"))
#STAFF
if ch==1:
    print("ENTER COMMAND\nENTER 1 TO ADD NEW STAFF ENTERIES\nENTER 2 TO EDIT EXISTING STAFF ENTERIES\nENTER 3 TO DELETE EXISTING STAFF ENTERIES\nENTER 4 TO FETCH DATA FROM ENTERIES\n\nwaiting for your command...")
    a=int(input("ENTER YOUR COMMAND:"))
    if a==1:
        while True:
            print("PLEASE ENTER THE FOLLOWING DETAILS OF NEW STAFF")
            ID=int(input("ENTER STAFF ID:"))
            Name=input("ENTER NAME:")
            FNAME=input("ENTER FATHER'S NAME:")
            Date_of_joining=input("ENTER DATE OF JOINING (DD/MM/YYYY):")
            Designation=input("ENTER DESIGNATION:")
            Salary=int(input("ENTER SALARY:"))
            DOB=input("ENTER DATE OF BIRTH (DD/MM/YYYY):")
            NATIONALITY=input("ENTER NATIONALITY:")
            CONTACT=input("ENTER E-MAIL OR CONTACT NUMBER:")
            query="Insert into staff values({},'{}','{}','{}','{}',{},'{}','{}','{}')".format(ID,Name,FNAME,Date_of_joining,Designation,Salary,DOB,NATIONALITY,CONTACT)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                    print("DATA ADDED SUCCESSFULLY!")
            else:
                print("COMMAND FAILED, maybe length too long to be addressed")
            x=int(input("ENTER 1 TO ADD MORE ENTERIES\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
            if x==2:
                  break
    elif a==2:
        print("ENTER THE DATA FIELD YOU WANT TO EDIT\nENTER 1 TO EDIT NAME\nENTER 2 TO EDIT FATHER'S NAME\nENTER 3 TO EDIT D.O.J\nENTER 4 TO EDIT DESIGNATION\nENTER 5 TO EDIT SALARY\nENTER 6 TO EDIT D.O.B\nENTER 7 TO EDIT NATIONALITY\nENTER 8 TO EDIT CONTACT\n\nwaiting for your command...")
        b=int(input("ENTER YOUR COMMAND:"))
        if b==1:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                ID=int(input("ENTER STAFF ID:"))
                Name=input("ENTER NAME:")
                query="update staff set Name='{}' where ID={}".format(Name,ID)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE NAMES OF STAFF(s)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==2:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                ID=int(input("ENTER STAFF ID:"))
                FNAME=input("ENTER FATHER'S NAME:")
                query="update staff set FNAME='{}' where ID={}".format(FNAME,ID)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE FATHER'S NAMES OF STAFF(s)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==3:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                ID=int(input("ENTER STAFF ID:"))
                Date_of_joining=input("ENTER DATE (DD/MM/YYYY):")
                query="update staff set Date_of_joining='{}' where ID={}".format(Date_of_joining,ID)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE DATES OF STAFF(S)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==4:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                ID=int(input("ENTER STAFF ID:"))
                Designation=input("ENTER DESIGNATION:")
                query="update staff set Designation='{}' where ID={}".format(Designation,ID)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE DESIGNATION OF STAFF(S)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==5:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                ID=int(input("ENTER STAFF ID:"))
                Salary=input("ENTER SALARY:")
                query="update staff set Salary='{}' where ID={}".format(Salary,ID)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE SALARIES OF STAFF(S)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==6:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                ID=int(input("ENTER STAFF ID:"))
                DOB=input("ENTER DOB:")
                query="update staff set DOB='{}' where ID={}".format(DOB,ID)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE DOB OF STAFF(S)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==7:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                ID=int(input("ENTER STAFF ID:"))
                NATIONALITY=input("ENTER NATIONALITY:")
                query="update staff set Name='{}' where ID={}".format(NATIONALITY,ID)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE NATIONALITY OF STAFF(s)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==8:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                ID=int(input("ENTER STAFF ID:"))
                CONTACT=input("ENTER CONTACT:")
                query="update staff set Name='{}' where ID={}".format(CONTACT,ID)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE CONTACTS OF STAFF(s)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break

    elif a==3:
        while True:
            print("PLEASE ENTER THE FOLLOWING DETAILS")
            ID=int(input("ENTER STAFF ID:"))
            query="delete from staff where ID={}".format(ID)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("DATA DELETED SUCCESSFULLY!")
            else:
                print("DATA NOT FOUND")
            x=int(input("ENTER 1 TO DELETE MORE STAFF RECORDS\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
            if x==2:
                break
    elif a==4:
        print("ENTER COMMAND\nENTER 1 TO FETCH DATA OF SPECIFIC PERSON\nENTER 2 TO FETCH DATA OF ENTIRE STAFF\n\nwaiting for your command...")
        c=int(input("ENTER YOUR COMMAND:"))
        if c==1:
            while True:
                print("ENTER THE FOLLOWING TO FETCH DATA")
                ID=int(input("ENTER STAFF ID TO BE FETCHED:"))
                query="select*from STAFF where ID={}".format(ID)
                cursor.execute(query)
                data=cursor.fetchone()
                print(data)
                if cursor.rowcount>0:
                    print("DATA FETCHED SUCCESSFULLY!")
                else:
                    print("DATA NOT FOUND")
                print("TOTAL NUMBER OF ROWS=",cursor.rowcount)
                x=int(input("ENTER 1 TO FETCH MORE DATA\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif c==2:
            while True:
                query="select*from STAFF"
                cursor.execute(query)
                data=cursor.fetchall()
                print(data)
                if cursor.rowcount>0:
                    print("DATA FETCHED SUCCESSFULLY!")
                else:
                    print("DATA NOT FOUND")
                print("TOTAL NUMBER OF ROWS=",cursor.rowcount)
                x=int(input("ENTER 1 TO FETCH MORE DATA\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
       
            
        
        
#*******************************************************************************************************************************************************************************************************************************

#PATIENTS

elif ch==2:
    print("ENTER COMMAND\nENTER 1 TO ADD NEW PATIENTS ENTERIES\nENTER 2 TO EDIT EXISTING PATIENTS ENTERIES\nENTER 3 TO DELETE EXISTING PATIENTS ENTERIES\nENTER 4 TO FETCH PATIENT'S DATA\n\nwaiting for your command...")
    a=int(input("ENTER YOUR COMMAND:"))
    if a==1:
        while True:
            print("PLEASE ENTER THE FOLLOWING DETAILS OF NEW PATIENT")
            PIT=int(input("ENTER PATIENT ID:"))
            NAME=input("ENTER NAME:")
            FNAME=input("ENTER FATHER'S NAME:")
            HEALTH_ISSUE=input("ENTER HEALTH ISSUE OF PATIENT:")
            DURATION=int(input("ENTER PATIENT'S TOTAL DURATION (IN DAYS) IN HOSPITAL:"))
            STATUS=input("ENTER STATUS OF PATIENT:")
            CONTACT=input("ENTER E-MAIL OR CONTACT NUMBER:")
            NATIONALITY=input("ENTER NATIONALITY:")
            DOB=input("ENTER DATE OF BIRTH:")
            BILL=int(input("ENTER TOTAL CHARGES TO BE PAID:"))
            query="Insert into patients values({},'{}','{}','{}',{},'{}','{}','{}','{}',{})".format(PIT,NAME,FNAME,HEALTH_ISSUE,DURATION,STATUS,CONTACT,NATIONALITY,DOB,BILL)
            cursor.execute(query)
            con.commit()
            print("DATA INSERTED SUCCESFULLY!")
            if cursor.rowcount>0:
                    print("DATA ADDED SUCCESSFULLY!")
            else:
                print("COMMAND FAILED, maybe length too long to be addressed")
            x=int(input("ENTER 1 TO ADD MORE ENTERIES\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
            if x==2:
                  break
            
    elif a==2:
        print("ENTER THE DATA FIELD YOU WANT TO UPDATE\nENTER 1 TO UPDATE NAME\nENTER 2 TO UPDATE FATHER'S NAME\nENTER 3 TO UPDATE HEALTH ISSUE\nENTER 4 TO UPDATE DURATION\nENTER 5 TO UPDATE STATUS\nENTER 6 TO UPDATE CONTACT\nENTER 7 TO UPDATE NATIONALITY\nENTER 8 TO UPDATE DOB\nENTER 9 TO UPDATE BILLS\n\nwaiting for your command...")
        b=int(input("ENTER YOUR COMMAND:"))
        if b==1:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                PIT=int(input("ENTER PATIENT ID:"))
                NAME=input("ENTER NAME:")
                query="update patients set NAME='{}' where PIT={}".format(NAME,PIT)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE NAMES OF PATIENT(s)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==2:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                PIT=int(input("ENTER PATIENT ID:"))
                FNAME=input("ENTER FATHER'S NAME:")
                query="update patients set FNAME='{}' where PIT={}".format(FNAME,PIT)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE FATHER'S NAMES OF PATIENT(s)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==3:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                PIT=int(input("ENTER PATIENT ID:"))
                HEALTH_ISSUES=input("ENTER HEALTH ISSUE:")
                query="update patients set HEALTH_ISSUES='{}' where PIT={}".format(HEALTH_ISSUES,PIT)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE HEALTH_ISSUES OF PATIENT(S)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==4:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                PIT=int(input("ENTER PATIENT ID:"))
                DURATION=int(input("ENTER DURATION (WEEKS, ENTER NUMBER ONLY!):"))
                query="update patients set DURATION='{}' where PIT={}".format(DURATION,PIT)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE DURATION OF PATIENT(S)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==5:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                PIT=int(input("ENTER PATIENT ID:"))
                STATUS=input("ENTER PATIENTS'S STATUS:")
                query="update patients set STATUS='{}' where PIT={}".format(STATUS,PIT)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE STATUS OF PATIENT(S)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==6:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                PIT=int(input("ENTER PATIENT ID:"))
                CONTACT=input("ENTER CONTACT (E-MAIL OR CONTACT NUMBER):")
                query="update patients set Name='{}' where PIT={}".format(CONTACT,PIT)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE CONTACTS OF PATIENT(s)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==7:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                PIT=int(input("ENTER PATIENT ID:"))
                NATIONALITY=input("ENTER NATIONALITY:")
                query="update patients set Name='{}' where PIT={}".format(NATIONALITY,PIT)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE NATIONALITY OF PATIENT(s)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==8:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                PIT=int(input("ENTER PATIENT ID:"))
                DOB=input("ENTER DOB: (DD/MM/YYYY)")
                query="update patients set DOB='{}' where PIT={}".format(DOB,PIT)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE DOB OF PATIENT(S)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==9:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                PIT=int(input("ENTER PATIENT ID"))
                BILL=int(input("ENTER TOTAL CHARGES NEED TO BE PAID"))
                query="update patients set BILL={} where PIT={}".format(BILL,PIT)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE DOB OF PATIENT(S)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
            
    elif a==3:
        while True:
            print("PLEASE ENTER THE PATIENT ID TO DELETE...")
            PIT=int(input("ENTER PATIENT ID:"))
            query="delete from patients where PIT={}".format(PIT)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("DATA DELETED SUCCESSFULLY!")
            else:
                print("DATA NOT FOUND")
            x=int(input("ENTER 1 TO DELETE MORE RECORDS OF PATIENT(S)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
            if x==2:
                break

    elif a==4:
        print("ENTER COMMAND\nENTER 1 TO FETCH DATA OF SPECIFIC PATIENT\nENTER 2 TO FETCH DATA OF ALL PATIENTS\n\nwaiting for your command...")
        c=int(input("ENTER YOUR COMMAND:"))
        if c==1:
            while True:
                print("ENTER THE FOLLOWING TO FETCH DATA")
                PIT=int(input("ENTER PATIENT ID TO BE FETCHED:"))
                query="select*from patients where PIT={}".format(PIT)
                cursor.execute(query)
                data=cursor.fetchone()
                print(data)
                if cursor.rowcount>0:
                    print("DATA FETCHED SUCCESSFULLY!")
                else:
                    print("DATA NOT FOUND")
                print("TOTAL NUMBER OF ROWS=",cursor.rowcount)
                x=int(input("ENTER 1 TO FETCH MORE DATA\nENTER 2 TO EXIT\nENTER COMMAND:"))
                if x==2:
                    break
        elif c==2:
            while True:
                query="select*from patients"
                cursor.execute(query)
                data=cursor.fetchall()
                print(data)
                if cursor.rowcount>0:
                    print("DATA FETCHED SUCCESSFULLY!")
                else:
                    print("DATA NOT FOUND")
                print("TOTAL NUMBER OF ROWS=",cursor.rowcount)
                x=int(input("ENTER 1 TO FETCH MORE DATA\nENTER 2 TO EXIT\nENTER COMMAND:"))
                if x==2:
                    break

#*******************************************************************************************************************************************************************************************************************************************

#AMBULANCES

elif ch==3:
    print("ENTER COMMAND\nENTER 1 TO ADD NEW AMBULANCE ENTERIES\nENTER 2 TO EDIT EXISTING AMBULANCE ENTERIES\nENTER 3 TO DELETE EXISTING AMBULANCE ENTERIES\nENTER 4 TO FETCH AMBULANCE DATA\n\nwaiting for your command...")
    a=int(input("ENTER YOUR COMMAND:"))
    if a==1:
        while True:
            print("PLEASE ENTER THE FOLLOWING DETAILS OF NEW AMBULANCE")
            ANO=int(input("ENTER AMBULANCE NUMBER:"))
            VEHICLE_NUMBER=input("ENTER VEHICLE_NUMBER:")
            CAPACITY=int(input("ENTER MAXIMUM CAPACITY OF AMBULANCE CAN CARRY:"))
            FACILITIES=input("ENTER FACILITIES:")
            query="Insert into AMBULANCES values({},'{}',{},'{}')".format(ANO,VEHICLE_NUMBER,CAPACITY,FACILITIES)
            cursor.execute(query)
            con.commit()
            print("DATA INSERTED SUCCESFULLY!")
            if cursor.rowcount>0:
                    print("DATA ADDED SUCCESSFULLY!")
            else:
                print("COMMAND FAILED, maybe length too long to be addressed")
            x=int(input("ENTER 1 TO ADD MORE ENTERIES\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
            if x==2:
                  break
    elif a==2:
        print("ENTER THE DATA FIELD YOU WANT TO EDIT\nENTER 1 TO UPDATE VEHICLE_NUMBER\nENTER 2 TO UPDATE CAPACITY\nENTER 3 TO UPDATE FACILITIES\n\nwaiting for your command...")
        b=int(input("ENTER YOUR COMMAND:"))
        if b==1:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                ANO=int(input("ENTER AMBULANCE NUMBER:"))
                VEHICLE_NUMBER=input("ENTER VEHICLE NUMBER:")
                query="update AMBULANCES set VEHICLE_NUMBER='{}' where ANO={}".format(VEHICLE_NUMBER,ANO)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE AMBULANCE ENTRIES(s)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==2:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                ANO=int(input("ENTER AMBULANCE NUMBER:"))
                CAPACITY=int(input("ENTER CAPACITY:"))
                query="update AMBULANCES set CAPACITY='{}' where ANO={}".format(CAPACITY,ANO)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE CAPACITY OF AMBULANCE(S)\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif b==3:
            while True:
                print("PLEASE ENTER THE FOLLOWING DETAILS")
                ANO=int(input("ENTER AMBULANCE NUMBER:"))
                FACILITIES=input("ENTER FACILITIES:")
                query="update AMBULANCES set FACILITIES='{}' where ANO={}".format(FACILITIES,ANO)
                cursor.execute(query)
                con.commit()
                if cursor.rowcount>0:
                    print("DATA UPDATED SUCCESSFULLY!")
                else:
                    print("NO DATA FOUND")
                x=int(input("ENTER 1 TO UPDATE MORE AMBULANCE FACILITIES\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break

    elif a==3:
        while True:
            print("ENTER AMBULANCE NUMBER TO DELETE")
            ANO=int(input("AMBULANCE NUMBER:"))
            query="delete from AMBULANCES where ANO={}".format(ANO)
            cursor.execute(query)
            con.commit()
            if cursor.rowcount>0:
                print("DATA DELETED SUCCESSFULLY!")
            else:
                print("DATA NOT FOUND")
            x=int(input("ENTER 1 TO DELETE MORE AMBULANCE RECORDS\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
            if x==2:
                break

    elif a==4:
        print("ENTER COMMAND\nENTER 1 TO FETCH DATA OF SPECIFIC AMBULANCE\nENTER 2 TO FETCH DATA OF ALL AMBULANCES\n\nwaiting for your command...")
        c=int(input("ENTER YOUR COMMAND:"))
        if c==1:
            while True:
                print("ENTER THE FOLLOWING TO FETCH DATA")
                ANO=int(input("ENTER AMBULANCE NUMBER TO BE FETCHED:"))
                query="select*from ambulances where ANO={}".format(ANO)
                cursor.execute(query)
                data=cursor.fetchone()
                print(data)
                if cursor.rowcount>0:
                    print("DATA FETCHED SUCCESSFULLY!")
                else:
                    print("DATA NOT FOUND")
                print("TOTAL NUMBER OF ROWS=",cursor.rowcount)
                x=int(input("ENTER 1 TO FETCH MORE DATA\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break
        elif c==2:
            while True:
                query="select*from ambulances"
                cursor.execute(query)
                data=cursor.fetchall()
                print(data)
                if cursor.rowcount>0:
                    print("DATA FETCHED SUCCESSFULLY!")
                else:
                    print("DATA NOT FOUND")
                print("TOTAL NUMBER OF ROWS=",cursor.rowcount)
                x=int(input("ENTER 1 TO FETCH MORE DATA\nENTER 2 TO EXIT\n\nENTER COMMAND:"))
                if x==2:
                    break



#*******************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************************

elif ch==4:
    print("PROGRAM CLOSED")
    exit()

elif ch==0:
    print("HMS UPDATE LOG\n\n'VERSION 1.0'=\nLAUNCHED ON 7 MARCH 2022\nFIRST VERSION OF HMS PROGRAM\nWAS ABLE TO ADD\EDIT\DELETE ENTERIES FROM DATA\n\n'VERSION 1.1'=\nLAUNCHED ON 8 MARCH 2022\nADDED FETCH DATA FEATURE\nVARIOUS BUGS FIXED\nADDED QUIT FEATURE\n\n'VERSION 1.2'=\nLAUNCHED ON 9 MARCH 2022\nADDED MYSQL PASSWORD FEATURE\nVARIOUS BUGS FIXED\n\n'VERSION 1.3'=\nLAUNCHED ON 12 MARCH 2022\nVARIOUS BUGS FIXED AND IMPROVED PROGRAM\n\n'VERSION 1.4'=\nLAUNCHED ON 14 MARCH 2022\nVARIOUS BUGS FIXED AND IMPROVED PROGRAM\n\n'VERSION 1.5'=\nLAUNCHED ON 22 MARCH 2022\nVARIOUS BUGS FIXED AND IMPROVED PROGRAM\n\n'VERSION 1.6'=\nLAUNCHED ON 31 MARCH 2022\nVARIOUS BUGS FIXED AND IMPROVED PROGRAM\n\nVERSION 1.7'=\nLAUNCHED ON 2 APRIL 2022\nADDED UPDATE LOG\nVARIOUS BUGS FIXED AND IMPROVED PROGRAM\n\n")
    x=int(input("ENTER ANY NUMBER TO QUIT:"))
    if x==int:
        exit()
else:
    print("INVALID COMMAND")

#_______________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________
#-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

#END OF FILE

