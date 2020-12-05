from domain.entities import Disciplina, Student, Nota, StudentNotaDTO
from validation.validators import ValidatorDisc, ValidatorStud, ValidatorNota
from errors.exceptions import ValidationException,RepoException
from infrastructure.repository import RepositoryDisc, RepositoryFileDisc, RepositoryFileNote, RepositoryFileStud, RepositoryNote, RepositoryStud
from controllere.controller import ControllerStud,ControllerDisc,ControllerNote
import unittest

class TestCaseDomain(unittest.TestCase):
    def setUp(self):
        self.student1 = Student(1,'bogdan')
        self.student2 = Student(1,'alex')
        self.disciplina1 = Disciplina(1,'informatica','prof1')
        self.disciplina2 = Disciplina(1,'matematica','prof2')
        self.nota1 = Nota(1,1,1,5.5)
        self.nota2 = Nota(1,2,2,8.6)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testStudent(self):
        self.assertEquals(self.student1.get_idStudent(),1)
        self.assertEquals(self.student1.get_nume(),'bogdan')
        self.assertEquals(str(self.student1),'1 bogdan')
        self.assertEquals(self.student1,self.student2)

    def testDisciplina(self):
        self.assertEquals(self.disciplina1.get_idDisciplina(),1)
        self.assertEquals(self.disciplina1.get_nume(),'informatica')
        self.assertEquals(self.disciplina1.get_profesor(),'prof1')
        self.assertEquals(str(self.disciplina1),'1 informatica prof1')
        self.assertEquals(self.disciplina1,self.disciplina2)

    def testNota(self):
        self.assertEquals(self.nota1.get_idNota(),1)
        self.assertEquals(self.nota1.get_idStudent(),1)
        self.assertEquals(self.nota1.get_idDisciplina(),1)
        self.assertEquals(self.nota1.get_punctaj(),5.5)
        self.assertEquals(str(self.nota1),'1 1 1 5.5')
        self.assertEquals(self.nota1,self.nota2)

class TestCaseValidators(unittest.TestCase):
    def setUp(self):
        self.valid_stud = ValidatorStud()
        self.student_valid = Student(1,'bogdan')
        self.student_invalid = Student(-23,'')
        self.valid_disc = ValidatorDisc()
        self.disciplina_valida = Disciplina(2,'informatica','prof')
        self.disciplina_invalida = Disciplina(-59,'','')
        self.valid_nota = ValidatorNota()
        self.nota_valida = Nota(3,1,2,7.5)
        self.nota_invalida = Nota(-1,-25,-28,0.5)

        self.repo_stud = RepositoryStud()
        self.repo_stud.store(self.student_valid)
        self.repo_disc = RepositoryDisc()
        self.repo_disc.store(self.disciplina_valida)
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testStudentValidator(self):
        self.assertEquals(self.valid_stud.valideaza(self.student_valid),None)
        self.assertRaisesRegex(ValidationException,'id invalid!\nnume invalid!\n',self.valid_stud.valideaza,self.student_invalid)
    
    def testDisciplinaValidator(self):
        self.assertEquals(self.valid_disc.valideaza(self.disciplina_valida),None)
        self.assertRaisesRegex(ValidationException,'id invalid!\nnume invalid!\nprofesor invalid!\n',self.valid_disc.valideaza,self.disciplina_invalida)
    
    def testNotaValidator(self):
        self.assertEquals(self.valid_nota.valideaza(self.nota_valida,self.repo_stud,self.repo_disc),None)
        self.assertRaisesRegex(ValidationException,'id invalid!\nid student invalid!\nid disciplina invalid!\npunctaj invalid!\n',self.valid_nota.valideaza,self.nota_invalida,self.repo_stud,self.repo_disc)

class TestCaseStudentRepository(unittest.TestCase):
    def setUp(self):
        self.repo = RepositoryStud()
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)
        
    def testStore(self):
        self.repo.store(Student(1,'bogdan'))
        self.repo.store(Student(2,'marius'))
        self.assertEquals(len(self.repo),2)
        self.assertRaises(RepoException,self.repo.store,Student(1,'alex'))

    def testSearch(self):
        self.assertRaises(RepoException,self.repo.search,Student(1,''))
        self.repo.store(Student(1,'bogdan'))
        result_stud = self.repo.search(Student(1,''))
        self.assertEquals(result_stud.get_idStudent(),1)
        self.assertEquals(result_stud.get_nume(),'bogdan')

    def testUpdate(self):
        self.assertRaises(RepoException,self.repo.update,Student(1,''))
        self.repo.store(Student(1,'bogdan'))
        result_stud = self.repo.search(Student(1,''))
        self.assertEquals(result_stud.get_idStudent(),1)
        self.assertEquals(result_stud.get_nume(),'bogdan')
        self.repo.update(Student(1,'marius'))
        result_stud = self.repo.search(Student(1,''))
        self.assertEquals(result_stud.get_idStudent(),1)
        self.assertEquals(result_stud.get_nume(),'marius')

    def testRemove(self):
        self.assertRaises(RepoException,self.repo.remove,Student(1,'bogdan'))
        self.repo.store(Student(1,'bogdan'))
        self.repo.store(Student(2,'alex'))
        self.assertEquals(len(self.repo),2)
        self.repo.remove(Student(1,''))
        self.assertEquals(len(self.repo),1)
        self.assertRaises(RepoException,self.repo.remove,Student(1,''))

