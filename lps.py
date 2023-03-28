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
