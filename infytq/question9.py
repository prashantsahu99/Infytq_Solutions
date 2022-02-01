# Question 9.
# Password generation
# Given input of array of string in format <emp name> <emp number> separated by comas
# ,Emp
# should contain only alphabets and employee number. You have to generate password for
# Ex:
# input: Robert: 36787, Tina: 68721, Jo:56389
# Output: tiX
# Conditions: len of robert is 6 and 6 is present in emp number
# robert (36787), so return the alphabet at position 6 that is t.
# Now len of tina is 4 and 3 is not present in the 68721 so select the number which is max and
# less than the len of tina so select 2 return the alphabet that is at position 2 that is i.
# Now In of Jo is 2 it is not present in 56389 and there is no present any number which is less
# than 2 so return X.
if __name__ == '__main__':
    list1 = [x for x in input().split(',')]
    print(list1)
    name = []
    length = []
    for i in list1:
        s, n = i.split(':')
        name.append(s)
        length.append(n)
    print(name)
    print(length)

    def pas(ss, n1):
        if str(len(ss)) in n1:
            return ss[len(ss)-1]
        elif str(len(ss)) not in n1:
            number1 = list(n1)
            sorted(number1, reverse=True)
            for j in number1:
                if int(j) < len(ss):
                    return ss[int(j)-1]
        return "X"

    for i in range(0, len(length)):
        print(pas(name[i], length[i]), end='')