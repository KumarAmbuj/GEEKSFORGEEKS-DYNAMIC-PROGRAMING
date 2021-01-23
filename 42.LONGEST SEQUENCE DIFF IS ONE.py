def findmaxsequence(arr):
    dp=[0 for i in range(len(arr))]

    for i in range(len(arr)):
        mx=0
        for j in range(i):
            if abs(arr[i]-arr[j])==1:
                mx=max(mx,dp[j])
        dp[i]=mx+1

    mx=0
    for i in range(len(arr)):
        mx=max(mx,dp[i])
    print(mx)

arr=[1, 2, 3, 2, 3, 7, 2, 1]
findmaxsequence(arr)

arr=[10, 9, 4, 5, 4, 8, 6]
findmaxsequence(arr)