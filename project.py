import pymysql as sql
mydb=sql.connect(host="localhost",user="root",password="9614877628m",database="db1")
cur=mydb.cursor()
#********ADMIN MODE********
def admin(username,pwd):
    if username=="meet" and pwd == "meet@01":
        print("Admin verfied...\nYou can access.")
        while(True):
            try:
                check=(input('''Choose any one:
            ->'addstudent' for ADDING STUDENT 
            ->'addfaculty' for ADDING FACULTY
            ->'showstudent' for SHOWIMG STUDENT'S DATA
            ->'showfaculty' for SHOWING FACULTY DATA
            ->'delstudent' for DELETING STUDENT
            ->'delfaculty' for DELETING FACULTY
            ->'coursemanagement' to MANAGING COURSES
            ->enter any other key to exit: '''))
                break            
            except:
                print("Invalid input enter a valid input.")

        #*********ADDING STUDENT(S)**********
        if check=='addstudent':
            def student(stu_id,stu_name,mobi,pswd):
                s="INSERT INTO Student(stu_id,name,mobile,password) values(%s,%s,%s,%s)"
                rec=(stu_id,stu_name,mobi,pswd)
                try:
                    mob=str(mobi)
                    if len(mob) == 10 and mob[0] in '9876':
                     cur.execute(s,rec)
                     print("Data of Student added successfully")
                     mydb.commit()
                    else:
                     print("Invalid mobile number. It must be 10 digits long and start with 9, 8, 7, or 6.")
                    
                except Exception as e:
                    print(f"Error {e} has occured.")
                    
            i=0
            num_rec=int(input("Enter the number of records you want to store: "))
            while i<num_rec:
                print(f"Enter the {i+1} record")
                while(True):
                    try:
                        id=int(input("Enter the student id: "))
                        break
                    except Exception as e:
                        print(f"Error {e} occured \n Enter valid id: ")
                name=input("Enter the student name: ")
                while(True):
                    try:
                        mobi=int(input("Enter the student's mobile number: "))
                        mob=str(mobi)
                        if len(mob) == 10 and mob[0] in'9876' :
                         break
                        else:
                         print("Enter a valid mobile number (10 digits and starting with 9, 8, 7, or 6).")
                    except Exception as e:
                     print(f"Error {e} has occured.")
                    

                pwd=input("Enter the student's password: ")
                student(id,name,mobi,pwd)
                i+=1
        #*********ADDING FACULTY(S)************
        elif check=='addfaculty':
            def faculty(fac_id,fac_name,mobi,pswd):
                s="INSERT INTO faculty (fac_id,name,mobile,password) VALUES(%s,%s,%s,%s)"
                rec=(fac_id,fac_name,mobi,pswd)
                cur.execute(s,rec)
                print("Data of faculty added successfully")
                mydb.commit()
            i=0
            num_rec=int(input("Enter the number of records you want to store: "))
            while i<num_rec:
                print(f"Enter the {i+1} record")
                while(True):
                    try:
                        id=int(input("Enter the faculty id: "))
                        break
                    except Exception as e:
                        print(f"Error {e} occured \n Enter valid id.")
                name=input("Enter the faculty name: ")
                while(True):
                    try:
                        mob=int(input("Enter the faculty's mobile number: "))
                        break
                    except:
                        print("Enter a valid mobile number.")
                pwd=input("Enter the faculty's password: ")
                faculty(id,name,mob,pwd)
                i+=1
        #*********REMOVING STUDENT**********
        elif check=='delstudent':
            def del_student(id):
                s="DELETE FROM student WHERE stu_id=%s"
                try:
                    cur.execute(s,(id,))
                    mydb.commit()
                    print("Student's record deleted successfully...")
                except Exception as e:
                    print(f"Error {e} has occured")
            try:
                ID=int(input("Enter the id of the student you want to delete: "))
                del_student(ID)
            except Exception as e:
                print(f"Error {e} has occured.")

        #*********REMOVING FACULTY**********
        elif check=='delfaculty':
            def del_faculty(userid):
                s="DELETE FROM faculty WHERE fac_id=%s"
                try:
                    cur.execute(s,(userid))
                    mydb.commit()
                    print("faculty's record deleted successfully...")
                except Exception as e:
                    print(f"Error {e} has occured")
            try:
                id=(input("Enter the id of the faculty you want to delete: "))
            except Exception as e:
                print(f"Error {e} has occured")
            del_faculty(id)
        
        #*********DISPLAY STUDENT'S DATA************ 
        elif check=='showstudent':
            def show_student():
                s="SELECT * FROM student"
                cur.execute(s)
                result=cur.fetchall()
                print("(stu_id,name,mobile,password,course)")
                for rec in result:
                    print(rec)
                print("student's data fetched successfully.")
            show_student()

        #*********DISPLAY FACULTY'S DATA************ 
        elif check=='showfaculty':
            def show_faculty():
                s="SELECT * FROM faculty"
                cur.execute(s)
                result=cur.fetchall()
                print("(fac_id,name,mobile,password,course)")
                for rec in result:
                    print(rec)
                print("Faculty's data fetched successfully.")
            show_faculty()

        #***********MANAGING COURSES*********
        elif check=='coursemanagement':
            def course_management():
                chk=input('''Enter:
        -> 'addition' for ADDING COURSES
        -> 'assign' for ASSIGNING COURSE TO FACULTY: ''')
                #***********COURSE ADDITION********
                if chk=="addition":
                    def add_course(id,name):
                        s="INSERT INTO course(course_id,course_name) VALUES(%s,%s)"
                        d=(id,name)
                        cur.execute(s,d)
                        mydb.commit()
                        print("Course added successfully..")
                    i=0
                    n=int(input("Enter the number of courses you want to add: "))
                    while i<n:
                        print(f"Enter the {i+1}th course")
                        cid=int(input("Enter the course id: "))
                        cname=input("Enter the name of the course: ")
                        add_course(cid,cname)
                        i+=1

                #**********ASSSIGNING COURSE TO FACULTY**********
                elif chk=="assign":
                    def assign_course(fid,cid): 
                        c="UPDATE course SET fac_id=%s WHERE course_id=%s"
                        f="UPDATE faculty SET course_name=(SELECT course_name FROM course WHERE course_id=%s) Where fac_id=%s"
                        try:
                            cur.execute(c,(fid,cid))
                            cur.execute(f,(cid,fid))
                            mydb.commit()
                            print("record updated successfully.")
                        except Exception as e:
                            print(f"Error {e} has occured.\n This course has been assigned.")
                    while True:
                        try:
                            FID=int(input("Enter the faculty id to assign the course: "))
                            CID=int(input("Enter the course id you want to assign: "))
                            break
                        except Exception as e:
                            print(f"Error {e} has occured.")
                            print("Enter the valid id.")
                    assign_course(FID,CID)
            course_management()
        #*********INVALID MODE********
        else:
            print("EXIT!!!")
    #*********INVALID ADMIN*********  
    else:
        print("SORRY...You can not access the database")

