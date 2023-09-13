import snoop

# Вводим исходный текст
text = input("Введите текст: ")

# Составляем таблицу частотности символов в тексте
freq = {}
for char in text:
    if char in freq:
        freq[char] += 1
    else:
        freq[char] = 1

# Составляем список узлов дерева, где каждый узел представляет собой один символ и его частоту
nodes = []
for char, f in freq.items():
    nodes.append((f, char))

# Находим два узла с наименьшими частотами, объединяем их в новый узел, и суммируем их частоты.
# Повторяем эту операцию до тех пор, пока не останется один узел.
while len(nodes) > 1:
    nodes.sort()
    smallest = nodes[:2]
    left = smallest[0]
    right = smallest[1]
    nodes = nodes[2:]
    node = (left[0]+right[0], left[1]+right[1])
    nodes.append(node)
    tree = nodes[0]
print(tree)
# Определяем коды каждого символа, проходя по дереву от корня до каждого листа и присваивая 0 или 1
# в зависимости от того, является ли путь к этому листу левым или правым.
codes = {}
@snoop
def code_tree(tree, code=""):
    if type(tree) is tuple:
        code_tree(tree[0], code + "0")
        code_tree(tree[1], code + "1")
    else:
        codes[tree] = code
code_tree(tree)

# Составляем таблицу соответствия символа и его кодового слова на основе полученных кодовых последовательностей
table = ""
for char, code in codes.items():
    table += f"{char}: {code}\n"

# Кодируем исходный текст, заменяя каждый символ на соответствующую ему кодовую последовательность
encoded_text = ""
for char in text:
    if char in codes:
        encoded_text += codes[char]
    else:
        encoded_text += "0"

# Выводим таблицу соответствия символа и кодового слова, закодированное предложение
print(f"Таблица кодов:\n{table}")
print(f"Закодированный текст:\n{encoded_text}")