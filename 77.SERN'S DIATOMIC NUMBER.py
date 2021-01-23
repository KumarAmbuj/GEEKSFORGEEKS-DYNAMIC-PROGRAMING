def findsternsNumber(n):
    dp=[0 for i in range(n+1)]
    dp[0]=0
    dp[1]=1

    for i in range(2,n+1):
        if i%2==0:
            dp[i]=dp[i//2]
        else:
            dp[i]=dp[(i-1)//2]+dp[(i+1)//2]
    print(dp[n])

findsternsNumber(7)
findsternsNumber(15)