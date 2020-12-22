def sorted_insert(iterable, *, key=lambda x:x, reverse:bool=False):
    iterable = list(iterable)

    for i in range(1,len(iterable)):
        poz = i-1
        elem = iterable[i]
        while poz >= 0 and key(elem) <= key(iterable[poz]):
            iterable[poz+1] = iterable[poz]
            poz = poz-1
        iterable[poz+1] = elem

    if reverse: iterable.reverse()
    return iterable

def sorted_comb(iterable, *, key=lambda x:x, reverse:bool=False, cmp=lambda x,y: x>y):
    gap = len(iterable)
    swapped = True

    iterable = list(iterable)

    while gap!=1 or swapped == True:
        gap = int(max((gap*10)/13,1))
        swapped = False

        for i in range(0, len(iterable)-gap):
            if cmp(key(iterable[i]),key(iterable[i+gap])):
                iterable[i], iterable[i+gap] = iterable[i+gap], iterable[i]
                swapped = True
        
    if reverse: iterable.reverse()
    return iterable

def comparare_stud(stud1,stud2):
    """
    Compara doua obiecte de tip StudentNotaDTO
    """
    if stud1.get_nume_stud() > stud2.get_nume_stud():
        return True
    if stud1.get_nume_stud() == stud2.get_nume_stud() and stud1.get_punctaj() > stud2.get_punctaj():
        return True
    return False
