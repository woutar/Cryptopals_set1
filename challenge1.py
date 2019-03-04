import base64
hexstring = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
base64string = "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t"

bytes = bytes.fromhex(hexstring)
encoded_result = base64.b64encode(bytes)
print("created: " + encoded_result.decode() + "\n" + "expected result: " + base64string)

