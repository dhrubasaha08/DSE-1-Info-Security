#Implement the code of encryption of shift cipher where we can put the key value manually.Implement
#the code of encryption of row column transposition cipher.


def main():
    print("Enter plaintext: ")
    plaintext = input()
    print("Enter key: ")
    key = input()
    print("Encrypted text: ")
    encrypt(plaintext, key)


def encrypt(plaintext, key):
    ciphertext = ""
    for i in plaintext:
        if i.isupper():
            ciphertext += chr((ord(i) + int(key) - 65) % 26 + 65)
        elif i.islower():
            ciphertext += chr((ord(i) + int(key) - 97) % 26 + 97)
        else:
            ciphertext += i
    print(ciphertext)
    

main()