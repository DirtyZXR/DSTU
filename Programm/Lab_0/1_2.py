while True:
    try:
        x = int(input('Введите первое число\n>>> '))
        break
    except:
        print('Введено не верное число')

while True:
    try:
        y = int(input('Введите второе число\n>>> '))
        break
    except:
        print('Введено не верное число')

print(f'{x}+{y}={x+y}')
print(f'{x}-{y}={x-y}')
print(f'{x}*{y}={x*y}')

if x != 0:
    print(f'{y}/{x}={y / x}')
    print(f'{y}//{x}={y // x}')
if y != 0:
    print(f'{x}/{y}={x / y}')
    print(f'{y}//{x}={y // x}')
if x == 0 and y == 0:
    print('Деление невозможно')

print(f'{x}^2={x*x}')
print(f'{y}^2={y*y}')

print(f'Первое число в двоичном виде = {bin(x)}')
print(f'Второе число в двоичном виде = {bin(y)}')

print(f'Первое число в восьмеричном виде = {oct(x)}')
print(f'Второе число в восьмеричном виде = {oct(y)}')

print(f'Первое число в шестнадцатеричном виде = {hex(x)}')
print(f'Второе число в шестнадцатеричном виде = {hex(x)}')