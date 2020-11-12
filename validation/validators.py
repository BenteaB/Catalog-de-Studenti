from errors.exceptions import ValidationException

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