
import random2

column1=[]

for k in range(100):
    column1.append(int(random2.random()))
for k in range(10):
    column1[int(random2.random()*100)]=77
print(column1)
