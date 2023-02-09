#Implement the code of decryption of hill cipher.

import numpy as np


def main():
    ciphertext = "RFQNXL"
    key = [[17, 17, 5], [21, 18, 21], [2, 2, 19]]

    decrypted_plaintext = decrypt(ciphertext, key)
    print("Ciphertext:", ciphertext)
    print("Decrypted Plaintext:", decrypted_plaintext)


def decrypt(ciphertext, key):
    n = len(key)
    m = len(ciphertext)
    if m % n != 0:
        ciphertext += 'A' * (n - m % n)
    ciphertext_matrix = np.array([ord(c) - ord('A') for c in ciphertext]).reshape(-1, n)
    key_inv = np.linalg.inv(key)
    plaintext_matrix = np.matmul(ciphertext_matrix, key_inv) % 26
    plaintext_matrix = np.round(plaintext_matrix).astype(int)
    plaintext = ''.join([chr(c + ord('A')) for c in plaintext_matrix.flatten().tolist()])

    return plaintext[:m]


main()