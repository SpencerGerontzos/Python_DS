"""
welcome to the directory on finding the extrema of a data set (smallest and largest values)
as im sure we realise by now, we have hundreds of ways to sort a piece of data,we can also see that this also is the
same for searching so lets dive into it, by finding the smallest and largest values
"""

"""
our approach to finding these values is simple, we are going to comare items in a list and find the largest/smallest
(This should sound like a familiar task from one of our sorting algorithims: insertion sort)
"""

"""
Time Complexity:

this algorithim will compare each item in the list to the current largest/smallest value
this means that we will have to copmare n items regardless of the ordering of the list
hence our best/worst case time complexity id O(n)
"""

def find_extrema(x, type):
    n = len(x)
    val = x[0]
    for i in range(1, n):
        comp = x[i] #here is the value in the list we are looking at
        if type == "max":
            if comp > val: #we are checking to see if the current largest value is smaller than our current value we are looking at
                val = comp # if this is the case we can set our new max/min to this value
        elif type == "min":
            if comp < val:
                val = comp
    return val

print(find_extrema([1,3,2,4,5], "min"))