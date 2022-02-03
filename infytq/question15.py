# Question15. Longest palindrome
# Find the longest palindrome from a string
# Input: moomso
# Possible cases
# Moom, mom, oso, 000, omo
# Longest is moom so output: moom

if __name__ == '__main__':
    s1 = input()
    list1 = [s1[i:j+1] for i in range(len(s1)) for j in range(i, len(s1))]
    large = 0
    result = ''
    for i in list1:
        if i[::-1] == i:
            if len(i) > large:
                large = len(i)
                result = i
    print(result)