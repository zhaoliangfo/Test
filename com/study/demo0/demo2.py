#
# list1 = [12,3,4]
# def fuction(x):
#     return x%2 == 0
#
# re = filter(fuction,list1)
# print(list(re))

#
# import functools
# list1 = [1,2,3,4,5]
# def func(a,b):
#     return a+b
#
# print(functools.reduce(func,list1))
# i = 1
# while True:
#     if i == 2:
#         break
#     i += 1
# print(i)
#
#
# a = 1
# b = 2
# c = 3
# print((a < b) and (b < c)) # True
# print((a > b) and (b < c)) # False
# print((a > b) or b) # True
# print(not (a > b))


list1_enumerate = [1,2,3,4,5,6,5,3,6]

for i in enumerate(list1_enumerate):
    print(i)

for i,j in enumerate(list1_enumerate):
    print(i,j)