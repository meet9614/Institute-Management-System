import pymysql as sql

try:
    # Connect to the database
    mydb = sql.connect(host="localhost", user="root", password="8617572956", database="db1")
    cur = mydb.cursor()

    # Create and alter tables
    tab1 = "CREATE TABLE student(stu_id INT, name VARCHAR(40), mobile VARCHAR(15), password VARCHAR(10))"
    tab2 = "CREATE TABLE faculty(fac_id INT, name VARCHAR(50), mobile VARCHAR(15), password VARCHAR(10))"
    tab3 = "ALTER TABLE faculty MODIFY password VARCHAR(50)"
    tab4 = "ALTER TABLE student MODIFY password VARCHAR(50)"
    tab5 = "CREATE TABLE course(course_id INT PRIMARY KEY, course_name VARCHAR(15), fac_id INT, FOREIGN KEY(fac_id) REFERENCES faculty(fac_id))"
    tab6 = "ALTER TABLE faculty ADD COLUMN course_name VARCHAR(50) UNIQUE"
    tab7 = "ALTER TABLE course ADD UNIQUE(course_name)"
    tab8 = "CREATE TABLE grade(stu_id INT, grade VARCHAR(5), FOREIGN KEY(stu_id) REFERENCES student(stu_id))"
    tab9 = "ALTER TABLE student ADD COLUMN course_name VARCHAR(20)"
    tab10 = "ALTER TABLE student ADD FOREIGN KEY(course_name) REFERENCES course(course_name)"
    tab11 = "ALTER TABLE grade ADD UNIQUE(stu_id)"

    cur.execute(tab1)
    cur.execute(tab2)
    cur.execute(tab3)
    cur.execute(tab4)
    cur.execute(tab5)
    cur.execute(tab6)
    cur.execute(tab7)
    cur.execute(tab8)
    cur.execute(tab9)
    cur.execute(tab10)
    cur.execute(tab11)

    # Commit changes
    mydb.commit()

except sql.Error as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and connection
    cur.close()
    mydb.close()
#*********ADDING STUDENT(S)**********
if check == 'addstudent':
    def student(stu_id, stu_name, mobi, pswd):
        s = "INSERT INTO Student(stu_id, name, mobile, password) values(%s, %s, %s, %s)"
        rec = (stu_id, stu_name, mobi, pswd)
        try:
            if len(mobi) == 10 :
                cur.execute(s, rec)
                print("Data of Student added successfully")
                mydb.commit()
            else:
                print("Invalid mobile number. It must be 10 digits long and start with 9, 8, 7, or 6.")
        except Exception as e:
            print(f"Error {e} has occurred.")

    i = 0
    num_rec = int(input("Enter the number of records you want to store: "))
    while i < num_rec:
        print(f"Enter the {i + 1} record")
        while True:
            try:
                stu_id = int(input("Enter the student id: "))
                break
            except Exception as e:
                print(f"Error {e} occurred \nEnter a valid id: ")
        name = input("Enter the student name: ")
        while True:
            mobi = input("Enter the student's mobile number: ")
            if mobi.isdigit() and len(mobi) == 10 and mobi[0] in '9876':
                break
            else:
                print("Enter a valid mobile number (10 digits and starting with 9, 8, 7, or 6).")

        pwd = input("Enter the student's password: ")
        student(stu_id, name, mobi, pwd)
        i += 1
