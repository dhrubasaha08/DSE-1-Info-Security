import sys


def main():
    print("""Rail-Fence Encryption/Decryption
    1. Encrypt
    2. Decrypt
    3. Exit""")
    choice = input("choice: ")
    if choice == str(1):
        encrypt()
    elif choice == str(2):
        decrypt()
    elif choice == str(3):
        sys.exit()
    else:
        print("Invalid option")
        main()


def encrypt():
    print("Encrypt")
    text = input("String: ")
    key = int(input("Key: "))
    print("Encrypted String: ", end="")
    rail = [["\n" for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0
    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down
        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != "\n":
                result.append(rail[i][j])
    print("".join(result))
    main()


def decrypt():
    print("Decrypt")
    text = input("String: ")
    key = int(input("Key: "))
    print("Decrypted String: ", end="")
    rail = [["\n" for i in range(len(text))] for j in range(key)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = "*"
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(key):
        for j in range(len(text)):
            if (rail[i][j] == "*") and (index < len(text)):
                rail[i][j] = text[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(text)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        if rail[row][col] != "*":
            result.append(rail[row][col])
            col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    print("".join(result))
    main()


main()
