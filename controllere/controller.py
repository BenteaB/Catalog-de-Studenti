from domain.entities import Disciplina, Student

class ControllerStud:
    
    def __init__(self,repo_studenti,validator_studenti):
        self.__repo_studenti = repo_studenti
        self.__valid_studenti = validator_studenti
    
    def add_student(self,idStudent,nume):
        student = Student(idStudent,nume)
        self.__valid_studenti.valideaza(student)
        self.__repo_studenti.store(student)

    def del_student(self,key_stud):
        self.__repo_studenti.remove(key_stud)

    def cauta_student(self,key_stud):
        return self.__repo_studenti.search(key_stud)

    def modifica_student(self,student):
        self.__valid_studenti.valideaza(student)
        self.__repo_studenti.update(student)

    def get_studenti(self):
        return self.__repo_studenti.get_all()

    def get_nr_studenti(self):
        return len(self.__repo_studenti)

class ControllerDisc:

    def __init__(self,repo_discipline,validator_discipline):
        self.__repo_discipline = repo_discipline
        self.__validator_discipline = validator_discipline

    def add_disciplina(self,idDisciplina,nume,profesor):
        disciplina = Disciplina(idDisciplina,nume,profesor)
        self.__validator_discipline.valideaza(disciplina)
        self.__repo_discipline.store(disciplina)
    
    def del_disciplina(self,key_disc):
        self.__repo_discipline.remove(key_disc)

    def cauta_disciplina(self,key_disciplina):
        return self.__repo_discipline.search(key_disciplina)

    def modifica_disciplina(self,disciplina):
        self.__validator_discipline.valideaza(disciplina)
        self.__repo_discipline.update(disciplina)

    def get_discipline(self):
        return self.__repo_discipline.get_all()

    def get_nr_discipline(self):
        return len(self.__repo_discipline)
