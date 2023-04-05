#Implement the code of encryption of affine cipher.


def main():
    print("Enter plaintext: ")
    plaintext = input()
    print("Enter key 1: ")
    key1 = int(input())
    print("Enter key 2: ")
    key2 = int(input())
    print("Encrypted text: ")
    encrypt(plaintext, key1, key2)


def encrypt(plaintext, key1, key2):
    ciphertext = ""
    for i in plaintext:
        if i.isupper():
            ciphertext += chr((key1 * (ord(i) - 65) + key2) % 26 + 65)
        elif i.islower():
            ciphertext += chr((key1 * (ord(i) - 97) + key2) % 26 + 97)
        else:
            ciphertext += i
    print(ciphertext)


main()