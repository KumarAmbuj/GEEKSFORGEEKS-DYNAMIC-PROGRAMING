def findmaxlen(arr):
    dp=[0 for i in range(len(arr))]


    for i in range(len(arr)):
        mx=0
        for j in range(i):
            a=abs(arr[j]-arr[i])
            if a==0 or a==1:
                mx=max(mx,dp[j])

        dp[i]=mx+1
    mx=0
    for i in range(len(arr)):
        mx=max(mx,dp[i])
    print(mx)
arr=[2, 5, 6, 3, 7, 6, 5, 8]
findmaxlen(arr)
arr=[-2, -1, 5, -1, 4, 0, 3]
findmaxlen(arr)