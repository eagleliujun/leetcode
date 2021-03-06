# 简洁的内置函数
# map，filter，reduce, zip。
# 它们都是处理序列的便捷函数。可以利用它们把一些小函数应用于一个序列的所有元素。从而节省编写显式循环的时间。
# 另外，这些中的每一个都是纯函数，有返回值。因此我们可以容易地将函数的返回结果用表达式来表示。
#  ============================================================================
# map()
# 函数的主要作用是可以把一个方法依次执行在一个可迭代的序列上，比如List等，具体的信息如下：
# 基础语法：map(fun, iterable)
# 参数：fun是map传递给定可迭代序列的每个元素的函数。iterable是一个可以迭代的序列，序列中的每一个元素都可以执行fun
# 返回值：map   object
# 好了，大白话就是利用map我们可以把一个函数fun 执行到序列iter的每一个元素上，用例子非常好理解
# List 包含1~5
# 五个数字，我们想要让每一个数 + 1:
#
# def add_one(n):
#     return n + 1
#
# numbers = [1, 2, 3, 4, 5]
# result = map(add_one, numbers)
# print(result)
# print(type(result))
# print(list(result))
# 在优化精简代码的同时，某种程度上讲实现了方法和循环部分的分离，
# 这里我们可以发现map返回就是map类，我们这里传递的序列是List，最后输出时经过类型转换也是list
#
# 在传递序列时只要这个序列是可迭代的就好，不一定非要List，比如我们换一种：
#
# numbers = (1, 2, 3, 4, 5)  # 序列为元组
# result = map(add_one, numbers)
# print(tuple(result))  # Out：(2, 3, 4, 5, 6)
#
# 输入的序列为同样可以迭代的元组，输出时我们也选择元组，效果一样的。
#
# 更进一步 还用刚才的例子，为了更加简洁，我们可以用lambda函数配合map使用，具体实现如下：
#
# numbers = (1, 2, 3, 4, 5)  # 迭代对象为tuple
# result = map(lambda x: x + 1, numbers)
# print(list(result))  # 输出对象为list
#
# Out：[2, 3, 4, 5, 6]
# 更加简洁优雅了对吧！！这个lambad函数我之后会说，今天它不是主角哈哈，先一带而过。
# 让我们重新把目光转移到map上来，除了刚才的用法，还要一种情况也十分常见，让我们看下面的例子：
#
# # List of strings
# words = ['paris', 'xiaobai', 'love']
#
# # 把数组中每个元素变为List
# test = list(map(list, words))
# print(test)
#
# Out: [['p', 'a', 'r', 'i', 's'], ['x', 'i', 'a', 'o', 'b', 'a', 'i'], ['l', 'o', 'v', 'e']]
# words是一个只包含字符串类型元素的list，我们用map可以实现将words的每一个元素全部转化为list类型，
# 这里有一点一定要注意，能实现的前提一定是每个元素都是可以迭代的类型，如果出现了如int类型的元素，就会出错啦：
#
# List of strings
# words = [18, 'paris', 'xiaobai', 'love']
#
# # 把数组中每个元素变为List
# test = list(map(list, words))
# print(test)
#
# Out：TypeError: 'int'
# object is not iterable
# 大家一看错误类型相比立刻就明白啦，所以正确的使用方法一定是类似这种:
#
# nums = [3, "23", -2]
# print(list(map(float, nums)))
#
# Out: [3.0, 23.0, -2.0]
# 总之就是类型要注意
# ==============================================================================================

