class student:                                 
    def __init__(self, StudentId, StudentnName, StudentDob, Gpa):
        self.__id = StudentId
        self.__name = StudentnName
        self.__dob = StudentDob
        self.__gpa = Gpa

    def print_std_id(self):
        return self.__id
    def print_std_name(self):
        return self.__name
    def print_std_dob(self):
        return self.__dob
    def print_std_gpa(self):
        return self.__gpa

    def set_std_id(self, stdId):
        self.__id = stdId
    def set_std_name(self, stdName):
        self.__name = stdName
    def set_std_id(self, strDob):
        self.__dob = strDob
    def set_std_gpa(self, Gpa):
        self.__gpa = Gpa

    def __str__(self):
        return f"id: {self.__id}, name: {self.__name}, dob: {self.__dob}."