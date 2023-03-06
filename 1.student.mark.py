# Students input
def input_num_students():       #return number of student
    nhap = input('Input number of students in the class: ')
    if nhap.isnumeric():
        numStudent = int(nhap)
    else:
        input_num_students()
    return numStudent

def input_students_info(x):     #return list of students
    students = []
    studentId = []
    studentName = []
    studentDoB = []
    for i in range(int(x)):
        studentId.append(i)
        studentName.append(i)
        studentDoB.append(i)
        
        print('Input the Id, name and DoB of the \"'+ str(i+1) +'\" student') 
        studentId[i] = (input('Id:'))
        studentName[i] = str(input('Name:'))
        studentDoB[i] = str(input('Date:'))

        student = {}
        student["Id"] = studentId[i]
        student["Name"] = studentName[i] 
        student["DoB"] = studentDoB[i]

        students.append(student)
        del student                 #not necessary because python clear it?
    return students

def print_students_info(x):     #feed list student in
    print('Select a number to print: ')
    print('1: List all students and information')
    for i in range(3):
        key_student = list(x[0].keys())
        print(str(i+2)+ ": "+ key_student[i])

    y = 0
    while y == 0:
        nhap = input('enter number in the given list: ')
        if nhap.isnumeric():
            if int(nhap) in range(1,4):
                y = int(nhap)
        else:
            print('please type in a number')

    if y==1:
        print(x)
    elif y==2:
        for i in range(len(x)):
            print(x[i]['Id'])        
    elif y==3:
        for i in range(len(x)):
            print(x[i]['Name'])
    else:
        for i in range(len(x)):
            print(x[i]['DoB'])        
    
    return 0

''' code check'''  #codeCheck #codeCheck #codeCheck #codeCheck #codeCheck #codeCheck 
# i need this but how to minimal ?
'''print('all students:',end=' ')
print(type(students))
print(type(students[0]))

print(students[0]['Name'], students[0]['Id'])
print(type(students[0]['Name']))

"""print(student)       #already deleted(del)
print(type(student))""" #this changed after each loop, only use studentS
     
leTroll 
'''                       #codeCheck #codeCheck #codeCheck #codeCheck #codeCheck #codeCheck 

# Input courses
def input_num_courses():    # return number of courses
    nhap = input('Input number of courses in this class: ')
    if nhap.isnumeric():
        numCourse = int(nhap)
    else:
        input_num_courses()
    return numCourse

def input_courses_info(x):  #return list of courses; need to eat an int
    courses = []
    courseId = []
    courseName = []
    for i in range(int(x)):
        courseId.append(i)
        courseName.append(i)

        print('Input the id and the name of the \"'+ str(i+1)+'\" course')
        courseId[i] = (input('Course Id:'))
        courseName[i] = str(input('Course name:'))

        course = {'id': courseId[i], 'name': courseName[i]}
        
        courses.append(course)
        del course                            
    return courses

def print_courses_info(x):  #return info, need to eat course list
    print('Select a number to print: ')
    print('1: List information of all courses')
    for i in range(2):
        key_courses = list(x[0].keys())
        print(str(i+2)+ ": "+ key_courses[i])

    y = 0
    while y == 0:
        nhap = input('enter number in the given list: ')
        if nhap.isnumeric():
            if int(nhap) in range(1,3):
                y = int(nhap)
        else:
            print('please type in a number')

    if y==1:
        print(x)
    elif y==2:
        for i in range(len(x)):
            print(x[i]['id'])
    else:
        for i in range(len(x)):
            print(x[i]['name'])
    return 0

def input_marks(a,b,c):     # a is numcourse; b is list of courses; c is list students
    print('Select a course to input students\' marks')
    a= int(a)
    for i in range(a):
        print(str(i+1)+ ": "+ b[i]['name'])

    x = 0
    while   x == 0:
        nhap = input('select a course: ')
        if nhap.isnumeric():
            if (int(nhap)) in range(1,a+1):
                x = int(nhap)
            else:
                print('form 1 to '+ str(a))
        else:
            print('Plz enter a number in the given list')
    
    print("Enter points of course "+ b[x-1]['name'])
    L = []
    for i in range(len(c)):
        mark = int(input('mark of '+ c[i]['Name']+ ' :' ))

        S = {'name': c[i]['Name'], 'mark': int(mark)}
        L.append(S)
        del S

    b[x-1]['mark'] = L
    return b

def show_marks(a):          # a is list of courses with marks
    for i in range(len(a)):
        print(str(i+1) + ': ' + a[i]['name'])  
    print('select course to output marks:')
    
    y = 0
    while y == 0:
        nhap = input('enter number in the given list: ')
        if nhap.isnumeric():
            if int(nhap) in range(1,len(a)+1):
                y = int(nhap)
        else:
            print('please type in a number')

    if 'mark' in a[y-1]:
        print(a[y-1]['mark'])
    
    return 0

#main func:

numstu = input_num_students()

student_list = input_students_info(numstu)

print_students_info(student_list)

numCours= input_num_courses()

course_list = input_courses_info(numCours)

print_courses_info(course_list)

courseList_w_Marks = input_marks(numCours,course_list,student_list)

show_marks(courseList_w_Marks)

print("Done input students, courses and marks!")

