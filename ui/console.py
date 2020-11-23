from domain.entities import Disciplina, Student, Nota
from errors.exceptions import ValidationException,RepoException

class uiStudent:

    def __ui_add_student(self):
        """
        Citirea de la consola a datelor pentru adaugarea de student
        """
        idStudent = int(input('Introduceti id student: '))
        nume = input('Introduceti nume student: ')
        self.__controller_studenti.add_student(idStudent,nume)

    def __ui_print_studenti(self):
        """
        Afiseaza toti studentii
        """
        studenti = self.__controller_studenti.get_studenti()
        if len(studenti) == 0:
            print('Nu exista studenti in catalog!')
            return
        for student in studenti:
            print(student)

    def __ui_del_student(self):
        """
        Citirea de la consola a datelor pentru stergerea unui student
        """
        idStudent = int(input('Introduceti id-ul studentului pe care doriti sa il stergeti: '))
        key_stud = Student(idStudent,'')
        self.__controller_studenti.del_student(key_stud)
        print('Studentul a fost sters din catalog!')

    def __ui_cauta_student(self):
        """
        Citirea de la consola a datelor pentru cautarea unui student
        """
        idStudent = int(input('Introduceti id-ul studentului pe care doriti sa il cautati: '))
        key_stud = Student(idStudent,'')
        result_student = self.__controller_studenti.cauta_student(key_stud)
        print("Studentul cautat este: ",result_student)

    def __ui_modifica_student(self):
        """
        Citirea de la consola a datelor pentru modificarea unui student
        """
        idStudent = int(input("Introduceti id-ul studentului caruia doriti sa ii modificati numele: "))
        nume = input("Introduceti numele nou al studentului: ")
        student = Student(idStudent,nume)
        self.__controller_studenti.modifica_student(student)

    def __ui_genereaza_studenti(self):
        nr_studenti = int(input("Introduceti numarul de studenti: "))
        self.__controller_studenti.genereaza_studenti(nr_studenti)

    def __init__(self,controller_studenti):
        self.__controller_studenti = controller_studenti
        self.__comenzi = {
            "add_student":self.__ui_add_student,
            "print_studenti":self.__ui_print_studenti,
            "del_student":self.__ui_del_student,
            "cauta_student":self.__ui_cauta_student,
            "modifica_student":self.__ui_modifica_student,
            "genereaza_studenti":self.__ui_genereaza_studenti
        }
        self.__meniu = [
            '• add_student => Adauga un student in catalog',
            '• del_student => Sterge un student din catalog',
            '• cauta_student => Cauta un student dupa id-ul lui',
            '• modifica_student => Modifica numele corespunzator unui student',
            '• print_studenti => Afiseaza toti studenti',
            '• genereaza_studenti => Afiseaza toti studenti',
            '• exit => Inchide sub-meniul'
        ]

    def run(self):
        while True:
            print("\n******** Studenti ********")
            for op in self.__meniu:
                print(op)
            print('*************************')

            cmd = input("\nDati comanda: ")
            if cmd == 'exit':
                print('\nSe va iesi din sub-meniu!\n')
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
    
