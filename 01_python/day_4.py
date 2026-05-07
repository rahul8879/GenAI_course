# for loop ? while loop ? if else??
# Data structure --> List --> sets, tuple, dict etc.

# message = ['m1','m2','m3','m4','m5','m6']

# # access any of the message ??
# # via index
# # print(message)
# # print(message[2])

# # slicing ??
# # print(message[1:4]) # it will exclude the 4th elements/end index
# # print(message[0:4:2])
# # print(message[4:])


# # method
# # 1. add more message in my list
# message.append('m7')
# # print(message)

# # add at specific location : insert(i,what you want )
# message.insert(4, 'm8')
# # print(message)

# # 
# message_2 = ['m10','m11','m12']
# # message.append(message_2)
# # print(message)

# message.extend(message_2)
# print(message)


# remove ?? I want to remove m12/m1

# message.remove('m1') # remove method will take your element sand then it will remove it from list
# print(message)

# pop ----> input --> remove --> elements as input
# but pop method take index as a input 
# message.pop(2)
# print("Aftr removing index 2 value",message)

# marks = [23,45,65,-1]
# # sort it --> increasing order ?????
# marks.sort(reverse=False) # if True --> decrasing 
# print(marks)

# message.clear()
# print(message)







# questions ?? 
# basic overview about function concept
# inbuilt --> user defined 
# len, type, print


# defined : 
# def testing(x,y,total_marks):
#     z = x+y
#     return z,total_marks,12
# # calling ??
# # testing()
# print(testing(5,6,100))



cart = []

def add_item(product,price):
    cart.append({'product':product,'price':price})
 

# call your functions
# before adding
print(cart)
add_item('apple',67)
# print(cart)
add_item('TV',100)
add_item('BANANA',50)
# print(cart)


# # remove 
product= 'banana'
def remove_item(product):
    new_cart = []
    for i in cart:
        if i['product'].lower() !=product.lower():
            new_cart.append(i)
    return new_cart


# print(cart)
# # call ??
# new_cart = remove_item('tv')
# print(new_cart)

def cart_total(cart):
    total_amount = 0
    for i in cart:
        total_amount = total_amount+i['price']
    return total_amount

# print(cart_total(cart))



# print(cart[2]['price'])


# interview ?? classroom/ homework
# def two_sum(lst,target):
#     # logic
#     return 0,1

# print(two_sum([2, 7, 11, 15], 9)) # index number which summation will be 9
# print(two_sum([2, 6, 11, 15], 17)) #output : ( 0,4), ((1,2))

#tuple

point = (10,20,30,40,50)
print(point[::2])

# access any elements : you can do the same as list

# data = 13,15,13,18
# print(type(data))
# print(data[0])

# # use case --> dynamic --List --fixed --tuple
# # methods --List --Lots of method
# # 1-2 : counter
# print(data.count(13))




cities = {
    'Mumbai'  : (19.0760, 72.8777),
    'Delhi'   : (28.6139, 77.2090),
    'Bangalore': (12.9716, 77.5946),
    'Hyderabad': (17.3850, 78.4867),
}


import math

def haversin_distance(loc1,loc2):
    lat1,lan1 = loc1
    lat2,lan2 = loc2
    R = 6371 # Earth radius in KM
    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lan2-lan1)
    a = math.sin(dlat/2)**2 + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2)**2
    return R * 2 * math.asin(math.sqrt(a))
# https://www.geeksforgeeks.org/dsa/haversine-formula-to-find-distance-between-two-points-on-a-sphere/
dist = haversin_distance(cities['Mumbai'],cities['Delhi'])
print(dist)
