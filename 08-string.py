my_str = 'programming is fun and creative'
value1 = my_str[3]
print(value1)
value2 = my_str[-3]
print(value2)
value3 = my_str[1:5]
print(value3)

# my_str[2] = 3  #str' object does not support item assignment
index = my_str.index('and')
print(index)

my_new_str = my_str.replace('and', '&')
print(my_new_str)

list = my_str.split(' ')
print(list)

str1 = ' ss '
str2 = str1.strip()
print(str2)

str4 = 'starts'
str3 = str4.strip('s')
print(str3)  # tart

count = my_str.count('m')
print(count)
length = len(my_str)
print(length)
