'''
Internal 2

Created by
Dhruba Saha
Ritidip Sarkar
Surajit Das
'''

import random
import sys


def encrypt(text, shift):
    salt = random.randint(1, 25)

    shift += salt

    salt_add = chr(salt+65)
    result = ""

    for i in range(len(text)):
        char = text[i]
        shift += salt

        if (char.isupper()):
            result += chr(((ord(char)) + shift - 65) % 26 + 65)

        else:
            result += chr(((ord(char)) + shift - 97) % 26 + 97)

    result = salt_add + result
    return result


def decrypt(text, shift):
    salt = ord(text[0]) - 65
    shift += salt
    result = ""

    for i in range(1, len(text)):
        char = text[i]
        shift += salt

        if (char.isupper()):
            result += chr(((ord(char)) - shift - 65) % 26 + 65)

        else:
            result += chr(((ord(char)) - shift - 97) % 26 + 97)

    return result


def main():
    print("Encryption/Decryption")
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
