def say_hi(name):
    """
    :param name: input users' name
    :return: username
    """
    print(f'hello, my name is {name}  ')
    return name


say_hi('Justin')
say_hi('Susan')

total_amount = 5000000
client_name = None
client_name = input('please input your name:')


def query(show):
    if show:
        print('------the balance-----')
    print(f"{client_name},your balance is {total_amount} dollars")


def saving(num):
    global total_amount
    total_amount += num
    print('------saving-----')
    print(f"{client_name},you saved {num} dollars")
    query(False)


def withdraw(num):
    global total_amount
    total_amount -= num
    print('------withdraw-----')
    print(f"{client_name},you withdrew {num} dollars")
    query(False)


def main():
    print('------menu-----')
    print(f'hello, {client_name},welcome to use ATM machine, ')
    print('check balance: \tinput[1]')
    print('save: \t\t\tinput[2]')
    print('withdraw: \t\tinput[3]')
    print('quit: \t\t\tinput[4]')
    return input('please select your operation:')


while True:
    keyword = main()
    if keyword == '1':
        query(True)
        continue
    elif keyword == "2":
        num = int(input('please input the saving amount:'))
        saving(num)
        continue
    elif keyword == '3':
        num = int(input('please input the withdraw amount:'))
        withdraw(num)
        continue
    else:
        print('goodbye')
        break
