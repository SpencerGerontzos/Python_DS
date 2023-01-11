"""
A bubble sort is one of the easier sorting algorithims we come by
where all we do is compare adjacent cells in the list until we reach the case where the number is in the correct spot
we do this process for all items in the list or until the algorithim has no swaps counted:

consider list |4 | 3 |2 | 9 | 10

starting from comparing index 0 and 1: 4>3 so we swap 3 | 4 | 2 | 9 | 10
                                       4>2 so we swap 3 | 2 | 4 | 9 | 10
                                       4 is now in place, now restart the process

                                       3>2 so we swap 2 | 3 | 4 | 9 | 10
                                       no other swaps recorded so we restart the process again

                                       as there were no swaps which took place this iteration we can claim the
                                       list is sorted and stop running the bubble sort

"""

"""
Time Complexity:

If we consider an already sorted list, we can use the condition that whenever we have not performed any swaps the list must be sorted
hence we can stop the algorithim quicker

As this still requires us to loop through the list, we still have linear time complexity hence O(n)

However if we consider the case where we have a list in descending order, for each iteration we will need to perform:
n-1,n-2,...,1 swap, hence we can write the time complexity as n-1 + n-2 + n-3 + ... + 1 which we know == n(n-1)/2
where we know this is quadratic time complexity or O(n^2)
"""

def Bubble_sort(x, type):
    n = len(x)
    count = 0
    for i in range(n):
        for j in range(n - i - 1):
            if type == "asc":
                if x[j] > x[j+1]:
                    swap_lst_items(x, j, j+1)
                    count +=1
            elif type == "desc":
                if x[j] < x[j+1]:
                    swap_lst_items(x, j, j+1)
                    count +=1
        if count == 0:
            return x
    return x

def swap_lst_items(x, i, j):
    x[i], x[j] = x[j], x[i]

#print(Bubble_sort([-2, 45, 0, 11, -9], "asc"))
#print(Bubble_sort([1,2,3,4], "asc"))

#inputLsts = [[],[1], [1,2], [2,1], [10, 0], [13,7,5], [23, 7, 13, 5], [1, 2, 2, 1, 0, 0, 15, 15], [135604, 1000000, 45, 78435, 456219832, 2, 546]]
#for i in range(len(inputLsts)):
#    print((sorted(inputLsts[i], reverse=True)) == Bubble_sort(inputLsts[i], "desc"))


#[-2, 45, 0, 11, -9]
#[-2, 0, 45, 11, -9]
#[-2, 0, 11, 45, -9]
#[-2, 0, 11, -9, -45]

#[-2, 0, 11, -9, -45]
#[-2, 0, 11, -9, -45]
#[-2, 0, -9, 11, -45]
#[-2, 0, -9, -45, 11]

#[-2, 0, -9, -45, 11]
#[-2, -9, 0, -45, 11]
#[-2, -9, -45, 0, 11]

#[-9, -2, -45, 0, 11]
#[-9, -45, -2, 0, 11]

#[-45, -9, -2, 0, 11]

