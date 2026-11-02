def rod_cutting(prices, n):

    # dp[i] stores maximum profit for rod length i
    dp = [0] * (n + 1)

    for i in range(1, n + 1):

        max_val = -1

        # Try every possible first cut
        for j in range(1, i + 1):

            max_val = max(
                max_val,
                prices[j - 1] + dp[i - j]
            )

        dp[i] = max_val

    return dp[n]


prices = [1, 5, 8, 9]
rod_length = 4

print("Maximum Profit:", rod_cutting(prices, rod_length))