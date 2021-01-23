def findmaxsum(arr):
    m=len(arr)
    n=len(arr[0])

    dp=[[0 for j in range(n)] for i in range(m)]

    for i in range(m-1,-1,-1):
        for j in range(i+1):
            if i==m-1:
                dp[i][j]=arr[i][j]
            elif j==0:
                dp[i][j]=max(dp[i+1][j],dp[i+1][j+1]) +arr[i][j]

            else:
                dp[i][j]=max(dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1])+arr[i][j]

    print(dp[0][0])

tri = [[1, 0, 0],
       [4, 8, 0],
       [1, 5, 3]]
findmaxsum(tri)
