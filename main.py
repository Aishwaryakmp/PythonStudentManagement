# create database connection

# endless while loop
    # get user input choice (1 insert, 2 view....)
    #  get user inputs 
    
    
from sqlite3 import Cursor
import mysql.connector

#establishing the connection
conn = mysql.connector.connect(
   user='root', password='password', host='127.0.0.1', database='demo'
)

#Creating a cursor object using the cursor() method
cursor = conn.cursor()

# #Dropping EMPLOYEE table if already exists.
# cursor.execute("DROP TABLE IF EXISTS EMPLOYEE")

# #Creating table as per requirement
# sql ='''CREATE TABLE EMPLOYEE(
#    FIRST_NAME CHAR(20) NOT NULL,
#    LAST_NAME CHAR(20),
#    AGE INT,
#    SEX CHAR(1),
#    INCOME FLOAT
# )'''
# cursor.execute(sql)

# query= "SELECT first_name FROM student"
# cursor.execute(query)
       
# names = cursor.fetchall()
# for first_name in names:
#     print(first_name)

# cursor.execute("SHOW TABLES")

# for student in cursor:
#        print(student)
print("Please select from given option :");
print("a. insert new student details.");
print("b. updating the student name/college_name.");
print("c. Delete the student id ")
choice = input("Enter your choice (a or b): ");
#for inserting
if choice == "a":
       #get dept input
       print('\nDepartment names:');
       cursor.execute("SELECT * from department");
       data = cursor.fetchall()
       for column in data:
              print(column);
       print("enter the department id: ");
       dept = input();

       # get college input
       print('\College names:');
       cursor.execute("""
                      SELECT c.id , c.college_name  from college_department cd 
       join college c on c.id = cd.college_id 
       where cd.dept_id = %s;
              """, [dept]);
       data = cursor.fetchall()
       for column in data:
              print(column);
       print("enter the college id: ");
       college = input();
       # get collgeDeptId
       cursor.execute("""
                      SELECT c.college_name, cd.id  from college_department cd 
       join college c on c.id = cd.college_id 
       where cd.dept_id = %s and cd.college_id = %s;
              """, [dept, college]);
       data = cursor.fetchone()
       collegeDeptId = data[1];
       #inserting values into table
       insert_data= (
       "INSERT INTO student(first_name, last_name, dept_id)"
       "VALUES (%s, %s, %s)"
       )
       print("Enter the first_name : ");
       a =  input();
       print("Enter the last_name : ");
       b = input();
       cursor.execute(insert_data, [a,b,collegeDeptId])
       print("Data inserted")
       conn.commit()
       print(cursor.rowcount, "was inserted.") 
                     
# #for updating
# # //display std id with name then get id as ip from user and then ask option like name or college if name ask for ip from user 1st name and last name if college means 1st step like display college name and college id and then usin that delete it
# elif choice == "b":
#        #get std id as input
#        print('\nstudent names with id :');
#        cursor.execute('''
# SELECT s.id ,s.first_name ,c.id, c.college_name, d.id ,d.name  from student s 
# join college_department cd on cd.id = s.dept_id 
# join college c on c.id = cd.college_id 
# join department d on d.id =cd.dept_id ''');
#        data = cursor.fetchall()
#        for column in data:
#               print(column);
#        print("enter the student id: ");
#        dept = input();
#        print("1. Update student name. ");
#        print("2. Update student college name. ")
#        choice_1 = input();
#        if choice_1 == '1':
#               print("i. update first_name:");
#               print("j. update last_name: ");
#               choose = input();
#               if choose == "i":
#                      print("enter the first_name to be changed: ")
#                      val_1 = input();
#                      print("enter the id: ")
#                      val_2 = int(input());
#                      sql = "UPDATE student SET first_name = %s WHERE id = %s"
#                      val = (val_1, val_2)
#                      cursor.execute(sql, val)
#                      conn.commit()
#               elif choose == "j":
#                      print("enter the last_name to be changed: ")
#                      val_1 = input();
#                      print("enter the id: ")
#                      val_2 = int(input());
#                      sql = "UPDATE student SET last_name = %s WHERE id = %s"
#                      val = (val_1, val_2)
#                      cursor.execute(sql, val)
#                      conn.commit()
#               else:
#                      print("you have entered incorrect choice. ")
#        elif choice_1 == "2":
#               print("i. Changing college name. ")
#               print("j. Changing college department. ")
              
                                

#Closing the connection
conn.close()