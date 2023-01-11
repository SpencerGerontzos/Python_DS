"""
A bucket sort takes a different approach to other sorting techniques as we are now going to create new storage units
or as in this algorithim 'buckets', to help sort the data

This sort works by creating n buckets for a list of size n

where each index of the bucket will correclate to the magnitudes of the input list.

lets consider the following example:

1.2 | .22 | .39 | .24 | .22 | 5.6

we first start by finding the optimal amount of buckets needed to complete the sort correctly
we can do this by dividing the largest number in our case 5.6 by the size of the input list (6)
5.6/6 = .9333 recurring

we will divide each input by this value and it should return the index of its respective bucket
1.2//.933 = 1
.22//.933 = 2
.39//.933 = 4
.24//.933 = 2
.22//.933 = 2
5.6//.933 = 6

lets now put these values into our buckets (nested lists):

[[1.2], [.22, .24, .22], [], [.39], [], [5.6]]

now we sort each list, in this example only list 2 needs to be sorted, the sorted lists look like:

[[1.2], [.22, .22, .24], [], [.39], [], [5.6]]

now we can concatenate all of these numbers together in their current order, excluding all of the emoty lists created

"""

"""
Time Complexity:

lets assume that all of the items were already sorted and even better assume that all of the input list is evenly distributed,
if the list is evenly distributed this implies that the buckets will be evenly filled. 

As a result of these two considerations we will be looping through the input list and subbing them into the buckets
which would be a linear time complexity O(n) and we can perform a sorting algorithim on the lists, now in this case we can
use an insertion sort which we also know is linear time complexity O(m), 

hence we will have a best case time complexity of O(n+m)

However lets assume in the worst case that all the numbers are not uniformly distributed, and they are all very close together
such as .99 | .98 | .97 | ... | .91

we can see that from performing our algorithim as described, all items will fall into the same nested list.
In this case now it depends on entirley the sorting algorithim we choose, lets consider the same algorithim we used, the insertion sort
as the list is in reverse order, we know that the algorithim runs in O(n^2) time, hence the bucket sort itsself runs in O(n^2) as well

We also need to consider the space complexity of the algorithim, or in other words how much additional space this algorithim takes up.
in most algorithims we dont consider this as we usually dont create any additional storage units (variables are not assumed to be storage units as they are minimal to runtime)

However in general if we have a list of size n and we dont create any lists or any additional DS's, our space complexity is O(n)
In the case of the bucket sort we have a list of size n, and an optimal amount of buckets m. Hence we have a space complexity of O(n+m)
"""

def Bucket_Sort(x, type):
    n = len(x)
    if n != 0:
        optimal_list_size = max(x)/n
    buckets = []

    for _ in range(n):#creates a nested list
        buckets.append([])

    for i in range(n):
        which_bucket = int(x[i]//optimal_list_size)#uses our opimal list size from above to determine which bucket the data should go to
        if which_bucket == n:
            buckets[which_bucket-1].append(x[i])#appending the largest piece of data into the bucket
        else:
            buckets[which_bucket].append(x[i])#appending the data into the buckets

    for i in range(n): #sorting each bucket
        if len(buckets[i]) > 1:#checking to see if there is anything to sort
            buckets[i] = Insertion_Sort(buckets[i], type) #sorts the buckets #NOTE we can use any sort in this algorithim

    res = []
    for i in range(n):#concatenate the result of each bucket
        res += buckets[i]
    return res

def Insertion_Sort(x, type):
    n = len(x) #indicates the size of the list
    #starting at the second item in the list as we assume that the first item is already sorted
    for i in range(1, n):
        # we take the item we want to sort into the sublist which is located at index i
        #we know that all items before index i are already sorted (in otherwords from index 0 to in index i-1 is already sorted)
        #we use this function to sort these items
        sort_item_into_sublist(x, i-1, i, type)
    return x

def sort_item_into_sublist(lst, j, i, type):#we use the input list, the index up to all items are sorted and the next item to sort
    if type == "asc":
        while j >= 0 and lst[j] > lst[i]:
            swap_lst_items(lst, i, j)#as we have compared the items we can see that they are smaller/larger hence we can swap them
            j -= 1 #as the items have been swapped we now need to compare the next 2 items hence subracting 1 from both
            i -= 1
    elif type == "desc":
        while j >= 0 and lst[j] < lst[i]:
            swap_lst_items(lst, i, j)#as we have compared the items we can see that they are smaller/larger hence we can swap them
            j -= 1 #as the items have been swapped we now need to compare the next 2 items hence subracting 1 from both
            i -= 1
def swap_lst_items(x, i, j):
    x[i], x[j] = x[j], x[i]


#print(Bucket_Sort([1.2, .22 ,.39, .24, .22, 5.6], "asc"))
#inputLsts = [[],[1], [1,2], [2,1], [10, 0], [13,7,5], [23, 7, 13, 5], [1, 2, 2, 1, 0, 0, 15, 15], [135604, 1000000, 45, 78435, 456219832, 2, 546]]
#for i in range(len(inputLsts)):
#    print((sorted(inputLsts[i])) == Bucket_Sort(inputLsts[i], "asc"))
