# tip1: find the common elements in two list
# or find the index of the element in one list

# arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
# arr2 = [2, 3, 9]
# common1 = [i for i, value in enumerate(arr1) if value == 2]
# common2 = []
# for item in arr2:
#     common2.extend(j for j, value in enumerate(arr1) if value == item )
#     # .append() add  one element , .extend : add a iterable element (list /dict..)
# print('common1: ', common1)
# print('common2: ', common2)

# for dict use ---->
# order = {i: v for i, v in enumerate(arr1) if v == 2}
# print('order:', order)
####################################################################################

# tip2: filter(fun,iterable)
# element which in arr1 but not in arr2 to a new list
# arr_not_in = list(filter(lambda x: x not in arr_sort, arr1))
##############################################################################


# tip3: Counter use method
# from collections import Counter
# >>> c = Counter(a=3, b=1)
# >>> d = Counter(a=1, b=2)
# >>> c + d                       # add two counters together:  c[x] + d[x]
# Counter({'a': 4, 'b': 3})
# >>> c - d                       # subtract (keeping only positive counts)
# Counter({'a': 2})
# >>> c & d                       # intersection:  min(c[x], d[x])
# Counter({'a': 1, 'b': 1})
# >>> c | d                       # union:  max(c[x], d[x])
# Counter({'a': 3, 'b': 2})
# ————————————————


# tip4: list to dict
#  for item in nums:  #功能类似Counter，生成一个字典，key是列表元素，value是元素出现的次数
#         dict_nums[item] = dict_nums.get(item, 0) + 1

# tip5:
#

# tip6:
#

# tip7:
#

# tip8:
#

# tip2:
#

# tip2:
#

# tip2:
#