class uiDisciplina:
    
    def __ui_add_disciplina(self):
        """
        Citirea de la consola a datelor pentru adaugarea unei discipline
        """
        idDisciplina = int(input('Introduceti id disciplina: '))
        nume = input('Introduceti numele disciplinei: ')
        profesor = input('Introduceti numele profesorului: ')
        self.__controller_disciplina.add_disciplina(idDisciplina,nume,profesor)

    def __ui_print_discipline(self):
        """
        Afisarea tuturor disciplinelor
        """
        discipline = self.__controller_disciplina.get_discipline()
        if len(discipline) == 0:
            print('Nu exista discipline in catalog')
            return
        for disciplina in discipline:
            print(disciplina)

    def __ui_del_disciplina(self):
        """
        Citirea de la consola a datelor pentru stergerea unei discipline
        """
        idDisciplina = int(input('Introduceti id-ul disciplinei pe care doriti sa o stergeti: '))
        key_disc = Disciplina(idDisciplina,'','')
        self.__controller_disciplina.del_disciplina(key_disc)
        print('Disciplina a fost stearsa din catalog!')
    
    def __ui_cauta_disciplina(self):
        """
        Citirea de la consola a datelor pentru cautarea unei discipline
        """
        idDisciplina = int(input('Introduceti id-ul disciplinei pe care doriti sa o cautati: '))
        key_disc = Disciplina(idDisciplina,'','')
        result_disciplina = self.__controller_disciplina.cauta_disciplina(key_disc)
        print("Disciplina cautata este: ",result_disciplina)
    
    def __ui_modifica_disciplina(self):
        """
        Citirea de la consola a datelor pentru modificarea unei discipline
        """
        idDisciplina = int(input('Introduceti id-ul disciplinei pe care doriti sa o modificati: '))
        nume = input('Introduceti numele nou al disciplinei: ')
        profesor = input('Introduceti numele nou al profesorului: ')
        disciplina = Disciplina(idDisciplina,nume,profesor)
        self.__controller_disciplina.modifica_disciplina(disciplina)
    
    def __init__(self,controller_disciplina):
        self.__controller_disciplina = controller_disciplina
        self.__comenzi = {
            "add_disciplina":self.__ui_add_disciplina,
            "print_discipline":self.__ui_print_discipline,
            "del_disciplina":self.__ui_del_disciplina,
            "cauta_disciplina":self.__ui_cauta_disciplina,
            "modifica_disciplina":self.__ui_modifica_disciplina
        }
        self.__meniu = [
            '• add_disciplina => Adauga o disciplina in catalog',
            '• del_disciplina => Sterge o disciplina din catalog',
            '• cauta_disciplina => Cauta o disciplina dupa id-ul ei',
            '• modifica_disciplina => Modifica numele si profesorul corespunzatoare unei discipline',
            '• print_discipline => Afiseaza toate disciplinele',
            '• exit => Inchide sub-meniul'
        ]

    def run(self):
        while True:
            print("\n******** Discipline ********")
            for op in self.__meniu:
                print(op)
            print('*************************')

            cmd = input("\nDati comanda: ")
            if cmd == 'exit':
                print('\nSe va iesi din sub-meniu!\n')
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

class uiCatalog:

    def __init__(self,controller_note):
        self.__controller_note = controller_note
        self.__comenzi = {
            "add_nota":self.__ui_add_nota,
            "print_note":self.__ui_print_note,
            "del_nota":self.__ui_del_nota,
            "cauta_nota":self.__ui_cauta_nota,
            "modifica_nota":self.__ui_modifica_nota
        }
        self.__meniu = [
            '• add_nota => Adauga o nota in catalog',
            '• del_nota => Sterge o nota din catalog',
            '• cauta_nota => Cauta o nota dupa id-ul ei',
            '• modifica_nota => Modifica punctajul corespunzator unei note',
            '• print_note => Afiseaza toate notele',
            '• exit => Inchide sub-meniul'
        ]

    def __ui_add_nota(self):
        idNota = int(input("Introduceti id nota: "))
        idStudent = int(input("Introduceti id student: "))
        idDisciplina = int(input("Introduceti id disciplina: "))
        punctaj = float(input("Introduceti punctajul: "))
        self.__controller_note.add_nota(idNota,idStudent,idDisciplina,punctaj)

    def __ui_print_note(self):
        note = self.__controller_note.get_note()
        if len(note) == 0:
            print('Nu exista note in catalog!')
            return
        for nota in note:
            print(nota)

    def __ui_del_nota(self):
        idNota = int(input('Introduceti id-ul notei pe care doriti sa o stergeti: '))
        key_nota = Nota(idNota,0,0,0)
        self.__controller_note.del_nota(key_nota)
        print('Nota a fost stearsa din catalog!')

    def __ui_cauta_nota(self):
        idNota = int(input('Introduceti id-ul notei pe care doriti sa o cautati: '))
        key_nota = Nota(idNota,0,0,0)
        result_nota = self.__controller_note.cauta_nota(key_nota)
        print('Nota cautata este: ',result_nota)
    
    def __ui_modifica_nota(self):
        idNota = int(input('Introduceti id-ul notei careia doriti sa ii modificati punctajul: '))
        punctaj = float(input('Introduceti noul punctaj: '))
        nota = Nota(idNota,0,0,punctaj)
        result_nota = self.__controller_note.cauta_nota(nota)
        nota.set_idStudent(result_nota.get_idStudent())
        nota.set_idDisciplina(result_nota.get_idDisciplina())
        self.__controller_note.modifica_nota(nota)

    def run(self):
        while True:
            print("\n******** Catalog ********")
            for op in self.__meniu:
                print(op)
            print('***************************')

            cmd = input("\nDati comanda: ")
            if cmd == 'exit':
                print('\nSe va iesi din sub-meniu!\n')
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

