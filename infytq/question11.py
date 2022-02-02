# Question11.
# Number sequence
# Input: a string of comma separated numbers. The numbers 5 and 8 are present in the list
# Assume
# that 8 always comes after 5.
# Case 1: num 1 = add all numbers which do not lie between 5 and 8 in the input.
# Case 2: num2= numbers formed by concatenating all numbers from 5 to 8.
# Output: sum of num1 and num2
# Example:1) 3,2,6,5,1,4,8,9
# Num1: 3+2+6+9 =20
# Num2: 5148
# O/p=5248+20=5168 #

if __name__ == '__main__':
    list1 = [int(x) for x in input().split(',')]
    s = 0
    for i in list1:
        if i == 5:
            t = list1.index(i)
            break
        s += i
    z = list1.index(8)
    num2 = 0
    s += sum(list1[z+1:len(list1)])
    for i in range(t, z+1):
        num2 = num2*10 + list1[i]
    print(s + num2)
