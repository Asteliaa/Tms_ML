import numpy as np

A = {
    1: np.array([[1, 2, 4],
                 [7, 5, -2],
                 [-2, 1, 3]]),
    2: np.array([[0, 3, 4],
                 [-7, 1, -2],
                 [2, -1, 3]]),
    3: np.array([[5, 2, 9],
                 [7, 0, -2],
                 [-2, 1, 6]]),
    4: np.array([[1, -2, 8],
                 [7, 5, -2],
                 [-2, 3, 0]]),
    5: np.array([[9, 2, 4],
                 [7, 5, -5],
                 [6, -2, 3]])
}

B = {
    1: np.array([[-1, 0, 3],
                 [2, -6, 1],
                 [-7, 1, 5]]),
    2: np.array([[1, 2, 4],
                 [7, 0, -2],
                 [-3, -2, 5]]),
    3: np.array([[1, -2, 1],
                 [7, 5, -2],
                 [-2, 8, 3]]),
    4: np.array([[0, 2, 4],
                 [1, -3, -2],
                 [-2, 1, 3]]),
    5: np.array([[8, 2, 4],
                 [0, 1, -3],
                 [-2, 1, 6]])
}

C = {
    1: np.array([[-2, 3],
                 [4, 0],
                 [7, -1]]),
    2: np.array([[-3, 2],
                 [0, 4],
                 [-1, 7]]),
    3: np.array([[-2, 3],
                 [4, 5],
                 [0, -1]]),
    4: np.array([[0, 3],
                 [5, -4],
                 [7, -1]]),
    5: np.array([[-2, 0],
                 [4, 8],
                 [1, -1]])
}

def solve(A, B, C, set_number):
    print(f"Для набора №{set_number}")

    print("\n1) A + B:")
    print(A + B)

    print("\n2) B - A:")
    print(B - A)

    print("\n3) A * C:")
    print(A.dot(C))

    print("\n4) A * B * C:")
    print(A.dot(B).dot(C))


print("Доступные наборы: 1, 2, 3, 4, 5")
choice = int(input("Введите номер набора: "))

if choice in A:
    solve(A[choice], B[choice], C[choice], f"№{choice}")
else:
    print(f"Набор с таким номером отсутствует")
