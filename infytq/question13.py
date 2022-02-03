# Question13.
# String rotation
# Input rhdt:246, ghftd:1246
# Expl: here every string is associated with the number sep by : if sum of squares of digits is
# even then rotate the string by 1
# if square of digits is odd then rotate the string left by 2 position 2*2+4*4+6*6=56 which is even so rotate
# rhdt -> trhd 1*1+2*2+4*4+6*6=57 which is odd then
# rotate string by 2 at left ‘ghftd”
# o/p: ftdgh

if __name__ == '__main__':
    def rotate(s1, num):
        total = 0
        for k in num:
            total = total + int(k)**2
        if total % 2 == 0:
            return s1[-1:] + s1[:-1]
        else:
            return s1[2:] + s1[:2]

    list1 = list(input().split(','))
    for i in list1:
        s, n = i.split(':')
        print(rotate(s, n))