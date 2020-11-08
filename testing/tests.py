from domain.entities import Student
from validation.validators import ValidatorStud
from errors.exceptions import ValidationException,RepoException
from infrastructure.repository import RepositoryStud
from controllere.controller import ControllerStud
 
class Tests:
    
    def __run_domain_tests(self):
        IDStudent = 24
        nume1 = 'nume1'
        student1 = Student(IDStudent,nume1)
        assert student1.get_idStudent() == 24
        assert student1.get_nume() == 'nume1'
        assert str(student1) == '24 nume1'

        nume2 = 'nume2'
        student2 = Student(IDStudent,nume2)
        assert student1 == student2

    def __run_validation_tests(self):
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

    def __run_repository_student_tests(self):
        student = Student(34,'bogdan')
        repo_studenti = RepositoryStud()
        assert len(repo_studenti) == 0

        repo_studenti.store(student)
        assert len(repo_studenti) == 1
        key_stud = Student(34,None)
        result_student = repo_studenti.search(key_stud)
        assert student.get_idStudent == result_student.get_idStudent

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

    def run_all_tests(self):
        self.__run_domain_tests()
        self.__run_validation_tests()
        self.__run_repository_student_tests()
        self.__run_controller_student_tests()