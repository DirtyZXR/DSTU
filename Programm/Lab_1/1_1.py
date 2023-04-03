def var_1(a, b, c, k):
    try:
        result = (
            ((a**2) / (b**2) + (c**2 * b**2)) / (a + b + c * (k - a / (b**3)))
            + c
            + (k / b - k / a) * c
        )
        result = abs(result)
    except ZeroDivisionError:
        result = "Ошибка! Деление на ноль"

    # if b == 0:
    #     result = 'Ошибка! Деление на ноль'
    # elif a == 0:
    #     result = 'Ошибка! Деление на ноль'
    # elif a + b + c*(k - a/(b**3)) == 0:
    #     result = 'Ошибка! Деление на ноль'
    # else:
    #     result = ((a ** 2) / (b ** 2) + (c ** 2 * b ** 2)) / (a + b + c * (k - a / (b ** 3))) + c + (k / b - k / a) * c
    #
    return result


def var_2(a, b, c, k, d):
    if b == 0 or a == 0:
        result = "Ошибка! Деление на ноль."
    else:
        result = (
            (a**2 - b**2 - c**3 * a**2) * (b - c + c * (k - d / b**3))
            - (k / b - k / a) * c
        ) ** 2 - 20000
        result = abs(result)

    return result


def var_3(a, b, c):
    if c - a != 0:
        result = (
            1 - a * b**c - a * (b**2 - c**2) + (b - c + a) * (12 + b) / (c - a)
        )
        result = abs(result)
    else:
        result = "Ошибка! Деление на ноль"

    return result


def var_4(a, b, c, d, f):
    if a != 0:
        result = a - b * c * d**3 + (c**5 - a**2) / a + f**3 * (a - 213)
        result = abs(result)
    else:
        result = "Ошибка! Деление на ноль"

    return result


while True:
    try:
        var = int(input("Введите вариант(1,4)\n>>> "))
        if 1 <= var <= 4:
            break
        else:
            print("Введите число от 1 до 4")
    except:
        print("Введите число")

while True:
    try:
        a = int(input("Введите a\n>>> "))
        break
    except:
        print("Введено не верное число")

while True:
    try:
        b = int(input("Введите b\n>>> "))
        break
    except:
        print("Введено не верное число")

while True:
    try:
        c = int(input("Введите c\n>>> "))
        break
    except:
        print("Введено не верное число")

if var == 1 or var == 2:
    while True:
        try:
            k = int(input("Введите k\n>>> "))
            break
        except:
            print("Введено не верное число")

if var == 2 or var == 4:
    while True:
        try:
            d = int(input("Введите d\n>>> "))
            break
        except:
            print("Введено не верное число")

if var == 4:
    while True:
        try:
            f = int(input("Введите f\n>>> "))
            break
        except:
            print("Введено не верное число")

if var == 1:
    res = var_1(a, b, c, k)
elif var == 2:
    res = var_2(a, b, c, k, d)
elif var == 3:
    res = var_3(a, b, c)
else:
    res = var_4(a, b, c, d, f)


print(res)
