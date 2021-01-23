def findways(n,arr):
    dp=[0 for i in range(n+1)]

    dp[0]=1

    for i in range(1,n+1):
        for j in range(len(arr)):
            if (i-arr[j])>=0:
                dp[i]+=dp[i-arr[j]]
    print(dp[n])

arr=[1,5,6]
findways(7,arr)