# filter()----------------------------fun的返回值为 true or false
# 函数构造
# filter（）方法借助于一个函数来过滤给定的序列，该函数测试序列中的每个元素是否为真。
#
# 基础语法：filter(fun, iterable)
# 参数：fun测试iterable序列中的每个元素执行结果是否为True，iterable为被过滤的可迭代序列
# 返回值：可迭代的序列，包含元素对于fun的执行结果都为True
# 简而言之就是filter可以帮助我们根据给出的条件过滤一组数据并返回结果
#
# 基础用法：
# 让我们先看一个例子：
#
# 过滤元音的方法
# def fun(variable):
#     letters = ['a', 'e', 'i', 'o', 'u']
#     if (variable in letters):
#         return True
#     else:
#         return False
# 给定序列
# sequence = ['I', 'l', 'o', 'v', 'e', 'p', 'y', 't', 'h', 'o', 'n']
#
# 根据条件得出结果
# filtered = list(filter(fun, sequence))
# print(filtered)
#
# Out：['o', 'e', 'o']
# 这里我们创建一个可以提取元音字母的方法fun，给定的可迭代序列为list，之后就可以用filter方法很容易的提取出结果啦，再看一个类似例子：
#
# 判断为正数
# def positive(num):
#     if num > 0:
#         return True
#     else:
#         return False
#
# 判断偶数
# def even(num):
#     if num % 2 == 0:
#         return True
#     else:
#         return False
#
#
# numbers = [1, -3, 5, -20, 0, 9, 12]
#
# positive_nums = list(filter(positive, numbers))
# even_nums = tuple(filter(even, numbers))
# 看到这里相比大家已经知道filter的基础用法啦， 要先有一个, 能返回True或者False的方法，或者表达式作为过滤条件就行啦
#
# 更进一步
# 这里其实和map一样了，基本上最简洁的用法都是和lambda混在一起，比如下面我们想要把刚才的一大串代码压缩一下：
#
# numbers = [0, 1, 2, -3, 5, -8, 13]
#
# # 提取奇数
# result = filter(lambda x: x % 2, numbers)
# print("Odd Numbers are :", list(result))
#
# # 提取偶数
# result = filter(lambda x: x % 2 == 0, numbers)
# print("Even Numbers are :", list(result))
#
# # 提取正数
# result = filter(lambda x: x > 0, numbers)
# print("Positive Numbers are :", list(result))
# ====================================================================================================================
#
# reduce()
# 函数构造
# 在列表上执行某些计算并返回结果。它将滚动计算应用于列表中的连续值。例如，如果要计算整数列表的累积乘，或者求和等等
#
# 基础语法：reduce(function, iterable)
# 参数：fun是连续作用于iterable每一个元素的方法，新的参数为上一次执行的结果，iterable为被过滤的可迭代序列
# 返回值：最终的function返回结果
# 在Python# 2中，reduce（）是一个内置函数。但是，在Python3中，它被移动到functools模块。
# 用法：
# from functools import reduce  # Python 3
#
# def do_sum(x1, x2):
#     return x1 + x2
#
# print(reduce(do_sum, [1, 2, 3, 4]))
#
# def multiply(x, y):
#     return x * y
#
# numbers = [1, 2, 3, 4]
# print(reduce(multiply, numbers))
#
# 还是和lambda混搭，更加简洁：

# from functools import reduce  # Python 3
#
# numbers = [1, 2, 3, 4,5]
# result_multiply = reduce((lambda x, y: x * y), numbers)
# result_add = reduce((lambda x, y: x + y), numbers)
#
# print(result_multiply)
# print(result_add)
# ===============================================================================================
#
# zip()
# 函数构造
# zip（）的目的是映射多个容器的相似索引，以便它们可以仅作为单个实体使用。
#
# 基础语法：zip(*iterators)
# 参数：iterators为可迭代的对象，例如list，string
# 返回值：返回单个迭代器对象，具有来自所有容器的映射值
# 基础用法：
# 其实之前我们在讲dict的创建方法时提到过它，这里从新回顾一下：
#
# keys = ['name', 'age']
# values = ['xiaobai', 18]
# my_dict = dict(zip(keys, values))
# print(my_dict)
#
# Out：{'name': 'xiaobai', 'age': 18}
# zip可以支持多个对象，比如下面的例子
#
# name = ["xiaobai", "john", "mike", "alpha"]
# age = [4, 1, 3, 2]
# marks = [40, 50, 60, 70]
#
# # using zip() to map values
# mapped = list(zip(name, age, marks))
#
# [('xiaobai', 4, 40), ('john', 1, 50), ('mike', 3, 60), ('alpha', 2, 70)]
# 这里我们可以很容易的的把name，age，marks这三个list里面相同index的值映射打包在一起
#
# 更进一步：
# 通过上面的例子，我们发现可以很容易的以类似1对1的形式把不同对象的同一索引位置的值打包起来，
# 那如果是解包呢？也是类似的，就是多了一个 * 而已
#
# names, ages, marks = zip(*mapped)
# print("The name list is : ", names)
# print("The age list is : ", ages)
# print("The marks list is : ", marks)
#