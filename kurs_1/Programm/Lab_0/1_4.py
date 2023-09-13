import re
def valid(x):
    result = re.match("/d{5}", x) is not None
    return result

x = input('Введите число\n>>> ')
res = valid(x)

if res:
    print('Верно')
else:
    print('Неверно')