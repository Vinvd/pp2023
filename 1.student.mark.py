"""
python program 1?
"""

numStudent = 0
while numStudent == 0:
    nhap = input('Input number of students in the class: ')
    if nhap.isnumeric():
        numStudent = int(nhap)
    else:
        print('please type in a number')

#print('There are '+ str(numStudent) +' students in the class')



studenId = []
studentName = []
DoB = []

for i in range(numStudent):
    studenId.append(i)
    studentName.append(i)
    DoB.append(i)
    
    print('Input the Id, name and DoB of the '+ str(i+1) +' student') 
    studenId[i] = (input('Id:'))
    studentName[i] = str(input('Name:'))
    DoB[i] = str(input('Date:'))

'''
print(studenId)
print(studentName[0])
print(studentName)
print(DoB)

leTroll 
'''


numCourse = 0
while   numCourse == 0:
    nhap = input('Input number of courses in this class: ')
    if nhap.isnumeric():
        numCourse = int(nhap)
    else:
        print('Plz enter a number')
#


courseId = []
courseName = []

for i in range(numCourse):
    courseId.append(i)
    courseName.append(i)

    print('Input the course id and the course name')
    courseId[i] = (input('course Id:'))
    courseName[i] = str(input('Course name:'))

'''
print(courseId)
print(courseName)
'''
print(courseId)
print(courseName)

#print('Select a course to input students\' marks by enter course name')
