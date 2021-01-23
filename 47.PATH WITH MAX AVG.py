def findmaxavg(arr):
    m=len(arr)
    n=len(arr[0])

    dp=[[0 for j in range(n)] for i in range(m)]

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):

            if i==m-1 and j==n-1:
                dp[i][j]=arr[i][j]
            elif j==n-1:
                dp[i][j]=dp[i+1][j]+arr[i][j]
            elif i==m-1:
                dp[i][j]=dp[i][j+1]+arr[i][j]
            else:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j])+arr[i][j]
    print(dp[0][0])
    avg=(dp[0][0]/(2*(m)-1))
    print(avg)

cost = [[1, 2, 3],
        [6, 5, 4],
        [7, 3, 9]]
findmaxavg(cost)
