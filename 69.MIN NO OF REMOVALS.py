def findminremoval(arr,k):
    dp=[0 for i in range(len(arr))]

    for i in range(len(arr)):
        mx=0
        for j in range(i):

            if abs(arr[i]-arr[j])<=k:
                mx+=1
        dp[i]=mx+1

    mx=0
    for i in range(len(arr)):
        mx=max(mx,dp[i])
    ans=len(arr)-mx
    print(ans)
a = [1, 3, 4, 9, 10, 11, 12, 17, 20]
k = 4

findminremoval(a,k)


a = [1, 5, 6, 2, 8]
k = 2

findminremoval(a,k)
