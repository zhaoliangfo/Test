# 第一题：
# list = [i for i in range(0,100,5)]
# print(list)
#
# list = [i for i in range(0,100) if i%5 == 0]
# print(list)

# 第二题：
# name = ["张三","李四","王五","赵六"]
# age = [25,26,27,28]
# student = {}
# i = 0
# while i <= len(name)-1:
#     student[name[i]] = age[i]
#     i += 1
# print(student)


# 第三题：
# 学生系统
student = [{"王五":"20"},{"赵六":"50"},{"张三":"43"},{"张三":"30"}]


def method():

    i = 1
    while i < 2:
        action = input("请输入想要做的操作（新增、查询、删除或退出）：")
        if action == "新增":
            add_user()
            print(student)
        elif action == "查询":
            search_user()
            print(student)
        elif action == "删除":
            delete_user()
            print(student)
        elif action == "退出":
            print("谢谢使用，拜拜")
            break
        else:
            print("无效操作，请重试")




# 添加学生
def add_user():
    # 创建薪字典
    user = {}
    # 输入框输入
    name = input("请输入学生姓名：")
    age = input("请输入学生年龄：")
    # 新字典添加数据
    user[name] = age
    # student列表添加数据
    student.append(user)
    print("添加成功")
    # 将局部变量变为全局变量
    # return student

# 查找学生
def search_user():
    # 输入学生姓名
    name = input("请输入想要查找的学生姓名：")
    # 增加用户存在标识
    user_exist = 0
    # 遍历学生列表
    count = 0
    for user in student:
        # 遍历字典key值
        for key in user.keys():
            # key值匹配，输出value
            if key == name:
                # 用户存在标识
                user_exist = 1
                count += 1
                print(f"第{count}位{name}的年龄是：{user[name]}")
    if user_exist == 0:
        print("查无此人")

# 删除学生
def delete_user():
    # 输入学生姓名
    name = input("请输入想要删除的学生姓名：")
    # 同姓名人数标识
    count = 0
    # 同名user列表
    count_list = []
    # 增加用户存在标识
    count_list_check = set()
    user_exist = 0
    # 遍历学生列表
    for user in student:
        # 遍历字典key值
        for key in user.keys():
            # key值匹配，查找列表中学生数量
            if key == name:
                # 同名user内部详情
                count_list_in = [0,0,0]
                # 用户存在标识
                user_exist = 1
                count += 1
                # 列表中新增数据
                count_list_check.add(f"{count}")
                count_list_in[0] = count
                count_list_in[1] = name
                count_list_in[2] = user[name]
                count_list.append(count_list_in)
    print(count_list_check)

    if user_exist == 0:
        print("删除失败，查无此人")


    else:
        print(f"一共存在{count}位{name}:{count_list}")
        delt = input("确认删除？请输入需要删除的编号，以逗号隔开；全部删除请输入\"确认\",取消请输入\"取消\"：")
        delt_list = delt.split(",")
        # 将输入放入set集合中
        delt_set = set()
        for i in delt_list:
            delt_set.add(i)
        delt_set_check = set()
        for i in delt_set:
            delt_set_check.add(i)
        for i in count_list_check:
            delt_set_check.add(i)
        print(delt_set)
        if delt == "确认":
            i = 0
            student_bak = student.copy()
            for user in student_bak:
                # 遍历字典key值
                for key in user.keys():
                    # key值匹配，删除列表中学生
                    if key == name:
                        student.remove(user)
                        i += 1
                        print(f"成功删除第{i}条数据")
        elif delt == "取消":
            print("删除失败")
        elif count_list_check == delt_set_check:
            count_d = 0
            # delt_list = delt.split(",")
            student_bak = student.copy()
            for user in student_bak:
                # 遍历字典key值
                for key in user.keys():
                    # key值匹配，删除列表中学生
                    if key == name:
                        count_d += 1
                        if str(count_d) in delt_list:
                            student.remove(user)
                            print(f"已删除编号为{count_d}，姓名为{name}的用户")
        else:
            print("输入无效请重试")

method()