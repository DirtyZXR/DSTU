import copy
import time
import snoop

# @snoop
def get_freq(some_str):
    result_dict = {}
    for char in some_str:
        if char in result_dict.keys():
            result_dict[char] += 1
        else:
            result_dict[char] = 1
    result = [{k: {k: v, "sum": v}} for k, v in sorted(result_dict.items(), key=lambda item: item[1])]
    return result

# @snoop
def make_tree(freq_dict: list):
    origin_freq_dict = copy.copy(freq_dict)
    while len(freq_dict) > 2:
        min_1: dict = freq_dict.pop(0)
        min_2: dict = freq_dict.pop(0)
        key_1: str = list(min_1.keys())[0]
        key_2: str = list(min_2.keys())[0]
        value_1 = min_1[key_1]
        value_2 = min_2[key_2]
        new_key: str = key_1 + key_2
        new_sum: int = value_1["sum"] + value_2["sum"]
        new_value: dict = dict(list(min_1.items()) + list(min_2.items()))
        new_value.update({"sum": new_sum})
        some_dict = {new_key: new_value}
        big_index = None
        for i in range(len(freq_dict)):
            i_key = list(freq_dict[i].keys())[0]
            i_sum = freq_dict[i][i_key]["sum"]
            if i_sum > new_sum:
                big_index = i
                break
        if big_index == 0:
            freq_dict.insert(0, some_dict)
        elif big_index is None:
            freq_dict.append(some_dict)
        else:
            freq_dict.insert(big_index, some_dict)
    return freq_dict, origin_freq_dict

# @snoop
def create_code_dict(branch, code_dict, decode_dict, symbol):
    branch_key = list(branch.keys())[0]
    if len(branch_key) == 1:
        code_dict.update({branch_key: symbol})
        decode_dict.update({symbol: branch_key})
    else:
        branch_items = branch[branch_key]
        added_symbol = -1
        for key, value in branch_items.items():
            if key != "sum":
                added_symbol += 1
                create_code_dict({key: value}, code_dict, decode_dict, symbol + str(added_symbol))

# @snoop
def encode(origin_string, code_dict):
    result_string = ""
    for char in origin_string:
        result_string += code_dict[char]
    return result_string

# @snoop
def decode(encoded_string, code_dict):
    decoded_string = ""
    checked_symbols = ""
    for char in encoded_string:
        checked_symbols += char
        if coded_symbol := code_dict.get(checked_symbols, None):
            decoded_string += coded_symbol
            checked_symbols = ""
    return decoded_string


# start_time = time.time()
# print(start_time)

test = "Hello, world"
start_str = test

freq_dict = get_freq(start_str)
tree, origin_freq_dict = make_tree(freq_dict)

encode_dict = {}
decode_dict = {}
create_code_dict(tree[0], encode_dict, decode_dict, "0")
create_code_dict(tree[1], encode_dict, decode_dict, "1")

encoded_string = encode(start_str, encode_dict)
print(encoded_string)
print()
print(encode_dict)

decoded_string = decode(encoded_string, decode_dict)
print(decoded_string)

# print(time.time())
# end_time = time.time() - start_time
# print(end_time)
