from input  import *
from output import *
import curses
import os
import zipfile

student_file_name = "students.txt"
Student_filepath = os.path.join(os.path.dirname(__file__), student_file_name)
course_file_name = "courses.txt"
course_filepath = os.path.join(os.path.dirname(__file__), course_file_name)
mark_file_name = "marks.txt"
mark_filepath = os.path.join(os.path.dirname(__file__), mark_file_name)

data_file_name = "students.dat"
data_file_path = os.path.join(os.path.dirname(__file__), data_file_name)

def first_time_run(stdscr):
    stdscr.clear()

    numStudent = input_num_students(stdscr)
    student_list = input_students_info(numStudent,stdscr)

    numCourse = input_num_courses(stdscr)
    course_list = input_courses_info(numCourse,stdscr)

    marks_list= input_marks(course_list, student_list,stdscr)

    stdscr.clear()
    return student_list, course_list, marks_list

def mainFunc(stdscr,student_list, course_list, marks_list):

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
        stdscr.addstr('\n7. Re-input information')
        
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

            elif type == 7:
                y=0
                while y==0:
                    stdscr.addstr('\n1. Re-input students information')
                    stdscr.addstr('\n2. Re-input courses information')
                    stdscr.addstr('\n3. Re-input marks in a course')

                    stdscr.addstr('\nEnter a choice: \n')
                    type = stdscr.getstr()
                    type = type.decode('utf-8')
                    if type.isnumeric():
                        if int(type) in range(1,4):
                            y = int(type)
                        else:
                            stdscr.addstr('\nEnter a number in the list.')
                
                if y == 1:
                    numStudent = input_num_students(stdscr)
                    student_list = input_students_info(numStudent,stdscr)
                elif y == 2:
                    numCourse = input_num_courses(stdscr)
                    course_list = input_courses_info(numCourse,stdscr)
                else:
                    marks_list= input_marks(course_list, student_list,stdscr)

        else:
            stdscr.addstr('\nEnter a number.')
    stdscr.clear()

    files_name = [Student_filepath, course_filepath, mark_filepath]
    data_file = data_file_path

    with zipfile.ZipFile(data_file, mode="w") as zf:
        # loop through the input filenames and add each to the zip file
        for filename in files_name:
            zf.write(filename)
    stdscr.addstr(f'\nDone compressed into .dat files')
    return stdscr.addstr(f'\nEverything done. Press any key to exit.')

def main_call(stdscr):
    try:
        student_list,course_list,marks_list = read_from_dat(stdscr)
    except FileNotFoundError:
        student_list,course_list,marks_list = first_time_run(stdscr)
        mainFunc(stdscr,student_list, course_list, marks_list)
    else:
        mainFunc(stdscr,student_list, course_list, marks_list)

def main(stdscr):
    stdscr.clear()
    curses.echo()
    main_call(stdscr)

    stdscr.refresh()
    stdscr.getkey()

curses.wrapper(main)