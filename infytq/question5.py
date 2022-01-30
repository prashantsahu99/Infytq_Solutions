# QUESTION 5:
# Number of odd sub-arrays.
# Find the number of distinct subarrays in an array of integers such that the sum of the subarray is an odd integer,
# two subarrays are considered different if they either start or end at different indexes.
# Input:
# 1
# 3
# 1 2 3
# Output:
# 4
# Explanation : Total subarrays are [1], [1, 2], [1, 2, 3], [2], [2, 3], [3]
# In this there are four subarrays which sum is odd i.e: [1],[1,2] ,[2,3],[3].
import itertools

if __name__ == '__main__':
    n = 3
    list1 = [1, 2, 3]
    com = []
    for i in range(1, n+1):
        comb = itertools.combinations(list1, i)
        com.extend(comb)
    com.sort()
    for i in com:
        if sum(i) % 2 != 0:
            print(list(i), end=" ")