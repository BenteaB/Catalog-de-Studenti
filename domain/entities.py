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
        other - obiect de tip student
        """
        return self.__idStudent == other.__idStudent

    def __lt__(self,other):
        return self.__idStudent < other.__idStudent

    def __gt__(self,other):
        return self.__idStudent > other.__idStudent

    def __le__(self,other):
        return self.__idStudent <= other.__idStudent

    def __ge__(self,other):
        return self.__idStudent >= other.__idStudent

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
        other - obicet de tip disciplina
        """
        return self.__idDisciplina == other.__idDisciplina

    def __lt__(self,other):
        return self.__idDisciplina < other.__idDisciplina

    def __gt__(self,other):
        return self.__idDisciplina > other.__idDisciplina

    def __le__(self,other):
        return self.__idDisciplina <= other.__idDisciplina

    def __ge__(self,other):
        return self.__idDisciplina >= other.__idDisciplina

class Nota:

    def __init__(self,idNota,idStudent,idDisciplina,punctaj):
        """
        Creeaza un obiect de tip nota
        idNota,idStudent,idDisciplina - numar natural
        punctaj - numar rational
        """
        self.__idNota = idNota
        self.__idStudent = idStudent
        self.__idDisciplina = idDisciplina
        self.__punctaj = punctaj

    def get_idNota(self):
        return self.__idNota

    def get_idStudent(self):
        return self.__idStudent

    def get_idDisciplina(self):
        return self.__idDisciplina

    def get_punctaj(self):
        return self.__punctaj

    def set_punctaj(self,value):
        self.__punctaj = value

    def set_idStudent(self,value):
        self.__idStudent = value

    def set_idDisciplina(self,value):
        self.__idDisciplina = value

    def __str__(self):
        """
        Returneaza un string ce contine toate detaliile unei note
        """
        return str(self.__idNota)+' '+str(self.__idStudent)+' '+str(self.__idDisciplina)+' '+str(self.__punctaj)

    def __eq__(self,other):
        """
        Verifica daca doua note sunt egale (au acelasi id)
        other - obicet de tip nota
        """
        return self.__idNota == other.__idNota

    def __lt__(self,other):
        return self.__idNota < other.__idNota

    def __gt__(self,other):
        return self.__idNota > other.__idNota

    def __le__(self,other):
        return self.__idNota <= other.__idNota

    def __ge__(self,other):
        return self.__idNota >= other.__idNota

class StudentNotaDTO:
    
    def __init__(self,nume_stud,punctaj):
        self.__nume_stud = nume_stud
        self.__punctaj = punctaj

    def get_nume_stud(self):
        return self.__nume_stud
    
    def get_punctaj(self):
        return self.__punctaj

class StudentMedieDTO:

    def __init__(self,nume_stud,medie):
        self.__nume_stud = nume_stud
        self.__medie = medie

    def get_nume_stud(self):
        return self.__nume_stud
    
    def get_medie(self):
        return self.__medie
