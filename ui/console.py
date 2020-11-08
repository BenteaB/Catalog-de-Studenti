from domain.entities import Student
from errors.exceptions import ValidationException,RepoException

class uiStudent:

    def __ui_add_student(self):
        idStudent = int(input('Introduceti id student: '))
        nume = input('Introduceti nume student: ')
        self.__controller_studenti.add_student(idStudent,nume)

    def __ui_print_studenti(self):
        studenti = self.__controller_studenti.get_studenti()
        if len(studenti) == 0:
            print('Nu exista studenti in catalog!')
            return
        for student in studenti:
            print(student)

    def __ui_del_student(self):
        idStudent = int(input('Introduceti id-ul studentului pe care doriti sa il stergeti: '))
        key_stud = Student(idStudent,'')
        self.__controller_studenti.del_student(key_stud)
        print('Studentul a fost sters din catalog!')

    def __ui_cauta_student(self):
        idStudent = int(input('Introduceti id-ul studentului pe care doriti sa il cautati: '))
        key_stud = Student(idStudent,'')
        result_student = self.__controller_studenti.cauta_student(key_stud)
        print("Studentul cautat este: ",result_student)

    def __ui_modifica_student(self):
        idStudent = int(input("Introduceti id-ul studentului caruia doriti sa ii modificati numele: "))
        nume = input("Introduceti numele nou al studentului: ")
        student = Student(idStudent,nume)
        self.__controller_studenti.modifica_student(student)

    def __init__(self,controller_studenti):
        self.__controller_studenti = controller_studenti
        self.__comenzi = {
            "add_student":self.__ui_add_student,
            "print_studenti":self.__ui_print_studenti,
            "del_student":self.__ui_del_student,
            "cauta_student":self.__ui_cauta_student,
            "modifica_student":self.__ui_modifica_student
        }

    def run(self):
        while True:
            cmd = input("\nDati comanda: ")
            if cmd == 'exit':
                print('\nSe va iesi din aplicatie...\n')
                return
            if cmd in self.__comenzi:
                try:
                    self.__comenzi[cmd]()
                except ValueError:
                    print('Valoare numerica invalida!')
                except ValidationException as ve:
                    print(ve)
                except RepoException as re:
                    print(re)
            else:
                print('Comanda invalida!')