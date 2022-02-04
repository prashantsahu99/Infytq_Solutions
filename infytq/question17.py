# Question17. Unique substring
# A string is given we have to find the longest substring which is unique (that has no repetition
# ) and min size is 3.
# If more than one sub string is found with max length then we have to print one which appeared
# first in thw string
# If no substring is present which matches the condition then we have to print -1;
# Ex input: A@bcd1abx”
# Output: “A@bcd1
if __name__ == '__main__':
    s = input()
    longest = []
    for i in s:
        if i.lower() in longest or i.upper() in longest:
            break
        else:
            longest.append(i)
    print(''.join(longest))