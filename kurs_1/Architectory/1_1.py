import heapq
from collections import defaultdict

class Node:
    def __init__(self, freq, symbol, left=None, right=None):
        self.freq = freq
        self.symbol = symbol
        self.left = left
        self.right = right

    def __lt__(self, other):
        return self.freq < other.freq

def huffman_encoding(text):
    if not text:
        return "", {}

    # Step 1: Create frequency dictionary
    freq_dict = defaultdict(int)
    for symbol in text:
        freq_dict[symbol] += 1

    # Step 2: Create priority queue
    heap = [Node(freq, sym) for sym, freq in freq_dict.items()]

    heapq.heapify(heap)

    # Step 3: Create Huffman tree
    while len(heap) > 1:
        node1 = heapq.heappop(heap)
        node2 = heapq.heappop(heap)
        # print(heap)
        merged = Node(node1.freq + node2.freq, None, node1, node2)
        heapq.heappush(heap, merged)
        # print(heap)
        # print(merged)
    # Step 4: Assign codes to symbols
    def assign_codes(node, code='', code_dict={}):
        if node is None:
            return
        if node.symbol is not None:
            code_dict[node.symbol] = code
        assign_codes(node.left, code + '0', code_dict)
        assign_codes(node.right, code + '1', code_dict)
        return code_dict

    code_dict = assign_codes(heap[0])

    # Step 5: Create symbol-code table
    table = {sym: code_dict[sym] for sym in freq_dict.keys()}

    # Step 6: Encode text
    encoded_text = ''.join(table[symbol] for symbol in text)

    return encoded_text, table

def huffman_decoding(encoded_text, table):
    if not encoded_text:
        return ""

    # Reverse symbol-code table
    rev_table = {code: sym for sym, code in table.items()}

    # Decode text
    decoded_text = ""
    code = ""
    for bit in encoded_text:
        code += bit
        if code in rev_table:
            decoded_text += rev_table[code]
            code = ""

    return decoded_text

text = "abracadabra,,,12,фыВ"
encoded_text, table = huffman_encoding(text)
print(f"Encoded text: {encoded_text}")

print("Symbol-Code table:")
for symbol, code in table.items():
    print(f"{symbol}: {code}")
# Output:
# Symbol-Code table:
# a: 01
# b: 001
# r: 111
# c: 1010
# d: 1011

decoded_text = huffman_decoding(encoded_text, table)
print(f"Decoded text: {decoded_text}")
# Output: Decoded text: abracadabra
