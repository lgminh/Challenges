def sumOfTwo(a,b,v):
    if a == [] or b == []:
        return False
    i = 0
    j = 0
    t = []

    a = sorted(a)
    b = sorted(b)

    while i < len(a) and j < len(b):
        if a[i] >= b[j]:
            t.append({'v': b[j], 'a': 1})
            j+=1
        else:
            t.append({'v': a[i], 'a': 0})
            i+=1

    while i < len(a):
        t.append({'v': a[i], 'a': 0})
        i +=1

    while j < len(b):
        t.append({'v': b[j], 'a': 1})
        j += 1


    t =  sorted(t)
    first = 0
    last = len(b) + len(a) - 1
    while first < last:
        if t[first]['v'] + t[last]['v'] < v:
            first += 1
        elif t[first]['v'] + t[last]['v'] > v:
            last -= 1
        elif (t[first]['a'] == 0 and t[last]['a'] == 1 ) or  \
                (t[first]['a'] == 1 and t[last]['a'] == 0 ):
            return True
        else:
            first += 1
            last -= 1
    return False



if __name__ == '__main__':
    #print sumOfTwo([1,2,3],[10,20,30,40],42)
    #print sumOfTwo([10, 1, 5, 3, 8],[100, 6, 3, 1, 5],4)
    print sumOfTwo([1, 2, 3], [10,20,30,40], 50)