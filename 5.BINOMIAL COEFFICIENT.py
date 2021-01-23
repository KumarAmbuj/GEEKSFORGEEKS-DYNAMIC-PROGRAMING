def findBinomialCoefficient(n,k):
    dp=[[0 for i in range(n+1)] for k in range(k+1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):

            if j==0:
                dp[i][j]=0
            elif i==0:
                dp[i][j]=1
            elif i==1:
                dp[i][j]=j
            elif i==j:
                dp[i][j]=1
            elif i>j:
                dp[i][j]=0
            elif i<j:
                dp[i][j]=dp[i][j-1]+dp[i-1][j-1]

    print(dp[k][n])

findBinomialCoefficient(5,2)
