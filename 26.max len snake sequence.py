def findSnakeSequence(arr):
    dp = [[0 for j in range(len(arr[0]))] for i in range(len(arr))]

    for i in range(len(arr)):
        for j in range(len(arr[0])):

            if i == 0 and j == 0:
                dp[i][j] = 0
            elif i == 0:
                if abs(arr[i][j] - arr[i][j - 1]) == 1 :
                    dp[i][j] = dp[i][j - 1]
            elif j == 0:
                if abs(arr[i][j] - arr[i - 1][j]) == 1:
                    dp[i][j] = dp[i - 1][j]

            else:
                m = 0
                n = 0
                if abs(arr[i][j] - arr[i][j - 1]) == 1:
                    m = dp[i][j - 1]

                if abs(arr[i][j] - arr[i - 1][j]) == 1:
                    n = dp[i - 1][j]
                dp[i][j]=max(m,n)
            dp[i][j]+=arr[i][j]

    for i in range(len(arr)):
        print(dp[i])


mat = [[9, 6, 5, 2],
       [8, 7, 6, 5],
       [9, 3, 1, 6],
       [1, 1, 1, 7]]

findSnakeSequence(mat)




