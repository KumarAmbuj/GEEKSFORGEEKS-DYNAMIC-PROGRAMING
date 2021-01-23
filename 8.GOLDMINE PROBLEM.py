def goldmine(arr):
    dp=[[0 for j in range(len(arr[0]))] for i in range(len(arr))]

    for j in range(len(dp[0])-1,-1,-1):
        for i in range(len(dp)):

            if j==len(dp[0])-1:
                dp[i][j]=arr[i][j]
            elif i==0:
                dp[i][j]=max(dp[i][j+1],dp[i+1][j+1])+arr[i][j]

            elif i==len(dp)-1:
                dp[i][j]=max(dp[i-1][j+1],dp[i][j+1])+arr[i][j]

            else:
                dp[i][j]=max(dp[i-1][j+1],dp[i][j+1],dp[i+1][j+1])+arr[i][j]
    mx=0
    for i in range(len(dp)):
        mx=max(mx,dp[i][0])

    print(mx)

gold = [[1, 3, 1, 5],
    [2, 2, 4, 1],
    [5, 0, 2, 3],
    [0, 6, 1, 2]]
goldmine(gold)
