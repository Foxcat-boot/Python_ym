str1 = " "
print("字符串1(空格  ->):", str1)
print("字符串1(判断是否为空字符串):", str1.isspace())

# 数字判断方法1
str2 = "123"
print("字符串1:", str2)
print("字符串2(判断是否是数字)[首选方法]:", str2.isalnum())

# 数字判断方法2
# 以下方法2选1
# str3 = "(123)"
str3 = "\u00b2"
print("字符串3:", str3)
print("字符串3(判断是否是数字):", str2.isdigit())

# 数字判断方法3
str4 = "一二三"
print("字符串4:", str4)
print("字符串4(判断是否是数字):", str4.isnumeric())
