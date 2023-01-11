"""
Comb sort takes a similar approach to a bubble sort, where we compare items and swap them wrt the order.
The difference being that instead of comparing adjacent items, we create a gap and compare these items sequentially.

Let me show you an example:

consider 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 | 10

where a bubble sort compares 1, 2
                             2, 3
                             3, 4
                             etc

a comb sort will compare items a 'gap' length apart
This gap will be determined by the |list|//1.3, we use 1.3 as it is shown to minimize the runtime of the algorithim
(logic will be shown in the in depth analysis). in this case 10//1.3 == 7

therefore we compare items:  1, 8
                             2, 9
                             3, 10

after we reach the end of the list we divied our gap futher by 1.3, where we do this until we have a gap size of 1
where we are at the base case (which is our bubble sort).

Lets now run through a proper example:

8, 4, 1, 56, 3, -44, 23, -6, 28, 0

we have |list| = 10
therefore our gap size is 10//1.3 = 7

compare: 8, -6 (as -6 < 8 swap)
         4, 28
         1, 0 (as 0 < 1 swap)

-6, 4, 0, 56, 3, -44, 23, 8, 28, 1

our new gap size is 7//1.3 = 5

compare: -6, -44  (as -44 < -6 swap)
          4, 23
          0, 8
          56, 28 (as 28 < 56 swap)
          3, 1 (as 1 < 3 swap)

-44, 4, 0, 28, 1, -6, 23, 8, 56, 3

our new gap size is 5//1.3 = 3

compare: -44, 28
          4, 1   (as 1 < 4 swap)
          0, -6  (as -6 < 0 swap)
          28, 23 (as 23 < 58 swap)
          1, 8
          -6, 56
          23, 3  (as 3 < 23 swap)

-44, 1, -6, 3, 4, 0, 28, 8, 56, 23

our new gap size is 3//1.3 = 2

compare: -44, -6
          1, 3
          -6, 4
          3, 0 (as 0< 3 swap)
          4, 28
          0, 8
          28, 56
          8, 23

-44, 1, -6, 0, 4, 3, 28, 8, 56, 23

our next gap size is 2//1.3 = 1

compare: -44, 1
         1, -6 (as -6 < 1 swap)
         -6, 0
         0, 4
         4, 3 (as 3 < 4 swap)
         3, 28
         28, 8 (as 8<28 swap)
         8, 56
         56, 23 (as 23< 56 swap)

-44 -6 0 1 3 4 8 23 28 56 and we are sorted!

"""

"""
Time Complexity:

##need to write a proper analysis
"""

def Comb_sort(x, type):
    const = 1.3
    n = len(x)
    gap_size = n // 1.3

    while gap_size >= 1:
        gs = int(gap_size)
        i = 0
        while gs < n:
            if type == "asc":
                if x[i] > x[gs]: #comparing gapped items
                    swap_lst(x, i, gs) #swap the items if they are not in correct order


            elif type == "desc":
                if x[i] < x[gs]:
                    swap_lst(x, i, gs)
            i += 1 #we increment both of our index's to compare the next 2 values
            gs += 1

        gap_size //= const #after we have compared the ith item and the last item in the list we can now find the new gap size
    return x


def swap_lst(x, i, j):
    x[i], x[j] = x[j], x[i]

inputLsts = [[],[1], [1,2], [2,1], [10, 0], [13,7,5], [23, 7, 13, 5], [1, 2, 2, 1, 0, 0, 15, 15], [135604, 1000000, 45, 78435, 456219832, 2, 546]]
for i in range(len(inputLsts)):
    print((sorted(inputLsts[i], reverse= True)) == Comb_sort(inputLsts[i], "desc"))
