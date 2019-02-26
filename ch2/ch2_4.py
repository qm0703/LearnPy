# 与列表一样 元组也是序列，唯一的差别在于元组是不可修改的
# 元组的创建 使用()
print((1, 2, 3))
# 空元组
print(())
# 一个元素的元组
print((23,))

print(3 * (40 + 2))
print(3 * (40 + 2,))

# tuple函数
print(tuple([1, 2, 3]))
print(tuple('abc'))
print(tuple((4, 5, 6)))

# 元组的访问
x = 1, 2, 3
print(x[1])
print(x[0:2])
