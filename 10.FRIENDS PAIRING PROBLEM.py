def FriendPairing(n):
    dp=[0 for i in range(n+1)]

    dp[1]=1
    dp[2]=2

    for i in range(3,len(dp)):
        dp[i]=dp[i-1]+(i-1)*dp[i-2]
    print(dp[n])

FriendPairing(3)