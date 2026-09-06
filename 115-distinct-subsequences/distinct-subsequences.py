class Solution:
    def numDistinct(self, s, t):
        m, n = len(s), len(t)
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(m):
            for j in range(n - 1, -1, -1):
                if s[i] == t[j]:
                    dp[j + 1] += dp[j]
                
        return dp[n]

        