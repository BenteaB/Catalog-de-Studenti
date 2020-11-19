import random
import string
from domain.entities import Disciplina, Student, Nota

class ControllerStud:
    
    def __init__(self,repo_studenti,validator_studenti,repo_note):
        """
        Initializeaza controllerul de studenti
        repo_studenti - obiect ce retine studentii
        validator_studenti - obiect ce valideaza studentii
        """
        self.__repo_studenti = repo_studenti
        self.__valid_studenti = validator_studenti
        self.__repo_note = repo_note
    
    def add_student(self,idStudent,nume):
        """
        Adauga un student in repository
        idStudent - numar
        nume - string
        """
        student = Student(idStudent,nume)
        self.__valid_studenti.valideaza(student)
        self.__repo_studenti.store(student)

    def del_student(self,key_stud):
        """
        Sterge un student din repository
        key_stud - obiect de tip student
        """
        self.__repo_studenti.remove(key_stud)
        idStudent = key_stud.get_idStudent()
        self.__repo_note.remove_stud(idStudent)

    def cauta_student(self,key_stud):
        """
        Cauta un student in repository
        key_stud - obiect de tip student
        """
        return self.__repo_studenti.search(key_stud)

    def modifica_student(self,student):
        """
        Modifica un student din repository
        student - obiect de tip student
        """
        self.__valid_studenti.valideaza(student)
        self.__repo_studenti.update(student)

    def get_studenti(self):
        return self.__repo_studenti.get_all()

    def get_nr_studenti(self):
        return len(self.__repo_studenti)

    def genereaza_studenti(self,nr):
        for i in range(0,nr):
            idStudent = random.randint(1,100)
            letters = string.ascii_lowercase
            nume = ''.join(random.choice(letters) for j in range(1,10))
            student = Student(idStudent,nume)
            self.__valid_studenti.valideaza(student)
            self.__repo_studenti.store(student)

class ControllerDisc:

    def __init__(self,repo_discipline,validator_discipline):
        """
        Initializeaza controllerul de discipline
        repo_discipline - obiect ce retine disciplinele
        validator_discipline - obiect ce valideaza disciplinele
        """
        self.__repo_discipline = repo_discipline
        self.__validator_discipline = validator_discipline

    def add_disciplina(self,idDisciplina,nume,profesor):
        """
        Adauga o disciplina in repository
        idDisciplina - numar
        nume - string
        """
        disciplina = Disciplina(idDisciplina,nume,profesor)
        self.__validator_discipline.valideaza(disciplina)
        self.__repo_discipline.store(disciplina)
    
    def del_disciplina(self,key_disc):
        """
        Sterge o disciplina din repository
        key_disc - obiect de tip disciplina
        """
        self.__repo_discipline.remove(key_disc)

    def cauta_disciplina(self,key_disciplina):
        """
        Cauta o disciplina in repository
        key_disc - obiect de tip disciplina
        """
        return self.__repo_discipline.search(key_disciplina)

    def modifica_disciplina(self,disciplina):
        """
        Modifica o disciplina din repository
        disciplina - obiect de tip disciplina
        """
        self.__validator_discipline.valideaza(disciplina)
        self.__repo_discipline.update(disciplina)

    def get_discipline(self):
        return self.__repo_discipline.get_all()

    def get_nr_discipline(self):
        return len(self.__repo_discipline)

class ControllerNote:

    def __init__(self,repo_note,validator_note,repo_studenti,repo_discipline):
        self.__repo_note = repo_note
        self.__valid_note = validator_note
        self.__repo_studenti = repo_studenti
        self.__repo_discipline = repo_discipline

    def add_nota(self,idNota,idStudent,idDisciplina,punctaj):
        nota = Nota(idNota,idStudent,idDisciplina,punctaj)
        self.__valid_note.valideaza(nota,self.__repo_studenti,self.__repo_discipline)
        self.__repo_note.store(nota)

    def del_nota(self,key_nota):
        self.__repo_note.remove(key_nota)

    def cauta_nota(self,key_nota):
        return self.__repo_note.search(key_nota)

    def modifica_nota(self,nota):
        self.__valid_note.valideaza(nota,self.__repo_studenti,self.__repo_discipline)
        self.__repo_note.update(nota)

    def get_note(self):
        return self.__repo_note.get_all()

    def get_nr_note(self):
        return len(self.__repo_note)

