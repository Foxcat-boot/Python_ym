# 判断是否以某字符串开头
str1 = "str123 321"
print(str1.startswith("str"))
print(str1.startswith("Str"))
"""
⬆此方法区分大小写
"""

# 判断是否以某字符串结尾
str2 = "hu1 mao"
print(str2.endswith("mao"))
print(str2.endswith("Mao"))
"""
同样区分大小写
"""

# 查找字符串
str3 = "123humao321159 xhm"
print(str3.find("159"))
print(str3.find("1"))
print(str3.find("zzz"))
"""
查找第一个符合要求的字符串
第一位为0
与index最大的区别:
find没有查找到返回-1
index没有查找到会报错

rfind 可以从右边开始查找
"""

# 替换字符串
str4 = "zxc123 asdqwe1 159"
print(str4.replace("123","369"))
print(str4)
"""
replace会返回一个新的字符串
不会修改原来的字符串
"""
