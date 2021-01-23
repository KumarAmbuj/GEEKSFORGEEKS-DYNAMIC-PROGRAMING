def RecursivelyBreakNumber(n):
    dp=[0 for i in range(n+1)]

    for i in range(1,n+1):
        dp[i]=max(i,dp[i//2]+dp[i//3]+dp[i//4])
    print(dp[n])

RecursivelyBreakNumber(12)
RecursivelyBreakNumber(24)
RecursivelyBreakNumber(23)
