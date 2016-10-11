def binary(slist, item):

    beg = 0
    mid = len(slist)/2
    end = len(slist) - 1
    found = False

    while beg <= end  and not found:

        mid = (beg + end)/2

        if slist[mid] > item:
            end = mid - 1

        elif slist[mid] < item:
            beg = mid + 1

        else:
            found = True

    return found

print binary([1,2,4,7,8,15,16], 8)
