from delta_encodiing import *
from delta_decoding import *
from huffman_decoding import *
from huffman_encoding import *
from elias_gamma_encoding import *
from elias_gamma_decoding import *


data = [100, 101, 104]
delta = delta_encode(data)
print(delta)

elias_gamma = elias_gamma_encode_list(delta)
print(elias_gamma)
print(len(elias_gamma))

def chunk_string(bitstream, chunk_size):
    chunks = []
    for i in range(0, len(bitstream), chunk_size):
        chunk = bitstream[i:i + chunk_size]
        chunks.append(chunk)
    return chunks

huffman_chunks = chunk_string(elias_gamma, len(elias_gamma) // 2)
print(huffman_chunks)

codes = generate_codes(build_huffman_tree(get_frequencies(huffman_chunks)))
print(codes)

encoded_list = encode_list(huffman_chunks, codes)
print(encoded_list)
tree_root = build_huffman_tree(get_frequencies(huffman_chunks))
decoded_list = huffman_decoded_list(encoded_list, tree_root)
print(decoded_list)

eg_decoded = elias_gamma_decode(decoded_list)
print(eg_decoded)

delta_decoded = delta_decode(eg_decoded)
print(delta_decoded)
print("-----------------------------------------")

original_bits = len(data) * 8  # each number stored as 8 bits originally
compressed_bits = len(encoded_list)  # already a bitstring

compression_ratio = original_bits / compressed_bits
compression_percentage = ((original_bits - compressed_bits) / original_bits) * 100

print(f"Original Size: {original_bits} bits")
print(f"Compressed Size: {compressed_bits} bits")
print(f"Compression Ratio: {compression_ratio:.2f}")
print(f"Compression Percentage: {compression_percentage:.2f}%")
