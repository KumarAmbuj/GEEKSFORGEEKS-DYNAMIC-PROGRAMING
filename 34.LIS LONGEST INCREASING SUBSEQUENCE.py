def findlis(arr):
    dp=[0 for i in range(len(arr))]


    for i in range(len(arr)):
        mx=0

        for j in range(i):

            if arr[j]<arr[i]:
                mx=max(mx,dp[j])

        dp[i]=mx+1

    mx=0
    for i in range(len(dp)):
        mx=max(mx,dp[i])
    print(mx)

arr = [10 , 22 , 9 , 33 , 21 , 50 , 41 , 60]
findlis(arr)