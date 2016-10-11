def sequential(slist, item):
    found = False
    pos = 0

    while pos < len(slist) and not found:
        if slist[pos] == item:
            found = True
        else:
            pos+=1

    return found

print sequential([9,2,4], 4)
