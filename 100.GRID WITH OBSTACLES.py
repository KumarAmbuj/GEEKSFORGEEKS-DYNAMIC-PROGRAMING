def finduniquepath(arr):
    m=len(arr)
    n=len(arr[0])

    dp=[[0 for j in range(n)] for i in range(m)]

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):
            if i==m-1 and j==n-1:
                dp[i][j]=1

            elif i==m-1:
                if arr[i][j]==0:
                    dp[i][j]=dp[i][j+1]

            elif j==n-1:
                if arr[i][j]==0:
                    dp[i][j]=dp[i+1][j]

            else:
                if arr[i][j]==0:
                    dp[i][j]=(dp[i+1][j]+dp[i][j+1])

    print(dp[0][0])

A = [[0, 0, 0],
     [0, 1, 0],
     [0, 0, 0]]
finduniquepath(A)