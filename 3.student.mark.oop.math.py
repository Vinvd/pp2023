import numpy as np
import math
import curses

class student:                                              #student_class
    def __init__(self, StudentId, StudentnName, StudentDob, Gpa):
        self.__id = StudentId
        self.__name = StudentnName
        self.__dob = StudentDob
        self.__gpa = Gpa

    def print_std_id(self):
        return self.__id
    def print_std_name(self):
        return self.__name
    def print_std_dob(self):
        return self.__dob
    def print_std_gpa(self):
        return self.__gpa

    def set_std_id(self, stdId):
        self.__id = stdId
    def set_std_name(self, stdName):
        self.__name = stdName
    def set_std_id(self, strDob):
        self.__dob = strDob
    def set_std_gpa(self, Gpa):
        self.__gpa = Gpa

    def __str__(self):
        return f"Student: id: {self.__id}, name: {self.__name}, dob: {self.__dob}."
    
class course:                                               #course_class
    def __init__(self, CourseId, CourseName, CourseCredit):
        self.__id = CourseId
        self.__name = CourseName
        self.__credit = CourseCredit

    def print_crs_id(self):
        return self.__id
    def print_crs_name(self):
        return self.__name
    def print_crs_credit(self):
        return self.__credit
    
    def set_crs_id(self,crsID):
        self.__id = crsID
    def set_crs_name(self,crsName):
        self.__name = crsName
    def set_crs_credit(self,crsCreddit):
        self.__credit = crsCreddit
    
    def __str__(self):
        return f"id: {self.__id}, Course name: {self.__name}, credit: {self.__credit}"
    
class mark(student, course):                                #mark_class
    def __init__(self, std, crs, mark):
        self.stdName   = std.print_std_name()
        self.crsName   = crs.print_crs_name()
        self.crsCredit = crs.print_crs_credit()
        self.__mark = mark

    def print_mark(self):
        return self.__mark
    
    def set_mark(self, mark):
        self.mark = mark

    def print_mark_info(self):
        return f"Student: {self.stdName}, Course: {self.crsName}, Mark: {self.__mark}"

def input_num_students(stdscr):       #return number of student
    
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

def input_students_info(x,stdscr):     #return list of students
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

def print_students_info(n,stdscr):     #feed list of students in
    stdscr.clear()
    
    stdscr.addstr(0, 0,'\nSelect a number to print: ')
    stdscr.addstr(1, 0,'1: List all students and information')
    stdscr.addstr(2, 0,'2: List all Id')
    stdscr.addstr(3, 0,'3: List all names')
    stdscr.addstr(4, 0,'4: List all Dob')
    stdscr.addstr(5, 0,'5: list student gpa')
    stdscr.refresh()

    z = 0
    while z == 0:
        y, x = stdscr.getyx()
        stdscr.addstr(y+1, 0, 'enter number in the given list: ')
        type = stdscr.getstr()
        type = type.decode('utf-8')

        if type.isnumeric():
            if int(type) in range(1,6):
                z = int(type)
                stdscr.refresh()
        else:
            y, x = stdscr.getyx()
            stdscr.addstr(y+1, 0,'please type in a number')
            stdscr.refresh()
            stdscr.getkey() 

    if z==1:
        stdscr.clear()
        for i in n:
            y, x = stdscr.getyx()
            stdscr.addstr(y+1, 0,f'Id: {i.print_std_id()}, name: {i.print_std_name()}, dob: {i.print_std_dob()}')
        stdscr.refresh()

    elif z==2:
        stdscr.clear()
        for i in range(len(n)):
            y, x = stdscr.getyx()
            stdscr.addstr(y+1, 0,n[i].print_std_id())
        stdscr.refresh()

    elif z==3:
        stdscr.clear()
        for i in n:
            y, x = stdscr.getyx()
            stdscr.addstr(y+1, 0,i.print_std_name())
        stdscr.refresh()

    elif z==4:
        stdscr.clear()
        for i in range(len(n)):
            y, x = stdscr.getyx()
            stdscr.addstr(y+1, 0,n[i].print_std_dob())      
        stdscr.refresh()

    elif z==5:
        stdscr.clear()
        if n[0].print_std_gpa() == None:
                stdscr.addstr('\n the gpa calculate have not run')
        
        else:    
            for i in n:    
                y, x = stdscr.getyx()
                stdscr.addstr(y+1, 0,i.print_std_gpa())                
        stdscr.refresh()

    stdscr.getkey()  
    stdscr.clear()
    return 0

def input_num_courses(stdscr): 
       # return number of courses
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

def input_courses_info(x,stdscr):  #return list of courses; need to eat an int
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

