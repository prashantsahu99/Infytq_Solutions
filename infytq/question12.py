# 12. Matrix problem
# Read m’m>4
# n=m+1
# Take m*n matrix
# If any num is consecutive for 3 times either in a row, column, diagonals print the num, if
# there are multiple num print min of those num
# Ex: m=6 take 6*7 matrix
# 2 3 4 5 6 2 4 3
# 2 3 4 7 6 7 6 2
# 2 3 5 5 5 5 2 5
# 2 3 1 1 2 1 3 6
# 1 1 1 1 9 0 3 5
# 2 3 1 1 5 1 2 7
# O/p=1

if __name__ == '__main__':
    m = int(input())
    n = m+1
    list1 = []
    for i in range(m):
        list2 = [int(x) for x in input().split()]
        list1.append(list2)
        result = []
    # column
    for i in range(m):
        for j in range(n-2):
            if list1[i][j] == list1[i][j+1] == list1[i][j+2]:
                result.append(list1[i][j])
    # row
    for i in range(m-2):
        for j in range(n):
            if list1[i][j] == list1[i+1][j] == list1[i+2][j]:
                result.append(list1[i][j])
    # diagonal
    for i in range(m-2):
        for j in range(n-2):
            if list1[i][j] == list1[i-1][j-1] == list1[i-2][j-2]:
                result.append(list1[i][j])
    print(min(result))

