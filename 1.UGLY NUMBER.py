def findnthugly(n):
    dp=[0 for i in range(n)]
    dp[0]=1
    multiple2=2
    multiple3=3
    multiple5=5
    i2=0
    i3=0
    i5=0
    for i in range(1,n):
        ele=min(multiple2,multiple3,multiple5)
        dp[i]=ele
        if ele==multiple2:
            i2+=1
            multiple2=dp[i2]*2
        if ele==multiple3:
            i3+=1
            multiple3=dp[i3]*3
        if ele==multiple5:
            i5+=1
            multiple5=dp[i5]*5
    print(dp[n-1])

findnthugly(150)