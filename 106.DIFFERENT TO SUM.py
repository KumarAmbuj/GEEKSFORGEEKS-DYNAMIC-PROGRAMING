def findsum(n):
    dp=[0 for i in range(n+1)]
    dp[0]=1

    for i in range(1,n+1):
        for j in range(1,i+1):
            dp[i]+=dp[i-j]

    print(dp[n])

findsum(2)