def findways(n):
    dp=[[0 for j in range(10)] for i in range(n+1)]


    for i in range(1,n+1):
        for j in range(1,10):

            if i==1:
                dp[i][j]=1

            elif j<i:
                dp[i][j]=0

            elif i==j:
                dp[i][j]=1

            else:
                dp[i][j]=dp[i][j-1]+dp[i-1][j-1]

    sum=0

    for i in range(10):
        sum+=dp[n][i]

    print(sum)

findways(2)
findways(3)
