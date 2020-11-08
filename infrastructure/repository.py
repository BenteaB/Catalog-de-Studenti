from errors.exceptions import RepoException

class RepositoryStud:

    def __init__(self):
        self.__elems = []

    def __len__(self):
        return len(self.__elems)

    def store(self,student):
        if student in self.__elems:
            raise RepoException('element deja existent!')
        self.__elems.append(student)

    def search(self,key_student):
        if key_student not in self.__elems:
            raise RepoException('element inexistent!')
        for elem in self.__elems:
            if elem == key_student:
                return elem

    def update(self,student):
        if student not in self.__elems:
            raise RepoException('element inexistent!')
        for i in range(len(self.__elems)):
            if self.__elems[i] == student:
                self.__elems[i] = student
                return 

    def remove(self,key_stud):
        if key_stud not in self.__elems:
            raise RepoException('element inexistent!')
        for i in range(len(self.__elems)):
            if self.__elems[i] == key_stud:
                del self.__elems[i]
                return
                
    def get_all(self):
        return self.__elems[:]

class RepositoryDisc:

    def __init__(self):
        self.__elems = []

    def __len__(self):
        return len(self.__elems)

    def store(self,disciplina):
        if disciplina in self.__elems:
            raise RepoException('element deja existent!')
        self.__elems.append(disciplina)

    def search(self,key_disc):
        if key_disc not in self.__elems:
            raise RepoException('element inexistent!')
        for disciplina in self.__elems:
            if key_disc == disciplina:
                return disciplina

    def update(self,disciplina):
        if disciplina not in self.__elems:
            raise RepoException('element inexistent!')
        for i in range(len(self.__elems)):
            if self.__elems[i] == disciplina:
                self.__elems[i] = disciplina
                return
    
    def remove(self,key_disc):
        if key_disc not in self.__elems:
            raise RepoException('element inexistent!')
        for i in range(len(self.__elems)):
            if self.__elems[i] == key_disc:
                del self.__elems[i]
                return
    
    def get_all(self):
        return self.__elems[:]
