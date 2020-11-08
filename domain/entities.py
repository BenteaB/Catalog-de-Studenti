class Student:

    def __init__(self, idStudent, nume):
        self.__idStudent = idStudent
        self.__nume = nume

    def get_idStudent(self):
        return self.__idStudent

    def get_nume(self):
        return self.__nume

    def set_nume(self,value):
        self.__nume = value
    
    def __str__(self):
        return str(self.__idStudent)+' '+self.__nume

    def __eq__(self,other):
        return self.__idStudent == other.__idStudent