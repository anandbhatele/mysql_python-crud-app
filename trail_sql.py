import pymysql
conn=pymysql.connect(
    host="localhost"
    ,user="root"
    ,password="",
    database="trail_sql"
)
cursor=conn.cursor()
while True:
    i=int(input("""
    1.Create DataBase
    2.Create Table
    3.Insert Data
    4.exit
    """))
    
    # if i==1:
    #     sql="create database trail_sql"
    #     try:
    #         cursor.execute(sql)
    #         print("Data Base Create succssessfullyyyy......")
    #     except Exception as a:
    #         print("error...",a)

    if i==2:
        # n=input("enter the table name class:--")
        #students table create--
        sql="create table students (student_id int auto_increment primary key,name varchar(20),age int,course varchar(20))"
        try:
            cursor.execute(sql)
            print("Table created succsses full.......")
        except Exception as e:
            print("error....",e)


            #courses table create--
        
        try:
            sql="create table courses (course_id int auto_increment primary key,course_name varchar(20),duration_years int)"
            cursor.execute(sql)
            print("Table created succsses full.......")
        except Exception as e:
            print("error....",e)


        #subjects table create--
        try:
            sql="create table subjects (subject_id int auto_increment primary key,course_id int ,subject_name varchar(50),FOREIGN KEY(course_id) REFERENCES courses(course_id) )"
            cursor.execute(sql)
            print("Table created succsses full.......")
        except Exception as e:
            print("error....",e)

        #teachers  table create
        
        try:
            sql="create table teachers (teacher_id int auto_increment primary key,name varchar(50) ,subject varchar(50))"
            cursor.execute(sql)
            print("Table created succsses full.......")
        except Exception as e:
            print("error....",e)

            #------------insert data--------------------------------------------------

    if i==3:
        while True:
            n=int(input("""Please Enter The Table Name :--
            1.Add Students
            2.Add Courses
            3.Add Subjects
            4.Show Student List
            5.Show Subjects List
            6.Show Subjects
            7.show Teachers List
            8.exit
            """))


            if n==1:
                try:
                    #students insert data------
                    name=input("Enter the name :--")
                    age=int(input("Enter the age :--"))
                    course=input("Enter the course name :--")
                    sql="insert into students (name,age,course) values (%s,%s,%s)"
                    data=(name,age,course)
                    cursor.execute(sql,data)
                    conn.commit()
                except Exception as a:
                    print("Error...",a)

            
            if n==2:
                try:
                    #courses insert data------
                    Course_name=input("Enter the name :--")
                    Duration_years=int(input("Enter The Duration_years :--"))
                    sql="insert into courses (course_name,duration_years) values (%s,%s)"
                    data=(Course_name,Duration_years)
                    cursor.execute(sql,data)
                    conn.commit()
                except Exception as a:
                    print("Error...",a)

            if n==3:
                try:
                    #subjects insert data------
                    Course_id=int(input("Enter the Course_id :--"))
                    Subject_name=input("Enter The Subject_name :--")
                    sql="insert into subjects (course_id,subject_name) values (%s,%s)"
                    data=(Course_id,Subject_name)
                    cursor.execute(sql,data)
                    conn.commit()
                except Exception as a:
                    print("Error...",a)

            if n==4:
                try:
                    sql="select name,age,course from students"
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    for i in data:
                        print(f"name:{i[0]},age:{i[1]},course:{i[2]}")
                except Exception as a :
                    print("Error....",a)

            if n==5:
                try:
                    sql="select course_name , duration_years from courses"
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    for i in data:
                        print(f"Course name:{i[0]},Duration:{i[1]}")
                except Exception as a :
                    print("Error....",a)

            if n==6:
                try:
                    sql="select course_id ,subject_name from subjects"
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    for i in data:
                        print(f"Course id:{i[0]},subject name:{i[1]}")
                except Exception as a :
                    print("Error....",a)


            if n==7:
                try:
                    sql="select name ,subject from teachers"
                    cursor.execute(sql)
                    data=cursor.fetchall()
                    for i in data:
                        print("Name:{i[0]},subject:{i[1]}")
                except Exception as a :
                    print("Error....",a)
            if n==8:
                break

    if i==4:
        break

            
        

            



