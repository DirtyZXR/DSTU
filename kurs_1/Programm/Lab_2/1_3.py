from random import randint, choice
import string

def var_1():
    st = ''
    for i in range(5):
        st += chr(randint(1040,1071))
    print(st)

def var_2():
    while True:
        try:
            n = int(input("Введите N\n>>> "))
            break
        except:
            print("Введите число")

    s = ''

    for i in range(n):
        s += "R"

    print(s)

def var_3():

    s = [choice('012456789') for _ in range(5)]
    s.insert(randint(0, 5), '3')
    print(''.join(s))

def var_4():
    s = [choice(string.ascii_letters + string.digits) for _ in range(8)]
    s.insert(randint(0, 8), choice(string.digits))
    print(''.join(s))

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