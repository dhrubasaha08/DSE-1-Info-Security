'''
this is an encryption algorithm; please try to understand how it works and
modify it thus it works for integers as well.
'''
# Assignment 01
# Dhruba Saha


import sys


def encrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr(((ord(char)) + shift - 65) % 26 + 65)

        else:
            result += chr(((ord(char)) + shift - 97) % 26 + 97)
    return result


def decrypt(text, shift):
    result = ""

    for i in range(len(text)):
        char = text[i]

        if (char.isupper()):
            result += chr(((ord(char)) - shift - 65) % 26 + 65)

        else:
            result += chr(((ord(char)) - shift - 97) % 26 + 97)
    return result


def main():
    print("Assignment 01 Encryption/Decryption")
    print("""1. Encrypt
2. Decrypt
3. Exit""")
    choice = input("choice: ")
    if choice == str(1):
        text = input("String: ")
        key = int(input("Key: "))
        print("Encrypted String: ", encrypt(text, key))
    elif choice == str(2):
        text = input("String: ")
        key = int(input("Key: "))
        print("Decrypted String: ", decrypt(text, key))
    elif choice == str(3):
        sys.exit()
    else:
        print("Invalid option")
        main()


main()