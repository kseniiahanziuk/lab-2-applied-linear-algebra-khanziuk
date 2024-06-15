import numpy as np


def eigen_decomposition(matrix):
    eigenvalues, eigenvectors = np.linalg.eig(matrix)

    for i in range(len(eigenvalues)):
        a_v = np.dot(matrix, eigenvectors[:, i])
        lambda_v = eigenvalues[i] * eigenvectors[:, i]
        if np.allclose(a_v, lambda_v):
            print(f"\nEigenvector №{i + 1}: A⋅v is equal to λ⋅v\n")
        else:
            print(f"\nEigenvalue №{i + 1}: A⋅v is not equal to λ⋅v\n")

    normalized_eigenvectors = np.zeros_like(eigenvectors)
    for i in range(len(eigenvectors)):
        norm = np.linalg.norm(eigenvectors[:, i])
        normalized_eigenvectors[:, i] = eigenvectors[:, i] / norm

    return eigenvalues, normalized_eigenvectors


def read_matrix():
    n = int(input("Enter the size of the matrix: "))

    matrix = []

    print("Enter the matrix row numbers one by one(using space):")
    for i in range(n):
        row = list(map(float, input(f"Row {i + 1}: ").split()))
        matrix.append(row)

    return np.array(matrix)


def main():
    matrix = read_matrix()

    eigenvalues, normalized_eigenvectors = eigen_decomposition(matrix)
    print("\nEigenvalues: \n", eigenvalues)
    print("\nEigenvectors: \n", normalized_eigenvectors)


main()
