def findSnakeSequence(arr):
    dp=[[None for j in range(len(arr[0]))] for i in range(len(arr))]


    for i in range(len(arr)):
        for j in range(len(arr[0])):

            if i==0 and j==0:
                dp[i][j]=arr[i][j]
            elif i==0:
                if abs(arr[i][j]-arr[i][j-1])==1 and dp[i][j-1]!=None:
                    dp[i][j]=dp[i][j-1]+arr[i][j]

            elif j==0:
                if abs(arr[i][j]-arr[i-1][j])==1 and dp[i-1][j]!=None:
                    dp[i][j]=dp[i-1][j]+arr[i][j]

            else:
                m=None
                n=None
                if abs(arr[i][j]-arr[i][j-1])==1 and dp[i][j-1]!=None:
                    m=dp[i][j-1]

                if abs(arr[i][j]-arr[i-1][j])==1 and dp[i-1][j]!=None:
                    n=dp[i-1][j]


                if m!=None and n==None:
                    dp[i][j]=m
                elif m==None and n!=None:
                    dp[i][j]=n
                elif m!=None and n!=None:
                    dp[i][j]=max(m,n)
                elif m==None and n==None:
                    dp[i][j]=None

                if dp[i][j]!=None:
                    dp[i][j]+=arr[i][j]

    for i in range(len(arr)):
        print(dp[i])

mat = [[9, 6, 5, 2],
       [8, 7, 6, 5],
       [9, 3, 1, 6],
       [1, 1, 1, 7]]

findSnakeSequence(mat)
print()
mat = [[9, 6, 5, 2],
       [8, 7, 6, 5],
       [9, 3, 7, 6],
       [1, 1, 8, 4]]

findSnakeSequence(mat)

