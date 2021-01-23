def golombsequence(n):
    dp=[0 for i in range(n+1)]
    dp[1]=1

    for i in range(2,n+1):
        dp[i]=1+dp[i-dp[dp[i-1]]]

    print(dp[n])

    for i in range(1,len(dp)):
        print(dp[i],end=' ')

golombsequence(9)