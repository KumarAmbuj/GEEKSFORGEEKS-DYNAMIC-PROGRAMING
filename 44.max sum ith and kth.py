def findmaxsum(arr,i,k):
    dp=[0 for i in range(len(arr))]

    for m in range(i+1):
        mx=0
        for n in range(m):
            if arr[n]<arr[m] and arr[n]<arr[k]:
                mx=max(mx,dp[n])
        if arr[m]<arr[k]:
            dp[m]=mx+arr[m]
        else:
            dp[m]=dp[m-1]

    sum=dp[i]+arr[k]
    print(sum)

arr = [1, 101, 2, 3, 100, 4, 5]
findmaxsum(arr,4,6)

arr = [1, 101, 2, 3, 100, 4, 5]
findmaxsum(arr,2,5)


