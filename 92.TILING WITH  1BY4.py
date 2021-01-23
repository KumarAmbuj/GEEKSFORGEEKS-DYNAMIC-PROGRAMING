def findways(n):
    dp=[0 for i in range(n+1)]
    dp[1]=1

    for i in range(2,n+1):
        if i<4:
            dp[i]=1
        elif i==4:
            dp[i]=2
        else:
            dp[i]=dp[i-1]+dp[i-4]
    print(dp[n])

findways(5)