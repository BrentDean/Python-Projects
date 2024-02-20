while True:
    print('Who are you?')
    name = input()
    if name != 'Brent':
        continue
    print('Hello Brent. Password?')
    password = input()
    if password == 'poocat':
        break
print('Access Granted.')