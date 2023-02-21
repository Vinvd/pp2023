"""
python program 1?  
"""                 #need to use function(def) :D

numStudent = 0
while numStudent == 0:
    nhap = input('Input number of students in the class: ')
    if nhap.isnumeric():
        if int(nhap)>10:
            print('Are you sure?')
        numStudent = int(nhap)
    else:
        print('please type in a number')

#print('There are '+ str(numStudent) +' students in the class')

students = []
studentId = []
studentName = []
studentDoB = []

for i in range(numStudent):
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

print('Select a number to print: ')
print('1: List all student and information')
for i in range(3):
    key_student = list(students[0].keys())
    print(str(i+2)+ ": "+ key_student[i])

x = 0
while x == 0:
    nhap = input('enter number in the given list: ')
    if nhap.isnumeric():
        if int(nhap) in range(1,4):
            x = int(nhap)
    else:
        print('please type in a number')

if x==1:
    print(students)
elif x==2:
    print(studentId)
elif x==3:
   print(studentName)
else:
    print(studentDoB)

''' code check'''  #codeCheck #codeCheck #codeCheck #codeCheck #codeCheck #codeCheck 

'''print('all students:',end=' ')
print(students)
print(type(students))

print(students[0])
print(type(students[0]))

print(students[0]['Name'], students[0]['Id'])
print(type(students[0]['Name']))
'''
"""print(student)       #already deleted(del)
print(type(student))""" #this changed after each loop, only use studentS

'''print(studentId)
print(studentId[0])

print(studentName)
print(studentName[0])'''

'''               #codeCheck #codeCheck #codeCheck #codeCheck #codeCheck #codeCheck 
leTroll 
'''

numCourse = 0
while   numCourse == 0:
    nhap = input('Input number of courses in this class: ')
    if nhap.isnumeric():
        numCourse = int(nhap)
    else:
        print('Plz enter a number')

courseId = []
courseName = []
courses = []

for i in range(numCourse):
    courseId.append(i)
    courseName.append(i)

    print('Input the id and the name of the \"'+ str(i+1)+'\" course')
    courseId[i] = (input('Course Id:'))
    courseName[i] = str(input('Course name:'))

    course = {'id': courseId[i], 'name': courseName[i]}
    
    courses.append(course)
    del course                            

'''
print(courses)
print(courseId)
print(courseName)
'''
print('Select a course to input students\' marks')
for i in range(numCourse):
    print(str(i+1)+ ": "+ courseName[i])

x = 0
while   x == 0:
    nhap = input('select a course: ')
    if nhap.isnumeric():
        if (int(nhap)) in range(1,numCourse+1):
            x = int(nhap)
        else:
            print('form 1 to '+ str(numCourse))
    else:
        print('Plz enter a number in the given list')
