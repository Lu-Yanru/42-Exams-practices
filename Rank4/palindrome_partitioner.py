# Dynamic programming


def palindrome_partitioner(s: str) -> int:
    """
    Returns the minimum number of cuts to partition s into palindromic substrings.
    Uses two DP tables: one for palindrome membership, one for minimum cuts.
    Time: O(n^2) | Space: O(n^2)
    """

    # --- Edge cases ---

    # An empty string needs no cuts by definition (problem spec).
    if not s:
        return 0

    n = len(s)

    # A single character is already a palindrome — no cut needed.
    if n == 1:
        return 0

    # --- Table 1: Palindrome membership ---
    # is_pal[i][j] = True if s[i..j] (inclusive) is a palindrome.
    # We initialise everything to False; we'll fill it via DP.
    is_pal = [[False] * n for _ in range(n)]

    # Every single character is trivially a palindrome.
    for i in range(n):
        is_pal[i][i] = True

    # Every pair of identical adjacent characters is a palindrome.
    # e.g. "aa" → True, "ab" → False
    for i in range(n - 1):
        is_pal[i][i + 1] = (s[i] == s[i + 1])

    # Fill substrings of length 3 up to n using previously computed results.
    # Outer loop: substring length (3, 4, ..., n)
    for length in range(3, n + 1):
        # Inner loop: starting index i
        for i in range(n - length + 1):
            j = i + length - 1          # ending index j

            # s[i..j] is a palindrome iff the outer chars match AND
            # the inner substring s[i+1..j-1] is also a palindrome
            # (already computed because it's shorter).
            is_pal[i][j] = (s[i] == s[j]) and is_pal[i + 1][j - 1]

    # --- Table 2: Minimum cuts for prefix s[0..i] ---
    # min_cuts[i] = minimum cuts to partition s[0..i] into palindromes.
    # Worst case: cut between every character → (i) cuts for prefix of length i+1.
    min_cuts = list(range(n))  # min_cuts[i] initialised to i (worst case)

    for i in range(1, n):       # i = last index of the current prefix

        # If the entire prefix s[0..i] is already a palindrome,
        # zero cuts are needed — no further search required.
        if is_pal[0][i]:
            min_cuts[i] = 0
            continue

        # Try every possible last segment s[j..i].
        # If s[j..i] is a palindrome, we can cut just before index j.
        # The cost is: min_cuts[j-1] (best cost for s[0..j-1]) + 1 (this cut).
        for j in range(1, i + 1):
            if is_pal[j][i]:
                min_cuts[i] = min(min_cuts[i], min_cuts[j - 1] + 1)

    # The answer is the minimum cuts needed for the full string s[0..n-1].
    return min_cuts[n - 1]


# ---------------------------------------------------------------------------
# Quick self-tests (no external library required)
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    cases = [
        ("",            0),   # empty string
        ("a",           0),   # single char
        ("aa",          0),   # already a palindrome
        ("ab",          1),   # "a" | "b"
        ("aab",         1),   # "aa" | "b"
        ("abcba",       0),   # entire string is a palindrome
        ("abcbad",      1),   # "abcba" | "d"
        ("abacaba",     0),   # entire string is a palindrome
        ("racecar",     0),   # classic palindrome
        ("aababaaab",   2),   # "aababaa|a|b"
        ("abcd",        3),   # all different
        ("aaabaaaba",   1),   # aa|abaaaba
    ]

    all_passed = True
    for s, expected in cases:
        result = palindrome_partitioner(s)
        status = "PASS" if result == expected else "FAIL"
        if status == "FAIL":
            all_passed = False
        print(f"[{status}] palindrome_partitioner({s!r:20}) = {result}  (expected {expected})")

    print("\nAll tests passed." if all_passed else "\nSome tests FAILED — review above.")
