def findgivensequence(m,n):
    dp=[[0 for j in range(m+1)] for i in range(n+1)]

    for i in range(len(dp)):
        for j in range(len(dp[0])):

            if i==0:
                dp[i][j]=0
            elif j==0:
                dp[i][j]=0
            elif i==1:
                dp[i][j]=j

            else:

                if j<(2**(i-1)):
                    dp[i][j]=0

                elif j==(2**(i-1)):
                    dp[i][j]=1

                else:
                    dp[i][j]=dp[i][j-1]+dp[i-1][j//2]
    print(dp[n][m])
    for i in range(len(dp)):
        print(dp[i])

findgivensequence(5,3)