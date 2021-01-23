def findpath(m,n):
    dp=[[0 for i in range(n+1)] for j in range(m+1)]

    dp[0][0]=1

    for i in range(m+1):
        for j in range(n+1):

            if i==0 and j==0:
                dp[i][j]=1
            elif i==0:
                dp[i][j]=dp[i][j-1]

            elif j==0:
                dp[i][j]=dp[i-1][j]

            else:
                dp[i][j]=dp[i-1][j]+dp[i][j-1]

    print(dp[m][n])

findpath(3,6)
findpath(3,0)
