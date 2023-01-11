"""
welcome to a different sorting algorithim, the cycle sort

the cycle sort takes a slightly dufferent approach to sorting
we start by taking the first item in the list, and comparing to see how many values are smaller than this first item.
we insert the item in this index and repeat the process for the next item. Now we will run through 2 examples here, one for a case with no duplicates and one with duplicates
you will see why momentarily
"""

"""
10 | 1 | 4 | -1 | 5 | 0

we first take 10 out of the list and count how many items are smaller than 10, 
in this case we have 5 items smaller than 10.
we then replace 10 with the 5th index item and now we have the 5th index item to do the same with

None | 1 | 4 | -1 | 5 | 10

we then see how many items are smaller than zero in our example only one number is (-1) so we replace it at this index: 1

None | 0 | 4 | -1 | 5 | 10 and we are now performing the same process for 1

as 2 items are less than one lets do the same process

None | 0 | 1 | -1 | 5 | 10 where we are now performing the same process for 4

None | 0 | 1 | 4 | 5 | 10 where -1 is next

in the case where nothing is smaller than -1 we can now replace it at the starting index where None is our place holder

-1 | 0 | 1 | 4 | 5 | 10


However now lets consider a duplicate case:

[1, 2, 2, 1, 0, 0, 15, 15]

for the sake of this example i will only explain the steps when necesarry 
if you are confused please refer to the first example to get up to speed with the current workings


"""


def Cycle_Sort(x):
    n = len(x)
    count = 0

    if n == 0:
        return []
    for i in range(n):
        val = x[i]
        x[i] = None
        while x[i] == None:
            for j in range(i + 1, n):
                if val > x[j]:
                    count += 1
            temp = x[count + i]
            if temp == val:
                temp = x[count + i + 1]
                x[count + i + 1] = val
            else:
                x[count + i] = val

            val = temp
            count = 0

    return x


# print(Cycle_Sort([1, 4, 6, -1, 0, 0]))

#
sets = [[], [1], [1, 2], [2, 1], [10, 0], [13, 7, 5], [23, 7, 13, 5], [135604, 1000000, 45, 78435, 456219832, 2, 546],
        [1, 2, 2, 1, 0, 0, 15, 15]]

for i in range(len(sets)):
    print(sorted(sets[i]) == Cycle_Sort(sets[i]))