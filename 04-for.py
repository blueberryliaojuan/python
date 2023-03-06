name = 'this is a book'
for x in name:
    print(x)
    if x == 'a':
        break

for i in range(1, 99, 3):
    print(i)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f"{j}*{i}={j * i}\t", end='')
    print()
