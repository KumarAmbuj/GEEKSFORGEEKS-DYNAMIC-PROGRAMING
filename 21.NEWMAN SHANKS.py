def newmanshank(n):
    dp=[0 for i in range(n+1)]
    dp[0]=1
    dp[1]=1

    for i in range(2,n+1):
        dp[i]=2*dp[i-1]+dp[i-2]
    print(dp[n])
    print(dp)

newmanshank(6)