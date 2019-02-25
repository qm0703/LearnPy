# append用于将一个对象附加到列表末尾，是就地修改列表。直接修改原列表
lst = [1, 2, 3]
lst.append(4)
print(lst)

# clear就地清空列表内容
lst.clear()
print(lst)

a = [1, 2, 3]
b = a
b[1] = 4
print(a)
# 要让a和b指向不同的链表，必须将b关联到a的副本
a = [1, 2, 3]
b = a.copy()
b[1] = 4
print(a)
# 类似于使用a[:]或者list(a)他们也返回a的复制

# count计算指定元素在列表里出现多少次
print(['a', 'b', 'c', 'to', 'ha', 'to'].count('to'))
x = [[1, 2], 1, 1, [2, 1, [1, 2]]]
print(x.count(1))
print(x.count([1, 20]))

# extend可以同时附加多个值到列表末尾，可以使用一个列表去拓展另一个列表
lst1 = [1, 2, 3]
lst2 = [4, 5, 6]
lst1.extend(lst2)
print('extend: ' + str(lst1))
# 这里类似一个拼接，但是和拼接存在一个区别，extend会修改被拓展的列表这里是lst1,但是拼接是返回了一个全新的列表
# 如果想要实现lst1 = lst1 + lst2的效果，使用extend效果会强于字符串拼接

# index查找指定值第一次出现的索引
hah = ['we', 'are', 'the', 'kn', 'kn', 'oo', 'kn']
print('index: ' + str(hah.index('kn')))
# print('index: ' + str(hah.index('a')))

# insert将一个对象插入列表
numbers = [1, 2, 3, 5, 6, 7, 8]
numbers.insert(3, 'four')
print(numbers)

# pop从列表中删除一个元素，为末尾的最后一个元素，并返回这个元素
x = [1, 2, 3]
print(x.pop())
print(x)
print(x.pop(0))
print(x)

# remove用于删除第一个指定值的元素
x = ['a', 'b', 'c', 'd', 'b']
# remove不会有返回值，且只删除第一个元素，就地修改元素
print(x.remove('b'))
print(x)

# reverse按相反的顺序排列列表中的元素，修改列表，但是不返回值
x = [1, 2, 3]
print(x.reverse())
print(x)

# sort用于对列表就地排序，意味着对原来的列表进行修改，不返回值
x = [6, 4, 8, 2, 9, 1, 0]
print(x.sort())
print(x)
# 排序x但是不对x进行改变，有两种办法
# 1 是使用copy
y = [8, 2, 9, 1, 6, 0, 4, 7]
z = y.copy()
z.sort()
print(y)
print(z)
# 2 是使用sorted
xx = sorted(y)
print(y)
print(xx)

# 高级排序：方法sort可以接受两个参数 key和reverse
# key类似于参数cmp，可以设置为一个用于排序的函数。然而不会直接使用函数来判断一个元素是不是比另一个元素小，
# 而是使用它为每个函数创建一个键值，再根据这个键值对函数进行排序
x = ['a', 'abababa', 'aassd', 'aa', 'c']
x.sort(key=len, reverse=True)
print(x)
