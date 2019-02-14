# 序列的成员资格
# 使用in表达式 返回为布尔值

string = "rw"
print('r' in string)
print('x' in string)

users = ['tom', 'cat', 'dog', 'tony', 'smith']
print(input('Enter your name pls:') in users)

sub = '$$$ haha $$$'
print('$$$' in sub)

# 示例1 检查用户名和密码
database = [
    ['tom', '1234'],
    ['kevin', 'pswd'],
    ['tony', 'hh123']
]

usrname = input('Please Enter your name: ')
pin = input('PIN code: ')

if [usrname, pin] in database:
    print('Access granted')

# 示例2 求最大值最小值
nums = [100, 23, 45]
print(len(nums))
print(max(nums))
print(min(nums))
print(max(2, 3))
print(min(1, 2, 3, 4, -100))
