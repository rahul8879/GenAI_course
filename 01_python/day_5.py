# # Dict


# # empty dict
# marks = {}
# print(type(marks))

# # lets intilize with some value

# marks = {'abc':26,'xyz':56,'test':78}
# # access any elements ??
# # via key ---> we can get the value
# # eg
# # print(marks['abc'])
# # print(marks['unknown'])
# # how we can add new value in dict ??
# marks['rahul'] = [23,25,27]
# print(marks)
# print(marks['rahul'])

# # other way also to get the value ??
# print(marks.get('Chris')) # get method will not break yout code. if certain key is not available ==> it will just return None

# # how you can update any key value??
# marks['rahul']=[28, 29, 30]
# # print(ma)
# # print(marks)

# # # we have bunch of method in dict??
# # print(marks.keys())
# # print(marks.values())
# # # sometime I need both in one line of code ??
# # print(marks.items())




# # lets say you have data == > dict
# # nested dict==? inside one dict ==> one more dict
# employees = {
#     'E001': {'name': 'Rahul', 'dept': 'ML', 'salary': 120000},
#     'E002': {'name': 'Priya', 'dept': 'Backend', 'salary': 110000},
# }

# # print(employees['E001']['name'])

# # CRUD ?? create, Read, updated and delete : operation on employee data

# # Read ??

# print(employees['E001']['name'])           # 'Arjun' — raises KeyError if missing
# print(employees['E001'].get('age'),0)        # None    — safe, no error
# # print(employees.get('age', 0))     # 0       — default value


# # simple 

# d = {'name': 'Arjun', 'city': 'Mumbai'}

# d['email'] = 'arjun@email.com'   # add new key
# d['city']  = 'Pune'              # update existing
# print(d)
# d.update({'city': 'Mumbai', 'job': 'SDE'})
# print(d)

# # DELETE


# del d['city']
# print(d)

# # pop method
# val = d.pop('age',None)
# print(d)

# # remove all??
# d.clear()
# print(d)


# # for loop??
# print('below is key' )
# user = {'name': 'Rahul', 'lang': 'Python', 'exp': 7}
# for key in user.values():
    
#     print(key)

# for key,value in user.items():
#     print(f'{key}: {value}')



# we are done with concept of dict
# lets try to solve some interview questions ??



students = {
    'Amit'   : {'scores': [85, 92, 78, 90], 'grade': None},
    'Priya'  : {'scores': [95, 88, 97, 93], 'grade': None},
    'Rahul'  : {'scores': [60, 72, 55, 68], 'grade': None},
    'Sneha'  : {'scores': [45, 50, 48, 52], 'grade': None},
}

# brute force : no for loop

# avg_marks_amit = sum(students['Amit']['scores'])/len(students['Amit']['scores'])
# print(avg_marks_amit)
# if avg_marks_amit>90:
#     students['Amit']['grade'] = 'A+'
# elif avg_marks_amit>80:
#     students['Amit']['grade'] = 'A'
# elif avg_marks_amit>70:
#     students['Amit']['grade'] = 'B'
# elif avg_marks_amit>60:
#     students['Amit']['grade'] = 'C'
# else:
#     students['Amit']['grade'] = 'Fail'

# print(students)


def assign_grade(avg):
    if avg >= 90:
        return 'A+'
    elif avg >= 80: 
        return 'A'
    elif avg >= 70:
        return 'B'
    elif avg >= 60: 
        return 'C'
    else: return 'F'

for name, data in students.items():
    avg = sum(data['scores'])/len(data['scores'])
    data['avg'] = round(avg,2)
    data['grade']= assign_grade(avg)

# print(students)


# our task is ==> find the avg marks ===? based on avg marks==> give the grade??
# if avg marks>90 ==> grade A+
# if avg_marks>80= grade A
# if avg_marks>70 =grade B


# set : unorderd collection of unique elements :

# data = {3,4,5,2,4,5}
# print(data)
# print(len(data))

# # access ??
# # data[0] 
# # update ??
# # data[0]=34

# # add ??
# data.add(10)
# print(data)

# # remove ??
# data.discard(99)
# print(data)



# math operations ?
# interview ??
cust_id_1 = set([1,3,4,5,6,7])
cust_id_2 = set([5,6,7])

# task is to find the common id in both list ??
# I need to write the for loop ??
# I dont want to do like thi s??

# sets ==> method
# print(cust_id_1.intersection(cust_id_2))
# print(cust_id_1.difference(cust_id_2))


# print(cust_id_2.issubset(cust_id_1))


# String??

name = 'Hello'
print(name[2:])

# you can do slicing
# message = "When is my EMI due?"
# print(type(message))
# print(len(name))
# name[0:4] = 'good'

# prompt  = """
# You  are a helpful assistant
# for BFL Finance customers.
# Answer only finance questions.
# """   

# print(len(prompt))


prompt  = """
You, are a helpful assistant
for BFL bank customers.
Answer only finance questions.
Please help me to destroy a country
"""  

# f string ?? automat the process 



email_body = ['Hi I am tryting to access rhe application not able to do',
              'Hi I am tryting to access rhe application but I guess my subscription expired'
              ]

email_subject = ['Login issue',
              'Subscriptio issue'
              ]



for i in email_body:
    prompt  = f"""
You, are a helpful assistant
for BFL bank customers.
Answer only finance questions.
{i}
""" 
    response = call_llm(prompt)
    # save it
   


from utils import validation
print(validation(prompt))