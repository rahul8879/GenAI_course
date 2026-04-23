# x = True
# y = 5
# z = x +y
# print(z)
# print(type(x))

# types of variable 
# integer
# float
# string
# Boolean???

# operation ??
# 2 number(intger or float) ---> add, substraction, multiplcation 

# eg 1;
x = 3 # integer
y = "5" # string

# print("Type of x is : ",type(x))
# print("Type of y is : ",type(y))

# type casting??
y_new = int(y)
# print("type of y_new",type(y_new))

x + y_new
# z = x + y
# print(z)

# when you are doing any operation. - datatypes should match ???

# x = "Rahul"
# y = "test"
# print(x+y)

# rules for declaring variable name ??
# 1. your variables cant start with digit
# 2 your variable name cant start with specail char/symbol
# 3. reserved keywords ---> you cant use them as a variable names
# age_1 = 24
# print(age_1)

# @age = 24
# print(age_1)

# list of keywords ??
import keyword
# print(keyword.kwlist)
# ['False', 'None', 'True', 'and', 'as', 'assert', 
#  'async', 'await', 'break', 'class', 'continue', 'def', 'del',
#    'elif', 'else', 'except', 'finally', 'for', 'from', 
#    'global', 'if', 'import', 'in', 'is', 'lambda', 
#  'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'try', 'while', 'with', 'yield']


# int --> str
# str -->int

# input from user ?? condtion??
# age = int(input("Enter your age"))
# print("type of age",type(age))

# # next 5 year ??
# print(age + 5)

# take the input from user 
# if age is less then 18 --> reject his application
# else accept his application

# age = int(input("enter you age"))

# print(age<18)

# if age<18:
#     print('you are not eligible')
# else:
#     print('Thank you ')


# int, str,boolean(True/False)
# 5 students --> store makrs ??
s1 = 34
s2 = 45
s3 = 65
s5 = 76
s4 = 86

# case 1 : tom 10 more students joins ---> again I neeed to define 10 new variable ??

avg_marks =(s1+s2+s3+s4+s5)/5
print(avg_marks)


# list  : data types 

marks = [34,65,77,86,92,34]
print('type of marks: ',type(marks))

avg_marks = round(sum(marks)/len(marks), 2)

print('avg marks of the class is: ',avg_marks)
