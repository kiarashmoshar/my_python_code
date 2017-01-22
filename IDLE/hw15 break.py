import random
majicNumber=int(100*random.random())
i=0
for n in range(100):
    i+=1
    if n is majicNumber:
        print(n," is majic Number")
        break
    else:
        print(n)

print(i," times loop")
