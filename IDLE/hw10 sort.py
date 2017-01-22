import random
li=[]
li_s=[]
for k in range(10,20):
    li.append(int(random.random()*10))
print("original list:",li)
li.sort(reverse=True)
print("asce list:",li)
li_s=sorted(li,reverse=False)
print("dec list:", li_s)


tup=(5,7,1,2,2,4,9)
s_tup=sorted(tup)
print("sort tuple:",s_tup)

dic={'Name':'kia' , 'Job':'SQL DBA' , 'Age':23 ,'OS':'Win'}
s_dic=sorted(dic)
print('sorted dictionary:',s_dic)


li2=[-6,-4,-2,1,3]
s_li2=sorted(li2,key=abs)
print('abs sorted:',s_li2)


class employee():
    def __init__(self,name,age,salary):
        self.name=name
        self.age=age
        self.salary=salary
    def __repr__(self):
        return '{},{},${}'.format(self.name,self.age,self.salary)

from operator import attrgetter
e1=employee('kia',23,50000)
e2=employee('amir',24,60000)
e3=employee('mohamad',22,70000)

employees=[e1,e2,e3]

def e_sort(emp):
    return emp.name
s_employee1=sorted(employees,key=e_sort)
s_employee2=sorted(employees,key=lambda e:e.salary)
s_employee3=sorted(employees,key=attrgetter('age'))

print('employee sorted:',s_employee1)
print('employee sorted:',s_employee2)
print('employee sorted:',s_employee3)





