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

class ValidatorNota:

    def valideaza(self,nota):
        """
        Valideaza o nota
        Ridica o exceptie in cazul in care nota nu este valida
        """
        errors = ''
        if nota.get_idNota() < 0 :
            errors += 'id invalid!\n'
        if nota.get_idStudent() < 0:
            errors += 'id student invalid!\n'
        if nota.get_idDisciplina() < 0:
            errors += 'id disciplina invalid!\n'
        if nota.get_punctaj() < 1 or nota.get_punctaj()>10:
            errors += 'punctaj invalid!\n'
        if len(errors) > 0:
            raise ValidationException(errors)