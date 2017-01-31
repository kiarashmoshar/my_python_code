__author__ = 'kiarash7'
def SquareRootBi(x,epsilon):
    assert x>=0,'x must be non negetive,not '+str(x)
    assert epsilon>0,'epsilon must be positive not '+str(epsilon)
    low=0
    high=x
    guess=(high+low)/2.0
    ctr=100
    while abs(guess**2-x)>epsilon and ctr<=10000:
        if guess**2<x:
            low=guess
        else:
            high=guess
        guess =(low+high)/2.0
        ctr+=1
    assert ctr<=10000,'itereation count exceed'
    print 'bi method. Num. iterations:',ctr,'estimate:',guess
    return guess

SquareRootBi(9,0.000000001)
