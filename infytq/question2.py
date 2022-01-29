# QUESTION 2:
# A string which is a mixture of letters, numbers, and special characters from which produce the largest
# even number from the available digit after removing the duplicates digits.
# If an even number did not produce then return -1.
# Ex: infosys@337
# O/p : -1
# — — — — — — — — — — — -
# Hello#81@21349
# O/p : 984312

if __name__ == '__main__':
    def largest(str1):
        l1 = []
        i = 0
        for i in str1:
            if i.isdigit():
                if i not in l1:
                    l1.append(i)
        l1.sort(reverse=True)
        for i in range(len(l1) - 1, 0, -1):
            if int(l1[i]) % 2 == 0:
                z = l1[i]
                l1.remove(z)
                l1.append(z)
                print("".join(l1))
                break
        if i == 1:
            print("-1")


    s1 = "infosys@337"
    s2 = "Hello#81@21349"
    largest(s1)
    largest(s2)