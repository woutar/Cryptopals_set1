from functools import reduce
hexstring = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"

letter_frequency_table = {
    'a' : 0.0812, 'b' : 0.0149, 'c' : 0.0271,
    'd' : 0.0432, 'e' : 0.1202, 'f' : 0.0230,
    'g' : 0.0203, 'h' : 0.0592, 'i' : 0.0732,
    'j' : 0.0010, 'k' : 0.0069, 'l' : 0.0398,
    'm' : 0.0261, 'n' : 0.0695, 'o' : 0.0768,
    'p' : 0.0182, 'q' : 0.0011, 'r' : 0.0602,
    's' : 0.0628, 't' : 0.0910, 'u' : 0.0288,
    'v' : 0.0111, 'w' : 0.0209, 'x' : 0.0017,
    'y' : 0.0211, 'z' : 0.0007, ' ' : 0.1300
}

def english_checker(encoded_string):
    letter_count = {}
    for i in encoded_string:
        # if character is a readable ascii character, else stop function
        if 32 <= i <= 126 or i == 10:
            # if character excists in the frequency table add it to the letter_count hashmap, else go to the next char
            if chr(i).lower() in letter_frequency_table:
                if chr(i).lower() in letter_count:
                    letter_count[chr(i).lower()] += 1
                else:
                    letter_count[chr(i).lower()] = 1
            else:
                continue
        else:
            return

    for letter in letter_count:
        letter_frequency = letter_count[letter] / reduce((lambda x, y : x + y), letter_count.values())

        # if the letter frequency is outside of the range (25% offset) of the frequency table, stop function
        if letter_frequency >= (letter_frequency_table[letter] + 0.25):
            return
    # encoded string can be seen as "sufficient" english
    return encoded_string

def letter_scoring(encoded_string):
    score = 0
    for i in encoded_string:
        if chr(i).lower() in letter_frequency_table:
            score += letter_frequency_table[chr(i).lower()]

    return score


#Old method uses English frequency method
def decipher_single_byte_xor_old(encoded_string):
    possible_results = []

    #try to decipher the encrypted string with all ascii characters (0-256)
    for key in range(0,256):
        xor_result = bytearray(len(encoded_string))
        for i in range(len(encoded_string)):
            xor_result[i] = encoded_string[i] ^ key

        if english_checker(xor_result) != None:
            possible_results.append("message: " + english_checker(xor_result).decode('utf-8') + " key: " + chr(key))

    for possible_result in possible_results:
        print(possible_result)


# decipher_single_byte_xor_old(bytes.fromhex(hexstring))

#New method uses Letter scoring
def decipher_single_byte_xor(encoded_string):
    possible_results = []

    # try to decipher the encrypted string with all ascii characters (0-256)
    for key in range(0, 256):
        xor_result = bytearray(len(encoded_string))
        for i in range(len(encoded_string)):
            xor_result[i] = encoded_string[i] ^ key

        possible_result = (chr(key), letter_scoring(xor_result))
        possible_results.append(possible_result)

    possible_results.sort(key=lambda kv:kv[1])
    return (possible_results[-1][0])

# decipher_single_byte_xor(bytes.fromhex(hexstring))






