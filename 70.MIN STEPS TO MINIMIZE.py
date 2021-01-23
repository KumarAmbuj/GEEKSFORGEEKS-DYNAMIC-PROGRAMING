def findminstep(n):
    dp=[0 for i in range(n+1)]
    dp[1]=0

    for i in range(2,len(dp)):
        mn=dp[i-1]

        if i%2==0:
            a=dp[i//2]
            if a<mn:
                mn=a
        if i%3==0:
            a=dp[i//3]
            if a<mn:
                mn=a
        dp[i]=mn+1

    print(dp[n])

findminstep(10)
findminstep(6)

findminstep(5)

