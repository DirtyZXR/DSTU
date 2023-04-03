from random import randint


def var_1(my_number):
    while True:
        try:
            user_number = int(input("Введите число\n>>> "))
            if user_number < my_number:
                print("Успех!")
                break
            else:
                print("Число больше или равно ", my_number)
        except:
            pass


def var_2(my_number):
    while True:
        try:
            user_number = int(input("Введите число\n>>> "))
            if user_number == my_number:
                print("Успех!")
                break
            else:
                print("Число не равно ", my_number)
        except:
            pass


def var_3(my_number):
    while True:
        try:
            user_number = int(input("Введите число\n>>> "))
            if user_number < my_number:
                print("Успех!")
                break
            else:
                print("Число больше или равно ", my_number)
        except:
            pass


def var_4(my_number):
    while True:
        try:
            user_number = int(input("Введите число\n>>> "))
            if user_number > my_number:
                print("Успех!")
                break
            else:
                print("Число меньше или равно ", my_number)
        except:
            pass


while True:
    try:
        var = int(input("Введите вариант\n>>> "))
        if 1 <= var <= 4:
            break
        else:
            print("Неверный вариант")
    except:
        print("Введите число")

my_number = randint(-10, 10)
print("my_number = ", my_number)

if var == 1:
    var_1(my_number)
elif var == 2:
    var_2(my_number)
elif var == 3:
    var_3(my_number)
else:
    var_4(my_number)
