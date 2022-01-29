# QUESTION 1:
# Input: Given a list of numbers separated with a comma. The numbers 5 and 8 are present in the list.
# Assume that 8 always comes after 5.
# Case 1: num1 -> Add all numbers which do not lie between 5 and 8 in the Input List.
# Case 2: num2 -> Numbers formed by concatenating all numbers from 5 to 8 in the list
# Output: Sum of num1 and num2
# Example: 3,2,6,5,1,4,8,9
# Num1: 3+2+6+9 =20
# Num2: 5148O/p=5148+20 = 5168

if __name__ == '__main__':
    list1 = [3, 2, 6, 5, 1, 4, 8, 9, 1, 2, 3]
    list2 = []
    for i in list1:
        if i == 5:
            break
        else:
            list2.append(i)
    j = list1.index(8)
    for k in range(j+1, len(list1)):
        list2.append(list1[k])
    num1 = sum(list2)
    num2 = 0
    for k in range(list1.index(5), list1.index(8)+1):
        num2 = num2*10+list1[k]
    print(list2)
    print(num1)
    print(num2)
    print(num2+num1)