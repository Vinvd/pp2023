from domains.students   import student
from domains.courses    import course
from domains.marks      import mark
import numpy as np
import math
import os
import zipfile

student_file_name = "students.txt"
Student_filepath = os.path.join(os.path.dirname(__file__), student_file_name)
course_file_name = "courses.txt"
course_filepath = os.path.join(os.path.dirname(__file__), course_file_name)
mark_file_name = "marks.txt"
mark_filepath = os.path.join(os.path.dirname(__file__), mark_file_name)

data_file_name = "students.dat"
data_file_path = os.path.join(os.path.dirname(__file__), data_file_name)


def input_num_students(stdscr):         #return number of student
    
    stdscr.clear()
    stdscr.addstr(0,0,'Input number of students in the class: ')

    type = stdscr.getstr()
    type = type.decode('utf-8')

    if type.isnumeric():
        numStudent = int(type)
    else:
        input_num_students()

    stdscr.refresh()
    stdscr.clear()
    return numStudent

def input_students_info(x,stdscr):      #return list of students
    students = []
    stdscr.clear()

    for i in range(int(x)):
        stdscr.addstr(f'\nInput the Id, name and DoB of student \"{str(i+1)}\"') 

        y, x = stdscr.getyx()
        stdscr.addstr(y+1, 0,'Id: ')
        studentId = stdscr.getstr()
        studentId = studentId.decode('utf-8')

        y, x = stdscr.getyx()
        stdscr.addstr(y+1, 0,'Name: ')
        studentName = stdscr.getstr()
        studentName = studentName.decode('utf-8')

        y, x = stdscr.getyx()
        stdscr.addstr(y+1, 0,'Date:')
        studentDoB = stdscr.getstr()
        studentDoB = studentDoB.decode('utf-8')

        Student = student(studentId,studentName,studentDoB,None)
        students.append(Student)
    stdscr.refresh()
    
    file = open(Student_filepath, "w")
    for i in students:
        file.write(f'{i}\n')
    file.close()
    stdscr.addstr(f'\nDone input student.txt')
    stdscr.getkey()
    stdscr.clear() 
    return students

def input_num_courses(stdscr):          #return number of courses       
    stdscr.clear()
    
    stdscr.addstr('\nInput number of courses in this class: ')
    type = stdscr.getstr()
    type = type.decode('utf-8')

    if type.isnumeric():
        numCourse = int(type)
        stdscr.refresh()
    else:
        input_num_courses(stdscr)
    stdscr.clear()
    return numCourse

def input_courses_info(x,stdscr):       #return list of courses; need to eat an int
    courses = []
    stdscr.clear()
    for i in range(int(x)):

        stdscr.addstr('\nInput the id and the name of the \"'+ str(i+1)+'\" course')
        
        stdscr.addstr('\nCourse Id:')
        courseId = stdscr.getstr()
        courseId = courseId.decode('utf-8')

        stdscr.addstr('\nCourse name:')
        courseName = stdscr.getstr()
        courseName = courseName.decode('utf-8')

        x = 0
        while   x == 0:
            stdscr.addstr('\nCourse credit: ')
            type = stdscr.getstr()
            type = type.decode('utf-8')

            if type.isnumeric():
                courseCredit = int(type)
                x += 1
            else:
                stdscr.addstr('\nCredit is a number ')

        Course = course(courseId,courseName,courseCredit)        
        courses.append(Course)
    stdscr.refresh()

    file = open(course_filepath, "w")
    for i in courses:
        file.write(f'{i}\n')
    file.close()
    stdscr.addstr(f'\nDone input course.txt')
    stdscr.getkey()
    stdscr.clear() 
    return courses

def input_marks(b,c,stdscr):     # b is list of courses; c is list students "i removed a :)"
    stdscr.clear() 
    stdscr.refresh()

    List_mark = []

    for x in range(len(b)):
        stdscr.addstr(f"\nEnter points of course {b[x].print_crs_name()}: ")

        for i in range(len(c)):
            y = 0
            while y == 0:
                while True: # loop until valid data is entered
                    stdscr.addstr(f"\nmark of {c[i].print_std_name()}: ")
                    mark_in = stdscr.getstr()
                    mark_in = mark_in.decode('utf-8')

                    try:
                        mark_in = float(mark_in)    # convert string to float
                        stdscr.addstr(f"Valid float number: {mark_in} \n")
                        y += 1
                        break                       # exit the loop
                    except ValueError:              # catch exception if conversion fails
                        stdscr.addstr(f"Invalid float number: {mark_in} \n")

            mark_in = math.floor(mark_in)
            S = mark(c[i], b[x-1], mark_in)
            List_mark.append(S)
            del S

    stdscr.refresh()
    
    file = open(mark_filepath, "w")
    for i in List_mark:
        file.write(f'{i}\n')
    file.close()

    stdscr.addstr(f'\nDone input marks.txt')
    stdscr.getkey()
    stdscr.clear()
    return List_mark

