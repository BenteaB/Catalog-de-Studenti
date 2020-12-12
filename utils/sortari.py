def sorted_insert(iterable, *, key=None, reverse=False):

    for i in range(1,len(iterable)):
        poz = i-1
        elem = iterable[i]
        while poz >= 0 and key(elem) <= key(iterable[poz]):
            iterable[poz+1] = iterable[poz]
            poz = poz-1
        iterable[poz+1] = elem

    if reverse: iterable.reverse()
    return iterable

def sorted_comb(iterable, *, key=None, reverse=False):
    
    gap = len(iterable)
    swapped = True

    while gap!=1 or swapped == True:
        gap = int(max((gap*10)/13,1))
        swapped = False

        for i in range(0, len(iterable)-gap):
            if key(iterable[i]) > key(iterable[i+gap]):
                iterable[i], iterable[i+gap] = iterable[i+gap], iterable[i]
                swapped = True
        
    if reverse: iterable.reverse()
    return iterable