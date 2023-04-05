#implement the code of decryption of affine cipher with the help of modular inverse.


def main():
    print("Enter ciphertext: ")
    ciphertext = input()
    print("Enter key 1: ")
    key1 = int(input())
    print("Enter key 2: ")
    key2 = int(input())
    print("Decrypted text: ")
    decrypt(ciphertext, key1, key2)


def inverse(a, m):
    for i in range(1, m):
        if (a * i) % m == 1:
            return i


def decrypt(ciphertext, key1, key2):
    plaintext = ""
    for i in ciphertext:
        if i.isupper():
            plaintext += chr((inverse(key1, 26) * (ord(i) - 65 - key2)) % 26 + 65)
        elif i.islower():
            plaintext += chr((inverse(key1, 26) * (ord(i) - 97 - key2)) % 26 + 97)
        else:
            plaintext += i
    print(plaintext)
    

main()