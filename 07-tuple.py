my_tuple = ('ww', 3, 4, 5)
print(my_tuple)
print(type(my_tuple))  # <class 'tuple'>

t1 = ('hello')
print(type(t1))  # <class 'str'>
t2 = ('hello',)
print(type(t2))  # <class 'tuple'>

t3 = (('hello0', 'hello1'), ('world0', "world1"))
print(t3[1][0])

t4 = ('hello', 'hello', 'hello0')
index = t4.index('hello')
print(index)  # 0
count = t4.count('hello')
print(count)  # 2
length = len(t4)
print(length)  # 3
index = 0
while index < length:
    print(t4[index])
    index += 1
for item in t4:
    print(item)
