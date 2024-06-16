import numpy as np


def encrypt_message(message, key_matrix):
    message_vector = np.array([ord(char) for char in message])
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diaogonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(eigenvalues)), np.linalg.inv(eigenvectors))
    encrypted_vector = np.dot(diaogonalized_key_matrix, message_vector)
    return encrypted_vector


def decrypt_message(encrypted_vector, key_matrix):
    eigenvalues, eigenvectors = np.linalg.eig(key_matrix)
    diagonalized_key_matrix = np.dot(np.dot(eigenvectors, np.diag(1 / eigenvalues)), np.linalg.inv(eigenvectors))
    decrypted_vector = np.dot(diagonalized_key_matrix, encrypted_vector)
    decrypted_message = ''.join(chr(int(np.round(np.real(val)))) for val in decrypted_vector)
    return decrypted_message


def main():
    message = "SKIBIDI DOP DOP DOP YES YES"
    print("Original message: ", message)
    key_matrix = np.random.randint(0, 256, (len(message), len(message)))
    encrypted_message = encrypt_message(message, key_matrix)
    print("\nEncrypted message: ", encrypted_message)
    print("\nDecrypted message: ", decrypt_message(encrypted_message, key_matrix))


main()

