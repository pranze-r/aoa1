def matrix_chain_order(p):

    n = len(p) - 1

    
    dp = [[0] * (n + 1) for _ in range(n + 1)]

    
    for L in range(2, n + 1):

        for i in range(1, n - L + 2):

            j = i + L - 1

            dp[i][j] = float('inf')

            # Try every possible split
            for k in range(i, j):

                cost = (
                    dp[i][k]
                    + dp[k + 1][j]
                    + p[i - 1] * p[k] * p[j]
                )

                if cost < dp[i][j]:
                    dp[i][j] = cost

    return dp[1][n]


dimensions = [10, 30, 5, 60]

print(
    "Minimum Multiplication Operations:",
    matrix_chain_order(dimensions)
)