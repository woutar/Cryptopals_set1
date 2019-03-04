string1 = "1c0111001f010100061a024b53535009181c"
string2 = "686974207468652062756c6c277320657965"
result_string = "746865206b696420646f6e277420706c6179"

bytearray1 = bytes.fromhex(string1)
bytearray2 = bytes.fromhex(string2)

xor_result = bytearray(len(bytearray1))
for i in range(len(bytearray1)):
    xor_result[i] = bytearray1[i] ^ bytearray2[i]

print("created: " + xor_result.hex() + "\n" + "expected result: " + result_string)
