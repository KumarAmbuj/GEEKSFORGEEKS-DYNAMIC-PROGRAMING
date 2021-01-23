def findmaxvalue(arr):
    arr.insert(0,0)

    dp=[0 for i in range(len(arr))]

    dp[0]=0
    dp[1]=1

    for i in range(2,len(dp)):
        mx=0

        for j in range(1,i+1):
            mx=max(mx,arr[j]+dp[i-j])
        dp[i]=mx

    print(dp[len(arr)-1])
    print(dp)
arr=[1,5,8,9,10,17,17,20]
findmaxvalue(arr)

