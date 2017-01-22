__author__ = 'kiarash7'
def bubblesort(mylist):
    for i in range(0,len(mylist)-1):
        for j in range(0,len(mylist)-1-i):
            if(mylist[j]>mylist[j+1]):
               temp=mylist[j]
               mylist[j]=mylist[j+1]
               mylist[j+1]=temp
    return mylist

theList=['1','2','5','3','9','0']
print(theList)
print bubblesort(theList)