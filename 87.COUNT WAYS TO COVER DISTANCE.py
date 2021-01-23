def findways(n):
    dp=[0 for i in range(n+1)]

    dp[0]=1

    for i in range(1,n+1):

        if i-1>=0:
            dp[i]+=dp[i-1]
        if i-2>=0:
            dp[i]+=dp[i-2]
        if i-3>=0:
            dp[i]+=dp[i-3]

    print(dp[n])

findways(3)
findways(4)