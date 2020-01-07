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
def xsqy(x, y, z):
    print(x ** y - z)


# 上面的函数可以用下面的表达式替换；
xsqy = lambda x, y, z: x ** y - z  # xsqy可以理解为一个函数，后面直接用‘=’左边的当作函数名使用；
print(xsqy(2, 3, 1))

# 推导式
keys = [1, 2, 3, 4]
x = [k for k in keys]
y = [k ** k for k in keys]
z = [k ** 3 for k in range(10) if k < 5]
print(x)
print(y)
print(z)
