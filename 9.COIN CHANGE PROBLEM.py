def findcoinchangeproblem(n,coins):
    dp=[0 for i in range(n+1)]

    dp[0]=1

    for i in range(1,len(dp)):
        ans=0
        for j in range(len(coins)):
            if i>=coins[j]:
                ans+=dp[i-coins[j]]
        dp[i]=ans

    print(dp[n])

findcoinchangeproblem(4,[1,2,3])
