from random import randint, choice
import string


def var_1():
    d = ['1', "2", '3', '4', '5', '6', '7', '8', '9', '0']
    s = [choice(string.ascii_letters + string.digits) for _ in range(10)]
    s = ''.join(s)
    print('Start string = ' + s)

    new_s = ''
    for i in s:
        if i in d:
            new_s += i

    print(new_s)


def var_2():
    d = string.ascii_letters
    s = [choice(string.ascii_letters + string.digits) for _ in range(10)]
    s = ''.join(s)
    print('Start string = ' + s)

    new_s = ''
    for i in s:
        if i in d:
            new_s += i

    print(new_s)

def var_3():
    russian_chr = ''
    for i in range(1040, 1072):
        russian_chr += chr(i)

    s = [choice(russian_chr + string.digits) for _ in range(10)]
    s = ''.join(s)
    print('Start string = ' + s)

    new_s = ''
    for i in s:
        if ord(i) == 1051:
            new_s += i

    print(new_s)

def var_4():
    d = ['1', "2", '3', '4', '5', '6', '7', '8', '9', '0']
    d_s = string.ascii_letters
    s = [choice(string.ascii_letters + string.digits) for _ in range(10)]
    s = ''.join(s)
    print('Start string = ' + s)

    new_s_1 = ''
    for i in s:
        if i in d:
            new_s_1 += i

    print(new_s_1)

    new_s_2 = ''
    for i in s:
        if i in d_s:
            new_s_2 += i

    print(new_s_2)

while True:
    try:
        var = int(input("Введите вариант\n>>> "))
        if 1 <= var <= 4:
            break
        else:
            print("Неверный вариант")
    except:
        print("Введите число")

if var == 1:
    var_1()
elif var == 2:
    var_2()
elif var == 3:
    var_3()
else:
    var_4()