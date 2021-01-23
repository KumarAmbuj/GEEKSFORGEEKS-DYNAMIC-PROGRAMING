def findncrmodulop(n,r,p):
    dp=[[0 for j in range(n+1)] for i in range(r+1) ]


    for i in range(len(dp)):
        for j in range(len(dp[0])):

            if j==0:
                dp[i][j]=0
            elif i==0:
                dp[i][j]=1%p
            elif i==1:
                dp[i][j]=j%p
            elif i==j:
                dp[i][j]=1%p
            elif i>j:
                dp[i][j]=0
            elif i<j:
                dp[i][j]=(dp[i][j-1]+dp[i-1][j-1])%p
    print(dp[r][n])

findncrmodulop(10,2,13)