import numpy as np
import math
# import curses

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

def input_num_students():       #return number of student
    type = input('Input number of students in the class: ')
    if type.isnumeric():
        numStudent = int(type)
    else:
        input_num_students()
    return numStudent

def input_students_info(x):     #return list of students
    students = []
    
    for i in range(int(x)):
                
        print(f'\nInput the Id, name and DoB of student \"{str(i+1)}\"') 
        studentId = input('Id:')
        studentName = str(input('Name:'))
        studentDoB = str(input('Date:'))

        Student = student(studentId,studentName,studentDoB,None)
        students.append(Student)
    return students

def print_students_info(x):     #feed list of students in
    print('\nSelect a number to print: ')
    print('1: List all students and information')
    print('2: List all Id')
    print('3: List all names')
    print('4: List all Dob')
    print('5: list student gpa')

    y = 0
    while y == 0:
        type = input('enter number in the given list: ')
        if type.isnumeric():
            if int(type) in range(1,6):
                y = int(type)
        else:
            print('please type in a number')

    if y==1:
        for i in x:
            print(i)
    elif y==2:
        for i in range(len(x)):
            print(x[i].print_std_id())
    elif y==3:
        for i in x:
            print(i.print_std_name())
    elif y==4:
        for i in range(len(x)):
            print(x[i].print_std_dob())        
    elif y==5:
        for i in x:
            print(i.print_std_gpa())
    return 0

def input_num_courses():    # return number of courses
    type = input('\nInput number of courses in this class: ')
    if type.isnumeric():
        numCourse = int(type)
    else:
        input_num_courses()
    return numCourse

def input_courses_info(x):  #return list of courses; need to eat an int
    courses = []
    for i in range(int(x)):

        print('Input the id and the name of the \"'+ str(i+1)+'\" course')
        courseId = (input('\nCourse Id:'))
        courseName = str(input('Course name:'))
        x = 0
        while   x == 0:
            type = input('Course credit: ')
            if type.isnumeric():
                courseCredit = int(type)
                x += 1
            else:
                print('Credit is a number ')

        Course = course(courseId,courseName,courseCredit)        
        courses.append(Course)
    return courses

def print_courses_info(x):  #return info, need to eat course list
    print('\nSelect a number to print: ')
    print('1: List information of all courses')
    print('2: list all course id')
    print('3: List all course name')  
    print('4: Show courses credit')

    y = 0
    while y == 0:
        type = input('enter number in the given list: \n')
        if type.isnumeric():
            if int(type) in range(1,5):
                y = int(type)
        else:
            print('please type in a number')

    if y == 1:
        for i in range(len(x)):
            print(x[i])
    elif y == 2:
        for i in range(len(x)):
            print(x[i].print_crs_id())
    elif y == 3:
        for i in x:
            print(i.print_crs_name())
    elif y ==4:
        for i in x:
            print(i.print_crs_credit())
    return 0

def input_marks(a,b,c):     # a is numcourse; b is list of courses; c is list students
    print('\nSelect number of a course to input students\' marks')
    a= int(a)
    for i in range(a):
        print(f'{str(i+1)}: {b[i].print_crs_name()}')

    x = 0
    while   x == 0:
        type = input('select a course: ')
        if type.isnumeric():
            if (int(type)) in range(1,a+1):
                x = int(type)
            else:
                print('form 1 to '+ str(a))
        else:
            print('Plz enter a number in the given list')

    print(f"Enter points of course {b[x-1].print_crs_name()}: ")
    List_mark = []
    for i in range(len(c)):
        y = 0
        while y == 0:
            while True: # loop until valid data is entered
                mark_in = input(f"mark of {c[i].print_std_name()}: ")
                try:
                    mark_in = float(mark_in)    # convert string to float
                    print("Valid float number:", mark_in)
                    y += 1
                    break                       # exit the loop
                except ValueError:              # catch exception if conversion fails
                    print("Invalid float number:", mark_in)

        mark_in = math.floor(mark_in)
        S = mark(c[i], b[x-1], mark_in)
        List_mark.append(S)
        del S
    return List_mark

