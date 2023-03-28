from domains.students   import student
from domains.courses    import course
from domains.marks      import mark

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
        for i in n:
            if i.print_std_gpa() == None:
                stdscr.addstr('\n the gpa calculate all have not run')
                break
            else:    
                y, x = stdscr.getyx()
                stdscr.addstr(y+1, 0,str(i.print_std_gpa()))                
        stdscr.refresh()

    stdscr.getkey()  
    stdscr.clear()
    return 0

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
