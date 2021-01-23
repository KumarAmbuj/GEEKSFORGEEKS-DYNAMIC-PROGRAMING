def findmaxsum(arr):
    dp=[0 for i in range(len(arr))]
    dp[0]=arr[0]

    for i in range(1,len(arr)):

        a=arr[i]+(dp[i-2] if i>=2 else 0)
        b=arr[i]+arr[i-1]+(dp[i-3] if i>=3 else 0)

        dp[i]=max(a,b)

    print(dp[len(arr)-1])

arr=[100, 1000, 100, 1000, 1]
findmaxsum(arr)
