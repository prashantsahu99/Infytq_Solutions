# QUESTION 3:
# Take input a number ’N’ and an array as given below.
# Input:-N = 2
# Array =1,2,3,3,4,4
# O/p : 2
# Find the least number of unique elements after deleting N numbers of elements from the array.
# In the above example, after deleting N=2 elements from the array.
# In above 1,2 will be deleted.
# So 3,3,4,4 will be remaining so,
# 2 unique elements are in the array i.e 3 and 4

if __name__ == '__main__':
    n = 2
    list1 = [1, 2, 3, 3, 4, 4]
    s = set(list1)
    print(len(s) - n)