def findmaxsum(arr,k):
    dp=[0 for i in range(len(arr))]
    arr.sort()
    dp[0]=0

    for i in range(1,len(arr)):
        dp[i]=dp[i-1]

        if (arr[i]-arr[i-1])<k:
            dp[i]=max(dp[i],(dp[i-2] if i>=2 else 0)+arr[i]+arr[i-1])

    print(dp[len(arr)-1])
    print(dp)

arr=[3, 5, 10, 15, 17, 12, 9]
k=4
findmaxsum(arr,k)

arr=[5, 15, 10, 300]
findmaxsum(arr,12)