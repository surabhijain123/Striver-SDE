def longest_pallindrome(s):
    if s == '':
        return 0
    longest = s[0]
    dp = [[False for i in range(len(s))] for j in range(len(s))]
    for i in range(len(s)):
        dp[i][i] = True
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            dp[i-1][i] = True
            longest = s[i]+s[i]
            
    for i in range(len(s) - 3, -1, -1):
        for j in range(i+2, len(s)):
            if dp[i+1][j-1] and s[i] == s[j]:
                dp[i][j] =True
                if len(longest) < (j - i + 1):
                    longest = s[i:j+1]
    return longest
print(longest_pallindrome("cbbd"))