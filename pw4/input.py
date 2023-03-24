from domains.students   import student
from domains.courses    import course
from domains.marks      import mark
import numpy as np
import math

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
        input_num_courses()
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
    stdscr.clear() 
    return courses

def input_marks(a,b,c,stdscr):     # a is numcourse; b is list of courses; c is list students
    stdscr.clear() 
    stdscr.refresh()

    List_mark = []

    for x in range(a):
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
