#applicaton of catalan no


def findways(n):

    dp=[0 for i in range(n+1)]

    dp[0]=1
    dp[1]=1
    for i in range(2,n+1):

        l=0
        r=i-1

        while(r>=0):
            dp[i]+=dp[l]*dp[r]
            l+=1
            r-=1

    print(dp[n])
findways(3)