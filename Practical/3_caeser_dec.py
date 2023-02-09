#Implement the code of decryption of ceasar cipher with key value = 5.


def main():
    print("Enter ciphertext: ")
    plaintext = input()
    key = 5
    print("Decrypted text: ")
    decrypt(plaintext, key)


def decrypt(ciphertext, key):
    plaintext = ""
    for i in ciphertext:
        if i.isupper():
            plaintext += chr((ord(i) - int(key) - 65) % 26 + 65)
        elif i.islower():
            plaintext += chr((ord(i) - int(key) - 97) % 26 + 97)
        else:
            plaintext += i
    print(plaintext)
    

main()