#******TAKING USER MODE********
user=input('''Choose login mode:
    ->'admin'
    ->'student' 
    ->'faculty': ''')

#********ADMIN********
if user=="admin":
    try:
        # name=input("Enter the name:")
        # passwd=input("Enter the password:")
        name="meet"
        passwd='meet@01'
        
    except:
        print("Enter valid name and password") 
    admin(name,passwd)

#*******STUDENT*********
elif user=='student': 
    def verify_student(id,pwd):
        ps="SELECT stu_id FROM student WHERE password=%s"
        cur.execute(ps, (pwd,))
        t=cur.fetchone()
         # Check if no student was found 
        if t is None:
           print("Student not found or incorrect password.")
           return
        # Extract the student ID from the tuple
        stu_id = t[0]
        # Verify if the provided ID matches the one in the database
        if str(id)==str(stu_id):
            print("student verified...")
            chk=input('''Enter ->'showcourses' for LIST OF COURSES
    ->'register' for REGISTER INTO COURSES:
    ->'deregister' for DEREGISTERING FROM COURSES
    ->'gradecard' for SEEING ASSIGNED GRADE: ''')

        #**********SHOWING LIST OF COURSES**********
            if chk=='showcourses':
                def show_course():
                    s="SELECT * FROM course"
                    cur.execute(s)
                    C=cur.fetchall()
                    print("(course_id,course_name,fac_id)")
                    for rec in C:
                            print(rec)
                    print("Data fetched successfully..")
                show_course()

            #**********REGISTER FOR ANY COURSE**********
            elif chk=="register":
                def reg_course(cid,sid):
                    s='UPDATE student SET course_name=(SELECT course_name FROM course WHERE course_id=%s) WHERE stu_id=%s'
                    cur.execute(s,(cid,sid))
                    mydb.commit()
                    print("Registered successfully...")
                try:
                    CID=int(input("Enter the course id you want to register for: "))
                except Exception as e:
                    print(f"Error {e} has occured.")
                reg_course(CID,ID)

            #*********DEREGISTER FROM ANY COURSE**********
            elif chk=='deregister':
                def dereg_course(sid):
                    s='UPDATE student SET course_name=null WHERE stu_id=%s'
                    cur.execute(s,(sid,))  #it must be of type list, tuple or dict as fetchone return tuple
                    mydb.commit()          #cur.execute(s,(sid,)) to convert into tuple.
                    print("DeRegistered successfully...")
                try:
                    CID=int(input("Enter the course id you want to deregister for: "))
                except Exception as e:
                    print(f"Error {e} has occured.")
                dereg_course(ID)

            #************VIEWING GRADECARD***********
            elif chk=='gradecard':
                def grade_card(id):
                    s="SELECT * FROM grade WHERE stu_id=%s"
                    cur.execute(s,(id,))
                    g=cur.fetchone()
                    if str(g)=='None':
                        print("You haven't assigned any grade yet.")
                    else:
                        print("(stu_id,grade)")
                        print(g)
                        print("data fetched successfully...")
                grade_card(ID)
            else:
                print("Invalid option selected.")
        else:
            print("Student ID does not match.")

    #********STUDENT ID AND PASSWORD*********
    ID=int(input("Enter your id: "))
    PWD=input("Enter password: ")
    verify_student(ID,PWD)

