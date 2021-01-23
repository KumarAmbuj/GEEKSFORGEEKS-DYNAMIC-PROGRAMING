def findmaxsum(arr):
    dp=[[0 for i in range(len(arr))]for j in range(len(arr))]

    for i in range(len(arr)-1,-1,-1):
        for j in range(i+1):

            if i==len(arr)-1:
                dp[i][j]=arr[i][j]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i+1][j+1])+arr[i][j]

    print(dp[0][0])

tri = [[1],
       [2,1],
       [3,3,2]]
findmaxsum(tri)