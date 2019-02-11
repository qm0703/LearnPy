# 通用的序列操作
# 1. 索引
greeting = 'Hello'
print(greeting[0] + ',' + greeting[1])

# 索引是从0开始的，也可以使用负数索引 例如 -1 是倒数第一个元素的位置
print(greeting[-1] + ',' + greeting[-2])

# 对于字符串字面量（以及其他的序列字面量），可直接对其执行索引操作，无需先将其赋值给一个变量
print('Hello'[1])

# 如果函数调用返回一个序列，可直接对其执行索引操作
fourth = input('Year:')[3]
print(fourth)

# 代码列表
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',
          'December']

endings = ['st', 'nd', 'rd'] + 17 * ['th'] + ['st', 'nd', 'rd'] + 7 * ['th'] + ['st']

year = input('Year:')
month = input('Month:')
day = input('Day:')

month_number = int(month)
day_number = int(day)

month_name = months[month_number - 1]
ordinal = day + endings[day_number - 1]

print(month_name + ' ' + ordinal + ',' + year)
