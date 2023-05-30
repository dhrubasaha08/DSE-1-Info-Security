'''
this is an encryption algorithm and it takes input as encrypt('text',[17,20])
write a decryption algorithm. Use Extended Euclidean Algorithm
 for finding modular inverse. So you have to keep in mind wheather 
 modular inverse exists or not.
'''
# Assignment 02
# Dhruba Saha


import sys


def encrypt(text, key):

    return ''.join([chr(((key[0]*(ord(t) - ord('A')) + key[1]) % 26)
                        + ord('A')) for t in text.upper().replace(' ', '')])


def decrypt(text, key):

    a_inv = 0
    flag = 0
    for i in range(26):
        x = 1 + i * 26
        if x % key[0] == 0:
            a_inv = int(x / key[0])
            flag = 1
            break

    if flag == 0:
        print("Modular inverse doesn't exist")
        sys.exit()
    else:
        return ''.join([chr(((a_inv*(ord(c) - ord('A') - key[1])) % 26) + ord('A'))
                        for c in text.upper().replace(' ', '')])


def main():
    print("Assignment 02 Encryption/Decryption")
    print("""1. Encrypt
2. Decrypt
3. Exit""")
    choice = input("choice: ")
    if choice == str(1):
        text = input("String: ")
        key = [int(x) for x in input("Key: ").split(',')]
        print("Encrypted String: ", encrypt(text, key))
    elif choice == str(2):
        text = input("String: ")
        key = [int(x) for x in input("Key: ").split(' ')]
        print("Decrypted String: ", decrypt(text, key))
    elif choice == str(3):
        sys.exit()
    else:
        print("Invalid option")
        main()


main()