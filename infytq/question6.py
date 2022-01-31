# Question 6.
# Maximum subarray
# An array is given suppose a =[3,5,8,2,19,12,7,11] One have to find the largest subarray that
# the element satisfy the following condition
# x[i]=x[i-1]+x[i-2] If more than one substring if found then largest one has to print the array
# which starts with the minimum elements and if they are also same then the array with
# minimum second element and so on.
# Here the subarrays |2,3,5,8],[3,8,11],[5,7,12,19] Expected is [2,3,5,8]

if __name__ == '__main__':
    list1 = [int(x) for x in input().split(",")]
    list2 = []
    list1.sort()
    list2.append(list1[0])
    list2.append(list1[1])
    for i in range(2, len(list1)):
        if (list2[i-1] + list2[i-2]) in list1:
            list2.append(list2[i-1] + list2[i-2])
        else:
            break
    print(list2)