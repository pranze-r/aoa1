def bad_char_heuristic(pattern, size):
    bad_char = [-1] * 256
    for i in range(size):
        bad_char[ord(pattern[i])] = i
    return bad_char

def boyer_moore_search(text, pattern):
    text_lower, pattern_lower = text.lower(), pattern.lower()
    n, m = len(text_lower), len(pattern_lower)
    bad_char = bad_char_heuristic(pattern_lower, m)
    s = 0
    found = False

    while s <= (n - m):
        j = m - 1
        
        while j >= 0 and pattern_lower[j] == text_lower[s + j]:
            j -= 1
            
        if j < 0:
            print(f"Pattern found at index {s}")
            found = True
            s += (m - bad_char[ord(text_lower[s + m])] if s + m < n else 1)
        else:
            s += max(1, j - bad_char[ord(text_lower[s + j])])
            
    if not found:
        print("Pattern not found in the text.")

print("--- Boyer-Moore String Matching ---")
user_text = input("Enter the main text: ")
user_pattern = input("Enter the pattern to search: ")
boyer_moore_search(user_text, user_pattern)