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
##############################################################################


# tip4: list to dict
#  for item in nums:  #功能类似Counter，生成一个字典，key是列表元素，value是元素出现的次数
#         dict_nums[item] = dict_nums.get(item, 0) + 1

################################################################################


# tip5:  How to sort a Python dict by value
# (== get a representation sorted by value)
xs = {'a': 4, 'b': 3, 'c': 2, 'd': 1}

output = sorted(xs.items(), key=lambda x: x[1])  # xs.items是可迭代对象，x 是每次迭代对象的items值
print(output)
# #[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
#
#
# # Or:
#
# import operator
# output = sorted(xs.items(), key=operator.itemgetter(1))
# print(output)
# #[('d', 1), ('c', 2), ('b', 3), ('a', 4)]
#########################################################################

# tip6: 计算列表中元素位数为偶的个数
# return len(nums) - sum((len(str(i))%2 for i in nums))
# return sum((not(len(str(i))%2) for i in nums))

# tip7:
#

# tip8:
#
'df'.isdecimal()

# tip2:
#

# tip2:
#

# tip2:
#

def main():
    pass

if __name__ == '__main__':
    main()