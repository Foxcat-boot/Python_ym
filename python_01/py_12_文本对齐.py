str1 = ["\n \t一二三",
        "小狐猫",
        "狐猫\n \t",
        "狐狸猫"]
for str_ in str1:
    # print("|%s|" % str_.rjust(10, "　"))  # 字符串右对齐
    # print("|%s|" % str_.ljust(10, "　"))  # 字符串左对齐
    print("|%s|" % str_.strip().center(10, "　"))  # 字符串居中
