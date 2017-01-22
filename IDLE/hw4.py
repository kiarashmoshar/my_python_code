import random
list=[]
for k in range(100):
    list.append(random.random())
curmax=list[0]
print(curmax)
print(list)
for k in range(len(list)):
   if(list[k]>curmax):
       curmax=list[k]
print(curmax)
