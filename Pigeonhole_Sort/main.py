"""
A pigeonhole sort uses an auxillary nested list

we start by finding the largest and smallest item in the list, we create nested lists, the amount is determined by the difference in the largst and the smallest values
we then loop through our input list and add the item in the index equal to the items value in the auxillary list.
We repeat this process for the entire input list and then we simply concatenate the non empty nested lists and we are complete

lets walk through an example:

9 | 2 | 3 | 8 | 1 | 6 | 9

we first create our auxillary list with max - min = 9 - 1 = 8 nested lists
[[],[],[],[],[],[],[]]

we then iterate through our list and add each item into the list (subtracting the smallest value so we can allow all elements to be included in the aux list)

9 - 1 = index 8
2 - 1 = index 1
3 - 1 = index 2
8 - 1 = index 7
1 - 1 = index 0
6-1 = index 5
9-1 = index 8

our auxillary list should look like:

[[1], [2], [3], [], [], [6], [], [8], [9, 9]]

and we concatenate each list item and hence: 1 | 2 | 3 | 6 | 8 | 9 | 9
"""

"""
Time Complexity:

as we can see we are creating an auxillary list so we will also have a non constant space complexity,
as can see the amount of nested lists are determined from the largest and smallest items in the list
in other words the range of the list items determines the amount of nested lists (these are the 'pigeonholes')

we also have an array which stores the input items hence size n

we can see that the space complexity will be O(n + range)

Similarly we need to add n items to k (k = range) buckets, and then we need to loop through the k buckets to extract the sorted values
hence we also have O(n+k) time complexity.

NOTE: this algorithim works when the items are close together, as if we have a max of 10000 and a min of 0
we will have to add each time to a giant auxillary list, which is very unpractical

"""
def create_nested_list(size):
    aux = []
    for _ in range(size):
        aux.append([])
    return aux


def Pigeonhole_sort(x, type):
    n = len(x)
    if n == 0:
        return [] #case where we have an empty input
    maxi = max(x) #finding the largest /smalllest inputs of the list
    mini = min(x)

    r = maxi - mini + 1#finding the range of list inputs

    aux = create_nested_list(r)#create our nested list of size r
    for i in range(n):

        phole_index = x[i] - mini #find the index where the item should be inserted
        aux[phole_index].append(x[i]) #append to the list

    i = 0
    p = 0
    k = len(aux)
    while i < k:#we iterate over the auxillary list
        count = 0
        j = 0
        m = len(aux[i])
        while j < m:#we iterate through the nested list
            x[p] = aux[i][j]#set the input list item to the nested list item
            if m == 1: #if the nested list only has one item we can increment it and move on to the next nested list
                i += 1
            p += 1#we then increment our input list index as we will be replacing the next item in the input list
            count += 1#keeps track of how many input items exist in the nested list
            j += 1#move through to the next item in the nested list

        if m != 1: # we check to see if we have a larger nested list size than 1
            i += 1 #and if this is the case we can move to the next nested list

    return x


#print(Pigeonhole_sort([1, 2, 2, 1, 0, 0, 15, 15], "asc"))
#print(Pigeonhole_sort([2, 1], "asc"))
#print(Pigeonhole_sort([13, 7, 5], "desc"))

#inputLsts = [[],[1], [1,2], [2,1], [10, 0], [13,7,5], [23, 7, 13, 5], [1, 2, 2, 1, 0, 0, 15, 15], [135604, 1000000, 45, 78435, 456219832, 2, 546]]
#for i in range(len(inputLsts)):
#    print((sorted(inputLsts[i],reverse=True)), Pigeonhole_sort(inputLsts[i], "desc"))
