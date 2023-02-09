#Implement the code of encryption of hill cipher.

import numpy as np


def main():
    plaintext = "HELLO"
    key = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]

    ciphertext = encrypt(plaintext, key)
    print("Plaintext:", plaintext)
    print("Ciphertext:", ciphertext)


def encrypt(plaintext, key):
    n = len(key)
    m = len(plaintext)
    if m % n != 0:
        plaintext += 'A' * (n - m % n)
    plaintext_matrix = np.array([ord(c) - ord('A') for c in plaintext]).reshape(-1, n)
    key_matrix = np.array(key)
    ciphertext_matrix = np.matmul(plaintext_matrix, key_matrix) % 26
    ciphertext = ''.join([chr(c + ord('A')) for c in ciphertext_matrix.flatten().tolist()])

    return ciphertext


main()