# 指定要设置其格式的值时，可以使用单个值(字符串或者数字)，也可以使用元组，还可以使用字典，最常见为元组
from string import Template
from math import pi, e

formatStr = "Hello, %s. %s enough for you?"
values = ('World', 'Hot')
print(formatStr % values)

tmpl = Template("Hello, $who! $what hahaha?")
print(tmpl.substitute(who="Mars", what="Good"))

print("{},{} and {}".format("first", "second", "third"))

print("{0},{1} and {2}".format("first", "second", "third"))

print("{0},{3},{1},{2},{3},{3}".format("a", "b", "c", "d"))

print("{name} is approximately {value:.2f}.".format(value=pi, name="pai"))

print("{name} is approximately {value}.".format(value=pi, name="pai"))
# 如果变量和替换字段同名，可以使用缩写，可以使用f字符串 在字符串前加上f
print(f"Good is {e}")

print("Good is {e}".format(e=e))
