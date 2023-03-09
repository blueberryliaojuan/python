# 序列 includes list, tuple,string
my_list = [0, 1, 2, 3, 4, 5, 6]
result1 = my_list[1:4:1]
print(result1)

my_tuple = (0, 1, 2, 3, 4, 5, 6)
result2 = my_tuple[:]  # from beginning to end
print(result2)

my_string = '0123456'
result3 = my_string[::2]
print(result3)

my_list = [0, 1, 2, 3, 4, 5, 6]
result4 = my_list[1:4:-1]  # backwards
print(result4)
result5 = my_list[::-1]
print(result5)
