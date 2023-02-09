#Implement the code of encryption of shift cipher with key value = 5.


def main():
    print("Enter plaintext: ")
    plaintext = input()
    key = 5
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