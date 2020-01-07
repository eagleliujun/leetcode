# 内置函数zip(),将多个可迭代对象（集合等）按照顺序进行组合成tuple元祖，放在zip 对象进行存储，；
# 当参数为空时候，返回空
# 如果 zip() 函数压缩的两个列表长度不相等，那么 zip() 函数将以长度更短的列表为准;
list_t1 = [1, 2, 3]
list_t2 = ['apple', 'orange', 'banana']
list_t3 = [50, 60, 70, 80]
list_t4 = (500, 600, 700, 800)

list_z1 = zip(list_t1, list_t2)
list_z2 = zip(list_t1, list_t2, list_t3)
list_z3 = zip(list_t1, list_t3)
list_z4 = zip(list_t1, list_t3)
list_z5 = zip(list_t1, list_t4)

print(list(zip(['apple', 'orange', 'banana'],'')))   # []
print(list(zip(['apple', 'orange', 'banana'])))      # [('apple',), ('orange',), ('banana',)]
print(list(zip(*['apple', 'orange', 'banana'])))
    # [('a', 'o', 'b'), ('p', 'r', 'a'), ('p', 'a', 'n'), ('l', 'n', 'a'), ('e', 'g', 'n')]

print(type(list_z1))  # <class 'zip'>
print(list(list_z1))  # [(1, 'apple'), (2, 'orange'), (3, 'banana')]
print(list(list_z2))  # [(1, 'apple', 50), (2, 'orange', 60), (3, 'banana', 70)]
print(list(list_z3))  # [(1, 50), (2, 60), (3, 70)]
print(list(list_z5))  # [(1, 500), (2, 600), (3, 700)]

# 将两个列表转换为字典
dict_from_list = dict(zip(list_t1, list_t2))
print(dict_from_list)  # {1: 'apple', 2: 'orange', 3: 'banana'}


# map() 根据提供的函数对指定序列做映射;
# 参数为map(func,iter,....),返回值为iter；
# 计算过程：对序列内的所有元素进行给定的方法计算，将所有计算结果在放到iter 中返回；
# 写法上要注意，只要写上方法的名字，不需要带括号之类的；
def squ_minus1(number):
    return number ** 2 - 1


tuple_test = (1, 2, 3, 4)
print(type(map(str, tuple_test)))  # <class 'map'>,理解为迭代器；
print(list(map(str, tuple_test)))  # 迭代器取值可以用转成list 或for 循环等；
for v in map(str, tuple_test):
    print(v)

print(list(map(float, tuple_test)))  # [1.0, 2.0, 3.0, 4.0]
print(list(map(squ_minus1, tuple_test)))  # [0, 3, 8, 15]  ,调用自定义函数

# 三元运算或三元表达式；
# 简单理解：当某个为真返回一个值，如果为假返回另一个，类似于if else；
digtal1, digtal2 = 1, 2
if digtal1 > 2:
    print(digtal1)
else:
    print(digtal2)
# ========\\
print(digtal1 if digtal1 > digtal2 else digtal2)  # 上面的if else 直接换成这种写法；
# 三元表达式对列表的处理
l = [1, 2, 3, 10, 20, 30]
# 这里是常规写法
l_temp = []
for i in l:
    if i >= 10:
        l_temp.append(i ** 2)
print(l_temp)
# 这里是三元表达式写法
print(list(v ** 2 for v in l if v >= 10))


# lambda 表达式;
# lambda表达式是一行的函数。它们在其他语言中也被称为匿名函数。即，函数没有具体的名称，而用def创建的方法是有名称的。
# 如果你不想在程序中对一个函数使用两次，你可以用lambda表达式；
# 表达式用 ：分开，左边是参数，右边是返回值，‘：’后只能有一个表达式，lambda函数不能共享给别的程序调用；
# if或for或print等语句不能用于lambda中，因为lambda 只是一个表达式；
# def xsqy(x, y, z):
#     print(x ** y - z)
#
#
# # 上面的函数可以用下面的表达式替换；
# xsqy = lambda x, y, z: x ** y - z  # xsqy可以理解为一个函数，后面直接用‘=’左边的当作函数名使用；
# print(xsqy(2, 3, 1))
#
# # 推导式
# keys = [1, 2, 3, 4]
# x = [k for k in keys]
# y = [k ** k for k in keys]
# z = [k ** 3 for k in range(10) if k < 5]
# print(x)
# print(y)
# print(z)

