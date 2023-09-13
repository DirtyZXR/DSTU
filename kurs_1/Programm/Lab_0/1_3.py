while True:
    try:
        time_work = int(input('Введите количество часов работы\n>>> '))
        if time_work >= 0:
            break
        else:
            print('Введено отрицательное чилсо')
    except:
        print('Введено не верное число')

while True:
    try:
        zar = int(input('Введите заработк в час\n>>> '))
        if zar >= 0:
            break
        else:
            print('Введено отрицательное чилсо')
    except:
        print('Введено не верное число')

if time_work > 40:
    print(f'Зарплата сотрудника {time_work * zar * 1.5}')
else:
    print(f'Зарплата сотрудника {time_work * zar}')