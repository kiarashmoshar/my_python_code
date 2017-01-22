__author__ = 'kiarash7'
def insertionSort(mylist):
    for i in range(0,len(mylist)-1):
        for j in range(i,-1,-1):
            if(mylist[j]>mylist[j+1]):
                mylist[j],mylist[j+1]=mylist[j+1],mylist[j]
            else:
                break
    return mylist
thelist1=[1,2,0,6,4,9]
print insertionSort(thelist1)

# big_O(n^2)