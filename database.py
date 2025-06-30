import pymysql as sql # ignore
mydb=sql.connect(host="localhost",user="root",password="9614877628m",database="db1")
cur=mydb.cursor()
# tab1="CREATE TABLE student(stu_id  int, name varchar(40),mobile varchar(15),password varchar(10))"
# tab2="CREATE TABLE faculty(fac_id int,name varchar(50),mobile varchar(15),password varchar(10))"
# tab1="alter table faculty modify  password varchar(50)"
# tab2="alter table student modify  password varchar(50)"
# tab1="CREATE TABLE course(course_id int primary key,course_name varchar(15),fac_id int, FOREIGN KEY(fac_id) REFERENCES faculty(fac_id))  "
# tab2="ALTER TABLE faculty ADD COLUMN course_name varchar(50) UNIQUE  "
# tab2="ALTER TABLE course ADD UNIQUE(course_name) "
# tab1="CREATE TABLE grade(stu_id int ,grade varchar(5),foreign key(stu_id) REFERENCES student(stu_id))"
# tab1="ALTER TABLE student ADD COLUMN course_name varchar(20)"
# tab2="ALTER TABLE student ADD FOREIGN KEY(course_name) REFERENCES course(course_name)"
tab1="ALTER TABLE grade ADD unique(stu_id) "
cur.execute(tab1)
# cur.execute(tab2)