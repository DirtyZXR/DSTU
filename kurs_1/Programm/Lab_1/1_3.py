from random import randint

list_ = []
for i in range(randint(7,15)):
    list_.append(randint(-20, 20))

print(list_)

sum = 0
for i in list_:
    if i > 10:
        sum += i
print(sum)
print()

sum = 0
for i in list_:
    if 1 < i < 10:
        sum += i
print(sum)
print()

sum = 1
for i in list_:
    if i < 10:
        sum *= i
print(sum)
print()




