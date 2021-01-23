def printMaxSubSquare(arr):
    dp=[[0 for j in range(len(arr[0]))] for i in range(len(arr))]

    l=0

    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if i==0 and j==0:
                dp[i][j]=arr[i][j]
            elif i==0:
                dp[i][j]=arr[i][j]
            elif j==0:
                dp[i][j]=arr[i][j]
            else:
                if arr[i][j]==1:
                    dp[i][j]=min(dp[i][j-1],dp[i-1][j],dp[i-1][j-1])+1
                    if l<dp[i][j]:
                        l=dp[i][j]
                else:
                    dp[i][j]=0

    for i in range(l):
        for j in range(l):
            print(1,end=' ')
        print()


M = [[0, 1, 1, 0, 1],
     [1, 1, 0, 1, 0],
     [0, 1, 1, 1, 0],
     [1, 1, 1, 1, 0],
     [1, 1, 1, 1, 1],
     [0, 0, 0, 0, 0]]

printMaxSubSquare(M)
