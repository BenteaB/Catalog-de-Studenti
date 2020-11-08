from controllere.controller import ControllerStud,ControllerDisc
from infrastructure.repository import RepositoryStud,RepositoryDisc
from validation.validators import ValidatorStud,ValidatorDisc
from testing.tests import Tests
from ui.console import uiStudent

if __name__ == '__main__':
    tests = Tests()
    tests.run_all_tests()
    valid_studenti = ValidatorStud()
    repo_studenti = RepositoryStud()
    controller_studenti = ControllerStud(repo_studenti,valid_studenti)

    valid_discipline = ValidatorDisc()
    repo_discipline = RepositoryDisc()
    controller_discipline = ControllerDisc(repo_discipline,valid_discipline)

    console = uiStudent(controller_studenti)
    console.run()