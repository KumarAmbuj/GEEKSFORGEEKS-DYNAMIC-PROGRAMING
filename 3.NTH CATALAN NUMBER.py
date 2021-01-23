def nthcatalan(x):
    dp=[0 for i in range(x)]

    dp[0]=1
    dp[1]=1

    for i in range(2,len(dp)):
        m=0
        n=i-1
        sum=0
        while(m<=n):
            if m==n:
                sum+=(dp[m]*dp[n])
            else:
                sum+=(2*(dp[m]*dp[n]))

            m+=1
            n-=1
        dp[i]=sum
    print(dp[x-1])

nthcatalan(10)