class TestCaseDisciplineRepository(unittest.TestCase):
    def setUp(self):
        self.repo = RepositoryDisc()
    
    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testStore(self):
        self.repo.store(Disciplina(1,'info','p'))
        self.repo.store(Disciplina(2,'mate','p'))
        self.assertEquals(len(self.repo),2)
        self.assertRaises(RepoException,self.repo.store,Disciplina(1,'',''))

    def testSearch(self):
        self.assertRaises(RepoException,self.repo.search,Disciplina(1,'',''))
        self.repo.store(Disciplina(1,'info','p'))
        result_disc = self.repo.search(Disciplina(1,'',''))
        self.assertEquals(result_disc.get_idDisciplina(),1)
        self.assertEquals(result_disc.get_nume(),'info')
        self.assertEquals(result_disc.get_profesor(),'p')

    def testUpdate(self):
        self.assertRaises(RepoException,self.repo.update,Disciplina(1,'',''))
        self.repo.store(Disciplina(1,'info','p'))
        result_disc = self.repo.search(Disciplina(1,'',''))
        self.assertEquals(result_disc.get_idDisciplina(),1)
        self.assertEquals(result_disc.get_nume(),'info')
        self.assertEquals(result_disc.get_profesor(),'p')
        self.repo.update(Disciplina(1,'mate','p2'))
        result_disc = self.repo.search(Disciplina(1,'',''))
        self.assertEquals(result_disc.get_idDisciplina(),1)
        self.assertEquals(result_disc.get_nume(),'mate')
        self.assertEquals(result_disc.get_profesor(),'p2')

    def testRemove(self):
        self.assertRaises(RepoException,self.repo.remove,Disciplina(1,'info','p'))
        self.repo.store(Disciplina(1,'info','p1'))
        self.repo.store(Disciplina(2,'mate','p2'))
        self.assertEquals(len(self.repo),2)
        self.repo.remove(Disciplina(1,'',''))
        self.assertEquals(len(self.repo),1)
        self.assertRaises(RepoException,self.repo.remove,Disciplina(1,'',''))

class TestCaseNoteRepository(unittest.TestCase):
    def setUp(self):
        self.repo = RepositoryNote()

    def tearDown(self):
        unittest.TestCase.tearDown(self)
    
    def testStore(self):
        self.repo.store(Nota(1,1,7,7.5))
        self.repo.store(Nota(2,2,7,5.5))
        self.assertEquals(len(self.repo),2)
        self.assertRaises(RepoException,self.repo.store,Nota(1,1,7,2))
    
    def testSearch(self):
        self.assertRaises(RepoException,self.repo.search,Nota(1,0,0,0))
        self.repo.store(Nota(1,1,7,9))
        result_nota = self.repo.search(Nota(1,0,0,0))
        self.assertEquals(result_nota.get_idNota(),1)
        self.assertEquals(result_nota.get_idStudent(),1)
        self.assertEquals(result_nota.get_idDisciplina(),7)
        self.assertEquals(result_nota.get_punctaj(),9)

    def testUpdate(self):
        self.assertRaises(RepoException,self.repo.update,Nota(1,0,0,0))
        self.repo.store(Nota(1,1,7,6.7))
        result_nota = self.repo.search(Nota(1,0,0,0))
        self.assertEquals(result_nota.get_idNota(),1)
        self.assertEquals(result_nota.get_idStudent(),1)
        self.assertEquals(result_nota.get_idDisciplina(),7)
        self.assertEquals(result_nota.get_punctaj(),6.7)
        self.repo.update(Nota(1,1,30,10))
        result_nota = self.repo.search(Nota(1,0,0,0))
        self.assertEquals(result_nota.get_idNota(),1)
        self.assertEquals(result_nota.get_idStudent(),1)
        self.assertEquals(result_nota.get_idDisciplina(),30)
        self.assertEquals(result_nota.get_punctaj(),10)

