from errors.exceptions import ValidationException

class ValidatorStud:

    def valideaza(self,student):
        errors = ''
        if student.get_idStudent() < 0:
            errors += 'id invalid!\n'
        if student.get_nume() == '':
            errors += 'nume invalid!\n'
        if len(errors) > 0:
            raise ValidationException(errors)