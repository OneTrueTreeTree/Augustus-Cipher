import math

alphabet = ["A", "a", "B", "b", "C", "c", "D", "d", "E", "e", "F", "f", "G", "g", "H", "h", "I", "i", "J", "j", "K", "k", "L", "l", "M", "m", "N", "n", "O", "o", "P", "p", "Q", "q", "R", "r", "S", "s", "T", "t", "U", "u", "V", "v", "W", "w", "X", "x", "Y", "y", "Z", "z", " ", ".", ",", "!", "'", "", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

def encrypt(string, key):
    stringlist = [*string]
    encoded = []

    for i in range (0, len(stringlist)):
        if stringlist[i] in alphabet:
            n = alphabet.index(stringlist[i])
            n = (n+int(key)+(i*i)) % len(alphabet)
            encoded.append(alphabet[n])
        else:
            encoded.append(stringlist[i])
    encoded = "".join(encoded)
    return encoded



def decrypt(string, key):
    stringlist = [*string]
    encoded = []

    for i in range (0, len(stringlist)):
        if stringlist[i] in alphabet:
            n = alphabet.index(stringlist[i])
            n = (n-int(key)-(i*i)) % len(alphabet)
            encoded.append(alphabet[n])
        else:
            encoded.append(stringlist[i])
    encoded = "".join(encoded)
    return encoded



def bruteforce(string):
    for a in range (0, len(alphabet)):
        print(decrypt(string, a))


def modify(string, key):
    if not key.isdigit():
        print("⚠️ Invalid key, attempting to use brute force. ⚠️")
        bruteforce(string)
        return

    mode = input("What mode should be used? (e/d)")

    if mode == "e":
        print("Encrypting...")
        print(encrypt(string, key))
    elif mode == "d":
        print("Decrypting...")
        print(decrypt(string, key))
    else:
        print("Invalid input!")

while True:
    string = input("This is a modified and improved Ceasar Cipher. Input string to modify: ")
    key = input("Input a key, or leave blank to attempt brute force: ")
    modify(string, key)
