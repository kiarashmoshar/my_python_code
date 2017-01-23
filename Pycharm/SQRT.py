__author__ = 'kiarash7'
def sqrt(number,root):
    ans=number**(1.00/root)
    return ans





def sqrt2(number):
    ans=0
    while ans*ans<=number:
        if(ans*ans==number):
            return ans
        else:
            ans+=0.1

    return ans


print sqrt(16,4)
print sqrt2(15)