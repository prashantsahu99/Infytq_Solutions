# Question10.
# Even number
# A string which is a mixture of letter and integer and special char from which find the largest
# even number from the available digit after removing the duplicates.
# If an even number is not formed then return-1.
# Ex: infosys@337
# O/p:-1
# Hello#81@21349
# O/p:984312
if __name__ == '__main__':
    s = input()
    list1 = []
    flag = 0
    for i in s:
        if i.isdigit() and i not in list1:
            list1.append(i)
            if int(i) % 2 == 0:
                flag = 1
    if flag == 1:
        list1.sort(reverse=True)
        for i in range(len(list1)-1, -1, -1):
            if int(list1[i]) % 2 == 0:
                list1.append(list1[i])
                list1.remove(list1[i])
                break
        print(''.join(list1))

    else:
        print("-1")