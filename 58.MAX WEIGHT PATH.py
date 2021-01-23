def findmaxwt(arr):
    dp=[[0 for i in range(len(arr[0]))]for j in range(len(arr))]

    for i in range(len(arr)-1,-1,-1):
        for j in range(len(arr[0])-1,-1,-1):

            if i==len(arr)-1:
                dp[i][j]=arr[i][j]
            elif j==len(arr[0])-1:
                dp[i][j]=dp[i+1][j]+arr[i][j]
            else:
                dp[i][j]=max(dp[i+1][j],dp[i+1][j+1])+arr[i][j]

    print(dp[0][0])

mat = [ [4, 1 ,5 ,6 , 1],
        [2 ,9 ,2 ,11 ,10],
        [15,1 ,3 ,15, 2],
        [16, 92, 41,4,3],
        [8, 142, 6, 4, 8]]
findmaxwt(mat)