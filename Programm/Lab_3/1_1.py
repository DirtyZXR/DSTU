string = "Добрый день, дорогие друзья! Сегодня мы собрались вместе, чтобы отпраздновать День Рождения нашего коллеги. " \
         "Желаем ему только счастья, радости и успехов в работе! Лишение всех пробелов, Лиза!"

# Вариант 1
words = []
for word in string.split(' '):
    if len(word) > 5:
        words.append(word)
new_string = ' '.join(words)
print('Вариант 1')
print(new_string, '\n')

# Вариант 2
words = []
for word in string.split(' '):
    if word.startswith('Ли'):
        words.append(word)
new_string = ' '.join(words)
print('Вариант 2')
print(new_string, '\n')

# Вариант 3
words = []
for word in string.split(' '):
    if len(word) >= 5 and len(word) <= 10:
        words.append(word)
new_string = ' '.join(words)
print('Вариант 3')
print(new_string, '\n')

# Вариант 4
words = []
for word in string.split(' '):
    if word[-2:] == 'ов':
        words.append(word)
new_string = ' '.join(words)
print('Вариант 4')
print(new_string, '\n')