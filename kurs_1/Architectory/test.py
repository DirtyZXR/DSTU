import heapq
from collections import defaultdict
import tkinter as tk

class HuffmanGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Huffman Encoder/Decoder")

        input_frame = tk.Frame(self.root)
        output_frame = tk.Frame(self.root)

        self.input_label = tk.Label(input_frame, text="Enter text:")
        self.input_entry = tk.Entry(input_frame)
        self.encode_button = tk.Button(
            input_frame, text="Encode", command=self.encode_text)

        self.output_label1 = tk.Label(output_frame, text="Encoded text:")
        self.output_text1 = tk.Text(output_frame, height=8)
        self.output_label2 = tk.Label(output_frame, text="Decoded text:")
        self.output_text2 = tk.Text(output_frame, height=8)

        self.input_label.pack(side=tk.LEFT, padx=10, pady=10)
        self.input_entry.pack(side=tk.LEFT, padx=10, pady=10)
        self.encode_button.pack(side=tk.LEFT, padx=10, pady=10)

        self.output_label1.pack(padx=10, pady=10)
        self.output_text1.pack(padx=10, pady=10)
        self.output_label2.pack(padx=10, pady=10)
        self.output_text2.pack(padx=10, pady=10)

        input_frame.pack()
        output_frame.pack()

    def encode_text(self):
        input_text = self.input_entry.get()
        encoded_text, huffman_dict = self.huffman_encoding(input_text)
        decoded_text = self.huffman_decoding(encoded_text, huffman_dict)
        self.output_text1.delete('1.0', tk.END)
        self.output_text1.insert(tk.END, encoded_text)
        self.output_text2.delete('1.0', tk.END)
        self.output_text2.insert(tk.END, decoded_text)

    def huffman_encoding(self, data):
        freq = defaultdict(int)
        for char in data:
            freq[char] += 1

        heap = [[weight, [symbol, ""]] for symbol, weight in freq.items()]
        heapq.heapify(heap)

        while len(heap) > 1:
            left_node = heapq.heappop(heap)
            right_node = heapq.heappop(heap)

            for pair in left_node[1:]:
                pair[1] = '0' + pair[1]
            for pair in right_node[1:]:
                pair[1] = '1' + pair[1]

            heapq.heappush(heap, [left_node[0] + right_node[0]] +
                           left_node[1:] + right_node[1:])

        huffman_dict = dict(heapq.heappop(heap)[1:])
        encoded_data = ''.join([huffman_dict[char] for char in data])
        return encoded_data, huffman_dict

    def huffman_decoding(self, encoded_data, huffman_dict):
        decoded_data = ''
        reverse_dict = {v: k for k, v in huffman_dict.items()}

        i = 0
        while i < len(encoded_data):
            j = i + 1
            while encoded_data[i:j] not in reverse_dict:
                j += 1
            decoded_data += reverse_dict[encoded_data[i:j]]
            i = j

        return decoded_data

root = tk.Tk()
gui = HuffmanGUI(root)
root.mainloop()