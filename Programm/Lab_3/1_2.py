my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
data = my_string.split(";_")
f = data[0].split(';')
print('{:^30}  {:^30}  {:^30}'.format(f[0]+f[1]+f[2],f[4],f[3]))
for i in data[1:]:
    data_split = i.split(';')
    str_ = '{:^30}  {:^30}  {:^30}'.format(data_split[0]+' '+data_split[1]+' '+data_split[2], data_split[4], data_split[3])
    print(str_)
print('\n\n')

my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
data = my_string.split(";_")
f = data[0].split(';')
print('{:^30}  {:^30}  {:^30}'.format(f[0]+f[1]+f[2],f[3],f[4]))
for i in data[1:]:
    data_split = i.split(';')
    str_ = '{:^30}  {:^30}  {:^30}'.format(data_split[0]+' '+data_split[1]+' '+data_split[2], data_split[3], data_split[4])
    print(str_)#
print('\n\n')

my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
data = my_string.split(";_")
f = data[0].split(';')
print('{:^10} {:^10} {:^10} {:^30}  {:^30}'.format(f[0], f[1], f[2], f[4],f[3]))
for i in data[1:]:
    data_split = i.split(';')
    str_ = '{:^10} {:^10} {:^10}  {:^30}  {:^30}'.format(data_split[0], data_split[1], data_split[2], data_split[4], data_split[3])
    print(str_)
print('\n\n')

my_string = "Ф;И;О;Возраст;Категория;_Иванов;Иван;Иванович;23 года;Студент 3 курса;_Петров;Семен;Игоревич;22 года;Студент 2 курса"
data = my_string.split(";_")
f = data[0].split(';')
print('{:^30} {:^30}'.format(f[0]+f[1]+f[2],f[3]+','+f[4]))
for i in data[1:]:
    data_split = i.split(';')
    str_ = '{:^30} {:^30}'.format(data_split[0]+' '+data_split[1]+' '+data_split[2], data_split[4]+','+data_split[3])
    print(str_)
print()