from input  import *
from output import *
import curses
import os
import pickle

student_file_name = "students.txt"
Student_filepath = os.path.join(os.path.dirname(__file__), student_file_name)
course_file_name = "courses.txt"
course_filepath = os.path.join(os.path.dirname(__file__), course_file_name)
mark_file_name = "marks.txt"
mark_filepath = os.path.join(os.path.dirname(__file__), mark_file_name)

def mainFunc(stdscr):
    stdscr.clear()

    numStudent = input_num_students(stdscr)
    student_list = input_students_info(numStudent,stdscr)

    numCourse = input_num_courses(stdscr)
    course_list = input_courses_info(numCourse,stdscr)

    marks_list= input_marks(numCourse, course_list, student_list,stdscr)  
    
    stdscr.clear()
    x=0
    while x==0:
        stdscr.clear()
        stdscr.addstr('\n0. Esc')
        stdscr.addstr('\n1. Print students information')
        stdscr.addstr('\n2. Print courses information')
        stdscr.addstr('\n3. Show students mark in a course')
        stdscr.addstr('\n4. Calculate Gpa for a student')
        stdscr.addstr('\n5. Calculate Gpa for all students')
        stdscr.addstr('\n6. Sort descending student list by Gpa')

        stdscr.addstr('\nEnter a choice: \n')
        type = stdscr.getstr()
        type = type.decode('utf-8')

        if type.isnumeric():
            if int(type) in range(7):
                type = int(type)
            else:
                stdscr.addstr('\nEnter a number in the list.')

            if type == 0:
                x = x+1

            elif type == 1:
                print_students_info(student_list,stdscr)

            elif type == 2:
                print_courses_info(course_list,stdscr)

            elif type == 3:
                print_marks(marks_list, course_list,stdscr)

            elif type == 4:
                choosenOne = choose_student_toCal_gpa(student_list,stdscr)
                choosenOne_Gpa = calculate_student_gpa(marks_list, choosenOne,stdscr)
                assign_student_gpa(choosenOne_Gpa,student_list,choosenOne,stdscr)

            elif type == 5:
                student_list = calculate_all_student(student_list,marks_list,stdscr)

            elif type == 6:
                if student_list[0].print_std_gpa() == None:
                    stdscr.addstr('\ngpa have not ben calculated')
                    stdscr.getkey()
                else:
                    student_list = sort_student_list(student_list,stdscr)
        else:
            stdscr.addstr('\nEnter a number.')
    stdscr.clear()

    file = open(Student_filepath, "w")
    for i in student_list:
        stdscr.addstr(f'\n {i}')
        file.write(f'{i}\n')
    file.close()

    file = open(course_filepath, "w")
    for i in course_list:
        stdscr.addstr(f'\n {i}')
        file.write(f'{i}\n')
    file.close()

    file = open(mark_filepath, "w")
    for i in marks_list:
        stdscr.addstr(f'\n {i}')
        file.write(f'{i}\n')
    file.close()
    
    stdscr.clear()
    stdscr.addstr(f'\nDone write into .txt files')
        
    return stdscr.addstr(f'\nEverything done. Press any key to exit.')

def main(stdscr):
    stdscr.clear()
    curses.echo()
    mainFunc(stdscr)

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)