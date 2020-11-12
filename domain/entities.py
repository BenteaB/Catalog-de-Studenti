class Student:

    def __init__(self, idStudent, nume):
        """
        Creeaza un student
        idStudent - numar
        nume - string
        """
        self.__idStudent = idStudent
        self.__nume = nume

    def get_idStudent(self):
        return self.__idStudent

    def get_nume(self):
        return self.__nume

    def set_nume(self,value):
        self.__nume = value
    
    def __str__(self):
        """
        Returneaza un string ce contine toate detaliile unui student
        """
        return str(self.__idStudent)+' '+self.__nume

    def __eq__(self,other):
        """
        Verifica daca doi studenti sunt egale (au acelasi id)
        """
        return self.__idStudent == other.__idStudent

class Disciplina:

    def __init__(self,idDisciplina,nume,profesor):
        """
        Creeaza o disciplina
        idDisciplina - numar
        nume,profesor - string
        """
        self.__idDisciplina = idDisciplina
        self.__nume = nume
        self.__profesor = profesor
    
    def get_idDisciplina(self):
        return self.__idDisciplina

    def get_nume(self):
        return self.__nume

    def get_profesor(self):
        return self.__profesor

    def set_nume(self,value):
        self.__nume = value

    def set_profesor(self,value):
        self.__profesor = value

    def __str__(self):
        """
        Returneaza un string ce contine toate detaliile unei discipline
        """
        return str(self.__idDisciplina)+' '+self.__nume+' '+self.__profesor
    
    def __eq__(self,other):
        """
        Verifica daca doua discipline sunt egale (au acelasi id)
        """
        return self.__idDisciplina == other.__idDisciplina

