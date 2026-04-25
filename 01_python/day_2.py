# input and output .. flow structure ( if else)


# output
# print("hello world")
# a = 10
# b=20
# print("the value of a is:",a, "and value of b is: ",b)

a = 10
b = 20
c = 15

# print("1. The value of a is {}, b is {} and c is {}".format(a,b,c)) # best approach

# print("2.the value of a is ",a, " the value of b is",b,'the value of c is',c)

# # variation into it.

# print("3. the value of a is {0} and b is {1}".format(a,b))



# flow structure ??

marks = [25,28,27,28] # assume I am adding. more value into list ??
# tom --> marks of 1000s student s??? 
# print(marks[1]) # access the element of list : via index 

# total_sum = marks[0] + marks[1] +marks[2] +marks[3] + marks[4]+marks[5] # here youy need to change the logic 
# print('Total sum is {}'.format(total_sum))


# idea ?? for loop ??
# total = 0
# for i in marks:
#     total = total +i

# print('total value is {}'.format(total))

# via indexing ??

# print(len(marks))
# print(range(5))


# total = 0
# for i in range(0, len(marks)):
#     total = total + marks[i]
# print('total value is {}'.format(total))




# 
data = ['rahul','test','xyz','abc','test']

# find where is 'test' ??
# key= test ?? return --> index
key = 'test'

# for i in range(len(data)):
#     if data[i]==key:
#         print('found it at index {}'.format(i))


# class work ??
# count how many time you got test ??

data = ['rahul','test','xyz','abc','test']

# find where is 'test' ??
# key= test ?? return --> index
# key = 'tasty'
# count = 0
# for i in range(len(data)):
#     if data[i]==key:
#         print('found it at index {}'.format(i))
#         count = count +1

# print("total occurance of {} is {}".format(key,count))


# end of discussion : flow control --> iterate ( list / tuple)

# data = (12,34,36,38,34,12,76)
# total = 1
# for i in data:
#     total = total*i

# print('product if given tuple is {}'.format(total))


# operator ??
# arithmetic 
# comparision operator
# logical operator
# bitwise operators
# assignment operator
# special operaotr

# Arithmetic operator : + , -, *, /, %, //, ** ( 2^2)

# print(5**3)

# >, <, ==, !=, >=, <=

# a = 10
# b = 11
# print(a<b)


# logical operator

is_ssn_number_valid = True
is_valid_passport = False


# print(not is_valid_passport)
print(is_ssn_number_valid or is_valid_passport)

a = 10
b = 11

# for and : both should be true --> true
# for or : any of them should be true --> true
# for or if both are false --> false



a = 100
b = 101

# bitwise AND
print(a and b) # | called as pipe operator