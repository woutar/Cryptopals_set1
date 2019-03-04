from challenge3 import decipher_single_byte_xor

xor_strings = open("xor_strings.txt").readlines()

for i in range(len(xor_strings)):
    xor_strings[i] = xor_strings[i].replace('\n', '')

for hex_string in xor_strings:
    decipher_single_byte_xor(hex_string)