def print_marks(list_mark, list_course):         
    print('\nSelect a number of the course to show marks')
    print('0: all ')
    for i in range(len(list_course)):
        print(str(i+1) + ': ' + list_course[i].print_crs_name())
    print('select course to output marks:')

    z = (len(list_course)+2)
    while z == (len(list_course)+2):
        type = input('enter number in the given list: \n')
        if type.isnumeric():
            if int(type) in range(len(list_course)+1):
                z = int(type)
        else:
            print('please type in a number')
    if z == 0:
        for i in list_mark:
                print(f'student: {i.stdName},course: {i.crsName}, marks: {i.print_mark()}')
    else:
        print('\n')
        for i in list_mark:
            if (i.crsName) == (list_course[z-1].print_crs_name()):
                print(f'student: {i.stdName}, marks: {i.print_mark()}')

    return 0

def choose_student_toCal_gpa(student_list):
    for i in range(len(student_list)):
        print(f'{i+1}: {student_list[i].print_std_name()}')
    y = 0
    while y == 0:
        type = input('enter number in the given list: ')
        if type.isnumeric():
            if int(type) in range(1,((len(student_list))+ 1)):
                y = int(type)
        else:
            print('please type in a number') 
    print(f'CHOOSEN: {student_list[y-1].print_std_name()}')
    return student_list[y-1].print_std_name()
    
def calculate_student_gpa(mark_list, std_name):
    only_marks = []
    only_credits = []

    for i in mark_list:
        if i.stdName == std_name:
            mark = i.print_mark()
            only_marks.append(mark)

            credit = i.crsCredit
            only_credits.append(credit)
    print(f'marks: {only_marks}')
    print(f'credits: {only_credits}')

    marks_np = np.array(only_marks)
    credits_np = np.array(only_credits)

    gpa = np.sum(marks_np * credits_np) / np.sum(credits_np)
    gpa = np.round(gpa,5)
    print(gpa)
    return gpa

def assign_student_gpa(gpa,student_list,choosen_One):
    for i in range(len(student_list)):
        if student_list[i].print_std_name() == choosen_One:
            student_list[i].set_std_gpa(gpa)
            print(f'student: {student_list[i].print_std_name()}, ',end='') 
            print(f'gpa: {student_list[i].print_std_gpa()}')
            print('\nAssigned\n')
    return student_list                 # :)

def calculate_all_student(student_list):
    for i in student_list:
        the_one = i.print_std_name()
        gpa = calculate_student_gpa(marks_list, the_one)
        new_studentGpa_list=assign_student_gpa(gpa,student_list, the_one)
    return new_studentGpa_list

def sort_student_list(student_list):
        
    # create a numpy array of gpa
    Gpas = np.array([person.print_std_gpa() for person in student_list])
    indices = np.argsort(Gpas)
        
    sorted_student_list = [student_list[i] for i in indices]
    for i in sorted_student_list:
        print(f'student: {i.print_std_name()}, gpa: {i.print_std_gpa()}')
    return sorted_student_list

#main :
numStudent = input_num_students()
student_list = input_students_info(numStudent)

numCourse = input_num_courses()
course_list = input_courses_info(numCourse)

x=0
while x==0:
    print('\n0. Esc')
    print('1. Input marks')
    print('2. Print students information')
    print('3. Print courses information')
    print('4. Show students mark in a course')
    print('5. Calculate Gpa for a student')
    print('6. Calculate Gpa for all students')
    print('7. Sort student list by Gpa')

    type = input('Enter a choice: \n')
    if type.isnumeric():
        if int(type) in range(8):
            type = int(type)
        else:
            print('Enter a number in the list.')

        if type == 0:
            x = x+1
        elif type == 1:
            if 'marks_list' in globals():
                print('\n1: Add more mark')
                print('2: clear marks')
      
                z = 0
                while z == 0:
                    type = input('Enter a choice: \n')
                    if type.isnumeric():
                        if int(type) in range(1,3):
                            z = int(type)
                        else:
                            print('Enter a number in the list.')
                            
                        if z == 1:
                            a = marks_list    
                            b = input_marks(numCourse, course_list, student_list)
                            a.extend(b) 
                            marks_list = a
                        if z == 2:
                            del marks_list
            else:
                marks_list=input_marks(numCourse, course_list, student_list)   
        elif type == 2:
            print_students_info(student_list)
        elif type == 3:
            print_courses_info(course_list)
        elif type == 4:
            print_marks(marks_list, course_list)
        elif type == 5:
            choosenOne = choose_student_toCal_gpa(student_list)
            choosenOne_Gpa = calculate_student_gpa(marks_list, choosenOne)
            assign_student_gpa(choosenOne_Gpa,student_list,choosenOne)
        elif type == 6:
            student_list = calculate_all_student(student_list)
        elif type == 7:
            sorted_list = sort_student_list(student_list)
    else:
        print('Enter a number.')