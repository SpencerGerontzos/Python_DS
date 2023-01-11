"""
Welcome to our first searching algorithim, the linear search

the Linear Search is one of the more straightforward algorithims to learn

simply take any list: a | b | c | d and any input say c

lets compare each item in the list with our input to check if our input list contains our input value
a != c, b!= c and then we see that c = c and we can return true. If our input is not in the list we simply return false
"""

"""
Time complexity:

As we can notice the best case would be if the first item in the list is our input item,
and since it is only the cost of a comparisn to check we can see that we have a best case time complexity of O(1)\

However consider the case where the input number is the last item in the list or even not in the list at all
we need to traverse through the entire list in order to return. Hence we can see why the algorithim is called a linear search 
as it completes the search in a worst case time comlexity of O(n)
"""

def Linear_Search(lst, x):
    n = len(lst)#length of list
    for i in range(n):#loops through each item in the list
        if lst[i] == x:#checks to see if the item in the list we are comparing to is the input
            return True
    return False#occurs when the input number is not in the input list