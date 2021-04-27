zidian = {"name": "thefoxcat",
          "age": 1,
          "color": "花"}

zidian1 = {"height": 12,
           "zhongliang": 6,
           "age": 3}
print("初始字典0:", zidian)
print("初始字典1:", zidian1)

# 取值
print("取值:", zidian["age"])

# 增加
zidian["color1"] = "white"

# 修改
zidian["name"] = "humao"

# 删除
zidian.pop("name")

# 合并
zidian.update(zidian1)
"""
把字典0中的数据合并到字典1，重复的项目会被覆盖
"""
# 清空
zidian1.clear()

print("打印字典0:",zidian)
print("打印字典1:",zidian1)