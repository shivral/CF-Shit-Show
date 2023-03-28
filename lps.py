def LPS(S):
        dp = [[0 for x in range(len(S))] for x in range(len(S))]
        
        for i in range(len(S) - 1, -1, -1):
            dp[i][i] = 1;
            for j in range(i + 1, len(S)):
                if S[i] == S[j]:
                    dp[i][j] = dp[i+1][j-1] + 2;
                 
                else:
                    dp[i][j] = max(dp[i+1][j], dp[i][j-1]);
                
            
        return dp[0][S.length()-1];


class Solution:
    def countPalindromicSubsequences(self, s: str) -> int:
    dp=[[0]*len(s) for i in range(len(s))]
    for l in range(len(s)-1,-1,-1):
        dp[l][l]=1
        for r in range(l+1,len(s)):
            if s[l]==s[r]:
                dp[l][r]+=dp[l][r-1]+1+dp[l+1][r]
            else:
                dp[l][r]+=dp[l][r-1]+dp[l+1][r]-dp[l+1][r-1]
        print(dp)
        return 1
