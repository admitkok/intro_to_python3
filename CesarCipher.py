def ceaser_cipher_encode(text_to_encode, key):
    s = list(text_to_encode.strip())
    res = []
    for i in s:
        x = ord(i)
        if 97 <= x <= 122 - key:
            x = (x + key - 97) % 26 + 97
        elif x > 122 - key:
            x = (x + key - 58 - 65) % 26 + 65
        elif x < 91 - key:
            x = (x + key - 65) % 26 + 65
        else:
            x = abs(x + key + 6 - 97) % 26 + 97
        res.append(chr(x))
    return ''.join(res)


def ceaser_cipher_decode(text_to_decode, key):
    s = list(text_to_decode.strip())
    res = []
    for i in s:
        x = ord(i)
        print(x - key)
        if x - key >= 97:
            x = x - key
        elif 97 <= x < 97 + key:
            x = x - 6 - key
        elif 91 - key < x <= 91:
            x = x - key
        else:
            x = x + 58 - key
        res.append(chr(x))
    return ''.join(res)


print(ceaser_cipher_encode("pIZza", 13))
print(ceaser_cipher_decode("CVmMn", 13))
