import base64
import binascii


MORSE_DICT = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.',
              'f': '..-.', 'g': '--.', 'h': '....', 'i': '..', 'j': '.---',
              'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---',
              'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-',
              'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--',
              'z': '--..', '0': '-----', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....',
              '7': '--...', '8': '---..', '9': '----.', '.': '.-.-.-',
              ',': '--..--', '?': '..--..', '\'': '.----.', '!': '-.-.--',
              '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
              ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.',
              '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-',
              '@': '.--.-.', ' ': '/'}


def base32decode(encoded):
    word = base64.b32decode(encoded)
    word = word.decode("utf-8")
    return word


def base64decode(encoded):
    word = base64.b64decode(encoded)
    word = word.decode("utf-8")
    return word


def base85decode(encoded):
    word = base64.b85decode(encoded)
    word = word.decode("utf-8")
    return word


def morsedecode(encoded):
    word = ""
    splitLetter = encoded.split("/")
    if len(splitLetter) == 1:
        raise ValueError
    else:
        for letter in splitLetter:
            for k in MORSE_DICT:
                if MORSE_DICT[k] == letter:
                    word = word + k
    return word


def hexToAscii(encoded):
    word = bytearray.fromhex(encoded).decode()
    return word


def encodeDetect(encoded):
    try:
        word = base32decode(encoded)
        print("Base32")
        return word
    except binascii.Error:
        pass
    try:
        word = base64decode(encoded)
        print("Base64")
        return word
    except binascii.Error:
        pass
    except ValueError:
        pass
    try:
        word = base85decode(encoded)
        print("Base85")
        return word
    except binascii.Error:
        pass
    except ValueError:
        pass
    try:
        word = hexToAscii(encoded)
        print("Hex")
        return word
    except ValueError:
        pass
    try:
        word = morsedecode(encoded)
        print("Morse")
        return word
    except ValueError:
        pass
    return "Error"


message = "../-./-.-./---/-./-.-././../...-/.-/-.../.-../-.--"
val = encodeDetect(message)
print(val)
