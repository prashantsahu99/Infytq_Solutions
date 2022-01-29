# QUESTION 2:
# A string which is a mixture of letters, numbers, and special characters from which produce the largest
# even number from the available digit after removing the duplicates digits.
# If an even number did not produce then return -1.
# Ex: infosys@337
# O/p : -1
# — — — — — — — — — — — -
# Hello#81@21349
# O/p : 984312
def largest(str):
    l = []
    for i in str:
        if(i.isdigit()):
            if i not in l:
                l.append(i)
    l.sort(reverse=True)
    for i in range( len(l)-1, 0, -1):
        if(int(l[i]) % 2 == 0):
            z = l[i]
            l.remove(z)
            l.append(z)
            print("".join(l))
            break
    if i == 1:
        print("-1")



if __name__ == '__main__':
    s1 = "infosys@337"
    s2 = "Hello#81@21349"
    largest(s1)
    largest(s2)