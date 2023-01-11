"""
Insertion Sort is again one of the most simple sorting techniques that we have in our arsenal
"""
"""
Description of algorithim
Insertion sort takes a similar approach to a selectino sort, however instead of finding the smallest element in each sublist and swapping it to the correct position
Insertion sort takes each item at a in the list, regardless of magnitude and sorts it into its correct position in the sublist

consider the example: 5 | 2 | 1 | 7 | 9

we start at item 2, as the assumtion of the algorithim is that the first item is always sorted, we can start at the next element
we can compare item 2 to the rest of the sorted list (in this iteration the only sorted item is item 5) and we realise that as item 2 is smaller than item 5
we swap the 2 items and do this until we have all our item 2 in the correct order in the sublist. we can now say that indexs 0 and 1 are in the correct order

2 | 5 | 1 | 7 | 9

now we view item 1, and realise that 1<5 so we swap these items and similarly note that 1<2 and we swap these items
so again, we sort our item into the correct order, and since the sublist is already in order, we know that adding a new item and sorting it in place will still keep the item sorted

we repeat this process until the list is complete
"""

"""
Time complexity: 

This is a great algorithim when we have items in a close to sorted order:

consider the sorted list 1 | 2 | 3 | 4 | 5

if we run our algorithim we can see 2 is larger than 1 in our first iteration
                                    3 is larger than 2 in our second iteration
                                    ....
                                    5 is larger than 4 in our last iteration
                                    
We can see that all we need to do is loop through each item of the list and nothing more, as nothing needs to be sorted
Hence we can see that the algorithim runs in linear time O(n)
                                    
However consider the example where the list is in reverse order:
                          5 | 4 | 3 | 2 | 1
                        
if we run our algorithim we can see that 4<5 so we need to sort 4 into place
                                         3<5 and 3<4 so we need to sort this list in place
                                         ...
                                         2 | 3 | 4 | 5 | 1 where 1 needs to be sorted to the front of the list
                                         
as we can see since each number needs to be sorted to the front of the sublist this algorithim runs with a quadratic complexity
O(n^2)
"""

"""
rigorous proof of time complexity:
... (Later)
"""
import unittest

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


"""
class insertion_sort_tests(unittest.TestCase):
    def sort(self, lst):
        copy = lst[:]
        Insertion_Sort(copy)
        return copy

    def test_empty_list(self):
        lst = []
        sorted_lst = self.sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_single_item(self):
        lst = [1]
        sorted_lst = self.sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_two_items_sorted(self):
        lst = [1, 2]
        sorted_lst = self.sort(lst)
        self.assertEqual(lst, sorted_lst)

    def test_two_items_unsorted(self):
        lst = [2, 1]
        sorted_lst = self.sort(lst)
        self.assertEqual(sorted_lst, [1, 2])

    def test_zero_in_list(self):
        lst = [10, 0]
        sorted_lst = self.sort(lst)
        self.assertEqual(sorted_lst, [0, 10])

    def test_odd_number_of_items(self):
        lst = [13, 7, 5]
        sorted_lst = self.sort(lst)
        self.assertEqual(sorted_lst, [5, 7, 13])

    def test_even_number_of_items(self):
        lst = [23, 7, 13, 5]
        sorted_lst = self.sort(lst)
        self.assertEqual(sorted_lst, [5, 7, 13, 23])

    def test_duplicate_integers_in_list(self):
        lst = [1, 2, 2, 1, 0, 0, 15, 15]
        sorted_lst = self.sort(lst)
        self.assertEqual(sorted_lst, [0, 0, 1, 1, 2, 2, 15, 15])

    def test_larger_integers(self):
        lst = [135604, 1000000, 45, 78435, 456219832, 2, 546]
        sorted_lst = self.sort(lst)
        self.assertEqual(sorted_lst,
                         [2, 45, 546, 78435, 135604, 1000000, 456219832])


if __name__ == '__main__':
    unittest.main()

"""

print(Insertion_Sort( [135604, 1000000, 45, 78435, 456219832, 2, 546], "desc"))
print(Insertion_Sort([1, 2, 2, 1, 0, 0, 15, 15], "desc"))
print(Insertion_Sort([23, 7, 13, 5], "desc"))
print(Insertion_Sort([13, 7, 5], "desc"))
print(Insertion_Sort([10, 0], "desc"))
print(Insertion_Sort([2, 1], "desc"))
print(Insertion_Sort([1, 2], "desc"))
print(Insertion_Sort([1], "desc"))
print(Insertion_Sort([], "desc"))