# 长字符串
print('''This is a notebook "hahah" les's go
but aha what do you think''')

# 原始字符串
print('C:\nowhere')

print('C:\\nowhere')

print(r'C:\nowhere')
# 使用原始字符串r表示的字符串 可以在原始字符串中包含大多数字符，但是引号需要在字符串中 使用通常情况的转义
# 所以 执行转义的反斜杠也会包含在最终的字符串中
print(r'Let\'s go')

# 原始字符串不能以反斜杠结尾，除非对其进行转义，但是转义时，用于转义的反斜杠也将是字符串的一部分
# print(r"this is what\")

print(r"hah \\")

# 如果必须要指定一个以反斜杠为末尾的原始字符串 可以如下
print(r'C:\Pra\foo\bar' '\\')
