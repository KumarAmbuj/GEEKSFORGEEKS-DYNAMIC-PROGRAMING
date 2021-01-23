def findallpath(m,n):
    dp=[[0 for i in range(n)] for j in range(m)]

    
    dp[m-1][n-1]=1

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):

            if i==m-1 and j==n-1:
                dp[i][j]=1
            elif i==m-1:
                dp[i][j]=dp[i][j+1]
            elif j==n-1:
                dp[i][j]=dp[i+1][j]
            else:
                dp[i][j]=dp[i+1][j]+dp[i][j+1]

    print(dp[0][0])
findallpath(2,3)