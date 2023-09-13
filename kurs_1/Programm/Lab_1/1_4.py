from random import randint

list_ = []
for i in range(randint(7,15)):
    list_.append(randint(-20, 20))

print(list_)

# print(max(list_))

max_ = list_[0]
for i in list_:
    max_ = i if i > max_ else max_

print('max = ', max_)
print()

min_ = list_[0]
for i in list_:
    min_ = i if i < min_ else min_

print('min = ',min_)
print()

sr = 0
for i in list_:
    sr += i

if len(list_) > 0:
    sr /= len(list_)
print('mean = %.3f'%sr)
print()

if len(list_) % 2 == 0:
    print('В массиве четное кол-во елементов. Нет срединного элемента')
else:
    mean = len(list_) // 2
    print('mean elem = ', list_[mean])
