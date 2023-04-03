while True:
    try:
        moth = int(input('Введите номер месяца\n>>> '))
        if moth >= 1 and moth <= 12:
            break
        else:
            print('Введен неверный месяц')
    except:
        print('Введите число')

moth_31 = (1,3,5,7,8,10,12)


if moth in moth_31:
    print('В месяце 31 день')
elif moth == 2:
    print('В месяце 28 дней')
else:
    print('В месяце 30 дней')