#   ================================================================
#
# lambda是什么
# Lambda表达了Python中用于创建匿名函数的特殊语法。我们将lambda语法本身称为lambda表达式，从这里得到的函数称之为lambda函数。
# 总结起来，可以理解为一个小的匿名函数，lambda函数可以使用任意数量的参数，但只能有一个表达式。
#
# 模板： lambda argument: manipulate(argument)
# 参数：argument就是这个匿名函数传入的参数，冒号后面是我们对这个参数的操作方法
# 让我们参考上面的定义模板和参数, 直接看一个最简单的例子:
#
# add_one = lambda x:x+1       # 1个参数，执行操作为+1
# add_nums = lambda x,y:x+y    # 2个参数，执行操作为相加
#
# print(add_one(2))            # 调用add_one
# print(add_nums(3,7))         # 调用add_nums
# 对于较为简单的功能，无需自己def一个了，单行就可以写下，传参和执行方法一气呵成
#
# lambda用法详解
# lambda一般情况下是和map，filter，reduce这些超棒的内置函数以及dict，list,tuple,set 等数据结构混用，这样才能发挥它的最大效果
# ==============================================================================================================
# lambda + map
# numbers = [1,2,3,4,5]
# add_one = list(map(lambda n:n+1,numbers))  # map(fun,sequence)
# print(list(add_one))
# print(tuple(add_one))
# 我们再看下一个例子,这是我自己备份日志时写的一小段代码,命名不是很规范：
#
# from datetime import datetime as dt
# logs = ['serverLog','appLog','paymentLog']
# format ='_{}.py'.format(dt.now().strftime('%d-%m-%y'))
# result =list(map(lambda x:x+format,logs))   # 利用map+lambda 实现字符串拼接
# print(result)
#
# Out:['serverLog_11-02-19.py', 'appLog_11-02-19.py', 'paymentLog_11-02-19.py']
# 这里和刚才的加1例子差不多，但是换成了字符串的拼接，然而我这里用lambda并不是很好的解决方案，
# 最后我们会说，现在大家应该对map + lambda 有一些感觉了，让我们再来个和dict字典互动的例子：
#
# person =[{'name':'Lilei','city':'beijing'},{'name':'HanMeiMei','city':'shanghai'}]
# names=list(map(lambda x:x['name'],person))
# print(names)
#
# Out：['Lilei', 'HanMeiMei']
#
# ============================================================================================================
# lambda + filter
# lambda和filter的组合也很常见，用于特定筛选条件下，现在让我们来看上篇文章filter的例子，就应该很好理解了：
#
# numbers = [0, 1, 2, -3, 5, -8, 13]
#
# # 提取奇数
# result = filter(lambda x: x % 2, numbers)
#
# # 提取偶数
# result = filter(lambda x: x % 2 == 0, numbers)
#
# 提取正数
# result = filter(lambda x: x>0, numbers)
#
# 这里无非就是我们把filter(fun,sequence)里面的fun换成了我们的lambda，
# 只是lambda的函数部分（x%2,x%2==0,x>0）都是可以返回True或者False来判断的，符合filter的要求
#
# person =[{'name':'Lilei','city':'beijing'},{'name':'HanMeiMei','city':'shanghai'}]
#
# names=list(filter(lambda x:x['name']=='Lilei',person)) # 提取李雷的信息
# print(names)
#
# Out：[{'name': 'Lilei', 'city': 'beijing'}]
# ==========================================================================================================
# lambda + reduce
#
# from functools import reduce          # Only Python 3
# numbers = [1,2,3,4]
# result_multiply = reduce((lambda x, y: x * y), numbers)
# result_add = reduce((lambda x,y: x+y), numbers)
#
# 这个例子用lambda和reduce的配合实现了list求累积和和累积乘法。
#
# 避免过度使用lambda
#
# 首先让我们拿lambda方法和常规def做个对比，我发现lambda和def的主要不同点如下：
# 可以立即传递（无需变量）
# 只需一行代码，简洁（未必高效）
# 可以会自动返回，无需return
# lambda函数没有函数名称
#
# 有关优点大家都可以看到，我主要想说一下它的缺点，
# 首先，从真正需求出发，我们在大多数时候是不需要lambda的，因为总可以找到更好的替代方法，
#
# from functools import reduce          # Only Python 3
#     numbers = [1,2,3,4]
#     result_multiply = reduce((lambda x, y: x * y), numbers)
#     result_add = reduce((lambda x,y: x+y), numbers)
# 这里用lambda并没有实现简单高效的目的，因为我们有现成的sum和mul方法可以用：
#
# from functools import reduce
# from operator import mul
#
# numbers = [1,2,3,4]
# result_add = sum(numbers)
# result_multiply =reduce(mul,numbers)
#
# print(result_add)
# print(result_multiply)
#
# 结果是一样的，但是显然用sum和mul的方案更加高效。
#
# 再举个常见的例子说明，假如我们有一个list存储了各种颜色，现在要求把每个颜色首字母大写，如果用lambda写出是这样：
#
# colors = ['red','purple','green','blue']
# result = map(lambda c:c.capitalize(),colors)
# print(list(result))
#
# Out：['Red', 'Purple', 'Green', 'Blue']
# 看着似乎不错，挺简洁的，但是我们有更好的方法：
#
#
# colors = ['red','purple','green','blue']
# result = [c.capitalize() for c in colors]
# print(result)
#
# Out：['Red', 'Purple', 'Green', 'Blue']
# 用sorted还能处理首字母不规范的情况，连排序都省了：
#
# colors = ['Red','purple','Green','blue']
# print(sorted(colors,key=str.capitalize))
#
# Out:['blue', 'Green', 'purple', 'Red']
# 