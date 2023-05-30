# Internal 02
# Dhruba Saha


import random
import sys
from collections import Counter


def encrypt(text, shift):

    salt = random.randint(1, 25)

    shift += salt
    e = chr(salt+65)
    result = ""

    v_shift = shift
    variable_shift_counter = 0

    for i in range(len(text)):
        char = text[i]

        variable_shift = result+str(char)
        variable_shift_data = Counter(variable_shift)

        variable_shift_counter += variable_shift_data[char]
        
        if variable_shift_counter > 1:
            v_shift *= variable_shift_counter

            if (char.isupper()):
                result += chr(((ord(char)) + v_shift - 65) % 26 + 65)

            else:
                result += chr(((ord(char)) + v_shift - 97) % 26 + 97)

        else:
            if (char.isupper()):
                result += chr(((ord(char)) + shift - 65) % 26 + 65)

            else:
                result += chr(((ord(char)) + shift - 97) % 26 + 97)

    result = e + result

    return result


def decrypt(text, shift):
    
        salt = ord(text[0])-65
        shift += salt
        result = ""
    
        v_shift = shift
        variable_shift_counter = 0
    
        for i in range(1, len(text)):
            char = text[i]
    
            variable_shift = result+str(char)
            variable_shift_data = Counter(variable_shift)
    
            variable_shift_counter += variable_shift_data[char]
            
            if variable_shift_counter > 1:
                v_shift *= variable_shift_counter
    
                if (char.isupper()):
                    result += chr(((ord(char)) - v_shift - 65) % 26 + 65)
    
                else:
                    result += chr(((ord(char)) - v_shift - 97) % 26 + 97)
    
            else:
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