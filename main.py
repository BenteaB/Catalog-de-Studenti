from controllere.controller import ControllerStud
from infrastructure.repository import RepositoryStud
from validation.validators import ValidatorStud
from testing.tests import Tests
from ui.console import UI

if __name__ == '__main__':
    tests = Tests()
    tests.run_all_tests()
    valid_studenti = ValidatorStud()
    repo_studenti = RepositoryStud()
    controller_studenti = ControllerStud(repo_studenti,valid_studenti)
    console = UI(controller_studenti)
    console.run()