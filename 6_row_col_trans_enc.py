#Implement the code of encryption of row column transposition cipher.


def main():
    print("Enter plaintext: ")
    plaintext = input()
    print("Encrypted text: ")
    encrypt(plaintext)


def transpose(matrix):
    return [list(i) for i in zip(*matrix)]


def encrypt(plaintext):
    plaintext = plaintext.replace(" ", "")
    matrix = []
    for i in range(0, len(plaintext), 4):
        matrix.append(list(plaintext[i:i+4]))
    matrix = transpose(matrix)
    ciphertext = ""
    for i in matrix:
        ciphertext += "".join(i)
    print(ciphertext)


main()