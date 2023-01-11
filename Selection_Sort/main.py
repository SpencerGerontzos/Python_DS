"""
Selection Sort is one of the most simplistic sorting algorithims we can come by in CS
really the starting journey for most of us

Selection sort is the idea of sorting 1 element at a time in the list, where at the end
of each iteration of the algorithim 1 more item will be sorted.

In other words an invariant of this algorithim (Something that stays constant)
is that after the ith iteration in the algorithim, cells 0 to i will be in ascending/descending order

with this in mind we can also deduce that items from i+1 to n will still be unsorted
"""
"""
Description of the algorithim:
    we start with an input: a list of 1xn in size and an indicator which tells us how we want the list sorted (in ascending/descending order) where we plan to output a the same list of size 1xn however in a sorted order
    
    our algorithim is all about swapping cells in our list into the correct spot,
    consider sorting in ascending order, we will loop through the list and find the smallest number and swap it with the first item in the list
    similarly once the smallest item is in the front of the list we can find the second smallest number in the list and swap it with the second item in the list
    (or we can find the smallest item in the list STARTING from the second item onwards).
    We notice that since we are always swapping items in an order from smallest to largest we will always end with a sorted list.
    
    The same logic works for descending order (convince yourself of this)
"""

"""
time complexity:

unfortunatley the selection sort doesnt actually review the quality of the order that a list is already in
as each iteration the list needs to find the smallest/largest item in the list to swap into place.
Even if the list was already sorted (lets assume it is sorted ascendingly) to find the smallest number in the first iteration
even though the smallest number our be the first item we would still need to compare it with the entire list. This process repeats itsself as described in the algorithim

hence we have to compare every value after each iteration of the algorithim
or in other words in each loop we perform we need to performa nother loop to compare all of the values inorder to find our smallest/largest

this can be viewed as a quadratic time complexoty or O(n^2) at all times

"""
import unittest

def selection_sort(x, type):
    n = len(x)
    for i in range(n): #we loop over the entire list
        index = i  #this is the variable that keeps track of the smallest item in the lsit
        for j in range(i+1, n):#we then look to compare items in the list that are not correctly sorted
            #we loop through our list until we find the smallest/largest item in the sublist we are viewing
            if type == "asc":
                if compare(x[index], x[j]):#we compare the smallest/largest item with the next item in the list we are viewing
                    index = j
            elif type == "desc":
                if compare(x[index], x[j]) == False:  #
                    index = j
        #after we have found the smallest/largest item in the sublist we are comparing we can swap
        #it with the ith cell in the list
        swap(x, index, i)
    return x

def swap(x, i, j):
    x[i],x[j] = x[j], x[i]

def compare(x, y):
    return (x > y)


class selection_sort_tests(unittest.TestCase):
    def sort(self, lst):
        copy = lst[:]
        selection_sort(copy, "asc")
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
#print(selection_sort_asc([27, 43, 78, 69, 134, 134, 12], "desc"))