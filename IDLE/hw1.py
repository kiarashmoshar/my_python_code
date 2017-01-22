import random
column1=[]
column2=[]
for k in range(100):
    column1.append(random.random())
column2=sorted(column1)
#print(column1)




f = open('hw1.csv','w')
for k in range(100):
    f.write(str(column1[k])+', ')
    
    f.write(str(column2[k])+'\n')

    
f.close()

