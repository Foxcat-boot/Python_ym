import os

card_list = []
card_dict = {}


def show_menu():
    """显示菜单"""
    print("*" * 50)
    print("欢迎使用[名片管理系统] V 1.0")
    print("")
    print("1. 新增名片")
    print("2. 显示全部")
    print("3. 搜索名片")
    print("-" * 50)
    print("9. 退出系统")
    print("*" * 50)


def new_card():
    """新增名片"""
    print("-" * 50)
    print("新增名片")
    name_str = input("请输入姓名:")
    phone_str = input("请输入电话:")
    qq_str = input("请输入QQ:")
    Email_str = input("请输入电子邮件:")
    card_dict = {"name": name_str,
                 "phone": phone_str,
                 "qq": qq_str,
                 "Email": Email_str}
    card_list.append(card_dict)

    print(card_list)

    print("添加 %s 的名片成功" % name_str)


def show_all():
    """显示所有名片"""
    print("-" * 50)
    print("显示所有名片")

    if len(card_list) == 0:
        print("当前没有名片,请使用新增功能添加名片")
        return

    for name in ["姓名", "电话", "QQ", "邮箱"]:
        print(name, end="\t")
    print("")

    print("==" * 25)

    for card_dict in card_list:
        print("%s\t%s\t%s\t%s" % (card_dict["name"],
                                  card_dict["phone"],
                                  card_dict["qq"],
                                  card_dict["Email"]))


def search_card():
    """搜索名片"""
    print("-" * 50)
    print("搜索名片")
    find_name = input("请输入要搜索的姓名:")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            os.system('cls')
            print("姓名\t电话\tQQ\t邮箱")
            print("==" * 25)
            print("%s\t%s\t%s\t%s" % (card_dict["name"],
                                      card_dict["phone"],
                                      card_dict["qq"],
                                      card_dict["Email"]))
            modify_card(card_dict)
            break
        else:
            os.system('cls')
            print("未找到 %s" % find_name)


def modify_card(find_dict):
    print(find_dict)
    action_str = input("选择要修改的选项: [1]修改 [2]删除 [任意键]返回上级菜单")
    while True:
        if action_str == "1":
            find_dict["name"] = input_card_info(find_dict["name"], "姓名:")
            find_dict["phone"] = input_card_info(find_dict["phone"], "电话:")
            find_dict["qq"] = input_card_info(find_dict["qq"], "QQ:")
            find_dict["Email"] = input_card_info(find_dict["Email"], "邮箱:")
            print("修改名片成功")
            break
        elif action_str == "2":
            card_list.remove(find_dict)
            print("删除名片成功")
            break
        else:
            break


def input_card_info(dict_value, tip_message):
    result_str = input(tip_message)
    if len(result_str) > 0:
        return result_str
    else:
        return dict_value
