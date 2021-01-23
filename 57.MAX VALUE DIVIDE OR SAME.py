def findmax(n):
    dp=[0 for i in range(n+1)]

    for i in range(1,n+1):
        dp[i]=max(dp[i//2]+dp[i//3]+dp[i//4]+dp[i//5],i)
    print(dp[n])

findmax(10)
findmax(2)