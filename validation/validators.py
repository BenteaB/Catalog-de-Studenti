from errors.exceptions import RepoException, ValidationException
from domain.entities import Student,Disciplina

class ValidatorStud:

    def valideaza(self,student):
        """
        Valideaza un student
        Ridica o exceptie in cazul in care studentul nu este valid
        """
        errors = ''
        if student.get_idStudent() < 0:
            errors += 'id invalid!\n'
        if student.get_nume() == '':
            errors += 'nume invalid!\n'
        if len(errors) > 0:
            raise ValidationException(errors)

class ValidatorDisc:

    def valideaza(self,disciplina):
        """
        Valideaza o disciplina
        Ridica o exceptie in cazul in care disciplina nu este valida
        """
        errors = ''
        if disciplina.get_idDisciplina() < 0:
            errors += 'id invalid!\n'
        if disciplina.get_nume() == '':
            errors += 'nume invalid!\n'
        if disciplina.get_profesor() == '':
            errors += 'profesor invalid!\n'
        if len(errors) > 0:
            raise ValidationException(errors)

class ValidatorNota:

    def valideaza(self,nota,repo_studenti,repo_discipline):
        """
        Valideaza o nota
        Ridica o exceptie in cazul in care nota nu este valida
        """
        errors = ''
        if nota.get_idNota() < 0 :
            errors += 'id invalid!\n'

        idStudent = nota.get_idStudent()
        student = Student(idStudent,'')
        try:
            result_stud = repo_studenti.search(student)
            gasit_stud = True
        except RepoException:
            gasit_stud = False
        if nota.get_idStudent() < 0 or gasit_stud == False:
            errors += 'id student invalid!\n'
        
        idDisciplina = nota.get_idDisciplina()
        disciplina = Disciplina(idDisciplina,'','')
        try:
            result_disc = repo_discipline.search(disciplina)
            gasit_disc = True
        except RepoException:
            gasit_disc = False
        if nota.get_idDisciplina() < 0 or gasit_disc == False:
            errors += 'id disciplina invalid!\n'
        
        if nota.get_punctaj() < 1 or nota.get_punctaj()>10:
            errors += 'punctaj invalid!\n'
        
        if len(errors) > 0:
            raise ValidationException(errors)