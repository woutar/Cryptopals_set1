import base64, math
from challenge3 import decipher_single_byte_xor
from challenge5 import clean_repeating_xor
from bitstring import BitArray

encrypted_base64 = open("encrypted_base64.txt").read()
encrypted_bytes = base64.b64decode(encrypted_base64)

def hamming_distance(bytearray1, bytearray2):
    bits1 = BitArray(hex=bytearray1.hex())
    bits2 = BitArray(hex=bytearray2.hex())

    hamming_counter = 0

    for i in range(len(bits1)):
        hamming_counter += (int(bits1[i]) ^ int(bits2[i]))

    return hamming_counter

def decipher_repeating_xor(encrypted_bytes, key_range_start, key_range_end):
    normalized_keys = {}

    for key_size in range(key_range_start, key_range_end):
        first_key_size_bytes = encrypted_bytes[:key_size]
        second_key_size_bytes = encrypted_bytes[key_size:(key_size*2)]

        normalized_distance = (hamming_distance(first_key_size_bytes, second_key_size_bytes) / key_size)
        normalized_keys[key_size] = normalized_distance

    key_value_list = sorted(normalized_keys.items(), key=lambda kv: kv[1])
    print(key_value_list)
    keys = [k[0] for k in key_value_list]

    #STEP 5
    for key in keys:
        block_position = 0
        key_block_list = []
        for i in range(math.ceil(len(encrypted_bytes) / key)):
            key_block_list.append(encrypted_bytes[block_position:(block_position + key)])
            block_position += key

        transposed_block_list = []
        for i in range(key):
            transposed_block = bytearray()
            for key_block in key_block_list:
                try:
                    transposed_block.append(key_block[i])
                except:
                    continue
            transposed_block_list.append(transposed_block)

        multibyte_key = ""
        for transposed_block in transposed_block_list:
            multibyte_key += decipher_single_byte_xor(transposed_block)

        decrypted_msg = clean_repeating_xor(encrypted_bytes, multibyte_key)
        print("key: " + multibyte_key + "\ndecrypted message: " + decrypted_msg)
        print("\n--------------------------------------------------------------\n")


decipher_repeating_xor(encrypted_bytes, 2,41)