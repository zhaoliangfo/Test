
# # 第一题
# # 定义动物类
# class Animal():
#     # 动物种类，吃的食物
#     def __init__(self,animal,food):
#         self.animal = animal
#         self.food = food
#     # 动物吃东西
#     def eat(self):
#         print(f"{self.animal}爱吃{self.food}")
#     # 动物喝水
#     def drink(self):
#         print(f"{self.animal}要喝水")
# animal = Animal("猫","鱼")
# animal.eat()
# animal.drink()
#
#
#
# # 定义人类
# class People():
#     def __init__(self,people,hgt):
#         self.people = people
#         self.hgt = hgt
#
#     def __str__(self):
#         return f"{self.people}的体重为{self.hgt}公斤"
#
#     def eat(self):
#         self.hgt += 1
#         print("吃东西体重增加1公斤")
#
#
#     def run(self):
#         self.hgt -= 0.5
#         print("跑步减肥公斤")
#
# xiaoming = People("小明",75)
# xiaohong = People("小红",45)
# xiaoming.eat()
# print(xiaoming)


# # 第二题
# # 家具类
# class Furniture():
#     def __init__(self,name,furniture_area):
#         self.name = name
#         self.furniture_area = furniture_area
#
#
# # 房子类
# class House():
#     def __init__(self,type,area):
#         self.type = type
#         self.area = area
#         self.free_area = area
#         self.furniture = []
#
#
#     def __str__(self):
#         return f'房子户型为{self.type},占地面积为{self.area},剩余面积为{self.free_area},家具有{self.furniture}'
#
#     # 搬家具
#     def move_furniture(self,item):
#         if self.free_area >= item.furniture_area:
#             self.free_area -= item.furniture_area
#             self.furniture.append(item.name)
#         else:
#             print("家具太大,无法容纳")
#
#
# jia1 = House('大户型',100)
# print(jia1)
# bed = Furniture('床',4)
# jia1.move_furniture(bed)
# print(jia1)
# wardrobe = Furniture('衣柜',2)
# jia1.move_furniture(wardrobe)
# print(jia1)
# desk = Furniture('餐桌',1.5)
# jia1.move_furniture(desk)
# print(jia1)



# 第三题
class Soldier():
    def __init__(self,name,gun,num):
        self.name = name
        self.gun = gun
        self.num =num

    def __str__(self):
        return f"士兵{self.name}用使用{self.gun}打出{self.fire_num}发子弹,枪中剩余{self.num}发子弹"

    def shoot(self,fire_num):
        self.fire_num = fire_num
        gun = Gun(self.num)
        self.num = gun.fire(self.fire_num)

class Gun():
    def __init__(self,num):
        self.num = num

    def fire(self,fire_num):
        if self.num >= fire_num:
            self.num -= fire_num
        else:
            print("子弹数量不够")
        return self.num

    def puton(self,num_add):
        self.num = num_add
        self.num += num_add

gun = Gun(1000)
gun.puton(1000)
soldier = Soldier("瑞恩","ak47",gun.num)
soldier.shoot(1000)
print(soldier)



