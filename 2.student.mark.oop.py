class student:
    def __init__(self, StudentId, StudentnName, StudentDob):
        self.id = StudentId
        self.name = StudentnName
        self.dob = StudentDob

    def __str__(self):
        return f"Student: id: {self.id}, name: {self.name}, dob: {self.dob}."
    

class course:
    def __init__(self, CourseId, CourseName):
        self.id = CourseId
        self.name = CourseName

    def __str__(self):
        return f"id: {self.id}, Course name: {self.name}"

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
        for i in range(len(x)):
            print(x[i])
    elif y==2:
        for i in range(len(x)):
            print(x[i].id)        
    elif y==3:
        for i in range(len(x)):
            print(x[i].name)
    else:
        for i in range(len(x)):
            print(x[i].dob)        
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
            if int(type) in range(1,3):
                y = int(type)
        else:
            print('please type in a number')
    print('\n')
    if y==1:
        for i in range(len(x)):
            print(x[i])
    elif y==2:
        for i in range(len(x)):
            print(x[i].id)
    else:
        for i in range(len(x)):
            print(x[i].name)
    return 0

#main :

numStudent = input_num_students()
student_list = input_students_info(numStudent)
print_students_info(student_list)

numCourse = input_num_courses()
course_list = input_courses_info(numCourse)
print_courses_info(course_list)