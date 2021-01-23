def makeincreasing(arr):
    dp=[0 for i in range(len(arr))]
    for i in range(len(arr)):
        mx=0

        for j in range(i):
            if arr[j]<arr[i]:
                mx=max(mx,dp[j])
        dp[i]=mx+1

    mx=0
    for i in range(len(arr)):
        mx=max(mx,dp[i])

    ans=len(arr)-mx
    print(ans)

arr=[ 1, 2, 6, 5, 4]
makeincreasing(arr)

arr=[ 1, 2, 3, 5, 7, 11]
makeincreasing(arr)


