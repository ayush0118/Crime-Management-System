mport datetime
import time
import mysql.connector as sqltor

#TO GET CURRENT DATE AND TIME
now = datetime.datetime.now()
ad=now.strftime("%Y-%m-%d %H:%M")

#TO GENERATE A RANDOM NUMBER TO USE FOR CASE.NO
case_no=int(round(time.time()))

#TO CONNECT MYSQL TO PYTHON
mycon=sqltor.connect(host="localhost",user="root",passwd="Zl18020#",database="crime")
cursor=mycon.cursor()


print("                                                            WELCOME TO COMPLAINT MANAGEMENT SYSTEM                                                             \n")
print("                                                            CURRENT DATE AND TIME : ",ad,"                                                                     \n")

print("1.REGISTRATION OF CASE:")
print("2.FINDING OF CASE:")
print("3.STATUS OF YOUR CASE:")
b=int(input("\n\nENTER YOUR CHOICE:"))


# CREATION OF FUNCTION TO REGISTER YOUR CASE
def crime_registration():
    global case_no
    c=case_no
    n=input("\n\nENTER YOUR NAME:")
    p=int(input("ENTER YOUR PHONE.NO:"))
    y=input("ENTER YOUR ADDRESS:")
    a=input("LOCATION OF INCIDENT:")
    d=input("DESCRIPTION OF INCIDENT:")
    r=input("YOUR RELATION WITH THE INCIDENT:")
    query="Insert into complaint4 values(%s,'%s',%s,'%s','%s','%s','%s')"%(c,n,p,y,a,d,r)
    cursor.execute(query)
    mycon.commit()
    
   
   
    print("\n\nYOUR CASE NUMBER IS",case_no)
    query1="insert into status4 values(%s,'%s','%s')"%(c,"STATION YET TO BE ASSIGNED","JUST REGISTERED")
    cursor.execute(query1)
    mycon.commit()
    return case_no

# CREATION OF FUNCTION TO FIND YOUR CASE
def find_case():
    a=int(input("\n\nENTER YOUR CASE NUMBER:"))
    cursor.execute("SELECT * FROM complaint4 WHERE case_no= {} ".format(a))
    myresult=cursor.fetchall()
    #TO PRINT DETAILS OF YOUR CASE
    for row in myresult:
        print("\n\nDETAILS OF YOUR CASE:\n\n")
        print("1)YOUR NAME:",row[1])
        print("2)YOUR PHONE.NO:",row[2])
        print("3)YOUR ADRESS:",row[3])
        print("4)AREA OF CASE:",row[4])
        print("5)DESCRIPTION OF CASE:",row[5])
        print("6)RELATION WITH THE CASE:",row[6]) 
        return a

#creation of function to view status
def view_case():
    acd=int(input("\n\nENTER YOUR CASE NUMBER:"))
    cursor.execute("SELECT * FROM status4 WHERE caseno= {} ".format(acd))
    myresult4=cursor.fetchall()
    for row4 in myresult4:
        print("\n\nPOLICE STATION ASSIGNED FOR YOUR CASE:",row4[1])
        print("STATUS OF YOUR CASE IS:",row4[2])
    





#CALLING OF CRIME REGISTRATION FUNCTION
if b==1:
    choice="y"
    #TO GIVE USER THE OPTION TO REGISTER ANOTHER CASE
    while choice=="y":
         crime_registration()
         print("\n")
         print("CASE REGISTERED SUCCESSFULLY")
         choice=input("\n\n DO YOU WANT TO REGISTER AN ANOTHER CASE? (y/n)")



#CALLING OF FIND CASE FUNCTION         
elif b==2:
    choice1="y"
    #TO GIVE USER THE OPTION TO FIND ANOTHER CASE
    while choice1=="y":
        find_case()
        print("\n")
        print("TASK SUCCESSFUL\n")
        choice1=input("\n\n DO YOU WANT TO FIND ANOTHER CASE? (y/n)\n")

#CALLING OF STATUS VIEWING FUNCTION
elif b==3:
    choice2='y'
    #FACILITY FOR THE USER TO REPEAT STATUS VIEWING FUNCTION 
    while choice2=="y":
        view_case()
        print("\n")
        print("TASK SUCCESSFUL\n")
        choice2=input("\n\n DO YOU WANT TO VIEW STATUS OF YOUR CASE? (y/n)\n")
    
        


