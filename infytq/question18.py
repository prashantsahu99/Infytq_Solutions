if __name__ == '__main__':
    lst = [int(x) for x in input().split(',')]
    l2 = []
    l1 = []
    for i in range(1, 26):
        l1.append(i)
        if len(l1) == 5:
            l2.append(l1)
            l1 = []
    for i in range(0, 5):
        for j in range(0, 5):
            if l2[i][j] in lst:
                l2[i][j] = 'X'
            else:
                l2[i][j] = 'O'


    outnum = 0
    d = 0
    for i in range(0, 5):
        r = 0
        c = 0
        for j in range(0, 5):
            if l2[i][j] == 'X':
                r += 1
            if l2[i][j] == 'X':
                c += 1
            if i + j == 4 and l2[i][j] == 'X':
                d += 1
        if c == 5 or r == 5:
            outnum = 1
            break
    if d == 5:
        outnum = 1


    d = 0
    for i in range(0, 5):
        if l2[i][i] == 'X':
            d += 1
    if d == 5:
        outnum = 1



    if outnum != 1:
        d = 0
        for i in range(0, 5):
            r = 0
            c = 0
            for j in range(0, 5):
                if l2[i][j] == 'O':
                    r += 1
                if l2[i][j] == 'O':
                    c += 1
                if i + j == 4 and l2[i][j] == 'O':
                    d += 1
            if c == 5 or r == 5:
                outnum = 2
                break
        if d == 5:
            outnum = 2

    if outnum != 1 and outnum != 2:
        d = 0
        for i in range(0, 5):
            if l2[i][i] == 'O':
                d += 1
        if d == 5:
            outnum = 2



    print(outnum)



    for i in range(0, 5):
        for j in range(0, 4):
            print(l2[i][j], end=',')
        print(l2[i][4])