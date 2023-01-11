""""
Welcome to our first divide and conquer algorithim, the Merge Sort

The concept of the divide and conquer paradigm is to recursivley break down the problem into subproblems until we reach
a state where we can solve these problems directly and recombine them to give us the original solution to the problem

lets take a look into mergesort and see what it can do for us

Merge sort divides the list of data into halves and sorts these halves respectivley
it then combines these halves together which as a result sorts the data in the implied ordering.

Lets break down an example:

| 5 | 8 | 2 | 4 | 7 | 1

lets break the list in half
| 5 | 8 | 2 |  and | 4 | 7 | 1 |

and again

| 5 | 8 | and | 2 |         and | 4 | 7 | and | 1 |

and 1 more time (subjective to the size of the input list)

| 5 | and | 8 | and | 2 |         and | 4 | and | 7 | and | 1 |


Now lets recombine the list from the base case BUT after each iteration lefts sort these sublists:

| 5 | 8 | and | 2 |             and | 4 | 7 | and | 1 | #happens to already be sorted

and recombine these 2 sublists again

| 2 | 5 | 8 |  and | 1 | 4 | 7 |

and recombine one more time

| 1 | 2 | 4 | 5 | 7 | 8 where we have a sorted list.

"""

"""
Time Complexity:

As the first step of the algorithim requires us to half the list until we are left with single items from the list\
we can see that log_2_(n) halfs will occur implying O(log(n). Furthermore we need to combine the n elements in each depth of the recursion
implying we have O(n). Combining these 2 halves of the algorithim yield O(nlog(n)) time complexity.

"""

def Merge_Sort(x):
        if len(x) > 1:
            mid = find_mid(x) #we find the middle index
            Left_lst = x[:mid]#half the list into left component and right component
            Right_lst = x[mid:]
            Merge_Sort(Left_lst) #recursivley call our function which splits the list into left and right until we only have items of size 1
            Merge_Sort(Right_lst)
            return Merge(x, Left_lst, Right_lst)#call our merge function which combines the lists

def Merge(x, lst1, lst2):
    i = j = k = 0
    while i < len(lst1) and j < len(lst2):#loop condition which checks that both lists still have items to compare
        if lst1[i] < lst2[j]:#checking the case where the left list (lst1) has the smaller item
            x[k] = lst1[i] #sets the item into our resulting list
            i +=1 #increment our left pointer
        else:
            x[k] = lst2[j] #case where the right list has the smaller item
            j += 1 # increment our right pointer
        k += 1#we can now increment the list pointer, so we can place the next item in the list

    #we notice that in the case where our left and right list sizes differ, we still have
    #a list(s) which will not have the items transferred into the resulting list
    #the following takes care of these cases for both the left and right sublist respectivley

    while i < len(lst1):
        x[k] = lst1[i] #fills the rest of the resulting array with the left list values
        i += 1
        k += 1

    while j < len(lst2): #fills the rest of the resulting array with the right list values
        x[k] = lst2[j]
        j += 1
        k += 1
    return x#returns our sorted list

def find_mid(lst):#used to find the middle index
    return (len(lst) // 2)

print(Merge_Sort([5, 8 ,2 ,4 ,7 ,1]))