#*********FACULTY************
elif user=='faculty':
    def verify_faculty(id,pwd):
        ps="SELECT fac_id FROM faculty WHERE password=%s"
        cur.execute(ps,(pwd,))
        t=cur.fetchone()
        if t is None:
           print("Faculty not found or incorrect password.")
           return
        # s=str(t)
        # print(s)
        # print(type(s))
        # i=int(s[1])
        fac_id=t[0]    # Extract faculty ID from the tuple
        # # Verify if the provided ID matches the one in the database
        if str(id)==str(fac_id):
            print("faculty verified...")
            #**********ASSIGNING GRADE************
            def grade_assign(sid,gr):
                s1="SELECT course_name FROM student WHERE stu_id=%s"
                cur.execute(s1,(sid,))
                cond1=cur.fetchone()
                s2="SELECT course_name FROM faculty WHERE fac_id=%s"
                cur.execute(s2,(FID,))
                cond2=cur.fetchone()
                if cond1==cond2:
                    s="INSERT INTO grade values(%s,%s)"
                    cur.execute(s,(sid,gr))
                    mydb.commit()
                    print("Grade assigned successfully...")
                else:
                    print("You can not assign grades to student other than your course.")    
            print("Assign grade to student..")
            SID=int(input("Enter the student's id: "))
            GR=input("Enter the grade--'A','B','C','D','F' : ")
            grade_assign(SID,GR)
    #**********FACULTY ID AND PASSWORD**********
    FID=int(input("Enter your id: "))
    PWD=input("Enter password: ")
    verify_faculty(FID,PWD)
    