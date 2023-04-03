import random
import string


def var_1(list_):
    for i in list_:
        if 5 < len(i) < 10:
            print(i)


def var_2(list_):
    for i in list_:
        if len(i) < 10:
            print(i)


def var_3(list_):
    for i in list_:
        if i[-1] == "r":
            print(i)


def var_4(list_):
    for i in list_:
        if i[1] == "r":
            print(i)


def generate_random_string(length):
    letters = string.ascii_lowercase
    rand_string = "".join(random.choice(letters) for i in range(length))

    return rand_string


list_ = []
for i in range(12):
    s = generate_random_string(random.randint(1, 15))
    list_.append(s)

print(list_)


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
    var_1(list_)
elif var == 2:
    var_2(list_)
elif var == 3:
    var_3(list_)
else:
    var_4(list_)