class uiStatistici:

    def __init__(self,controller_note):
        self.__controller_note = controller_note
        self.__comenzi = {
            "lista_disciplina_note":self.__ui_disc_note,
            "lista_disciplina_nume":self.__ui_disc_nume,
            "lista_medii":self.__ui_medii_20p
        }
        self.__meniu = {
            '• lista_disciplina_note => Afisarea listei de studenti si a notelor lor la o disciplina ordonata descrescator dupa nota',
            '• lista_disciplina_nume => Afisarea listei de studenti si a notelor lor la o disciplina ordonata alfabetic dupa nume',
            '• lista_medii => Afisarea listei cu primii 20{} studenti in ordinea mediilor'.format('%'),
            '• exit => Inchide sub-meniul'
        }

    def __ui_disc_note(self):
        idDisciplina = int(input("Introduceti id-ul disciplinei pentru care se genereaza lista: "))
        lista = self.__controller_note.get_note_disc(idDisciplina)
        sorted_list = self.__controller_note.sorteaza_desc_nota(lista)

        for elem in sorted_list:
            print("Studentul",elem.get_nume_stud(),"cu nota",elem.get_punctaj())

    def __ui_disc_nume(self):
        idDisciplina = int(input("Introduceti id-ul disciplinei pentru care se genereaza lista: "))
        lista = self.__controller_note.get_note_disc(idDisciplina)
        sorted_list = self.__controller_note.sorteaza_alf_nume(lista)

        for elem in sorted_list:
            print("Studentul",elem.get_nume_stud(),"cu nota",elem.get_punctaj())

    def __ui_medii_20p(self):
        print("Primii 20 la suta studenti sunt: ")
        lista_medii = self.__controller_note.get_medii_stud()
        sorted_list = sorted(lista_medii, key=lambda stud_medie: stud_medie.get_medie(),reverse=True)
        
        primii = max(len(sorted_list)/5,1)
        sorted_list = sorted_list[:primii]

        for elem in sorted_list:
            print("Studentul",elem.get_nume_stud(),"cu media",elem.get_medie())

    def run(self):
        while True:
            print("\n******** Statistici ********")
            for op in self.__meniu:
                print(op)
            print('***************************')

            cmd = input("\nDati comanda: ")
            if cmd == 'exit':
                print('\nSe va iesi din sub-meniu!\n')
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

class uiMain:

    def __init__(self,controller_studenti,controller_discipline,controller_note):
        self.__ui_student = uiStudent(controller_studenti)
        self.__ui_disciplina = uiDisciplina(controller_discipline)
        self.__ui_catalog = uiCatalog(controller_note)
        self.__ui_statistici = uiStatistici(controller_note)
        self.__comenzi = {
            '1':self.__ui_student.run,
            '2':self.__ui_disciplina.run,
            '3':self.__ui_catalog.run,
            '4':self.__ui_statistici.run
        }
        self.__meniu = [
            '1. Meniu Studenti',
            '2. Meniu Discipline',
            '3. Meniu Catalog',
            '4. Meniu Statistici',
            'exit. Inchide Aplicatia'
        ]

    def run(self):
        while True:
            print("\n******** CATALOG ********")
            for op in self.__meniu:
                print(op)
            print('*************************')

            cmd = input("\nDati numarul sub-meniului: ")
            if cmd == 'exit':
                print('\nSe va inchide aplicatia...\n')
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
