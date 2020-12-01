from domain.entities import Disciplina, Nota, Student
from errors.exceptions import RepoException

class RepositoryStud:

    def __init__(self):
        self.__elems = []

    def __len__(self):
        """
        Returneaza numarul de studenti din repository (numar natural)
        """
        return len(self.__elems)

    def store(self,student):
        """
        Retine studentii 
        student - obiect de tip student
        ridica o exceptie in cazul in care elementul deja exista
        """
        if student in self.__elems:
            raise RepoException('element deja existent!')
        self.__elems.append(student)

    def search(self,key_student):
        """
        Cauta un element in repository
        key_student - obiect de tip student
        returneaza un obiect de tip student
        """
        if key_student not in self.__elems:
            raise RepoException('element inexistent!')
        for elem in self.__elems:
            if elem == key_student:
                return elem

    def update(self,student):
        """
        Actualizeaza un student din repository
        student - obiect de tip student
        """
        if student not in self.__elems:
            raise RepoException('element inexistent!')
        for i in range(len(self.__elems)):
            if self.__elems[i] == student:
                self.__elems[i] = student
                return 

    def remove(self,key_stud):
        """
        Sterge din repository
        key_stud - obiect de tip student
        """
        if key_stud not in self.__elems:
            raise RepoException('element inexistent!')
        for i in range(len(self.__elems)):
            if self.__elems[i] == key_stud:
                del self.__elems[i]
                return
                
    def get_all(self):
        return self.__elems[:]

    def get_id_studenti(self):
        """
        Returneaza o lista cu id-urile studentilor din repository
        """
        lista_id = []
        studenti = self.get_all()
        for stud in studenti:
            if stud.get_idStudent() not in lista_id:
                lista_id.append(stud.get_idStudent())
        return lista_id

class RepositoryDisc:

    def __init__(self):
        self.__elems = []

    def __len__(self):
        """
        Returneaza numarul de discipline din repository (numar natural)
        """
        return len(self.__elems)

    def store(self,disciplina):
        """
        Retine disciplinele 
        disciplina - obiect de tip disciplina
        ridica o exceptie in cazul in care elementul deja exista
        """
        if disciplina in self.__elems:
            raise RepoException('element deja existent!')
        self.__elems.append(disciplina)

    def search(self,key_disc):
        """
        Cauta un element in repository
        key_disc - obiect de tip disciplina
        returneaza un obiect de tip disciplina
        """
        if key_disc not in self.__elems:
            raise RepoException('element inexistent!')
        for disciplina in self.__elems:
            if key_disc == disciplina:
                return disciplina

    def update(self,disciplina):
        """
        Actualizeaza o disciplina din repository
        disciplina - obiect de tip disciplina
        """
        if disciplina not in self.__elems:
            raise RepoException('element inexistent!')
        for i in range(len(self.__elems)):
            if self.__elems[i] == disciplina:
                self.__elems[i] = disciplina
                return
    
    def remove(self,key_disc):
        """
        Sterge din repository
        key_disc - obiect de tip disciplina
        """
        if key_disc not in self.__elems:
            raise RepoException('element inexistent!')
        for i in range(len(self.__elems)):
            if self.__elems[i] == key_disc:
                del self.__elems[i]
                return
    
    def get_all(self):
        return self.__elems[:]

class RepositoryNote:
    
    def __init__(self):
        self.__elems = []

    def __len__(self):
        """
        Returneaza numarul de note din repository (numar natural)
        """
        return len(self.__elems)

    def store(self,nota):
        """
        Retine notele
        nota - obiect de tip nota
        ridica o exceptie in cazul in care elementul deja exista
        """
        if nota in self.__elems:
            raise RepoException('element deja existent!')
        self.__elems.append(nota)

    def search(self,key_nota):
        """
        Cauta un element in repository
        key_nota - obiect de tip nota
        returneaza un obiect de tip nota
        """
        if key_nota not in self.__elems:
            raise RepoException('element inexistent!')
        for nota in self.__elems:
            if key_nota == nota:
                return nota
    
    def update(self,nota):
        """
        Actualizeaza o nota din repository
        nota - obiect de tip nota
        """
        if nota not in self.__elems:
            raise RepoException('element inexistent!')
        for i in range(len(self.__elems)):
            if self.__elems[i] == nota:
                self.__elems[i] = nota
                return

    def remove(self,key_nota):
        """
        Sterge din repository:
        key_nota - obicet de tip nota
        """
        if key_nota not in self.__elems:
            raise RepoException('element inexistent!')
        for i in range(len(self.__elems)):
            if self.__elems[i] == key_nota:
                del self.__elems[i]
                return

    def remove_stud(self,idStudent):
        """
        Sterge notele unui student care se doreste a fi sters
        """
        for i in range(len(self.__elems)):
            if self.__elems[i].get_idStudent() == idStudent:
                del self.__elems[i]
                return
        #raise RepoException('element inexistent!')

    def get_all(self):
        return self.__elems[:]


