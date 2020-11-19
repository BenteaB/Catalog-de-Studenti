from typing import Collection
from controllere.controller import ControllerNote, ControllerStud,ControllerDisc
from infrastructure.repository import RepositoryNote, RepositoryStud,RepositoryDisc
from validation.validators import ValidatorNota, ValidatorStud,ValidatorDisc
from testing.tests import Tests
from ui.console import uiMain, uiStudent, uiDisciplina

if __name__ == '__main__':
    tests = Tests()
    tests.run_all_tests()

    valid_studenti = ValidatorStud()
    repo_studenti = RepositoryStud()
    repo_note = RepositoryNote()
    controller_studenti = ControllerStud(repo_studenti,valid_studenti,repo_note)

    valid_discipline = ValidatorDisc()
    repo_discipline = RepositoryDisc()
    controller_discipline = ControllerDisc(repo_discipline,valid_discipline)

    valid_note = ValidatorNota()
    
    controller_note = ControllerNote(repo_note,valid_note,repo_studenti,repo_discipline)

    consoleMain = uiMain(controller_studenti,controller_discipline,controller_note)
    consoleMain.run()