def choose_student_toCal_gpa(student_list,stdscr):
    stdscr.clear()

    for i in range(len(student_list)):
        stdscr.addstr(f'\n {i+1}: {student_list[i].print_std_name()}')
    y = 0
    while y == 0:
        stdscr.addstr(f'\n enter number in the given list: ')
        type = stdscr.getstr()
        type = type.decode('utf-8')

        if type.isnumeric():
            if int(type) in range(1,((len(student_list))+ 1)):
                y = int(type)
        else:
            stdscr.addstr('\nplease type in a number') 

    stdscr.addstr(f'\nCHOOSEN: {student_list[y-1].print_std_name()}')
    stdscr.refresh() 
    stdscr.getkey() 
    stdscr.clear()
    return student_list[y-1].print_std_name()
    
def calculate_student_gpa(mark_list, std_name,stdscr):
    only_marks = []
    only_credits = []
    stdscr.clear()
    for i in mark_list:
        if i.stdName == std_name:
            mark = i.print_mark()
            only_marks.append(mark)

            credit = i.crsCredit
            only_credits.append(credit)
    stdscr.addstr(f'\nmarks: {only_marks}')
    stdscr.addstr(f'\ncredits: {only_credits}')
    stdscr.getkey()
    marks_np = np.array(only_marks)
    credits_np = np.array(only_credits)

    gpa = np.sum(marks_np * credits_np) / np.sum(credits_np)
    gpa = np.round(gpa,5)
    stdscr.addstr(f'\n \n{gpa} \n')

    stdscr.refresh() 

    return gpa

def assign_student_gpa(gpa,student_list,choosen_One,stdscr):
    for i in range(len(student_list)):
        if student_list[i].print_std_name() == choosen_One:
            student_list[i].set_std_gpa(gpa)
            stdscr.addstr(f'\nstudent: {student_list[i].print_std_name()}, gpa: {student_list[i].print_std_gpa()}\n') 

            stdscr.addstr('\nAssigned\n')
    stdscr.refresh() 
    stdscr.getkey() 
    stdscr.clear()
    return student_list                 # :)

def calculate_all_student(student_list,marks_list,stdscr):
    for i in student_list:
        the_one = i.print_std_name()
        gpa = calculate_student_gpa(marks_list, the_one,stdscr)
        new_studentGpa_list=assign_student_gpa(gpa,student_list, the_one,stdscr)
    return new_studentGpa_list

def sort_student_list(student_list,stdscr):
    stdscr.clear()
    # create a numpy array of gpa
    Gpas = np.array([person.print_std_gpa() for person in student_list])
    indices = np.argsort(-Gpas)
        
    sorted_student_list = [student_list[i] for i in indices]
    for i in sorted_student_list:
        stdscr.addstr(f'\nstudent: {i.print_std_name()}, gpa: {i.print_std_gpa()}')
    stdscr.getkey() 
    stdscr.clear()
    return sorted_student_list

def read_from_dat(stdscr):
    students = []
    courses = []
    Marks = []
    stdscr.clear()
    # name of the compressed file
    compressed_file = data_file_path

    # create a ZipFile object for the compressed file
    # FileNotFoundError
    with zipfile.ZipFile(compressed_file, mode="r") as zf:

        # stdscr.addstr(f'\n{zf.namelist()}')         # list the contents of the zip file

        student_file = zf.namelist()[0]
        course_file = zf.namelist()[1]
        mark_file = zf.namelist()[2]

        with zf.open(student_file, "r") as f:
            lines = f.readlines()
            for line in lines:
                line = line.decode("utf-8")
                line = line.replace(".\r\n","")
                fields = line.split(", ")

                # extract the data for each field
                id = fields[0][4:]
                name = fields[1][6:]
                dob = fields[2][5:]

                Student = student(id,name,dob,None)
                students.append(Student)

        with zf.open(course_file, "r") as f2:
            lines = f2.readlines()
            for line in lines:
                line = line.decode("utf-8")
                line = line.replace("\r\n","")
                fields = line.split(", ")

                # extract the data for each field
                id = fields[0][4:]
                name = fields[1][13:]
                credit = fields[2][8:]

                Course = course(id,name,credit)
                courses.append(Course)

        with zf.open(mark_file, "r") as f3:
            lines = f3.readlines()
            for line in lines:
                line = line.decode("utf-8")
                line = line.replace("\r\n","")
                fields = line.split(", ")

                # extract the data for each field
                Mark_Student = fields[0][9:]
                Mark_course = fields[1][8:]
                Mark_value = fields[2][6:]

                for i in students:
                    if Mark_Student == i.print_std_name():
                        Mark_Student = i
                for i in courses:
                    if Mark_course == i.print_crs_name():
                        Mark_course = i

                Mark = mark(Mark_Student, Mark_course, Mark_value)
                Marks.append(Mark)

    file = open(Student_filepath, "w")
    for i in students:
        file.write(f'{i}\n')
    file.close()

    file = open(course_filepath, "w")
    for i in courses:
        file.write(f'{i}\n')
    file.close()

    file = open(mark_filepath, "w")
    for i in Marks:
        file.write(f'{i}\n')
    file.close()
    stdscr.addstr(f'\nstudents.dat found, data imported')
    stdscr.getkey()
    return students, courses, Marks