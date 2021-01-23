def findmaxsegment(n,a,b,c):
    dp=[None for i in range(n+1)]
    dp[0]=0

    for i in range(1,len(dp)):
        mx=None
        if i>=a and dp[i-a]!=None:
            mx=dp[i-a]
        if i>=b and dp[i-b]!=None:
            if mx!=None:
                mx=max(mx,dp[i-b])
            else:
                mx=dp[i-b]
        if i>=c and dp[i-c]!=None:
            if mx!=None:
                mx=max(mx,dp[i-c])
            else:
                mx=dp[i-c]
        if mx!=None:
            dp[i]=mx+1
    print(dp[n])




findmaxsegment(8,5,2,5)

findmaxsegment(17,2,1,3)





