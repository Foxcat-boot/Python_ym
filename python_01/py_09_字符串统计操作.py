xh_str = "hello hello 123"

print("原字符串为:", xh_str)

# 字符串第5个字符位置
print("字符串第5个字符为:", xh_str[4])

# 统计字符串长度
print("字符串长度为:", len(xh_str))

# 统计某个(子)字符串出现次数
print('"hel"字符串出现的次数:', xh_str.count("hel"))
print('"zxc"字符串出现的次数:', xh_str.count("zxc"))

# 某个子字符串出现的位置
str1 = int(xh_str.index("2")) + 1
str2 = int(xh_str.index("o")) + 1
str3 = int(xh_str.index("llo")) + 1
# str4 = int(xh_str.index("zxc")) + 1
print('字符串"2"出现的位置:', str1)
print('字符串"o"出现的位置:', str2)
print('字符串"llo"出现的位置:', str3)
# print('字符串"zxc"出现的位置:',str4)
"""
使用index传递不存在字符串位置会报错
"""
