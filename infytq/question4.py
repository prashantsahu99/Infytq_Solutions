# QUESTION 4:
# A non-empty string containing only alphabets. print the longest prefix from the input string which is the same as the
# suffix.
# Prefix and Suffix should not be overlapped.
# Print -1 if no prefix exists which is also the suffix without overlap.
# Do case-sensitive comparison.
# Positions start from 1.
# Input : xxAbcxxAbcxx
# o/p: xx (‘xx’ in the prefix and ‘xx’ in the suffix and this is the longest one in the input string so the output will
# be ‘xx’).
# Input: Racecar
# o/p: -1 (There is no prefix which is also a suffix so the output will be -1).

if __name__ == '__main__':
    def prefix_suffix(str1):
        size = len(str1)//2
        pre = ''
        for i in range(0, size):
            pre = str1[0:i+1]
            suf = str1[len(str1)-1-i:len(str1)]
            if pre == suf:
                continue
            else:
                break
        if pre[0:len(pre)-1] != "":
            print(pre[0:len(pre)-1])
        else:
            print("-1")





    s1 = "xxxAbcxxAbcxxx"
    s2 = "Racer"
    prefix_suffix(s1)
    prefix_suffix(s2)