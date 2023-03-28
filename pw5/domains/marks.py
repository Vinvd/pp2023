from domains.courses import course
from domains.students import student


class mark(student, course):                                #mark_class
    def __init__(self, std, crs, mark):
        self.stdName   = std.print_std_name()
        self.crsName   = crs.print_crs_name()
        self.crsCredit = crs.print_crs_credit()
        self.__mark = mark

    def print_mark(self):
        return self.__mark
    
    def set_mark(self, mark):
        self.mark = mark

    def __str__(self):
        return f"Student: {self.stdName}, Course: {self.crsName}, Mark: {self.__mark}"