class course:                                     
    def __init__(self, CourseId, CourseName, CourseCredit):
        self.__id = CourseId
        self.__name = CourseName
        self.__credit = CourseCredit

    def print_crs_id(self):
        return self.__id
    def print_crs_name(self):
        return self.__name
    def print_crs_credit(self):
        return self.__credit
    
    def set_crs_id(self,crsID):
        self.__id = crsID
    def set_crs_name(self,crsName):
        self.__name = crsName
    def set_crs_credit(self,crsCreddit):
        self.__credit = crsCreddit
    
    def __str__(self):
        return f"id: {self.__id}, Course name: {self.__name}, credit: {self.__credit}"