class RepositoryFileStud(RepositoryStud):

    def __init__(self,fileName):
        RepositoryStud.__init__(self)
        self.__fName = fileName

    def __len__(self):
        return len(self.__loadFromFile())

    def __loadFromFile(self):
        try:
            f = open(self.__fName,"r")
        except IOError:
            return
        line = f.readline().strip()
        rez = []
        while line!="":
            date = line.split(';')
            stud = Student(int(date[0]),date[1])
            rez.append(stud)
            line = f.readline().strip()
        f.close()
        return rez

    def __storeToFile(self,studenti):
        with open(self.__fName,'w') as f:
            for stud in studenti:
                strf = str(stud.get_idStudent()) + ';' + stud.get_nume() + '\n'
                f.write(strf)

    def store(self,stud):
        allStud = self.__loadFromFile()
        if stud in allStud:
            raise RepoException('element deja existent!')
        allStud.append(stud)
        self.__storeToFile(allStud)

    def update(self,student):
        allStud = self.__loadFromFile()
        if student not in allStud:
            raise RepoException('element inexistent!')
        for i in range(len(allStud)):
            if allStud[i] == student:
                allStud[i] = student
                return 

    def remove(self,key_stud):
        allStud = self.__loadFromFile()
        if key_stud not in allStud:
            raise RepoException('element inexistent!')
        for i in range(len(allStud)):
            if allStud[i] == key_stud:
                del allStud[i]
                self.__storeToFile(allStud)
                return
    
    def search(self, key_student):
        allStud = self.__loadFromFile()
        if key_student not in allStud:
            raise RepoException('element inexistent!')
        for elem in allStud:
            if elem == key_student:
                return elem

    def remove_all(self):
        self.__storeToFile([])
    
    def get_all(self):
        return self.__loadFromFile()

    def get_id_studenti(self):
        lista_id = []
        studenti = self.get_all()
        for stud in studenti:
            if stud.get_idStudent() not in lista_id:
                lista_id.append(stud.get_idStudent())
        return lista_id

class RepositoryFileDisc(RepositoryDisc):

    def __init__(self,fileName):
        RepositoryDisc.__init__(self)
        self.__fName = fileName

    def __len__(self):
        return len(self.__loadFromFile())
    
    def __loadFromFile(self):
        try:
            f = open(self.__fName,'r')
        except IOError:
            return
        line = f.readline().strip()
        rez = []
        while line!="":
            date = line.split(';')
            disc = Disciplina(int(date[0]),date[1],date[2])
            rez.append(disc)
            line = f.readline().strip()
        f.close()
        return rez

    def __storeToFile(self,discipline):
        with open(self.__fName,'w') as f:
            for disc in discipline:
                strf = str(disc.get_idDisciplina()) + ';' + disc.get_nume() + ';' + disc.get_profesor() + '\n'
                f.write(strf)

    def store(self,disc):
        allDisc = self.__loadFromFile()
        if disc in allDisc:
            raise RepoException('element deja existent!')
        allDisc.append(disc)
        self.__storeToFile(allDisc)

    def update(self, disciplina):
        allDisc = self.__loadFromFile()
        if disciplina not in allDisc:
            raise RepoException('element inexistent!')
        for i in range(len(allDisc)):
            if allDisc[i] == disciplina:
                allDisc[i] = disciplina
                return

    def remove(self, key_disc):
        allDisc = self.__loadFromFile()
        if key_disc not in allDisc:
            raise RepoException('element inexistent!')
        for i in range(len(allDisc)):
            if allDisc[i] == key_disc:
                del allDisc[i]
                self.__storeToFile(allDisc)
                return

    def search(self, key_disc):
        allDisc = self.__loadFromFile()
        if key_disc not in allDisc:
            raise RepoException('element inexistent!')
        for elem in allDisc:
            if elem == key_disc:
                return elem
    
    def remove_all(self):
        self.__storeToFile([])

    def get_all(self):
        return self.__loadFromFile()

class RepositoryFileNote(RepositoryNote):

    def __init__(self,fileName):
        RepositoryNote.__init__(self)
        self.__fName = fileName

    def __len__(self):
        return len(self.__loadFromFile())

    def __loadFromFile(self):
        try:
            f = open(self.__fName,'r')
        except IOError:
            return
        line = f.readline().strip()
        rez = []
        while line!="":
            date = line.split(';')
            nota = Nota(int(date[0]),int(date[1]),int(date[2]),float(date[3]))
            rez.append(nota)
            line = f.readline().strip()
        f.close()
        return rez

    def __storeToFile(self,note):
        with open(self.__fName,'w') as f:
            for nota in note:
                strf = str(nota.get_idNota()) + ';' + str(nota.get_idStudent()) + ';' + str(nota.get_idDisciplina()) + ';' + str(nota.get_punctaj()) + '\n'
                f.write(strf)

    def store(self,nota):
        allNote = self.__loadFromFile()
        if nota in allNote:
            raise RepoException('element deja existent')
        allNote.append(nota)
        self.__storeToFile(allNote)

    def update(self, nota):
        allNote = self.__loadFromFile()
        if nota not in allNote:
            raise RepoException('element inexistent!')
        for i in range(len(allNote)):
            if allNote[i] == nota:
                allNote[i] = nota
                return

    def remove(self, key_nota):
        allNote = self.__loadFromFile()
        if key_nota not in allNote:
            raise RepoException('element inexistent!')
        for i in range(len(allNote)):
            if allNote[i] == key_nota:
                del allNote[i]
                self.__storeToFile(allNote)
                return

    def search(self, key_nota):
        allNote = self.__loadFromFile()
        if key_nota not in allNote:
            raise RepoException('element inexistent!')
        for elem in allNote:
            if elem == key_nota:
                return elem

    def remove_all(self):
        self.__storeToFile([])

    def get_all(self):
        return self.__loadFromFile()
