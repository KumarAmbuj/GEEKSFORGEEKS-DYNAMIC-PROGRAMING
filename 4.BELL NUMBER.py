def findBellno(n):
    dp=[[0 for j in range(n)] for i in range(n)]

    dp[0][0]=1

    for i in range(1,len(dp)):

        dp[i][0]=dp[i-1][i-1]
        for j in range(1,i+1):
            dp[i][j]=dp[i][j-1]+dp[i-1][j-1]
    print(dp[n-1][n-1])
findBellno(5)
