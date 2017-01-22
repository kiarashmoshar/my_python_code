class employee:
    def __init__(self,first,last,pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first + '.' + last +'@company.com'
    def fullname(self):
        return '{} {}'.format(self.first,self.last)


emp_1=employee('kiarash','moshar',60000)
emp_2=employee('amir','farsadi',50000)
#print(emp_1)
#print(emp_2)

#emp_1.first='kiarash'
#emp_1.last='mpshar'
#emp_1.email='kiarashmoshar@gmail.com'
#emp_1.pay=50000


#emp_2.first='test'
#emp_2.last='test2'
#emp_2.email='test@gmail.com'
#emp_2.pay=60000

print(emp_2.email)
print(emp_1.email)
#print ('{} {}'.format(emp_1.first,emp_1.last))
print(emp_2.fullname())
print(employee.fullname(emp_2))
