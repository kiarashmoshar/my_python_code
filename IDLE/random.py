import random
column1=[]

for k in range(100):
    column1.append(int(random.random()))
for k in range(10):
    column1[int(random.random()*100)]=77
print(column1)
