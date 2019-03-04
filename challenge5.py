plain_text = "Burning 'em, if you ain't quick and nimble\nI go crazy when I hear a cymbal"
key = "ICE"
expected_result = "0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f"

def repeating_xor(text, key, expected_result):
    extended_key = ((key * len(text))[:len(text)])
    encoded_text = text.encode()
    encoded_key = extended_key.encode()
    encrypted_msg = bytearray(len(encoded_text))

    for i in range(len(encoded_text)):
        encrypted_msg[i] = encoded_text[i] ^ encoded_key[i]

    if encrypted_msg.hex() == expected_result:
        return "correct!"
    else:
        return "encrypted message not correct \n" + "encrypred_result: " + encrypted_msg.hex() + "\n expected result: " + expected_result

# print(repeating_xor(plain_text, key,expected_result))


def clean_repeating_xor(encoded_string, key):
    extended_key = ((key * len(encoded_string))[:len(encoded_string)])
    encoded_key = extended_key.encode()
    decrypted_msg = bytearray(len(encoded_string))

    for i in range(len(encoded_string)):
        decrypted_msg[i] = encoded_string[i] ^ encoded_key[i]

    return decrypted_msg.decode()
