def main():
    print("Encryption/Decryption")
    print("""1. Encrypt
2. Decrypt
3. Exit""")
    choice = input("choice: ")
    if choice == str(1):
        encrypt()
    elif choice == str(2):
        decrypt()
    elif choice == str(3):
        exit()
    else:
        print("Invalid option")
        main()


def encrypt():
    print("Encrypt")
    text = input("String: ")
    key = input("Key: ")
    cipher = 0
    print("Encrypted String: ", end="")
    for i in range(len(text)):
        if text[i].isalpha() and text[i].isupper():
            cipher = int(ord(text[i]))+int(key)
            if cipher <= 90:
                print(chr(cipher), end = "")
            elif cipher > 90:
                cipher = (cipher+65)-91
                print(chr(cipher), end = "")
        if text[i].isalpha() and text[i].islower():
            cipher = int(ord(text[i]))+int(key)
            if cipher <= 122:
                print(chr(cipher), end = "")
            elif cipher > 122:
                cipher = (cipher+97)-123
                print(chr(cipher), end = "")
    print("")
    main()


def decrypt():
    print("Decrypt")
    text = input("String: ")
    key = input("Key: ")
    cipher = 0
    print("Decrypted String: ", end="")
    for i in range(len(text)):
        if text[i].isalpha() and text[i].isupper():
            cipher = int(ord(text[i]))-int(key)
            if cipher >= 65:
                print(chr(cipher), end = "")
            elif cipher < 65:
                cipher = 91-(65-cipher)
                print(chr(cipher), end = "")
        if text[i].isalpha() and text[i].islower():
            cipher = int(ord(text[i]))-int(key)
            if cipher >= 97:
                print(chr(cipher), end = "")
            elif cipher < 97:
                cipher = 123-(97-cipher)
                print(chr(cipher), end = "")
    print("")
    main()


main()
