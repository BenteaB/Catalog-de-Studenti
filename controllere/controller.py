from domain.entities import Student

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
