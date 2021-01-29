# 定义动物类
class Animal():
    # 动物种类，吃的食物
    def __init__(self,animal,food):
        self.animal = animal
        self.food = food
    # 动物吃东西
    def eat(self):
        print(f"{self.animal}爱吃{self.food}")
    # 动物喝水
    def drink(self):
        print(f"{self.animal}要喝水")
animal = Animal("猫","鱼")
animal.eat()
animal.drink()

# 定义人类
class People():
    def __init__(self,hgt):
        self.hgt = hgt

    def eat(self):
