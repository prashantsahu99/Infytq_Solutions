# Question7.
# Special string reverse
# special string reverse
# Input Format: b@rd
# output Format: d@rb
# Explanation:
# We should reverse the alphabets of the string by keeping the special characters in the same position

if __name__ == '__main__':
    str1 = input()
    list1 = []
    list2 = []
    list3 = []
    for i in range(0, len(str1)):
        if str1[i].isdigit() or str1[i].isalpha():
            list1.append(str1[i])
        else:
            list2.append(str1[i])
            list3.append(i)
    list1.reverse()
    for i in range(0, len(list2)):
        list1.insert(list3[i], list2[i])
    print("".join(list1))