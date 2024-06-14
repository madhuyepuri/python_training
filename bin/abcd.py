# 1st programm
class EmployeeClass:
    def __init__(self, emp_name,emp_id, emp_salary ):
        self.eemp_name = emp_salary
        self.eemp_id = emp_id
        self.eemp_salary = emp_salary


E1 = EmployeeClass("10","20",30)

# 2nd second programm

class EmployeeClass2:

    @classmethod
    def get_emp_name(cls, ename):
        cls.name = ename
        return cls.name

    @classmethod
    def get_emp_id(cls, eid):
        cls.eeidid = eid
        return cls.eeidid
    
    @classmethod
    def get_emp_salary(cls, esal):
        cls.eesal = esal
        return cls.eesal
    
# 3rd Question
# Decorator
def my_decorator(my_func):
    def decorated_func(x, y): # This can be used for 2 argument functions
        print("Result Is:")
        my_func(x,y)
        print("End Of The Result")
    return decorated_func


# -----------------
# Function-1: add
###################
@my_decorator
def add(a,b):
    print(a + b)

add(10,20)

# @my_decorator will take care of below 2 steps
# inner_func = my_decorator(add)
# inner_func(10, 20)
###################

# -----------------
# Function-2: sub
###################
@my_decorator
def sub(a,b):
    print(a - b)

sub(10, 20)

# @my_decorator will take care of below 2 steps
# inner_func = my_decorator(sub)
# inner_func(10,20)
###################


print("FINAL and CORRECT IMPLEMENTATION")
print("#"*40, end="\n\n")
########################################################

"""
Task-5: 
Write 2 class-methods where one method to set company head 
name and another method to get company head name 
Example: 
EmployeeClass.set_company_head_name(‘head-1’) 
print(EmployeeClass.get_company_head_name) # output ‘head-1’ 

"""
def set_comp_name(self, cname):
    self.compname = cname
    return self.compname

def get_comp_name(self, coname):
    self.compname = coname
