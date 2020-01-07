
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
