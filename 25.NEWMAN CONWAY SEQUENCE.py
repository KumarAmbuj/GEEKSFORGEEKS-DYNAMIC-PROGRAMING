def newmanconway(n):

    dp=[0 for i in range(n+1)]
    dp[1]=1
    dp[2]=1

    for i in range(3,n+1):
        dp[i]=dp[dp[i-1]]+dp[i-dp[i-1]]

    print(dp[n])


newmanconway(2)
newmanconway(10)