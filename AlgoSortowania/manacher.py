def longest_pali(s, i):
    n = len(s)
    # l = 1
    # if s[i] == "|":
    #     l -= 1
    j = 1
    while i-j >= 0 and i+j < n and s[i-j] == s[i+j]:
        j += 1
    return (j-1)


def manacher(s):
    n = len(s)
    T_S = ["|"]*(n*2+1)
    for i in range(n):
        T_S[i*2+1] = s[i]
    s = "".join(T_S)
    n = n*2+1
    L = [0]*n
    L[0] = 0
    L[1] = 1
    # Legenda
    C = 1  # center position
    R = 2  # center right position
    i = None  # current right postion
    iMirror = 0  # current left postion

    maxLength = 1
    maxCenter = 1

    for i in range(2, n):
        iMirror = 2*C-i
        diff = R-i
        if diff > 0:
            L[i] = min(L[iMirror], diff)

        L[i] = longest_pali(s, i)
        if maxLength < L[i]:
            maxLength = L[i]
            maxCenter = i
        if L[i] + i > R:
            C = i
            R = i+L[i]

    # print(L)
    return max(L)


manacher("aa")


class Solution:
    # Manacher algorithm
    # http://en.wikipedia.org/wiki/Longest_palindromic_substring

    def longestPalindrome(self, s):
        # Transform S into T.
        # For example, S = "abba", T = "^#a#b#b#a#$". # ^ and $ signs are sentinels appended to each end to avoid bounds checking
        T = '#'.join('^{}$'.format(s))
        n = len(T)
        P = [0] * n
        C = R = 0
        for i in range(1, n-1):
            # equals to i' = C - (i-C)
            P[i] = (R > i) and min(R - i, P[2*C - i])
            # Attempt to expand palindrome centered at i
            while T[i + 1 + P[i]] == T[i - 1 - P[i]]:
                P[i] += 1

            # If palindrome centered at i expand past R,
            # adjust center based on expanded palindrome.
            if i + P[i] > R:
                C, R = i, i + P[i]

        # Find the maximum element in P.
        maxLen, centerIndex = max((n, i) for i, n in enumerate(P))
        return len(s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2])

        # return s[(centerIndex - maxLen)//2: (centerIndex + maxLen)//2]


a = Solution()
print(a.longestPalindrome("ababa"))