class TestCaseStudentController(unittest.TestCase):
    def setUp(self):
        validator = ValidatorStud()
        self.ctr = ControllerStud(RepositoryStud(),validator,RepositoryNote())
        student1 = Student(1,'bogdan')
        self.ctr.add_student(1,'bogdan')
        student2 = Student(2,'alex')
        self.ctr.add_student(2,'alex')

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAdauga(self):
        self.assertEquals(self.ctr.get_nr_studenti(),2)
        self.assertRaises(ValidationException,self.ctr.add_student,-1,'')
        self.assertRaises(RepoException,self.ctr.add_student,1,'andrei')
    
    def testDelete(self):
        self.assertEquals(self.ctr.get_nr_studenti(),2)
        self.ctr.del_student(Student(1,''))
        self.assertEquals(self.ctr.get_nr_studenti(),1)
        self.assertRaises(RepoException,self.ctr.del_student,Student(1,''))

    def testCauta(self):
        key_stud = Student(1,'')
        result_stud = self.ctr.cauta_student(key_stud)
        self.assertEquals(result_stud.get_idStudent(),1)
        self.assertEquals(result_stud.get_nume(),'bogdan')
        key_stud = Student(3,'')
        self.assertRaises(RepoException,self.ctr.cauta_student,key_stud)
    
    def testModifica(self):
        student3 = Student(1,'tudor')
        self.ctr.modifica_student(student3)
        result_stud = self.ctr.cauta_student(student3)
        self.assertEquals(student3.get_idStudent(),result_stud.get_idStudent())
        self.assertEquals(student3.get_nume(),result_stud.get_nume())
        key_stud = Student(5,'')
        self.assertRaises(ValidationException,self.ctr.modifica_student,key_stud)
        key_stud = Student(5,'marius')
        self.assertRaises(RepoException,self.ctr.modifica_student,key_stud)

class TestCaseDisciplineController(unittest.TestCase):
    def setUp(self):
        validator = ValidatorDisc()
        self.ctr = ControllerDisc(RepositoryDisc(),validator)
        disciplina1 = Disciplina(1,'informatica','prof1')
        disciplina2 = Disciplina(2,'matematica','prof2')
        self.ctr.add_disciplina(1,'informatica','prof1')
        self.ctr.add_disciplina(2,'matematica','prof2')

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAdauga(self):
        self.assertEquals(self.ctr.get_nr_discipline(),2)
        self.assertRaises(ValidationException,self.ctr.add_disciplina,-1,'','')
        self.assertRaises(RepoException,self.ctr.add_disciplina,1,'sport','prof')

    def testDelete(self):
        self.assertEquals(self.ctr.get_nr_discipline(),2)
        self.ctr.del_disciplina(Disciplina(1,'',''))
        self.assertEquals(self.ctr.get_nr_discipline(),1)
        self.assertRaises(RepoException,self.ctr.del_disciplina,Disciplina(1,'',''))

    def testCauta(self):
        key_disc = Disciplina(1,'','')
        result_disc = self.ctr.cauta_disciplina(key_disc)
        self.assertEquals(result_disc.get_idDisciplina(),1)
        self.assertEquals(result_disc.get_nume(),'informatica')
        self.assertEquals(result_disc.get_profesor(),'prof1')
        key_disc = Disciplina(3,'','')
        self.assertRaises(RepoException,self.ctr.cauta_disciplina,key_disc)

    def testModifica(self):
        disciplina3 = Disciplina(1,'fundamentele programarii','prof3')
        self.ctr.modifica_disciplina(disciplina3)
        result_disc = self.ctr.cauta_disciplina(disciplina3)
        self.assertEquals(disciplina3.get_idDisciplina(),result_disc.get_idDisciplina())
        self.assertEquals(disciplina3.get_nume(),result_disc.get_nume())
        self.assertEquals(disciplina3.get_profesor(),result_disc.get_profesor())
        key_disc = Disciplina(5,'','')
        self.assertRaises(ValidationException,self.ctr.modifica_disciplina,key_disc)
        key_disc = Disciplina(5,'sport','prof5')
        self.assertRaises(RepoException,self.ctr.modifica_disciplina,key_disc)

