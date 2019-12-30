"""
    Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

    Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2. 
    Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.

 

Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]
 

Constraints:

arr1.length, arr2.length <= 1000
0 <= arr1[i], arr2[i] <= 1000
Each arr2[i] is distinct.
Each arr2[i] is in arr1.
"""


def relativesort1(arr1, arr2):
    arr_sort = []
    for i in arr2:
        temp = arr1.count(i)
        cin = [i] * temp
        arr_sort += cin
    arr_not_in = list(filter(lambda x: x not in arr_sort, arr1))
    arr_not_in.sort()
    arr_sort += arr_not_in
    return arr_sort

# def relativesort2(arr1, arr2):
#     arr_sort = []
#     arr_not_in = []
#     for i, j in enumerate(arr2):
#         temp = arr1.count(j)
#         if temp == 0:
#
#         cin = [j] * temp
#         arr_sort += cin
#
#     return arr_sort

def relative_sort_array(arr1, arr2):
    sorted_stack = []
    unsorted_stack = []
    for item2 in arr2:
        if item2 in arr1:
            found_indices = [i for i, x in enumerate(arr1) if x == item2]
            for i in found_indices:
                sorted_stack.append(arr1[i])
    for item in arr1:
        if item not in sorted_stack:
            unsorted_stack.append(item)

    return sorted_stack+sorted(unsorted_stack)


def relative_sort_array2(arr1, arr2):
    sorted_stack = []
    unsorted_stack =[]

    for item2 in arr2:
        found_indices = [i for i, x in enumerate(arr1) if x == item2]
        found_stack = [y for i, y in enumerate(arr1) if i in found_indices]
        sorted_stack.extend(found_stack)

    for item in arr1:
        if item not in sorted_stack:
            unsorted_stack.append(item)

    return sorted_stack+sorted(unsorted_stack)


# this is coded by Ricky, super smart and efficient
def relative_sort_array3(arr1, arr2):
    res = []
    for each in arr2:           # iterate all items in arr2
        while (each in arr1):   # as long as the item in arr2 can be found in arr1
            res.append(each)    # add the item to the end of the list to be returned

            arr1.remove(each)  # and immediately remove the item in arr1, therefore in the end of the for loop,
            #                    arr1 will only contains items not found in arr2
    return res+sorted(arr1)


# this is an extremely concise and efficient pythonic code for this question
def relative_sort_array4(arr1, arr2):
    order = {v: i for i, v in enumerate(arr2)}  # create a dictionary to be used for sorting key, or can be called a
    #                                             sorting pattern

    return sorted(arr1, key=lambda a: order.get(a, 1000 + a))   # with the sorting key, arr1 can be ordered by the key



# arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
# arr2 = [2, 1, 4, 3, 9, 6]
arr1 = [28,6,22,8,44,17]
arr2 = [22,28,8,6]
print(relativesort(arr1, arr2))

