def findmoserdebruijn(n):
    dp=[0 for i in range(n+1)]
    dp[0]=0
    dp[1]=1

    i=2
    ele=1
    next=2
    s=1
    while(i<(n+1)):

        if i==next:
            s=1
            ele=ele*4
            dp[i]=ele
            next=next*2
        else:
            dp[i]=dp[s]+ele
            s+=1
        i+=1
    print(dp)
findmoserdebruijn(5)
findmoserdebruijn(9)





