# !!!!!!!!! 字符串是不可变的 所以 所有的元素赋值和切片赋值都是非法的
website = "http://www.abc.com"
print(website[-3:])
website[-3:] = 'org'
