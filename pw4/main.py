from input  import *
from output import *
import curses

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