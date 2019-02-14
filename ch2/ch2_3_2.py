# 基本的列表操作
# 可对列表执行所有标准的序列操作，如 索引、切片、拼接和相乘，但是重点在于列表是可以修改的

# 1 修改列表： 给元素赋值
x = [1, 1, 1]
print(x)
x[1] = 2
print(x)

# 2 删除元素
name = ['Alice', 'Tom', 'Tony', 'Kevin', 'James']
print(name)
del name[2]
print(name)

# 3 给切片赋值
user = list('Alice')
print(user)
user[2:] = 'balabala'
print(user)
# 使用切片赋值 还可以 在不替换原有元素的情况下 插入新元素
nums = [1, 5]
nums[1:1] = [2, 3, 4]
print(nums)

# 使用切片赋值 还可以 进行元素的删除
nums[1:4] = []
print(nums)

# 设置步长大于1的赋值
nums = [1, 2, 3, 4, 5]
# nums[1:4:2] = 97
nums[1:4:2] = [96, 98]
print(nums)
# 设置步长小于0的赋值
nums[4:1:-2] = [99, 97]
print(nums)
