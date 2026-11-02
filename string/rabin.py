def rabin_karp(text, pattern):
    n = len(text)
    m = len(pattern)

    d = 256
    q = 101

    h = pow(d, m - 1, q)

    p = 0
    t = 0

    
    for i in range(m):
        p = (d * p + ord(pattern[i])) % q
        t = (d * t + ord(text[i])) % q

   
    for i in range(n - m + 1):

        
        if p == t:
            if text[i:i + m] == pattern:
                print("Pattern found at index:", i)

        
        if i < n - m:
            t = (d * (t - ord(text[i]) * h)
                 + ord(text[i + m])) % q

            if t < 0:
                t += q



text = input("Enter the text: ")
pattern = input("Enter the pattern: ")

rabin_karp(text, pattern)