#PART OF CODE FOR THE RECEIVER OR THE POLICE 
elif b==5014:
     print("\n\n                                                         WELCOME TO POLICE DATABASE                                                                  ")
     
     for w in range(0,500):
         for k in range(0,500):
                 x="notbreak"
                 userid=int(input("\n\nPLEASE ENTER STATION ID:"))
                 pwd=input("PLEASE ENTER YOUR PASSWORD:")
             
                 cursor.execute("SELECT * FROM station1 WHERE user_id={}".format(userid))
                 myresult1=cursor.fetchall()
                 for r in myresult1:
                     if r[1]==pwd:
                         print("1.CASE RECORDS")
                         print("2.SPECIFIC CASE DETAILS")
                         print("3.ASSIGNMENT OF CASES")
                         print("4.STATUS UPDATION")
                         x=int(input("ENTER YOUR CHOICE:"))
                     
                         if x==1:
                             cursor.execute("SELECT * FROM complaint4")
                             data=cursor.fetchall()
                             for row1 in data:
                                 print(row1)
                            
                                 
                         elif x==2:
                             for abc in range(0,500):
                                     q=int(input("\n\nENTER YOUR CASE NUMBER:"))
                                     cursor.execute("SELECT * FROM complaint4 WHERE case_no= {} ".format(q))
                                     myresult2=cursor.fetchall()
                                     for row in myresult2:
                                             print("DETAILS OF YOUR CASE:\n")
                                             print("1)YOUR NAME:",row[1])
                                             print("2)YOUR PHONE.NO:",row[2])
                                             print("3)YOUR ADRESS:",row[3])
                                             print("4)AREA OF CASE:",row[4])
                                             print("5)DESCRIPTION OF CASE:",row[5])
                                             print("6)RELATION WITH THE CASE:",row[6])
                                     strn=input("PRESS 'y' TO SEARCH  FOR ANOTHER CASE OR ANY OTHER KEY TO EXIT THE SEARCH")
                                     if strn=='y' or strn=='Y':
                                             print("SEARCHING FOR ANOTHER CASE\n")
                                     else:
                                             print("YOUR RESULT\n")
                                             break
                                 
                         elif x==3:
                              for j  in range(0,500):
                                  m=int(input("\n\nENTER THE CASE NUMBER:"))
                                  o=input("ENTER THE POLICE STATION TO BE ASSIGNED:")
                                  st="UPDATE status4 SET assignment='%s' WHERE caseno='%s' "%(o,m)
                                  cursor.execute(st)
                                  mycon.commit()
                                  str=input("PRESS 'y' TO REPEAT THE PROCESS OR ANY OTHER KEY TO EXIT")
                                  if str=='y' or str=='Y':
                                      print("\n\nASSIGNING FOR A DIFFERENT CASE")
                                  else:
                                      print("ASSIGNED SUCESSFULLY")
                                      break


                         elif x==4:
                              for u in range(0,500):
                                  v=int(input("ENTER THE CASE NUMBER:"))
                                  ab=input("ENTER THE UPDATED STATUS:")
                                  st1="UPDATE status4 SET status='%s' WHERE caseno='%s' "%(ab,v)
                              
                                  cursor.execute(st1)
                                  mycon.commit()
                                  str1=input("PRESS 'y' TO REPEAT THE PROCESS OR ANY OTHER KEY TO EXIT")
                                  if str1=='y' or str1=='Y':
                                      print("\n\n ASSIGNING FOR A DIFFERENT CASE")
                                  else:
                                      print("STATUS UPDATED SUCESSFULLY")
                                      break
            
                        
                         else:
                             print("INVALID INPUT")
                             break
                 
                     else:
                         x="break"
                         print("\n\n YOUR USERNAME OR PASSWORD IS INCORRECT")
                         break

                        
                 x="break"
                 if x=="break":
                     break


         str2=input("PRESS 'y' TO LOGIN AGAIN AND ANY OTHER KEY TO EXIT THE DATABASE")
         if str2=='y' or str2=='Y':
             print("WELCOME BACK")  
         else:
             print("")
             break     

    
 




#TO FILTER OUT UNWANTED INPUT        
else:
    print("\n\nINVALID CHOICE")
    
    



print("\n")
print("                                                                            THANK YOU FOR YOUR TIME                                                      ")



