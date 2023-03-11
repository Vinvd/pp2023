class student:
    def __init__(self, StudentId, StudentnName, StudentDob):
        self.__id = StudentId
        self.__name = StudentnName
        self.__dob = StudentDob

    def print_std_id(self):
        return self.__id
    def print_std_name(self):
        return self.__name
    def print_std_dob(self):
        return self.__dob

    def set_std_id(self, stdId):
        self.__id = stdId
    def set_std_name(self, stdName):
        self.__id = stdName
    def set_std_id(self, strDob):
        self.__id = strDob

    def __str__(self):
        return f"Student: id: {self.__id}, name: {self.__name}, dob: {self.__dob}."
    
class course:
    def __init__(self, CourseId, CourseName):
        self.__id = CourseId
        self.__name = CourseName

    def print_crs_id(self):
        return self.__id
    def print_crs_name(self):
        return self.__name
    
    def set_crs_id(self,crsID):
        self.__id = crsID
    def set_crs_name(self,crsName):
        self.__name = crsName
    
    def __str__(self):
        return f"id: {self.__id}, Course name: {self.__name}"
    
class mark(student, course):
    def __init__(self, std, crs, mark):
        self.stdName = std.print_std_name()
        self.crsName = crs.print_crs_name()
        self.__mark = mark

    def print_mark(self):
        return self.__mark

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
                
        print('\nInput the Id, name and DoB of the \"'+ str(i+1) +'\" student') 
        studentId = input('Id:')
        studentName = str(input('Name:'))
        studentDoB = str(input('Date:'))

        Student = student(studentId,studentName,studentDoB)

        students.append(Student)
    return students

def print_students_info(x):     #feed list of students in
    print('\nSelect a number to print: ')
    print('1: List all students and information')
    print('2: List all Id')
    print('3: List all names')
    print('4: List all Dob')

    y = 0
    while y == 0:
        type = input('enter number in the given list: ')
        if type.isnumeric():
            if int(type) in range(1,5):
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
    else:
        for i in range(len(x)):
            print(x[i].print_std_dob())        
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
        courseId = (input('Course Id:'))
        courseName = str(input('Course name:'))

        Course = course(courseId,courseName)        
        courses.append(Course)
    return courses

def print_courses_info(x):  #return info, need to eat course list
    print('\nSelect a number to print: ')
    print('1: List information of all courses')
    print('2: list all course id')
    print('3: List all course name')  

    y = 0
    while y == 0:
        type = input('enter number in the given list: ')
        if type.isnumeric():
            if int(type) in range(1,4):
                y = int(type)
        else:
            print('please type in a number')

    if y==1:
        for i in range(len(x)):
            print(x[i])
    elif y==2:
        for i in range(len(x)):
            print(x[i].print_crs_id())
    else:
        for i in x:
            print(i.print_crs_name())
    return 0

def input_marks(a,b,c):     # a is numcourse; b is list of courses; c is list students
    print('\nSelect number of a course to input students\' marks')
    a= int(a)
    for i in range(a):
        print(str(i+1)+ ': '+ b[i].print_crs_name())

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
            mark_in = input(f"mark of {c[i].print_std_name()}: ")
            if mark_in.isnumeric():
                mark_in = int(mark_in)
                y += 1
            else:
                print('please type in a number')

        S = mark(c[i], b[x-1], mark_in)
        List_mark.append(S)
        del S
    return List_mark

def print_marks(list_mark, list_course):         
    print('\nSelect a number of the course to show marks')
    for i in range(len(list_course)):
        print(str(i+1) + ': ' + list_course[i].print_crs_name())
    
    print('select course to output marks:')
    z = 0
    while z == 0:
        type = input('enter number in the given list: ')
        if type.isnumeric():
            if int(type) in range(1,len(list_course)+1):
                z = int(type)
        else:
            print('please type in a number')

    for i in list_mark:
        if (i.crsName) == (list_course[z-1].print_crs_name()):
            print(f'student: {i.stdName}, marks: {i.print_mark()}')
    
    return 0

#main :

numStudent = input_num_students()
student_list = input_students_info(numStudent)
print_students_info(student_list)

numCourse = input_num_courses()
course_list = input_courses_info(numCourse)
print_courses_info(course_list)

marks_list=input_marks(numCourse, course_list, student_list)
print_marks(marks_list, course_list)

print("\nDone input students, courses and marks!\n\nListing functions:")

x=0
while x==0:
    print('0. Esc')
    print('1. Print students information')
    print('2. Courses information')
    print('3. Show students mark in a course')
    type = input('Enter a choice: ')
    if type.isnumeric():
        if int(type) in range(4):
            type = int(type)
        else:
            print('Enter a number in the list.')
        if type == 0:
            x = x+1
        elif type == 1:
            print_students_info(student_list)
        elif type == 2:
            print_courses_info(course_list)
        else:
            print_marks(marks_list, course_list)
    else:
        print('Enter a number.')