class TestCaseNoteController(unittest.TestCase):
    def setUp(self):
        repo_stud = RepositoryStud()
        repo_disc = RepositoryDisc()
        repo_note = RepositoryNote()

        self.ctr_stud = ControllerStud(repo_stud,ValidatorStud(),repo_note)
        self.ctr_disc = ControllerDisc(repo_disc,ValidatorDisc())

        self.ctr_stud.add_student(1,'bogdan')
        self.ctr_stud.add_student(2,'alex')

        self.ctr_disc.add_disciplina(7,'informatica','prof')

        validator = ValidatorNota()
        self.ctr = ControllerNote(repo_note,validator,repo_stud,repo_disc)
        self.ctr.add_nota(10,1,7,9.8)
        self.ctr.add_nota(20,2,7,8.5)

        self.lista_stud_nota = []
        stud_nota1 = StudentNotaDTO('bogdan',9.8)
        stud_nota2 = StudentNotaDTO('alex',8.5)
        self.lista_stud_nota.append(stud_nota1)
        self.lista_stud_nota.append(stud_nota2)
        self.valid1 = []
        self.valid1.append(stud_nota1)
        self.valid1.append(stud_nota2)
        self.valid2 = []
        self.valid2.append(stud_nota2)
        self.valid2.append(stud_nota1)

    def tearDown(self):
        unittest.TestCase.tearDown(self)

    def testAdauga_white(self):
        self.assertEquals(self.ctr.get_nr_note(),2)
        self.ctr.add_nota(1,1,7,9.8)
        self.assertEquals(self.ctr.get_nr_note(),3)
        self.assertRaises(ValidationException,self.ctr.add_nota,12,1,7,0.5)
        self.assertRaises(RepoException,self.ctr.add_nota,10,1,7,10)

    def testAdauga_black(self):
        self.assertRaises(ValidationException,self.ctr.add_nota,-1,0,0,0)
        self.ctr.add_nota(1,1,7,9.8)
        self.assertEquals(self.ctr.get_nr_note(),3)

    def testDelete(self):
        self.assertEquals(self.ctr.get_nr_note(),2)
        self.ctr.del_nota(Nota(10,0,0,0))
        self.assertEquals(self.ctr.get_nr_note(),1)
        self.assertRaises(RepoException,self.ctr.del_nota,Nota(10,0,0,0))

    def testCauta(self):
        key_nota = Nota(10,0,0,0)
        result_nota = self.ctr.cauta_nota(key_nota)
        self.assertEquals(result_nota.get_idNota(),10)
        self.assertEquals(result_nota.get_idStudent(),1)
        self.assertEquals(result_nota.get_idDisciplina(),7)
        self.assertEquals(result_nota.get_punctaj(),9.8)
        key_nota = Nota(30,0,0,0)
        self.assertRaises(RepoException,self.ctr.cauta_nota,key_nota)

    def testModifica(self):
        nota = Nota(10,1,7,3.5)
        self.ctr.modifica_nota(nota)
        result_nota = self.ctr.cauta_nota(nota)
        self.assertEquals(nota.get_idNota(),result_nota.get_idNota())
        self.assertEquals(nota.get_idStudent(),result_nota.get_idStudent())
        self.assertEquals(nota.get_idDisciplina(),result_nota.get_idDisciplina())
        self.assertEquals(nota.get_punctaj(),result_nota.get_punctaj())
        key_nota = Nota(50,0,0,0)
        self.assertRaises(ValidationException,self.ctr.modifica_nota,key_nota)
        key_nota = Nota(50,2,7,6.2)
        self.assertRaises(RepoException,self.ctr.modifica_nota,key_nota)
    
    def testSorteazaDescNota(self):
        self.lista_stud_nota = self.ctr.sorteaza_desc_nota(self.lista_stud_nota)
        self.assertEquals(self.lista_stud_nota,self.valid1)

    def testSorteazaAlfNume(self):
        self.lista_stud_nota = self.ctr.sorteaza_alf_nume(self.lista_stud_nota)
        self.assertEquals(self.lista_stud_nota,self.valid2)

class TestCaseLoadToFile(unittest.TestCase):
    def setUp(self):
        self.repo_file_stud = RepositoryFileStud("testing/test_stud.txt")
        self.repo_file_disc = RepositoryFileDisc('testing/test_disc.txt')
        self.repo_file_note = RepositoryFileNote('testing/test_note.txt')

    def tearDown(self):
        self.repo_file_stud.remove_all()
        self.repo_file_disc.remove_all()
        self.repo_file_note.remove_all()

    def testStudFile(self):
        self.assertEquals(len(self.repo_file_stud),0)
        self.repo_file_stud.store(Student(1,'bogdan'))
        self.repo_file_stud.store(Student(2,'marius'))
        self.repo_file_stud.store(Student(3,'alex'))
        self.assertEquals(len(self.repo_file_stud),3)
    
    def testDiscFile(self):
        self.assertEquals(len(self.repo_file_disc),0)
        self.repo_file_disc.store(Disciplina(1,'info','p1'))
        self.repo_file_disc.store(Disciplina(2,'mate','p2'))
        self.repo_file_disc.store(Disciplina(3,'sport','p3'))
        self.assertEquals(len(self.repo_file_disc),3)
    
    def testNoteFile(self):
        self.assertEquals(len(self.repo_file_note),0)
        self.repo_file_note.store(Nota(1,1,1,10))
        self.repo_file_note.store(Nota(2,2,2,6.8))
        self.repo_file_note.store(Nota(3,3,3,8.4))
        self.assertEquals(len(self.repo_file_note),3)
