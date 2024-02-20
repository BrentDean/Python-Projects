number = input()

def collatz():
    if int(number) % 2 == 0:
        print('str(number) // 2')
    elif int(number) % 2 == 1:
        print('3 * str(number) + 1')

