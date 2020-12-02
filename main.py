from controllere.controller import ControllerNote, ControllerStud,ControllerDisc
from infrastructure.repository import RepositoryFileDisc, RepositoryFileNote, RepositoryFileStud, RepositoryNote, RepositoryStud,RepositoryDisc
from validation.validators import ValidatorNota, ValidatorStud,ValidatorDisc
#from testing.tests import Tests 
from ui.console import uiMain

if __name__ == '__main__':
    #tests = Tests()
    #tests.run_all_tests()

    while True:
        op = input("\nDoriti sa lucrati cu fisiere? (Y/N) ")

        if op == 'Y': 
            repo_studenti = RepositoryFileStud("students.txt")
            repo_discipline = RepositoryFileDisc("discipline.txt")
            repo_note = RepositoryFileNote("note.txt")
            break
        elif op == 'N':
            repo_studenti = RepositoryStud()
            repo_discipline = RepositoryDisc()
            repo_note = RepositoryNote()
            break
        else:
            print("Comanda invalida!")

    valid_studenti = ValidatorStud()
    controller_studenti = ControllerStud(repo_studenti,valid_studenti,repo_note)

    valid_discipline = ValidatorDisc()
    controller_discipline = ControllerDisc(repo_discipline,valid_discipline)

    valid_note = ValidatorNota()
    controller_note = ControllerNote(repo_note,valid_note,repo_studenti,repo_discipline)

    consoleMain = uiMain(controller_studenti,controller_discipline,controller_note)
    consoleMain.run()
