def findminsum(arr):
    dp=[[0 for i in range(len(arr))]for j in range(len(arr))]

    for i in range(len(arr)-1,-1,-1):
        for j in range(i+1):

            if i==len(arr)-1:
                dp[i][j]=arr[i][j]
            elif j==0:
                dp[i][j]=min(dp[i+1][j],dp[i+1][j+1])+arr[i][j]
            else:
                dp[i][j]=min(dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1])+arr[i][j]

    print(dp[0][0])

A = [[ 2 ],
    [3, 9 ],
    [1, 6, 7 ]]
findminsum(A)