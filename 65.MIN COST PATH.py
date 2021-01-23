def findmincostpath(arr,m,n):
    x=len(arr)
    y=len(arr[0])

    dp=[[0 for j in range(y)] for i in range(x)]

    for i in range(x):
        for j in range(y):

            if i==0 and j==0:
                dp[i][j]=arr[i][j]
            elif j==0:
                dp[i][j]=dp[i-1][j]+arr[i][j]
            elif i==0:
                dp[i][j]=dp[i][j-1]+arr[i][j]
            else:
                dp[i][j]=min(dp[i][j-1],dp[i-1][j-1],dp[i-1][j])+arr[i][j]

    print(dp[m][n])
cost= [ [1, 2, 3],
        [4, 8, 2],
        [1, 5, 3] ]
findmincostpath(cost,2,2)