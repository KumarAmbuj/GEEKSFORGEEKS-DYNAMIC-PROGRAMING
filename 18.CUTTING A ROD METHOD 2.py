def findmaxprice(arr):
    arr.insert(0,0)
    dp=[0 for i in range(len(arr))]

    dp[0]=0
    dp[1]=1

    for i in range(2,len(dp)):
        l=1
        r=i-1
        mx=arr[i]

        while(l<=r):
            mx=max(mx,dp[l]+dp[r])
            l+=1
            r-=1
        dp[i]=mx
    print(dp[len(arr)-1])
    print(dp)
arr=[1,5,8,9,10,17,17,20]
findmaxprice(arr)


