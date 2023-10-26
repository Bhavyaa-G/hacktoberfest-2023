def longest_palindromic_subsequence(s):
    """
    Find the Longest Palindromic Subsequence (LPS) in a given string.

    Args:
        s (str): The input string for which to find the LPS.

    Returns:
        str: The longest palindromic subsequence.

    Algorithm:
    This program uses dynamic programming to find the LPS.
    1. Create a 2D table to store the length of the LPS for different substrings.
    2. Initialize the table with 1 for single characters.
    3. Iterate over the string, considering all possible substrings of different lengths.
    4. For each substring, check if the characters at both ends are the same.
    5. If they are the same, add 2 to the length of the LPS for that substring.
    6. If they are different, take the maximum of LPS lengths from the two adjacent substrings.
    7. Finally, the bottom-right cell of the table stores the length of the LPS for the entire string.
    8. Backtrack the table to find the actual LPS.

    Example:
    >>> longest_palindromic_subsequence("bbabcbcab")
    "bbabb"

    Note: There can be multiple valid LPS for the same input string.
    """
    n = len(s)
    # Create a table to store LPS lengths for different substrings.
    dp = [[0] * n for _ in range(n)]

    # Initialize the table for single characters.
    for i in range(n):
        dp[i][i] = 1

    # Fill the table for substrings of different lengths.
    for cl in range(2, n + 1):
        for i in range(n - cl + 1):
            j = i + cl - 1
            if s[i] == s[j] and cl == 2:
                dp[i][j] = 2
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1] + 2
            else:
                dp[i][j] = max(dp[i][j - 1], dp[i + 1][j])

    # Backtrack to find the LPS.
    lps = []
    i, j = 0, n - 1
    while i < j:
        if s[i] == s[j]:
            lps.append(s[i])
            i += 1
            j -= 1
        elif dp[i][j] == dp[i + 1][j]:
            i += 1
        else:
            j -= 1

    if i == j:
        lps.append(s[i])

    return ''.join(lps)

# Example usage:
input_string = "bbabcbcab"
lps = longest_palindromic_subsequence(input_string)
print("Longest Palindromic Subsequence:", lps)
