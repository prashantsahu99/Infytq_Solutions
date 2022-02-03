# Question14. Pronic number
# Input:- 93012630
# Output-2,6,12,30,930,
# We should divide the total number into substrings, and we should verify each num is pronic
# num or not if pronic we should print that num
# Pronic: means it is a multiple of two consecutive integers
# Ex: 6->2*3 it’s a pronic
# 12->3*4 it’s a pronic
# Input: 12665042
# Output: 2,6,12,42,650

if __name__ == '__main__':
    def ispronic(num):
        for i in range(1, num//2 + 1):
            if i * (i+1) == num:
                return True
        return False

    num1 = input()
    list1 = [num1[i:j+1] for i in range(len(num1)) for j in range(i, len(num1))]
    result = set()
    for i in list1:
        if ispronic(int(i)):
            result.add(int(i))
    print(sorted(result))