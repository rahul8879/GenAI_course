
# Agenda ??
# For loop.  ?? very very imp --> iterview --> product/solution AI --> 
# while loop
# what is break ? what is continue
# what is python functions ?? different types of python fucntions --> 
# what is module/packages ??

# example 1: Simple for loop
# marks = [35,36,37,38]
# total_marks = 0
# for i in marks:
#     total_marks = total_marks + i

# print('avg marks is {}'.format(total_marks/len(marks)))


# Examples : 2 : nested list
# marks = [[34,35,37,42],[67,68,55,89],[89,98,79,65]]

# final_result = []
# for i in marks:
#     total_marks = 0
#     for j in i:
#         total_marks = total_marks + j
#     avg_marks = total_marks/len(i)
#     final_result.append(avg_marks)

# print('final_result is : ',final_result)



# example 3: sales data ??
# daily sales data
# sales_data = [[123,254,678],[231,432,678],[675,891,912],[234,246,769]]
# # 
# avg_sales = []
# for sale in sales_data:
#     total_sales=0
#     for j in sale:
#         total_sales += j
#     avg_sales.append(round(total_sales/len(sale),2))

# print('total sales are : ',avg_sales)
    

# sales data --> daily sales ---> for different product ( 2 product --> avg sales)

# sales = [[[23,45,67],[23,34,53,67]],[[45,45,100],[34,89,79,67]]]

# final_output = []
# for i in sales:
#     day_sales=[]
#     for j in i:
#         total_sales = 0
#         for k in j:
#             total_sales +=k
#         day_sales.append(round(total_sales/len(j),2))
#     final_output.append(day_sales)

# print('final score/output',final_output)


# while loop
# marks = [23,34,56]
# print(len(marks))
# while len(marks)>1:
#     print('give me more data')
#     stop = input("enter EXIT to kill the process ")
#     if stop=='EXIT':
#         break

# print('outside of while block')

# program to check given number is prime number or not ??


num = int(input("Enter a number : "))

isDivisible= False
i = 2

while i<num:
    if num % i ==0:
        isDivisible = True
    i = i+1

if isDivisible:
    print('{} is not a prime number'.format(num))
else:
    print('{} is a prime number'.format(num))