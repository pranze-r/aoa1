def longest_common_subsequence(text1, text2):

    m = len(text1)
    n = len(text2)

    
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    
    for i in range(1, m + 1):

        for j in range(1, n + 1):

            if text1[i - 1] == text2[j - 1]:

                dp[i][j] = 1 + dp[i - 1][j - 1]

            else:

                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    
    lcs_chars = []

    i = m
    j = n

    while i > 0 and j > 0:

        if text1[i - 1] == text2[j - 1]:

            lcs_chars.append(text1[i - 1])

            i -= 1
            j -= 1

        elif dp[i - 1][j] > dp[i][j - 1]:

            i -= 1

        else:

            j -= 1

    lcs_str = "".join(reversed(lcs_chars))

    return dp[m][n], lcs_str


seq1 = "BATMAN"
seq2 = "CATWOMAN"

length, sequence = longest_common_subsequence(seq1, seq2)

print("LCS Length:", length)
print("Subsequence:", sequence)