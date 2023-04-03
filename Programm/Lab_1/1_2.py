list_ = [1, 10 , 'g', '2', 13, -2 , '-2', 15, 'h', 's', 11, 'f', -1230, 0]
print(list_)

'''
Если имеется в виду что порядок элемента
'''
for i in range(0,len(list_),2):
    print(list_[i])
print()

for i in range(1,len(list_),2):
    print(list_[i])
print()

st = ''
for i in range(0,len(list_),2):
    st += str(list_[i])
print(st)
print()

st = ''
for i in range(1,len(list_),2):
    st += str(list_[i])
print(st)
print()