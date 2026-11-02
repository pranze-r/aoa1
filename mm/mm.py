import timeit

def matrix_multiply(A, B):
    return [
        [
            sum(A[i][k] * B[k][j] for k in range(len(B)))
            for j in range(len(B[0]))
        ]
        for i in range(len(A))
    ]

# Input dimensions
rA, cA = map(int, input("Enter rows and columns of A: ").split())
rB, cB = map(int, input("Enter rows and columns of B: ").split())

if cA != rB:
    print("Matrix multiplication is not possible.")
else:
    print("Enter Matrix A:")
    A = [list(map(int, input().split())) for _ in range(rA)]

    print("Enter Matrix B:")
    B = [list(map(int, input().split())) for _ in range(rB)]

    result = matrix_multiply(A, B)

    print("Result:")
    for row in result:
        print(row)

    execution_time = timeit.timeit(
        lambda: matrix_multiply(A, B),
        number=10000
    )

    print("Execution time:", execution_time)