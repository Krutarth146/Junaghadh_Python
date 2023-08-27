import mysql.connector

mydb = mysql.connector.connect(user = 'root', password = 'mysql', host = 'localhost', database='dktv')

if(mydb.is_connected()):
    print("Connection Established")
else:
    print("Not Connected")
# print(mydb)  # <mysql.connector.connection_cext.CMySQLConnection object at 0x0000020824F224A0>
cur = mydb.cursor()

# cur.execute("CREATE DATABASE shilp")

# cur.execute("CREATE TABLE  students(name varchar(20), roll int(4), marks float(3))")

# cur.execute("CREATE TABLE sample(name varchar(20), roll int(4), salary decimal(5,3), comment varchar(100))")
# cur.execute("CREATE TABLE sample1(id int(4) AUTO_INCREMENT NOT NULL, name varchar(20) NOT NULL, roll int(4), salary decimal(5,3), comment varchar(100), PRIMARY KEY (id))")
# cur.execute("CREATE TABLE sample2(id int(4) AUTO_INCREMENT NOT NULL, name varchar(20) NOT NULL, roll int(4), CONSTRAINT INAME PRIMARY KEY (id,name))")
# cur.execute("ALTER TABLE sample ADD PRIMARY KEY (roll)")
# cur.execute("ALTER TABLE sample drop PRIMARY KEY")
# cur.execute("ALTER TABLE sample2 drop COnstraint INAME")


# cur.execute("CREATE TABLE PERSON(PERSON_ID INT(10) NOT NULL ,NAME VARCHAR(30) NOT NULL, AGE INT(4) NOT NULL, GENDER VARCHAR(10) NOT NULL, EMAIL VARCHAR(90), PRIMARY KEY (PERSON_ID))")
# cur.execute("create table cust (id int, name varchar(20))")

# qu1 = "insert into cust values(%s, %s)"
# val = (1, "Dhruv")
# cur.execute(qu1, val)

# cur.execute("CREATE TABLE CUST_DETAILS(ID int AUTO_INCREMENT NOT NULL,NAME VARCHAR(50) NOT NULL, MOB_NUMBER int NOT NULL, SUBS_END DATE NOT NULL, JOIN_DATE DATE NOT NULL, PASSWORD varchar(15) NOT NULL, GENDER varchar(10), PRIMARY KEY(ID,NAME))")
# import date class
from datetime import date
# extract current local date
# today1 = date.today()

# name=input("Enter Full Name:")
# number=int(input("Enter Mobile number"))
# joining= today1
# password=input("Enter Password:")
# gender=input("Enter Gender M/F/O:")
cur.execute("SELECT DATE_FORMAT(DATE_ADD(SYSDATE(), INTERVAL 1 YEAR)) FROM DUAL")
subscription=cur.fetchone()
print(subscription)
subscription = subscription[0]
# print(subscription)
# que="INSERT INTO CUST_DETAILS (ID,NAME,MOB_NUMBER,SUBS_END,JOIN_DATE,PASSWORD,Gender)VALUES(%s,%s,%s,%s,%s,%s,%s)"
# val=['1',name,number,subscription,joining,password,gender]

# -----------------------------------------------

cur.execute("SELECT NAME, SALARY FROM SAMPLEL")
record = cur.fetchone()

print(record)
print(record[0])



# -----------------------------------------------



from datetime import datetime
now = datetime.now()
# id = 1
print(now)

# cur.execute(que,(1,name,number,formatted_date,joining,password,gender))
# cur.execute("CREATE TABLE AADHAR(AADHAR_ID INT(10) NOT NULL, A_NAME VARCHAR(30) NOT NULL, PERSON_ID INT, PRIMARY KEY (AADHAR_ID), FOREIGN KEY (PERSON_ID) REFERENCES PERSON(PERSON_ID))")


# S = "INSERT INTO PERSON (PERSON_ID, NAME, AGE, GENDER, EMAIL) VALUES (%s, %s , %s, %s, %s)"
# dk = (20, "Dev", 45, "male", "123")


# S = "INSERT INTO AADHAR VALUES (%s, %s, %s)"
# dk = (33333, "Manoj", 20)

# cur.execute(S,dk)

# mydb.commit()



# S = "INSERT INTO sample2 VALUES (%s, %s, %s)"
# dk = (2, "Manoj", 10)

# cur.execute(S,dk)

# mydb.commit()



# a = 1290070078170102666248196035845070394933441741644993085810116441344597492642263849

# num = 3
# c = 1
    
# while a != num:
#     c+=1
#     a = a // num
#     # print(a)

# print(c)

# 47. Write a Python program to filter for numbers in a given list whose sum of digits is > 0, where the first digit can be negative.

