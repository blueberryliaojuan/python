name_list = ['Tom', 'Jerry', 'Susie', "Jason"]
print(type(name_list))  # <class 'list'>
print(name_list[2])
print(name_list[-1])
print(name_list.index('Tom'))

name_list.append('Jessy')
print(name_list)
extra_name_list = ['Bob', "Lily", "Lucy", "Joy", "Jessy"]
name_list.extend(extra_name_list)
print(name_list)
name_list.insert(2, 'Julie')
print(name_list)

name_list.pop(1)
print(name_list)
del name_list[0]
print(name_list)
name_list.remove('Lily')
print(name_list)

print(name_list.count('Jessy'))
print(len(name_list))

index = 0
while index < len(name_list):
    print(name_list[index])
    index += 1

for item in name_list:
    print(item)

name_list.clear()
print(name_list)

complex_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(complex_list[0][1])
