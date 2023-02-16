"""
python program 1?
"""

print('Input number of students in the class:')
numStudent = int(input(''))
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

print('Input the number of courses in this class: ')
numCourse = int(input(''))

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

print('Select a course to input students\' marks by enter course name')

