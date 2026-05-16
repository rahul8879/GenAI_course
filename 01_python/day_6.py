

# Objective 
# To learn what is class and objects in python




# 
name_1 = 'rahul'
salary_1 = 4500

name_2 = 'Chris'
salary_2 = 3500

name_3 = 'Nancy'
salary_3 = 5000

name_4 = 'Rohit'
salary_4 = 4000

# if my task is to update the salary of Rahul with 10%
salary_1 = salary_1*0.10 + salary_1
print(salary_1)

# so I f want to update the salary of "nancy
salary_3 = salary_3*0.10 + salary_3
print(salary_3)

# Problem with above code
# what if we have 100 employees??
# what if we have 1000 employees??

# what if we have 10000 employees?
# 1000 ==> each employe willl have 2-3 info like name, salary etc.
# total variable will be 2000
# and managing all this variable will be a problem
# Problems

# 1. we have to update the salary of nancy
# 2. we have to update the salary of rohit

# 3. we have to update the salary of rahul

# 4. we have to update the salary of chris
# if I need to reduce the salary of employee and then again I need do lot of updae 


# Class and objects 
#Class : it is kind of template or blueprint

# class Employee:
#     def __init__(self,name,salary):
#         self.name = name
#         self.__salary = salary
    
#     def update_salary(self,pct_hike):
#         self.__salary = self.__salary + self.__salary*pct_hike
#         return self.__salary
    
#     def display_details(self):
#         print(f"Name: {self.name}")
#         print(f"Salary: {self.__salary}")




# # 
# emp_1 = Employee('rahul',4500)
# # emp_2 = Employee('chris',3500)
# # print(emp_2.update_salary(0.10))
# print(emp_1.update_salary(0.10))
# emp_1.display_details()
# # print(emp_1.__salary)



# # 



from utils import LLMModel

prompt = "who are you"

model = LLMModel('openai','gpt-4o')


model = LLMModel('openai','gpt-4o-mini')

output = model.generate(prompt)
print(output)



# concept ??
# Inheritance 



class Parent:
    def __init__(self,name):
        
        self.name = name

    def property(self):
        print('property of parent class')


class Child(Parent):
    def __init__(self,name):
        super().__init__(name)

    def salary(self, salary):
        print('salary of child is ',salary)

 
obj_1 = Parent('rahul')
obj_1.salary(5000)
obj_1.property()