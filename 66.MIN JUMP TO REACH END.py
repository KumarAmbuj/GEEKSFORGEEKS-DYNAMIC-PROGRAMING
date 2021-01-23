def findminjump(arr):
    dp=[0 for i in range(len(arr))]
    dp[len(arr)-1]=0

    for i in range(len(arr)-2,-1,-1):
        mn=99
        for j in range(1,arr[i]+1):

            if (i+j) < len(arr):

                mn=min(mn,dp[i+j])
        dp[i]=mn+1

    print(dp[0])


arr= [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
findminjump(arr)


arr= [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
findminjump(arr)

