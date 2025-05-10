from sqlmodel import SQLModel, Field, Relationship, create_engine , Session, select
from typing import Optional, List
from datetime import datetime



# StudentCourseLink Model (Link Table):
# • student_id: Integer, foreign key referencing student.id, primary key.
# • course_id: Integer, foreign key referencing course.id, primary key.
# • enrollment_date: Optional datetime (use datetime from Python's datetime module). This is a relationship attribute.
# • grade: Optional String (e.g., "A", "B+", "In Progress"). Another relationship attribute.
class StudentCourseLink(SQLModel, table=True):
    student_id: int = Field(foreign_key="student.id", primary_key=True)
    course_id: int = Field(foreign_key="course.id", primary_key=True)

    enrollment_date: Optional[datetime] = Field(default=None)
    grade: Optional[str] = Field(default=None)
    
    
    
# • Department Model:
# • id: Integer, primary key, optional.
# • name: String, required, unique.
# • building: String, optional.
# • courses: List of Course objects (relationship). Use
# Relationship(back_populates=...).
class Department(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str = Field(index=True, nullable=False, unique=True)
    building: Optional[str] = None

    # Relationship to Course
    courses: List["Course"] = Relationship(back_populates="department")
    
    
# Student Model:
# • id: Integer, primary key, optional.
# • first_name: String, required.
# • last_name: String, required.
# • email: String, required, unique.
# • courses: List of Course objects (relationship via link table). Use
# Relationship(back_populates=..., link_model=...).
class Student(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    first_name: str
    last_name: str
    email: str = Field(unique=True, nullable=False)

    courses: List["Course"] = Relationship(
        back_populates="students",
        link_model=StudentCourseLink
    )


# Course Model:
# • id: Integer, primary key, optional.
# • title: String, required, indexed.
# • code: String, required, unique.
# • department_id: Integer, foreign key referencing department.id, optional.
# • department: Optional Department object (relationship). Use Relationship(back_populates=...).
# • students: List of Student objects (relationship via link table). Use Relationship(back_populates=..., link_model=...).
class Course(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    title: str = Field(index=True)
    code: str = Field(unique=True, nullable=False)

    department_id: Optional[int] = Field(default=None, foreign_key="department.id")
    department: Optional[Department] = Relationship(back_populates="courses")

    students: List[Student] = Relationship(
        back_populates="courses",
        link_model=StudentCourseLink
    )
    

    
# Create SQLite Engine
DATABASE_URL = "sqlite:///university.db"
engine = create_engine(DATABASE_URL, echo=True)

# Create all tables in the database
SQLModel.metadata.create_all(engine)


# Write functions to create_department, create_student, create_course.
def create_department(name: str, building: str=None):       #Takes in name (required) and building (optional).
    department = Department(name=name, building=building)       #Creates a Department object
    with Session(engine) as session:                 #Creates a session to interact with the database. 
        # It acts as a middle layer between your Python code and the database.
        # with ensures the session automatically closes after the block ends.
        session.add(department)     #Adds the department object to the session.
        session.commit()        #Commits the changes to the database.
        session.refresh(department)     #Refreshes the object to include any data the DB may have auto-generated (like id).  #Returns the department object.
    return department       # Returns the department object.

def create_student(first_name: str, last_name: str, email: str):
    student = Student(first_name=first_name, last_name=last_name, email=email)
    with Session(engine) as session:
        session.add(student)
        session.commit()
        session.refresh(student)
    return student

def create_course(title: str, code: str, department_id: int=None):
    course = Course(title=title, code=code, department_id=department_id)
    with Session(engine) as session:
        session.add(course)
        session.commit()
        session.refresh(course)
    return course

# Write functions to get_department_by_name, get_student_by_email, get_course_by_code.
def get_department_by_name(name: str):
    with Session(engine) as session:
        statement = select(Department).where(Department.name==name)     
        result = session.exec(statement).first()    #session.exec(statement) executes the query , first() fetches the first row that matches (or None if not found).
        return result

def get_student_by_email(email: str):
    with Session(engine) as session:
        statement = select(Student).where(Student.email==email)
        result = session.exec(statement).first()
        return result

def get_course_by_code(code: str):
    with Session(engine) as session:
        statement = select(Course).where(Course.code==code)
        result = session.exec(statement).first()
        return result
    
# Write functions to list all entities (e.g., list_all_students).
def list_all_students():
    with Session(engine) as session:
        statement = select(Student)
        results = session.exec(statement).all()     #Fetches all rows from the Student table.
        return results

def list_all_courses():
    with Session(engine) as session:
        statement = select(Course)
        results = session.exec(statement).all()
        return results

def list_all_departments():
    with Session(engine) as session:
        statement = select(Department)
        results = session.exec(statement).all()
        return results
    
# Write a function to update a student's email (update_student_email).
def update_student_email(student_id :int, new_email: str):
    with Session(engine) as session:
        statement = select(Student).where(Student.id==student_id)
        student = session.exec(statement).first()
        if student:
            student.email = new_email
            session.commit()
            session.refresh(student)
            return student
        else:
            return None
        
# Write a function to delete a course by its code (delete_course).
def delete_course(code : str):
    with Session(engine) as session:
        statement = select(Course).where(Course.code==code)
        course = session.exec(statement).first()
        if course:
            session.delete(course)
            session.commit()
            return True
        else:
            return False
 
 

# Write a function enroll_student(student_id: int, course_id: int, enrollment_date: Optional[datetime] = None):
# • Creates an entry in the StudentCourseLink table.
# • Handle potential errors (e.g., student or course not found, student already enrolled).
def enroll_student(student_id : int, course_id : int, enrollment_date: datetime=None):
    with Session(engine) as session:
        # Check if student exists
        student = session.get(Student,student_id)       # session.get(Model, primary_key) - Use this when you're fetching a single row by its primary key (PK).
        if not student:
            raise ValueError(f"Student with ID {student_id} does not exist.")
        
        # Check if course exist
        course = session.get(Course,course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} does not exist.")
        
        # Check if student is already enrolled in the course
        statement = select(StudentCourseLink).where((StudentCourseLink.student_id==student_id) & (StudentCourseLink.course_id==course_id))
        existing_enrollment = session.exec(statement).first()
        if existing_enrollment:
            raise ValueError("Student is already enrolled in the course.")
        
        # Create enrollment
        link = StudentCourseLink(       ## Creates a new StudentCourseLink object.
            student_id=student_id,
            course_id=course_id,
            enrollment_date=enrollment_date
        )
        session.add(link)
        session.commit()
        return link     # Returns the created enrollment link object.
    
# Write a function get_courses_for_student(student_id: int):
# • Retrieves a student.
# • Returns the list of courses they are enrolled in by accessing the student.courses relationship attribute. Print the course titles.
def get_courses_for_student(student_id: int):
    with Session(engine) as session:
        #Retrive the student
        student = session.get(Student, student_id)
        if not student:
            raise ValueError(f"Student with ID {student_id} does not exist.")
        #Access the courses for the student
        courses = student.courses
        
        if not courses:
            raise ValueError(f"Student with ID {student_id} is not enrolled in any courses.")
        else:
            print(f"Courses enrolled by the student:")
            for course in courses:
                print(f"- {course.title}")
        return courses
    
# Write a function get_students_in_course(course_id: int):
# • Retrieves a course.
# • Returns the list of students enrolled by accessing the course.students relationship attribute. Print the student names.
def get_students_in_course(course_id : int):
    with Session(engine) as session:
        #Retrieve the course
        course = session.get(Course,course_id)
        if not course:
            raise ValueError(f"Course with ID {course_id} does not exist.")
        #Access the students for the course
        students = course.students
        if not students:
            raise ValueError(f"No students are enrolled in the course with ID {course_id}.")
        else:
            print(f"Students enrolled in the course:")
            for i in students:
                print(f"- {i.first_name} {i.last_name} ")
        return students
    
# Write a function set_enrollment_grade(student_id: int, course_id: int, grade: str):
# • Finds the specific StudentCourseLink entry for the given student and course.
# • Updates the grade attribute on that link table entry.
# • Commits the change.
def set_enrollment_grade(student_id : int, course_id:int , grade: str):
    with Session(engine) as session:
        # Find the specific StudentCourseLink entry
        statement = select(StudentCourseLink).where(
            (StudentCourseLink.student_id==student_id) & 
            (StudentCourseLink.course_id==course_id)
        )
        enrollment = session.exec(statement).first()
        
        if not enrollment:
            raise ValueError(f"No enrollment found for student ID {student_id} in course ID {course_id}.")
        else:
            enrollment.grade=grade
            session.commit()
            session.refresh(enrollment)  # Refresh the object to get the updated data
            print(f"Grade updated to '{grade}' for student ID {student_id} in course ID {course_id}.")


# Write a function unenroll_student(student_id: int, course_id: int):
# • Finds and deletes the corresponding entry from the StudentCourseLink table.
def unenroll_student(student_id : int , course_id: int):
    with Session(engine) as session:
        # Find the enrollment link entry
        statement = select(StudentCourseLink).where(
            (StudentCourseLink.student_id==student_id) & 
            (StudentCourseLink.course_id==course_id)
        )
        enrollment=session.exec(statement).first()
        
        if not enrollment:
            raise ValueError(f"No enrollment found for student ID {student_id} in course ID {course_id}.")
        else:
            session.delete(enrollment)
            session.commit()
            print(f"Student ID {student_id} has been unenrolled from course ID {course_id}.")
            

if __name__ == "__main__":
    #Create departments
    cs_dept = create_department(name="Computer Science", building="Main Block")
    math_dept = create_department(name="Mathematics", building="Science Block")
    print(f"Created Department: {cs_dept.name}, Building: {cs_dept.building}")
    print(f"Created Department: {math_dept.name}, Building: {math_dept.building}")
    
    #Create courses
    dsa = create_course(title="Data Structures and Alogorithms", code="CS101", department_id=cs_dept.id)
    java = create_course(title="Java Programming", code="CS102", department_id=cs_dept.id)
    web_dev = create_course(title="Web Development", code="CS103", department_id=cs_dept.id)
    
    calc = create_course(title="Calculus", code="MATH101", department_id=math_dept.id)
    stats = create_course(title="Statistics", code="MATH102", department_id=math_dept.id)
    
    print(f"Created Course: {dsa.title}, Code: {dsa.code}, Department ID: {dsa.department_id}")
    print(f"Created Course: {java.title}, Code: {java.code}, Department ID: {java.department_id}")
    print(f"Created Course: {web_dev.title}, Code: {web_dev.code}, Department ID: {web_dev.department_id}")
    print(f"Created Course: {calc.title}, Code: {calc.code}, Department ID: {calc.department_id}")
    print(f"Created Course: {stats.title}, Code: {stats.code}, Department ID: {stats.department_id}")
    
    #Create students
    student1 = create_student(first_name="MS", last_name="Dhoni", email="msdhoni777@thala.com")
    student2 = create_student(first_name="Virat", last_name="Kohli", email="kholi18@king.com")
    student3 = create_student(first_name="Keerthan", last_name="K", email="keerthan@gmail.com")
    
    #Enroll students in courses
    enroll_student(student1.id, dsa.id)
    enroll_student(student1.id, java.id , enrollment_date=datetime.now())
    enroll_student(student2.id, web_dev.id)
    enroll_student(student3.id, calc.id)
    enroll_student(student3.id, stats.id)
    
    #List courses for a specific student
    print("\nCourses for Student 1:")
    courses_for_student1 = get_courses_for_student(student1.id)
    for course in courses_for_student1:
        print(f"- {course.title} (Code: {course.code})")
        
    #List students in a specific course
    print("\nStudents in Web Development Course:")
    students_in_web_dev = get_students_in_course(web_dev.id)
    for student in students_in_web_dev:
        print(f"- {student.first_name} {student.last_name} (Email: {student.email})")
        
    #Set a grade for one of the enrollments
    set_enrollment_grade(student1.id, dsa.id, "A+")
    
    #Unenroll a student from a course.List the students in that course again to verify the unenrollment.
    unenroll_student(student1.id, java.id)
    print("\nStudents in Java Programming Course after unenrollment:")
    students_in_java = get_students_in_course(java.id)
    for student in students_in_java:
        print(f"- {student.first_name} {student.last_name} (Email: {student.email})")
    
    
    #Perform basic CRUD operations (update a student, delete a course) and verify.
    #Update a student's email
    updated_student = update_student_email(student1.id, "csk123@gmail.com")
    print(f"Updated Student Email: {updated_student.email}")
    
    #Delete a course
    course_deleted = delete_course("CS102")
    if course_deleted:
        print("Course CS102 deleted successfully.")
    else:
        print("Course CS102 not found.")
        
    #List all students, courses, and departments to verify the database state.
    print("\nAll Students:")
    all_students = list_all_students()
    for student in all_students:
        print(f"- {student.first_name} {student.last_name} (Email: {student.email})")
    
    print("\nAll Courses:")
    all_courses = list_all_courses()
    for course in all_courses:
        print(f"- {course.title} (Code: {course.code})")
        
    print("\nAll Departments:")
    all_departments = list_all_departments()
    for department in all_departments:
        print(f"- {department.name} (Building: {department.building})")
    
    #Get a specific department by name
    department = get_department_by_name("Computer Science")
    if department:
        print(f"Department Found: {department.name}, Building: {department.building}")
    else:
        print("Department not found.")
    
    #Get a specific student by email
    student = get_student_by_email("csk123@gmail.com")
    if student:
        print(f"Student Found: {student.first_name} {student.last_name}, Email: {student.email}")
    else:
        print("Student not found.")
    
    #Get a specific course by code
    course = get_course_by_code("CS101")
    if course:
        print(f"Course Found: {course.title}, Code: {course.code}, Department ID: {course.department_id}")
    else:
        print("Course not found.")
    