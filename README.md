# Institute-Management-System
Overview
This project is a Student Management System built using Python and MySQL. It provides functionalities for administrators, faculty, and students to manage academic records, courses, and grades.

Features
Admin Features
Add/Delete students and faculty

View student and faculty records

Manage courses (add/assign to faculty)

Faculty Features
Assign grades to students in their courses

View course assignments

Student Features
View available courses

Register/Deregister for courses

View grade reports

Database Schema
The system uses the following tables:

student: Stores student information (ID, name, mobile, password, course)

faculty: Stores faculty information (ID, name, mobile, password, course)

course: Stores course information (ID, name, faculty ID)

grade: Stores student grades (student ID, grade)

Installation
Clone the repository:

bash
git clone https://github.com/yourusername/student-management-system.git
cd student-management-system
Install dependencies:

bash
pip install pymysql
Set up MySQL database:

Create a database named db1

Update the connection details in database.py and project.py with your MySQL credentials

Run the setup script to create tables:

bash
python database2.py
Usage
Run the main application:

bash
python project.py
Login Options:
Admin:

Username: meet

Password: meet@01

Faculty/Student: Use credentials created by admin

Code Structure
database.py: Initial database setup script

database2.py: Complete database schema creation script

project.py: Main application with all functionalities

Contributing
Contributions are welcome! Please fork the repository and create a pull request with your changes.
