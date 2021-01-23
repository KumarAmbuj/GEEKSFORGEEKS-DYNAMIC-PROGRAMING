def fibonacci(n):
    dp=[0 for i in range(n)]

    dp[0]=0
    dp[1]=1

    for i in range(2,len(dp)):
        dp[i]=dp[i-1]+dp[i-2]

    print(dp[n-1])

fibonacci(9)