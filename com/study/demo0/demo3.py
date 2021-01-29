f = open("data.txt","r")
i = 1
while i <= 3:
   w1 = f.readline()
   list1 = w1.split(",")
   for j in list1:
       list2 = j.split(":")
       if int(list2[1]) > 18:
           print(list2[0])
       # print(list2)
   i += 1