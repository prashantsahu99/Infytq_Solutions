# Question8.
# Special character out
# Write a python program that it should consist of special char numbers and chars. if there are
# even numbers of special chars Then the series should start with even followed by odd
# Input: 19@a42&516
# Output: 492561
# If there are odd numbers of special chars then the output will be starting with odd followed
# by even
# Input: 5u6@25g7#@
# Output: 56527
# If there are any number of additional digits append them at last

if __name__ == '__main__':
    str1 = input()
    even = []
    odd = []
    special = 0
    for i in str1:
        if i.isdigit():
            if int(i) % 2 == 0:
                even.append(i)
            else:
                odd.append(i)
        elif i.isalpha():
            continue
        else:
            special += 1
    if len(even) > len(odd):
        size = len(odd)
        flag = 1
    else:
        size = len(even)
        flag = 2
    if special % 2 == 0:
        for i in range(0, size):
            print(even[i], end='')
            print(odd[i], end='')
    elif special % 2 != 0:
        for i in range(0, size):
            print(odd[i], end='')
            print(even[i], end='')
    if len(even) != len(odd):
        for i in range(size, len(even) + len(odd) - size):
            if flag == 1:
                print(even[i], end='')
            elif flag == 2:
                print(odd[i], end='')

