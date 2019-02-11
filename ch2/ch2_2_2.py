# 2. 切片
# 除了使用索引来访问单个元素之外，还可以使用切片来访问特定范围内的元素。为此，可以使用两个索引并用冒号分隔
tag = '<a href="http://www.python.org">Python Web Site</a>'
print(tag[9:30])
print(tag[32:-4])

# 两个索引，元素包含第一个索引的元素，不包含第二个元素的索引
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
print(numbers[3:6])
print(numbers[0:1])

# 表示数字列表的后三个元素
print(numbers[7:10])

# 如果需要从列表的后面开始数，可以使用负数索引
print(numbers[-3:-1])
# 但是可以从执行结果中看出，无法表示最后一个元素

# 如果使用这种表示方法：
print(numbers[-3:0])
# 表示了一个空的集合

# 重点：：：如果切片里 第一个索引 在 第二个索引 之后 那么返回的结果都是空：：：

# 解决办法：
# 如果切片结束于序列的末尾，则可以省略第二个索引
print(numbers[-3:])
print(numbers[7:])

# 如果切片开始于序列的开头，则可以省略第一个索引
print(numbers[:3])
print(numbers[:-7])

# 如果需要整个序列，可将两个索引都省略
print(numbers[:])

# 举例
print(numbers[1:-1])

# 切片使用步长
print(numbers[0:10:1])
print(numbers[0:10:2])
print(numbers[3:6:3])
print(numbers[::4])
# 步长不可以为0 否则不能移动
# 步长可以为负数 意味着从右向左提取元素
# 步长为负数时 依旧包含第一个索引 不包含第二个索引 第一个索引为最右 第二个索引为最左
print(numbers[8:3:-1])
print(numbers[9:3:-2])
print(numbers[9999999:3:-2])
print(numbers[0:10:-2])
print(numbers[::-2])
print(numbers[5::-2])
print(numbers[:5:-2])
