"""
Welcome to our first searching algorithim, the Binary search

now by now from the first few algorithims im sure we can realise a simple way to search through a list to find the desired algorithim
heres the pseudocode:

for i in range(array):
    if array[i] == desired_item:
        return True
return False

where all we are doing is comparing each item with the list until we reach the end.

We can see that if the item we are searching for is the first item of the list we are complete.
Hence we only require one compairson hence O(1) time complexity

However consider the convrese where the item is the last item in the list, we still need to loop through the entire list
hence we have O(n) time complexity
"""

"""
This is where the binary search comes in (NOTE: The list must be sorted in a specified order for this algorithim to work)

We start by finding the middle item in the list and compare it with the value we are searching for, if it is the value, great we are finished
and if it isnt we identify if our value is smaller or larger than the middle value, since the list is already sorted we can reject the half of the list where we arent interested in and repeat
we do this until we have 1 item left, where it is the item we are looking for, or the item is not in the list.

Lets give an example:

consider we are finding the number 3 from the set: 1 | 2 | 3 | 4 | 5 | 6 | 7

we start by finding the middle value in our case index 3 is the middle value with magnitude of 4
we compare this with our number 3 and realise that 3<4 hence we reject items of index from 3 to 6 so we are now searching
1 | 2 | 3 , we find the middle index and find that 2<3 hence we reject index's 0 and 1. Now we are left with | 3 | and we have found our value
"""

"""
Time Complexity:

We realise that the quickest time that we can find our number is in the list is if the number we are comparing si the middle item of the list in the first iteration of the binary search
as it is only 1 compare, hence we can justify that the best case time complexity is simply a comparision, hence O(1)

However lest consider the case like our example, where after each iteration we need to half the size of the list until we find the desired value
we can see that if it takes it would take log_2_(n) halvings of the list to correctly determine if the item is in the list or not
hence we can say that our worst case time complexity is O(log(n)) time complexity
"""
import unittest


def Binary_search(x, input):
    while len(x) > 0:
        index = find_mid(x) #used to find the middle index of the list
        if x[index] == input:#checking case where the middle value of the list is equal to the input
            return True
        elif x[index] > input:#case where middle value is larger than input
            x = x[0:index]#reject all items from the index and above
        else: #case where middle value is smaller than the input
            x = x[index+1:] #reject all values from index 0 to the index
    return False#if we cannot find the number (case of comparing an empty list we must not have the intem in our list)

def find_mid(lst):
    return (len(lst)//2)

class TestBinarySearch(unittest.TestCase):

    def test_binary_search(self):
        self.assertEqual(Binary_search([], 3), False)
        self.assertEqual(Binary_search([1, 2], 3), False)
        self.assertEqual(Binary_search([1, 2, 3, 4], 3), True)
        self.assertEqual(Binary_search([1, 2, 3, 4, 5], 3), True)
        self.assertEqual(Binary_search([1, 2, 3, 4], 3), True)
        self.assertEqual(Binary_search([1, 2, 3, 4], 1), True)
        self.assertEqual(Binary_search([1, 2, 3, 4], 4), True)

if __name__ == '__main__':
    unittest.main()

#print(Binary_search([1,2,3,4,5,6,7], 0))