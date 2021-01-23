def findmintime(n,insert,remove,copy):
    dp=[0 for i in range(n+1)]

    for i in range(1,n+1):
        if i%2==0:

            dp[i]=min(dp[i-1]+insert,dp[i//2]+copy)
        else:
            dp[i]=min(dp[i-1]+insert,dp[(i+1)//2]+copy+remove)

    print(dp[n])

findmintime(9,1,2,1)