def print_courses_info(x,stdscr):  #return info, need to eat course list
    stdscr.clear()

    stdscr.addstr('\nSelect a number to print: ')
    stdscr.addstr('\n1: List information of all courses')
    stdscr.addstr('\n2: list all course id')
    stdscr.addstr('\n3: List all course name')  
    stdscr.addstr('\n4: Show courses credit')
    stdscr.refresh()

    y = 0
    while y == 0:
        stdscr.addstr('\nenter number in the given list:')
        type = stdscr.getstr()
        type = type.decode('utf-8')

        if type.isnumeric():
            if int(type) in range(1,5):
                y = int(type)
        else:
            stdscr.addstr('\nplease type in a number')


    if y == 1:
        for i in range(len(x)):
            stdscr.addstr(f'\n{x[i]}')
    elif y == 2:
        for i in range(len(x)):
            stdscr.addstr(f'\n{x[i].print_crs_id()}')
    elif y == 3:
        for i in x:
            stdscr.addstr(f'\n{i.print_crs_name()}')
    elif y ==4:
        for i in x:
            stdscr.addstr(f'\n{i.print_crs_credit()}')

    stdscr.refresh()
    stdscr.getkey() 
    stdscr.clear()
    return 0

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

def print_marks(list_mark, list_course,stdscr):         
    stdscr.clear()

    stdscr.addstr('\nSelect a number of the course to show marks')
    stdscr.addstr('\n0: all ')

    for i in range(len(list_course)):
        stdscr.addstr('\n' + str(i+1) + ': ' + list_course[i].print_crs_name())
    stdscr.addstr('\nselect course to output marks:')

    stdscr.refresh()
    z = (len(list_course)+2)
    while z == (len(list_course)+2):

        stdscr.addstr(f'\nenter number in the given list: \n')
        type = stdscr.getstr()
        type = type.decode('utf-8')

        if type.isnumeric():
            if int(type) in range(len(list_course)+1):
                z = int(type)
        else:
            stdscr.addstr('\nplease type in a number')
    if z == 0:
        for i in list_mark:
                stdscr.addstr(f'\n student: {i.stdName},course: {i.crsName}, marks: {i.print_mark()}')
    else:
        stdscr.addstr('\n')
        for i in list_mark:
            if (i.crsName) == (list_course[z-1].print_crs_name()):
                stdscr.addstr(f'\nstudent: {i.stdName}, marks: {i.print_mark()}')
    stdscr.refresh()
    stdscr.getkey() 
    stdscr.clear()
    return 0

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
    indices = np.argsort(Gpas)
        
    sorted_student_list = [student_list[i] for i in indices]
    for i in sorted_student_list:
        stdscr.addstr(f'\nstudent: {i.print_std_name()}, gpa: {i.print_std_gpa()}')
    stdscr.getkey() 
    stdscr.clear()
    return sorted_student_list

#main :
def mainFunc(stdscr):
    stdscr.clear()

    numStudent = input_num_students(stdscr)
    student_list = input_students_info(numStudent,stdscr)

    numCourse = input_num_courses(stdscr)
    course_list = input_courses_info(numCourse,stdscr)
    marks_list = [0]

    stdscr.clear()
    x=0
    while x==0:
        stdscr.clear()
        stdscr.addstr('\n0. Esc')
        stdscr.addstr('\n1. Input marks')
        stdscr.addstr('\n2. Print students information')
        stdscr.addstr('\n3. Print courses information')
        stdscr.addstr('\n4. Show students mark in a course')
        stdscr.addstr('\n5. Calculate Gpa for a student')
        stdscr.addstr('\n6. Calculate Gpa for all students')
        stdscr.addstr('\n7. Sort student list by Gpa')

        stdscr.addstr('\nEnter a choice: \n')
        type = stdscr.getstr()
        type = type.decode('utf-8')

        if type.isnumeric():
            if int(type) in range(8):
                type = int(type)
            else:
                stdscr.addstr('\nEnter a number in the list.')

            if type == 0:
                x = x+1

            elif type == 1:
                stdscr.clear()
                marks_list= input_marks(numCourse, course_list, student_list,stdscr)  

            elif type == 2:
                print_students_info(student_list,stdscr)
            elif type == 3:
                print_courses_info(course_list,stdscr)

            elif type == 4:
                if marks_list[0] == 0:
                    stdscr.addstr('\nthere are no mark existed')
                    stdscr.getkey()
                else:
                    print_marks(marks_list, course_list,stdscr)
            elif type == 5:
                choosenOne = choose_student_toCal_gpa(student_list,stdscr)
                if marks_list[0] == 0:
                    stdscr.addstr('\nthere are no mark existed')
                    stdscr.getkey()
                else:
                    choosenOne_Gpa = calculate_student_gpa(marks_list, choosenOne,stdscr)
                    assign_student_gpa(choosenOne_Gpa,student_list,choosenOne,stdscr)
            elif type == 6:
                if marks_list[0] == 0:
                    stdscr.addstr('\nthere are no mark existed')
                    stdscr.getkey()
                else:
                    student_list = calculate_all_student(student_list,marks_list,stdscr)
            elif type == 7:
                if student_list[0].print_std_gpa() == None:
                    stdscr.addstr('\ngpa have not ben calculated')
                    stdscr.getkey()
                else:
                    student_list = sort_student_list(student_list,stdscr)
        else:
            stdscr.addstr('\nEnter a number.')
    return 0


def main(stdscr):
    stdscr.clear()
    curses.echo()
    mainFunc(stdscr)

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)