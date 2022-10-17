from sqlite3 import Cursor
import mysql.connector
#establishing the connection
conn = mysql.connector.connect(
   user='root', password='password', host='127.0.0.1', database='demo'
)
#Creating a cursor object using the cursor() method
cursor = conn.cursor()
def get_department():  
       print('\nDepartment names:');
       cursor.execute("SELECT * from department");
       data = cursor.fetchall()
       for column in data:
              print(column);
       print("enter the department id: ");
       dept = input();
       return dept  
def get_college_info():
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
       return college
def get_collegeDept_info():
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
    return ( insert_data)       
def get_student_info():
    print('\nstudent names with id :');
    cursor.execute('''
SELECT s.id ,s.first_name ,c.id, c.college_name, d.id ,d.name  from student s 
join college_department cd on cd.id = s.dept_id 
join college c on c.id = cd.college_id 
join department d on d.id =cd.dept_id ''');
    data = cursor.fetchall()
    for column in data:
            print(column);
    print("enter the student id: ");
    dept = input();
    return dept       
def college():
    cursor.execute('''
SELECT * from college''');
    data = cursor.fetchall()
    for column in data:
        print(column);       
    print("enter the college id to be changed: ")
    val_1 = int(input()); 
    return val_1       
def delete_data():
       print("deleting a student id")
       cursor.execute('''
       select s.id, s.first_name  from student s order by id asc;''');
       data = cursor.fetchall()
       for column in data:
              print(column);  
       print("enter the student id to be deleted: ")  
       choices = int(input());
       delete_data =  "DELETE FROM student WHERE id = %s "
       cursor.execute(delete_data, [choices])
       return(delete_data);
print("Please select from given option :");
print("a. insert new student details.");
print("b. updating the student name/college_name.");
print("c. Delete the student id ")
choice = input("Enter your choice (a/b/c): ");
#for inserting
if choice == "a":
       #get dept input
        dept = get_department();
       # get college input
        college = get_college_info();   
       # get collgeDeptId
        get_collegeDept_info();
        print("Data inserted")
        conn.commit()
        print(cursor.rowcount, "was inserted.") 
#for updating
elif choice == "b":
       #get std id as input
       get_student_info();
       print("1. Update student name. ");
       print("2. Update student college name. ")
       choice_1 = input();
       if choice_1 == '1':
              print("i. update first_name:");
              print("j. update last_name: ");
              choose = input();
              if choose == "i":
                     print("enter the first_name to be changed: ")
                     val_1 = input();
                     print("enter the id: ")
                     val_2 = int(input());
                     sql = "UPDATE student SET first_name = %s WHERE id = %s"
                     val = (val_1, val_2)
                     cursor.execute(sql, val)
                     conn.commit()
              elif choose == "j":
                     print("enter the last_name to be changed: ")
                     val_1 = input();
                     print("enter the id: ")
                     val_2 = int(input());
                     sql = "UPDATE student SET last_name = %s WHERE id = %s"
                     val = (val_1, val_2)
                     cursor.execute(sql, val)
                     conn.commit()
              else:
                     print("you have entered incorrect choice. ")
       elif choice_1 == "2":
              # choose_1 = input();
              cursor.execute('''
SELECT * from college''');
              data = cursor.fetchall()
              for column in data:
                print(column);       
              print("enter the college id to be changed: ")
              val_1 = int(input());       
              cursor.execute('''
SELECT * from department''');
              data = cursor.fetchall()
              for column in data:
                     print(column);  
              print("enter the department id to be changed: ")  
              val_2 = int(input());
              cursor.execute("""
                     SELECT c.college_name, cd.id  from college_department cd 
       join college c on c.id = cd.college_id 
       where cd.dept_id = %s and cd.college_id = %s;
              """, [val_1, val_2]);
              data = cursor.fetchone()
              collegeDeptId = data[1];
              #inserting values into table
              insert_data= (
              "INSERT INTO student(dept_id)"
              "VALUES (%s)")
              cursor.execute(insert_data, [collegeDeptId])
              print("Data updated")   
#For deleting 
elif choice == "c":
    delete_data();
    print("Data deleted") 
    conn.commit()                   
# #Closing the connection
# conn.close()