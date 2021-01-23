def findmaxsum(arr):
    dp=[[0 for j in range(len(arr[0]))] for i in range(len(arr))]
    m=len(arr)
    n=len(arr[0])

    for i in range(m-1,-1,-1):
        for j in range(n-1,-1,-1):

            if i==m-1 :
                dp[i][j]=arr[i][j]
            elif j==0:
                dp[i][j]=max(dp[i+1][j],dp[i+1][j+1])+arr[i][j]

            elif j==n-1:
                dp[i][j]=max(dp[i+1][j-1],dp[i+1][j])+arr[i][j]

            else:
                dp[i][j]=max(dp[i+1][j-1],dp[i+1][j],dp[i+1][j+1])+arr[i][j]

    mx=0
    for i in range(n):
        mx=max(mx,dp[0][i])

    print(mx)

Mat = [[4, 2, 3, 4],
       [2, 9, 1, 10],
       [15, 1, 3, 0],
       [16, 92, 41, 44]]
findmaxsum(Mat)