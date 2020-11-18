from domain.entities import Disciplina, Student, Nota
from validation.validators import ValidatorDisc, ValidatorStud, ValidatorNota
from errors.exceptions import ValidationException,RepoException
from infrastructure.repository import RepositoryDisc, RepositoryNote, RepositoryStud
from controllere.controller import ControllerStud,ControllerDisc,ControllerNote
 
class Tests:
    
    def __run_domain_tests(self):
        """
        Functie de test pentru entitati
        """
        #STUDENT
        IDStudent = 24
        nume1 = 'nume1'
        student1 = Student(IDStudent,nume1)
        assert student1.get_idStudent() == 24
        assert student1.get_nume() == 'nume1'
        assert str(student1) == '24 nume1'
        nume2 = 'nume2'
        student2 = Student(IDStudent,nume2)
        assert student1 == student2

        #DISCIPLINA
        idDisciplina = 10
        nume1 = 'nume1'
        profesor1 = 'profesor1'
        disciplina1 = Disciplina(idDisciplina,nume1,profesor1)
        assert disciplina1.get_idDisciplina() == 10
        assert disciplina1.get_nume() == 'nume1'
        assert disciplina1.get_profesor() == 'profesor1'
        nume2 = 'nume2'
        profesor2 = 'profesor2'
        disciplina2 = Disciplina(idDisciplina,nume2,profesor2)
        assert disciplina1 == disciplina2

        #NOTA
        idDisciplina = 10
        nume1 = 'nume1'
        profesor1 = 'profesor1'
        disciplina1 = Disciplina(idDisciplina,nume1,profesor1)
        idStudent = 24
        nume1 = 'nume1'
        student1 = Student(idStudent,nume1)
        punctaj = 9.6
        idNota = 7
        nota = Nota(idNota,idStudent,idDisciplina,punctaj)
        assert nota.get_idNota() == 7
        assert nota.get_idStudent() == 24
        assert nota.get_idDisciplina() == 10
        assert nota.get_punctaj() == 9.6

    def __run_validation_tests(self):
        """
        Functie de test pentru validari
        """
        #STUDENT
        student = Student(-23,"")
        validator_Stud = ValidatorStud()
        try:
            validator_Stud.valideaza(student)
            assert False
        except ValidationException as ve:
            assert str(ve) == "id invalid!\nnume invalid!\n"
        student_valid = Student(40,"alex")
        validator_Stud.valideaza(student_valid)
        assert True

        #DISCIPLINA
        disciplina = Disciplina(-59,'','')
        validator_Disc = ValidatorDisc()
        try:
            validator_Disc.valideaza(disciplina)
            assert False
        except ValidationException as ve:
            assert str(ve) == 'id invalid!\nnume invalid!\nprofesor invalid!\n'
        disciplina_valida = Disciplina(59,'matematica','prof')
        validator_Disc.valideaza(disciplina_valida)
        assert True

        #NOTA
        nota = Nota(-1,-25,-28,0.5)
        validator_Nota = ValidatorNota()
        try:
            validator_Nota.valideaza(nota)
            assert False
        except ValidationException as ve:
            assert str(ve) == 'id invalid!\nid student invalid!\nid disciplina invalid!\npunctaj invalid!\n'
        nota2 = Nota(2,12,41,7.3)
        validator_Nota.valideaza(nota2)
        assert True

    def __run_repository_student_tests(self):
        """
        Functie de test pentru repository-ul de studenti
        """
        student = Student(34,'bogdan')
        repo_studenti = RepositoryStud()
        assert len(repo_studenti) == 0

        repo_studenti.store(student)
        assert len(repo_studenti) == 1
        key_stud = Student(34,None)
        result_student = repo_studenti.search(key_stud)
        assert student.get_idStudent() == result_student.get_idStudent()

        student2 = Student(34,'catalin')
        try:
            repo_studenti.store(student2)
            assert False
        except RepoException as re:
            assert str(re) == 'element deja existent!'
        
        student3 = Student(67,'maria')
        try:
            repo_studenti.update(student3)
            assert False
        except RepoException as re:
            assert str(re) == 'element inexistent!'
        
        student4 = Student(34,'alex')
        repo_studenti.update(student4)
        result_student = repo_studenti.search(key_stud)
        assert result_student.get_nume() == 'alex'

        repo_studenti.remove(key_stud)
        assert len(repo_studenti) == 0
        try:
            repo_studenti.remove(key_stud)
            assert False
        except RepoException as re:
            assert str(re) == 'element inexistent!'

    def __run_controller_student_tests(self):
        """
        Functie de test pentru controller-ul de studenti
        """
        #add_student
        repo_studenti = RepositoryStud()
        validator_studenti = ValidatorStud()
        controller_studenti = ControllerStud(repo_studenti,validator_studenti)
        idStudent = 20
        nume = 'daria'
        controller_studenti.add_student(idStudent,nume)
        assert controller_studenti.get_nr_studenti() == 1
        try:
            controller_studenti.add_student(idStudent,nume)
            assert False
        except RepoException as re:
            assert str(re) == 'element deja existent!'
        try:
            controller_studenti.add_student(-idStudent,'')
            assert False
        except ValidationException as ve:
            assert str(ve) == 'id invalid!\nnume invalid!\n'

        #del_student
        idStudent = 22
        nume = 'alexandra'
        controller_studenti.add_student(idStudent,nume)
        idStudent = 40
        nume = 'marius'
        controller_studenti.add_student(idStudent,nume)
        assert controller_studenti.get_nr_studenti() == 3
        key_stud = Student(22,'')
        controller_studenti.del_student(key_stud)
        assert controller_studenti.get_nr_studenti() == 2
        try:
            controller_studenti.del_student(key_stud)
            assert False
        except RepoException as re:
            assert str(re) == 'element inexistent!'

        #cauta_student
        key_stud = Student(40,'')
        student = controller_studenti.cauta_student(key_stud)
        assert True
        key_stud = Student(99,'')
        try:
            student = controller_studenti.cauta_student(key_stud)
            assert False
        except RepoException as re:
            assert str(re) == 'element inexistent!'

        #modifica_student
        student = Student(40,'andrei')
        controller_studenti.modifica_student(student)
        result_student = controller_studenti.cauta_student(student)
        assert result_student.get_nume() == 'andrei'
        try:
            key_stud = Student(40,'')
            controller_studenti.modifica_student(key_stud)
        except ValidationException as ve:
            assert str(ve) == 'nume invalid!\n'
        try:
            key_stud = Student(30,'andrei')
            controller_studenti.modifica_student(key_stud)
        except RepoException as re:
            assert str(re) == 'element inexistent!'

    def __run_repository_disciplina_tests(self):
        """
        Functie de test pentru repository-ul de discipline
        """
        disciplina = Disciplina(11,'matematica','prof1')
        repo_discipline = RepositoryDisc()
        assert len(repo_discipline) == 0

        repo_discipline.store(disciplina)
        assert len(repo_discipline) == 1
        key_disc = Disciplina(11,'','')
        result_disciplina = repo_discipline.search(key_disc)
        assert result_disciplina.get_idDisciplina() == disciplina.get_idDisciplina()

        disciplina2 = Disciplina(11,'informatica','prof2')
        try:
            repo_discipline.store(disciplina2)
            assert False
        except RepoException as re:
            assert str(re) == 'element deja existent!'

        disciplina3 = Disciplina(45,'fizica','prof3')
        try:
            repo_discipline.update(disciplina3)
            assert False
        except RepoException as re:
            assert str(re) == 'element inexistent!'

        disciplina4 = Disciplina(11,'chimie','prof4')
        repo_discipline.update(disciplina4)
        result_disciplina = repo_discipline.search(key_disc)
        assert result_disciplina.get_nume() == 'chimie'
        assert result_disciplina.get_profesor() == 'prof4'

        repo_discipline.remove(key_disc)
        assert len(repo_discipline) == 0
        try:
            repo_discipline.remove(key_disc)
            assert False
        except RepoException as re:
            assert str(re) == 'element inexistent!'

    def __run_controller_disciplina_tests(self):
        """
        Functie de test pentru controller-ul de discipline
        """
        #add_disciplina
        repo_discipline = RepositoryDisc()
        validator_discipline = ValidatorDisc()
        controller_discipline = ControllerDisc(repo_discipline,validator_discipline)
        idDisciplina = 20
        nume = 'matematica'
        profesor = 'prof'
        controller_discipline.add_disciplina(idDisciplina,nume,profesor)
        assert controller_discipline.get_nr_discipline() == 1
        try:
            controller_discipline.add_disciplina(idDisciplina,nume,profesor)
            assert False
        except RepoException as re:
            assert str(re) == 'element deja existent!'
        try:
            controller_discipline.add_disciplina(-idDisciplina,'','')
            assert False
        except ValidationException as ve:
            assert str(ve) == 'id invalid!\nnume invalid!\nprofesor invalid!\n'

        #del_disciplina
        idDisciplina = 24
        nume = 'informatica'
        controller_discipline.add_disciplina(idDisciplina,nume,profesor)
        idDisciplina = 42
        nume = 'fizica'
        controller_discipline.add_disciplina(idDisciplina,nume,profesor)
        assert controller_discipline.get_nr_discipline() == 3
        key_disc = Disciplina(24,'','')
        controller_discipline.del_disciplina(key_disc)
        assert controller_discipline.get_nr_discipline() == 2
        try:
            controller_discipline.del_disciplina(key_disc)
            assert False
        except RepoException as re:
            assert str(re) == 'element inexistent!'

        #cauta_disciplina
        key_disc = Disciplina(42,'','')
        disciplina = controller_discipline.cauta_disciplina(key_disc)
        assert True
        key_disc = Disciplina(99,'','')
        try:
            disciplina = controller_discipline.cauta_disciplina(key_disc)
            assert False
        except RepoException as re:
            assert str(re) == 'element inexistent!'

        #modifica_disciplina
        disciplina = Disciplina(42,'chimie','prof4')
        controller_discipline.modifica_disciplina(disciplina)
        result_disciplina = controller_discipline.cauta_disciplina(disciplina)
        assert result_disciplina.get_nume() == 'chimie'
        assert result_disciplina.get_profesor() == 'prof4'
        try:
            key_disc = Disciplina(42,'','')
            controller_discipline.modifica_disciplina(key_disc)
        except ValidationException as ve:
            assert str(ve) == 'nume invalid!\nprofesor invalid!\n'
        try:
            key_disc = Disciplina(85,'biologie','prof5')
            controller_discipline.modifica_disciplina(key_disc)
        except RepoException as re:
            assert str(re) == 'element inexistent!'

    def __run_repository_note_tests(self):
        """
        Functie de test pentru repository-ul de note
        """
        nota = Nota(1,11,24,9.6)
        repo_note = RepositoryNote()
        assert len(repo_note) == 0

        repo_note.store(nota)
        assert len(repo_note) == 1
        key_nota = Nota(1,'','',0)
        result_nota = repo_note.search(key_nota)
        assert result_nota.get_idNota() == nota.get_idNota()

        nota2 = Nota(1,10,20,8.8)
        try:
            repo_note.store(nota2)
            assert False
        except RepoException as re:
            assert str(re) == 'element deja existent!'

        nota3 = Nota(2,5,6,4.7)
        try:
            repo_note.update(nota3)
            assert False
        except RepoException as re:
            assert str(re) == 'element inexistent!'

        nota4 = Nota(1,12,20,6.5)
        repo_note.update(nota4)
        result_nota = repo_note.search(key_nota)
        assert result_nota.get_idStudent() == 12
        assert result_nota.get_idDisciplina() == 20
        assert result_nota.get_punctaj() == 6.5

        repo_note.remove(key_nota)
        assert len(repo_note) == 0
        try:
            repo_note.remove(key_nota)
            assert False
        except RepoException as re:
            assert str(re) == 'element inexistent!'

    def __run_controller_note_tests(self):
        """
        Functie de test pentru controller-ul de note
        """
        #add_nota
        repo_note = RepositoryNote()
        validator_note = ValidatorNota()
        repo_studenti = RepositoryStud()
        repo_discipline = RepositoryDisc()
        controller_note = ControllerNote(repo_note,validator_note,repo_studenti,repo_discipline)
        idNota = 1
        idStudent = 10
        idDisciplina = 15
        punctaj = 8.2
        controller_note.add_nota(idNota,idStudent,idDisciplina,punctaj)
        assert controller_note.get_nr_note() == 1
        try:
            controller_note.add_nota(idNota,idStudent,idDisciplina,punctaj)
            assert False
        except RepoException as re:
            assert str(re) == 'element deja existent!'
        try:
            controller_note.add_nota(-idNota,-idStudent,-idDisciplina,-punctaj)
            assert False
        except ValidationException as ve:
            assert str(ve) == 'id invalid!\nid student invalid!\nid disciplina invalid!\npunctaj invalid!\n'

        #del_nota
        idNota = 5
        idStudent = 1
        idDisciplina = 1
        punctaj = 10
        controller_note.add_nota(idNota,idStudent,idDisciplina,punctaj)
        idNota = 6
        idStudent = 2
        idDisciplina = 2
        punctaj = 10
        controller_note.add_nota(idNota,idStudent,idDisciplina,punctaj)
        assert controller_note.get_nr_note() == 3
        key_nota = Nota(5,0,0,0)
        controller_note.del_nota(key_nota)
        assert controller_note.get_nr_note() == 2
        try:
            controller_note.del_nota(key_nota)
            assert False
        except RepoException as re:
            assert str(re) == 'element inexistent!'

        #cauta_nota
        key_nota = Nota(90,0,0,0)
        try:
            result_nota = controller_note.cauta_nota(key_nota)
            assert False
        except RepoException as re:
            assert str(re) == 'element inexistent!'
        key_nota = Nota(6,0,0,0)
        result_nota = controller_note.cauta_nota(key_nota)
        assert result_nota.get_idNota() == 6
        assert result_nota.get_punctaj() == 10

        #modifica_nota
        idNota = 6
        punctaj = 3.5
        key_nota = Nota(6,0,0,3.5)
        controller_note.modifica_nota(key_nota)
        key_nota = Nota(6,0,0,0)
        result_nota = controller_note.cauta_nota(key_nota)
        assert result_nota.get_punctaj() == 3.5

    def run_all_tests(self):
        """
        Functie ce apeleaza toate functiile de test
        """
        self.__run_domain_tests()
        self.__run_validation_tests()
        self.__run_repository_student_tests()
        self.__run_controller_student_tests()
        self.__run_repository_disciplina_tests()
        self.__run_controller_disciplina_tests()
        self.__run_repository_note_tests()
        self.__run_controller_note_tests()
